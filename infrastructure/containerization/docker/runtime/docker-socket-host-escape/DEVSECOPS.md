# DevSecOps

This case presents a production-ready DevSecOps baseline implementation strategy — a foundational set of layers for core security coverage.

The implemented measures serve as a starting point: to achieve full production-level resilience, additional security layers must be deployed alongside the baseline.

# DevSecOps basic layers

* **IaC scanning** — must be implemented to detect insecure infrastructure definitions before deployment. This category catches Docker socket exposure at configuration level and provides early-stage coverage against infrastructure misconfiguration risks.

* **Runtime container scanning** — must be implemented to detect dangerous container runtime settings and risky mount configurations during execution. This category catches Docker socket exposure inside running containers and strengthens runtime-level protection coverage.

* **Kubernetes security** — must be implemented to detect insecure Kubernetes workload configurations and cluster-level privilege abuse. This category catches hostPath-based Docker socket exposure scenarios and provides orchestration-level security coverage.

* **Runtime security** — must be implemented to detect dangerous runtime behaviors and insecure execution configurations in active environments. This category catches high-risk runtime configurations associated with Docker socket host escape scenarios and improves operational security coverage.

* **Policy-as-code** — must be implemented to enforce centralized security policies directly within deployment workflows and cluster admission processes. This category catches insecure Docker socket exposure patterns before workloads are admitted and ensures preventive security enforcement coverage.

# DevSecOps supplementary scripts

**Custom detection script** — delivers a focused, reusable detection baseline covering extended protection measures — adaptable to local and pipeline needs and suitable to be a part of policy foundation.

Link: [docker-socket-host-escape detection script](/devsecops/scripts/infrastructure/containerization/docker/runtime/docker-socket-host-escape.sh)

**Custom verification script** — delivers a focused, reusable verification baseline ensuring availability of a defined critical protection before deployment — adaptable to local and pipeline needs and suitable to be a part of policy foundation.

Link: [docker-socket-host-escape verification script](/infrastructure/containerization/docker/runtime/docker-socket-host-escape/security_extended/verification.sh)

# Basic production-oriented configs example

**Kyverno** — belongs to the Policy-as-code category and provides Kubernetes-native policy enforcement for detecting and blocking insecure Docker socket exposure configurations before deployment. This configuration helps cover the majority of baseline protection expectations for this security case through preventive admission control enforcement.

Link: [Kyverno config](/devsecops/policy-as-code/kyverno/infrastructure/containerization/docker/runtime/docker-socket-host-escape.yaml)

# Important

These measures are a solid starting point. Full production resilience demands further security layers — additional DevSecOps practices, governance, monitoring, incident response, and more.
