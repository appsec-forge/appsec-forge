# Table of Contents

[1. Before You Start](#1-before-you-start)
- [Vulnerability Overview](#vulnerability-overview)
- [Getting Started](#getting-started)
- [General Learning Path](#general-learning-path)
- [Developer Path](#developer-path)
- [DevOps Path](#devops-path)
- [AppSec Path](#appsec-path)
- [DevSecOps Path](#devsecops-path)
- [Security Engineer Path](#security-engineer-path)

[2. Case Structure](#2-case-structure)
- [Repository Structure](#repository-structure)
- [Case Files](#case-files)

[3. Continue Learning](#3-continue-learning)
- [Public vs Pro](#public-vs-pro)
- [License](#license)

---

# 1. Before You Start

## Vulnerability Overview

**Class**

Cross-Site Scripting (XSS)

**Summary**

Untrusted input is rendered as executable HTML in the browser.

**Typical Impact**

Session theft, account takeover, and execution of arbitrary actions on behalf of the victim.

---

## Getting Started

Every **appsec-forge** case is designed to be **studied rather than executed**.

Each file explains one stage of the vulnerability lifecycle, allowing you to understand:

- why the vulnerability appears;
- how it can be exploited;
- how the root cause is remediated;
- how DevSecOps practices help prevent similar issues;
- how production-oriented security extends beyond the basic fix.

All cases follow the same repository structure, making it easy to navigate new technologies, languages, frameworks, infrastructure, and supply chain topics.

Start with the **General Learning Path** below or choose the workflow that best matches your role.

---

## General Learning Path

1. **README.md**  
   Understand the case structure and recommended study workflow.

2. **feature.md**  
   Learn the engineering context, expected behaviour, attack scenario, and impact.

3. **vuln_app/** or **vuln_config/**  
   Identify the implementation or configuration mistake.

4. **exploit.md**  
   Understand how the weakness can be abused.

5. **fixed_app/** or **fixed_config/**  
   Compare vulnerable and remediated implementations.

6. **FIX_OVERVIEW.md**  
   Understand the remediation rationale and secure engineering decisions.

7. **DEVSECOPS.md**  
   Explore security tooling, configurations, automation, and supporting controls.

8. **security_extended/** *(available in appsec-forge-pro)*  
   Continue with production-oriented security engineering practices.

---

## Developer Path

### Recommended Order

feature.md

↓

vuln_app/

↓

exploit.md

↓

fixed_app/

↓

FIX_OVERVIEW.md

↓

DEVSECOPS.md

### Focus On

- secure coding patterns;
- root cause analysis;
- remediation decisions;
- security-focused code reviews.

---

## DevOps Path

### Recommended Order

feature.md

↓

vuln_config/

↓

exploit.md

↓

fixed_config/

↓

FIX_OVERVIEW.md

↓

DEVSECOPS.md

### Focus On

- secure configuration;
- deployment risks;
- infrastructure security;
- CI/CD protection.

---

## AppSec Path

### Recommended Order

README.md

↓

feature.md

↓

vuln_app/ or vuln_config/

↓

exploit.md

↓

fixed_app/ or fixed_config/

↓

FIX_OVERVIEW.md

↓

DEVSECOPS.md

↓

security_extended/*

### Focus On

- vulnerability analysis;
- secure design;
- threat assessment;
- remediation strategy.

---

## DevSecOps Path

### Recommended Order

feature.md

↓

vuln_app/ or vuln_config/

↓

fixed_app/ or fixed_config/

↓

DEVSECOPS.md

↓

security_extended/*

### Focus On

- security automation;
- security tooling;
- implementation-aware detection;
- verification workflows.

---

## Security Engineer Path

### Recommended Order

README.md

↓

feature.md

↓

exploit.md

↓

security_extended/*

### Focus On

- threat modelling;
- layered defence;
- hardening;
- detection strategy.

---

# 2. Case Structure

## Repository Structure

Every case follows the same structure.

```text
README.md
feature.md
vuln_app/ or vuln_config/
fixed_app/ or fixed_config/
exploit.md or exploit/exploit.md
FIX_OVERVIEW.md
DEVSECOPS.md
security_extended/ (appsec-forge-pro)
```

---

## Case Files

### README.md

Introduces the repository structure, recommended learning workflow, and role-specific study paths.

### feature.md

Explains the engineering context, business problem, attack scenario, and security impact.

### vuln_app/ or vuln_config/

Contains the intentionally vulnerable implementation recreated in a realistic project structure.

### exploit.md

Demonstrates practical exploitation techniques and attacker perspective.

### fixed_app/ or fixed_config/

Provides the foundational remediation for the root cause.

Public includes a baseline implementation intended as a learning foundation.

Production-oriented remediation is available in **appsec-forge-pro**.

### FIX_OVERVIEW.md

Explains why the remediation works and the engineering decisions behind it.

Public focuses on the foundational fix.

Production-oriented layered defenses rationale is available in **appsec-forge-pro**.

### DEVSECOPS.md

Defines baseline security layers, tooling, configs, and scripts.

### security_extended/

Available in **appsec-forge-pro**.

Contains production-oriented security engineering documentation including:

- CHECKLIST.md
- THREAT_MODEL.md
- HARDENING.md
- DETECTION.md
- verification.sh
- README.md

---

# 3. Continue Learning

## Public vs Pro

### Public

- Vulnerability demonstration
- Exploit examples
- Foundational remediation
- Remediation overview
- Baseline DevSecOps guidance

### Pro

Everything included in **Public**, plus:

- production-oriented remediation;
- security checklist;
- threat model;
- hardening guidance;
- detection strategy;
- verification script;
- production-oriented DevSecOps assets.

> In the Public repository, production-oriented files are included as placeholders and indicate that their complete content is available in **appsec-forge-pro**.

---

## License

See the root **LICENSE** file for details.

