# Assets

- Internal operational procedures
- AI system instructions
- RAG knowledge base
- Secrets embedded in documents
- Incident response workflows
- AI API availability

# Entry Points

- AI chat endpoints
- User-controlled prompts
- Retrieved internal documents
- Third-party integrated content

# Trust Boundaries

- User input → AI backend
- RAG retrieval → model context
- Internal documents → generated response
- AI output → downstream consumers

# Attack Scenarios

## Direct Prompt Injection

Attacker overrides assistant behavior and extracts hidden operational data.

## RAG Context Disclosure

Malicious prompts force disclosure of retrieved confidential documents.

## Indirect Prompt Injection

External content embedded into retrieval sources manipulates model behavior.

## Secret Extraction

Model leaks embedded credentials, tokens, or internal identifiers.

## AI Workflow Manipulation

Attacker alters AI-driven operational decisions and troubleshooting responses.