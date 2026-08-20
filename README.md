# appsec-forge

Created for **Developers, DevOps, AppSec, DevSecOps, and Security Engineers**.

A repository-first security knowledge base covering secure development, application security, infrastructure, software supply chain, AI, and DevSecOps.

Study security problems the same way experienced engineering teams solve them: understand the feature, identify the root cause, analyze the exploit, compare the remediation, and explore the supporting security engineering practices.

---

# Table of Contents

[1. Before You Start](#1-before-you-start)
- [About](#about)
- [Pro Access](#pro-access)
- [What to Expect?](#what-to-expect)
- [How to Study appsec-forge](#how-to-study-appsec-forge)

[2. Repository Structure](#2-repository-structure)
- [Repository Layout](#repository-layout)
- [How to Navigate Cases](#how-to-navigate-cases)
- [Inside Every Case](#inside-every-case)

[3. Continue Learning](#3-continue-learning)
- [Public vs Pro](#public-vs-pro)
- [License](#license)

---

# 1. Before You Start

## About

**appsec-forge** organizes production-inspired security engineering cases into a consistent Git repository structure.

Each case reconstructs a realistic security problem from its engineering context through vulnerability analysis, exploitation, remediation, and supporting security practices.

The repository is available in two editions: **Public** and **Pro**. Both editions contain the same cases and follow the same learning workflow. The Pro edition extends each Public case with additional production-oriented security engineering content.

The repository is designed for studying and comparing implementations rather than running interactive labs or sandbox environments.

---

## Pro Access

This repository contains the free **appsec-forge Public edition**.

**appsec-forge-pro is available exclusively through the official appsec-forge website.** Pro purchases and access are managed through GitHub after purchase.

To learn more about Pro and purchase access, visit the official appsec-forge website:

[www.appsecforge.com](https://www.appsecforge.com)

---

## What to Expect

The repository assumes familiarity with modern software development and is intended for engineers who want to strengthen practical security engineering skills.

Rather than focusing on isolated vulnerability examples, you'll learn how security issues emerge during everyday software development, how they are exploited, and how experienced engineering teams reduce risk through secure implementation, review, and automation.

Because every case follows the same structure, moving between languages, frameworks, infrastructure, and supply chain topics becomes consistent and predictable.

---

## Educational Use Only

The materials in this repository are provided for educational and security engineering purposes.

Vulnerable code, configurations, exploit demonstrations, fixes, security controls, and other examples are reference implementations. They are not guaranteed to be suitable for production use and should not be copied into production environments without appropriate review, testing, adaptation, and validation.

Production security decisions must account for the specific architecture, threat model, dependencies, infrastructure, operational requirements, and applicable compliance obligations of the environment.

Only perform exploit demonstrations or security testing against systems you own or are explicitly authorized to test.


---

## How to Study appsec-forge

Start with the technology, framework, infrastructure, or tooling you already use.

Then follow the recommended learning order inside each case:

1. Understand the engineering context.
2. Identify the vulnerable implementation.
3. Analyze the exploit.
4. Compare vulnerable and remediated implementations.
5. Understand the remediation rationale.
6. Review supporting DevSecOps practices.
7. Continue with production-oriented security engineering in **appsec-forge-pro**.

The same workflow is used throughout the repository, making it easy to transfer security engineering knowledge across different technologies and environments.

---

# 2. Repository Structure

## Repository Layout

The repository is organized around the origin of security problems.

```text
languages/
    language/
        context/
            framework/
                case/

infrastructure/
    area/
        technology/
            context/
                case/

supply-chain/
    domain/
        tool/
            technology/
                context/
                    case/

devsecops/
    category/
        tool/
            context/
                example/
```

---

## How to Navigate Cases

Choose the area that matches your current work.

### Application Security

```text
language
    ↓
context
    ↓
framework
    ↓
case
    ↓
DevSecOps
    ↓
configs
```

---

### Infrastructure Security

```text
area
    ↓
technology
    ↓
context
    ↓
case
    ↓
DevSecOps
    ↓
configs
```

---

### Supply Chain Security

```text
domain
    ↓
tool / technology
    ↓
context
    ↓
case
    ↓
DevSecOps
    ↓
configs
```

---

### DevSecOps

```text
category
    ↓
tool
    ↓
context
    ↓
example
```

---

## Inside Every Case

Every case follows the same internal structure.

```text
README.md
feature.md
vuln_app.* or vuln_config/
exploit.md
fixed_app.* or fixed_config/
FIX_OVERVIEW.md
DEVSECOPS.md
security_extended/ (appsec-forge-pro)
```

Each document focuses on a specific stage of the engineering lifecycle.

| File | Purpose |
|-------|---------|
| README.md | Introduces the case and recommended learning workflow. |
| feature.md | Explains the engineering context, attack scenario, and impact. |
| vuln_code.* or vuln_config/ | Demonstrates the vulnerable implementation. |
| exploit.md | Shows how the vulnerability can be exploited. |
| fixed_code.* or fixed_config/ | Provides the foundational remediation. |
| FIX_OVERVIEW.md | Explains why the remediation works. |
| DEVSECOPS.md | Demonstrates supporting security tooling and automation. |
| security_extended/ | Extends the case with production-oriented security engineering documentation (Pro). |

---

# 3. Continue Learning

## Public vs Pro

Both editions share the same repository structure and learning workflow.

### appsec-forge (Public)

Includes:

- realistic vulnerable implementations;
- exploit examples;
- foundational remediation;
- remediation overview;
- baseline DevSecOps guidance.

### appsec-forge-pro

Everything included in the Public edition, plus:

- production-oriented remediation;
- threat modelling;
- security review checklist;
- production hardening;
- detection strategy;
- verification scripts;
- production DevSecOps assets.

The Public edition introduces the vulnerability and its foundational remediation.

The Pro edition extends the same case with production-oriented security engineering practices.

---

## License

See the root **LICENSE** file for details.
