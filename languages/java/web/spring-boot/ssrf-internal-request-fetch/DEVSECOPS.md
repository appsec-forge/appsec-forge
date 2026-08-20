# DevSecOps

This case presents a production-ready DevSecOps baseline implementation strategy — a foundational set of layers for core security coverage.

The implemented measures serve as a starting point: to achieve full production-level resilience, additional security layers must be deployed alongside the baseline.

# DevSecOps basic layers

* **SAST** — must be implemented to identify unsafe URL usage patterns directly in application code before deployment. This layer provides foundational code-level coverage for detecting SSRF-related logic flaws and insecure request handling paths.

* **DAST** — must be implemented to actively probe SSRF behavior in running applications and validate externally reachable attack paths. This layer provides runtime interaction coverage and helps identify exploitable request-forwarding behavior missed during static analysis.

* **IAST** — must be implemented to provide in-application context during execution and correlate vulnerable data flows with runtime behavior. This layer improves precision of SSRF detection by combining application telemetry with security analysis during execution.

* **Runtime Security** — must be implemented to detect abnormal outbound calls and suspicious network activity during application runtime. This layer provides operational protection coverage against active SSRF exploitation attempts and unauthorized external communication.

* **Policy-as-code** — must be implemented to enforce allowed network access rules and prevent unauthorized outbound connectivity patterns. This layer provides governance-driven protection coverage by enforcing security controls consistently across environments and deployments.

# DevSecOps supplementary scripts

**Custom detection script** — delivers a focused, reusable detection baseline covering extended protection measures — adaptable to local and pipeline needs and suitable to be a part of policy foundation.

Link: [ssrf-internal-request-fetch detection script](/devsecops/scripts/languages/java/web/spring-boot/ssrf-internal-request-fetch.sh)

**Custom verification script** — delivers a focused, reusable verification baseline ensuring availability of a defined critical protection before deployment — adaptable to local and pipeline needs and suitable to be a part of policy foundation.

Link: [ssrf-internal-request-fetch verification script](/languages/java/web/spring-boot/ssrf-internal-request-fetch/security_extended/verification.sh)

# Basic production-oriented configs example

**Semgrep** — belongs to the SAST category and provides static analysis coverage for detecting unsafe internal request handling patterns associated with SSRF scenarios while covering the majority of baseline protection expectations for this case.

Link: [Semgrep config](/devsecops/sast/semgrep/languages/java/web/spring-boot/ssrf-internal-request-fetch.yml)

# Important

These measures are a solid starting point. Full production resilience demands further security layers — additional DevSecOps practices, governance, monitoring, incident response, and more.
