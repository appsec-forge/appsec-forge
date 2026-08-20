# DevSecOps

This case presents a production-ready DevSecOps baseline implementation strategy — a foundational set of layers for core security coverage.

The implemented measures serve as a starting point: to achieve full production-level resilience, additional security layers must be deployed alongside the baseline.

# DevSecOps basic layers

* **SAST** — must be implemented to detect unsafe query construction patterns directly in source code before deployment. This layer provides foundational code-level coverage for identifying vulnerable data flow paths and insecure query handling related to this case.

* **DAST** — must be implemented to identify injection points through runtime interaction with the running application. This layer provides runtime attack-surface validation coverage and helps detect exploitable behavior that may bypass static analysis.

* **Runtime Security** — must be implemented to detect abnormal database access behavior and suspicious runtime activity during application execution. This layer provides behavioral and execution-time coverage for identifying exploitation attempts and unexpected database interaction patterns related to this case.

* **WAF** — must be implemented to filter and block malicious HTTP requests targeting vulnerable endpoints. This layer provides perimeter-level protection coverage by mitigating common exploitation attempts before they reach the application.

# DevSecOps supplementary scripts

**Custom detection script** — delivers a focused, reusable detection baseline covering extended protection measures — adaptable to local and pipeline needs and suitable to be a part of policy foundation.

Link: [sql-injection-search-endpoint detection script](/devsecops/scripts/languages/python/web/flask/sql-injection-search-endpoint.sh)

**Custom verification script** — delivers a focused, reusable verification baseline ensuring availability of a defined critical protection before deployment — adaptable to local and pipeline needs and suitable to be a part of policy foundation.

Link: [sql-injection-search-endpoint verification script](/languages/python/web/flask/sql-injection-search-endpoint/security_extended/verification.sh)

# Basic production-oriented configs example

**Semgrep** — belongs to the SAST category and provides static code analysis focused on detecting insecure query construction patterns and vulnerable input handling associated with this case while covering most baseline protection expectations.

Link: [Semgrep config](/devsecops/sast/semgrep/languages/python/web/flask/sql-injection-search-endpoint.yaml)

# Important

These measures are a solid starting point. Full production resilience demands further security layers — additional DevSecOps practices, governance, monitoring, incident response, and more.
