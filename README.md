\# CloudOps: GitOps \& DevSecOps Automated Platform



An enterprise-grade, end-to-end Kubernetes platform demonstrating modern \*\*GitOps Continuous Delivery (ArgoCD)\*\*, \*\*Automated DevSecOps (Trivy CVE Scanning)\*\*, \*\*Dynamic Auto-Scaling (HPA v2)\*\*, and \*\*Declarative Infrastructure-as-Code (Terraform)\*\* across a multi-node cluster topology.



\---



\## 🏗 Architecture \& Delivery Flow



```text

\[Developer Commit / PR]

&#x20;      │

&#x20;      ▼

\[GitHub Actions CI/CD]

&#x20;  ├── 1. Unit \& Smoke Tests (Python 3.11 / FastAPI)

&#x20;  ├── 2. Multi-Stage Docker Image Build

&#x20;  ├── 3. DevSecOps Container Scan (Aqua Security Trivy - High/Crit Gates)

&#x20;  └── 4. Automated Manifest Sync (Commit commit SHA to GitOps repo via PAT)

&#x20;      │

&#x20;      ▼

\[GitHub: cloudops-gitops] ──(Declarative State of Truth)

&#x20;      │

&#x20;      ▼ (Poll / Webhook Reconciliation)

\[ArgoCD Controller (In-Cluster)]

&#x20;      │

&#x20;      ▼ (Automated Zero-Downtime Rolling Update)

\[Kind Multi-Node Cluster]

&#x20;  ├── Control Plane (NGINX Ingress Controller)

&#x20;  ├── Worker 1 \& Worker 2

&#x20;  ├── Kubernetes Metrics Server (Kubelet Telemetry)

&#x20;  └── HPA Engine (Target: 50% CPU | Replicas: 2 Min – 6 Max)

