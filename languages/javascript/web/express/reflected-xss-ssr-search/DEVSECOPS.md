# DevSecOps

This case presents a production-ready DevSecOps baseline implementation strategy — a foundational set of layers for core security coverage.

The implemented measures serve as a starting point: to achieve full production-level resilience, additional security layers must be deployed alongside the baseline.

# DevSecOps basic layers

* **SAST** — must be implemented to detect unsafe rendering patterns directly in source code before deployment. Provides strong baseline coverage against reflected XSS risks by identifying vulnerable application logic during development and CI stages.

* **DAST** — must be implemented to catch reflected XSS behavior during runtime testing against live applications and endpoints. Provides external attack-surface validation and confirms whether exploitable reflection paths are reachable in practice.

* **IAST** — must be implemented to provide in-application runtime context for reflected XSS flows and vulnerable execution paths. Strengthens detection accuracy by correlating source, sink, and execution behavior inside the running application.

* **WAF** — must be implemented to block and mitigate malicious reflected XSS requests at the edge before they reach application logic. Provides runtime protection coverage and reduces exploitation risk even when vulnerable code paths exist.

# DevSecOps supplementary scripts

**Custom detection script** — delivers a focused, reusable detection baseline covering extended protection measures — adaptable to local and pipeline needs and suitable to be a part of policy foundation.
Link: [reflected-xss-ssr-search detection script](/devsecops/scripts/languages/javascript/web/express/reflected-xss-ssr-search.sh)

**Custom verification script** — delivers a focused, reusable verification baseline ensuring availability of a defined critical protection before deployment — adaptable to local and pipeline needs and suitable to be a part of policy foundation.
Link: [reflected-xss-ssr-search verification script](/languages/javascript/web/express/reflected-xss-ssr-search/security_extended/verification.sh)

# Basic production-oriented configs example

**Semgrep** — belongs to the SAST category and provides static application security analysis focused on detecting insecure rendering and reflected XSS-related implementation patterns in Express applications while covering most baseline protection expectations for this case.
Link: [Semgrep config](/devsecops/sast/semgrep/languages/javascript/web/express/reflected-xss-ssr-search.yml)

# Important

These measures are a solid starting point. Full production resilience demands further security layers — additional DevSecOps practices, governance, monitoring, incident response, and more.
