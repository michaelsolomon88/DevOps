# DevOps

A hands-on DevOps project that grows over 12 versions, from a small Flask app in a container to a full setup with Kubernetes, CI/CD, infrastructure as code, GitOps and monitoring on AWS.

The app itself is deliberately tiny so the focus stays on the tooling around it. Each version has its own write-up in [`docs/`](docs/) covering why it was needed, how it was built, and how to test it.

## Tech stack

Python, Flask, Docker

## Roadmap

| Version | What's added | Concept demonstrated | Status + Docs |
|---------|--------------|----------------------|---------------|
| v1.0 | Flask app + Docker + HTML dashboard | Containerization | ✅ Done · [details](docs/v1-containerization.md) |
| v2.0 | Kubernetes (`kind`) + dev/staging/production namespaces | Orchestration, environment isolation | Planned |
| v3.0 | Helm chart | Package management for Kubernetes | Planned |
| v4.0 | GitHub Actions (branch-based deploy) | CI/CD pipeline | Planned |
| v5.0 | Terraform (EC2 + VPC) + Ansible (k3s install) | Infrastructure as Code, Configuration Management | Planned |
| v6.0 | Run all environments on the v5 EC2/k3s server, deployed with GitHub Actions | Extending existing CI/CD to a real cloud target | Planned |
| v7.0 | ArgoCD | GitOps-based Continuous Deployment | Planned |
| v8.0 | Jenkins pipeline as an alternative to GitHub Actions | Alternative CI tooling | Planned |
| v9.0 | Prometheus + Grafana | Observability & monitoring | Planned |
| v10.0 | Loki + Grafana Alloy + Alertmanager | Log aggregation & alerting | Planned |
| v11.0 | Load Balancer + AWS CloudFormation | Networking, alternative IaC | Planned |
| v12.0 | Migration to Amazon EKS | Managed Kubernetes, IRSA, AWS Load Balancer Controller | Planned |

## License

MIT
