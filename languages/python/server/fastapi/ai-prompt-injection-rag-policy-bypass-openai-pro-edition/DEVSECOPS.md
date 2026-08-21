# DevSecOps 

This case presents a production-ready DevSecOps baseline implementation strategy — a foundational set of layers for core security coverage. 

The implemented measures serve as a starting point: to achieve full production-level resilience, additional security layers must be deployed alongside the baseline.

# DevSecOps basic layers

* **AI FIREWALL** — must be implemented because it detects prompt injection patterns, unsafe instruction overrides, and malicious LLM interaction flows targeting AI application boundaries. It provides critical runtime protection coverage for direct prompt injection abuse paths.

* **AI RUNTIME SECURITY** — must be implemented because it monitors live model behavior, anomalous responses, and policy violations during inference execution. It provides production-level visibility into active exploitation attempts and unsafe AI runtime states.

* **AI POLICY** — must be implemented because it enforces prompt governance, instruction boundaries, and response control policies required to reduce unauthorized disclosure risks. It provides baseline protection against unsafe model behavior and policy bypass attempts.

* **DAST** — must be implemented because it identifies externally reachable AI API attack paths, prompt abuse vectors, and insecure request handling patterns exposed through runtime interfaces. It provides practical coverage against exploitable application-layer exposure.

* **SAST** — must be implemented because it detects insecure prompt construction patterns, unsafe trust-boundary merging, and vulnerable LLM integration logic directly in source code. It provides foundational detection coverage during development and review stages.

# DevSecOps supplementary scripts

**Custom detection script** — delivers a focused, reusable detection baseline covering extended protection measures — adaptable to local and pipeline needs and suitable to be a part of policy foundation.

Link: [ai-prompt-injection-rag-policy-bypass-openai detection script](/devsecops/scripts/languages/python/server/fastapi/ai-prompt-injection-rag-policy-bypass-openai.sh)

**Custom verification script** — delivers a focused, reusable verification baseline ensuring availability of a defined critical protection before deployment — adaptable to local and pipeline needs and suitable to be a part of policy foundation.

Link: [ai-prompt-injection-rag-policy-bypass-openai verification script](/languages/python/server/fastapi/ai-prompt-injection-rag-policy-bypass-openai/security_extended/verification.sh)

# Basic production-oriented configs example

**Semgrep Whitney** — belongs to the AI-SAST category and provides static analysis coverage for insecure LLM integration patterns, unsafe prompt construction, and direct trust-boundary violations commonly leading to prompt injection exposure in AI APIs. It helps cover most baseline protections required for this vulnerability class.

Link: [Semgrep Whitney config](/devsecops/ai-sast/semgrep-whitney/languages/python/server/fastapi/ai-prompt-injection-rag-policy-bypass-openai.yaml)

# Important

These measures are a solid starting point. Full production resilience demands further security layers — additional DevSecOps practices, governance, monitoring, incident response, and more.