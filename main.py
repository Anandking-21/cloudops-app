from fastapi import FastAPI, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time

app = FastAPI(title="CloudOps Core API", version="1.0.0")

# Prometheus Metrics for SRE Monitoring
REQUEST_COUNT = Counter("http_requests_total", "Total HTTP Requests", ["method", "endpoint", "status"])
REQUEST_LATENCY = Histogram("http_request_duration_seconds", "HTTP Request Latency", ["endpoint"])

@app.middleware("http")
async def monitor_requests(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    
    REQUEST_COUNT.labels(method=request.method, endpoint=request.url.path, status=response.status_code).inc()
    REQUEST_LATENCY.labels(endpoint=request.url.path).observe(duration)
    return response

@app.get("/")
def read_root():
    return {"message": "CloudOps Core API is active", "version": "1.0.0"}

@app.get("/healthz")
def health_check():
    return {"status": "healthy"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)