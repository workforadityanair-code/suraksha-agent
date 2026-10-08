# SurakshaAgent 

An autonomous, sandboxed security auditor designed to evaluate untrusted client workloads targeting Indian Digital Public Infrastructure (DPI) specifications (UPI, ONDC/Beckn Protocol).

## Overview
SurakshaAgent isolates client integration scripts inside resource-constrained Docker containers and executes them against a local mock gateway. It inspects runtime output, HTTP status codes, and authorization parameters to produce an automated compliance and security audit report.

## Architecture
- **Sandbox Environment:** Isolated Docker container running under non-root permissions with strict memory (`256MB`) and CPU quotas (`0.5 core`).
- **Mock DPI Gateway:** FastAPI-based service simulating national signature verification endpoints (`/v1/dpi/verify`).
- **Audit Engine:** Captures runtime telemetry and evaluates rule adherence (e.g., verifying `X-Gateway-Auth` headers and preventing credential leakage in logs).

## Getting Started

### 1. Build the Sandbox
```bash
docker build -t dpi-sandbox:latest -f docker/Dockerfile.sandbox .