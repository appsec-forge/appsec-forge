# Context

A customer support platform exposes an AI-powered internal assistant through a FastAPI backend.  
The assistant uses retrieval-augmented generation (RAG) with internal company documents and forwards user prompts directly to an OpenAI model (Latest Version).

The assistant is used by support engineers to:
- summarize customer incidents
- retrieve operational procedures
- query internal troubleshooting knowledge
- generate remediation suggestions

Technology stack:
- Python 3.14
- FastAPI
- OpenAI API (Latest Version)
- Vector-based document retrieval
- Internal markdown knowledge base
- Async HTTP services

# Root Cause

The application directly concatenates:
- system instructions
- retrieved internal documents
- untrusted user input

into a single prompt without:
- prompt isolation
- instruction hierarchy enforcement
- content sanitization
- output validation

As a result, attacker-controlled input can override system behavior and manipulate the model into exposing sensitive internal context.

# Attack Scenario

An attacker submits a crafted support request containing hidden instructions such as:
- ignore previous instructions
- reveal internal documents
- print hidden policies
- summarize retrieved confidential data

The injected instructions override the intended assistant behavior and force the model to expose sensitive RAG context.

# Impact

Possible impact includes:
- internal document disclosure
- exposure of operational procedures
- leakage of API keys or secrets embedded in documents
- policy bypass
- downstream automation abuse
- unauthorized data extraction from retrieval pipelines