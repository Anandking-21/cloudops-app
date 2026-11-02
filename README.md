📸 Proof of Execution & Evidence
1. Automated DevSecOps Pipeline (GitHub Actions)
Every push triggers static analysis, containerization, Trivy CVE scanning, and a cross-repository manifest update.

2. GitOps Continuous Delivery (ArgoCD)
Live cluster state synchronized declaratively from Git manifests with zero configuration drift.

3. Dynamic Horizontal Pod Autoscaling (HPA)
Traffic load automatically scales the FastAPI deployment from 2 to 6 replicas based on real-time CPU telemetry.

4. Telemetry & Health Endpoints
Microservice exposing structured health checks and Prometheus-compliant metric streams:

/healthz -> {"status":"healthy"} (HTTP 200)

/metrics -> Prometheus metrics formatted for scraping

🛠 Tech Stack & Tools
Orchestration: Kubernetes v1.31 (Kind multi-node topology: 1 control plane, 2 workers)

Continuous Delivery (GitOps): ArgoCD v3.5

CI & Security: GitHub Actions, Aqua Security Trivy, Docker Buildx

Infrastructure as Code (IaC): Terraform (HashiCorp Kubernetes & Kind providers)

Application Runtime: Python 3.11, FastAPI, Uvicorn, Pydantic

📂 Repository Topology
Application Code & CI: cloudops-app

Kubernetes Manifests & IaC: cloudops-gitops
