# Stage 1: Build virtual environment
FROM python:3.11-slim AS builder
WORKDIR /app
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final minimal runtime
FROM python:3.11-slim
WORKDIR /app

# Copy isolated virtual environment
COPY --from=builder /opt/venv /opt/venv
COPY main.py .

ENV PATH="/opt/venv/bin:$PATH"

# Run as non-root user
USER 10001

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]