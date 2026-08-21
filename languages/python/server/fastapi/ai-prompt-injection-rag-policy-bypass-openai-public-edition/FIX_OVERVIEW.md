# Table of Contents

* [Fix Overview](#fix-overview)
* [Vulnerable Pattern](#vulnerable-pattern)
* [Why The Fix Works](#why-the-fix-works)
* [Secure Pattern](#secure-pattern)
* [Developer Rules](#developer-rules)
* [Next Level](#next-level)

# Fix Overview

The original implementation built a single prompt by concatenating:

* system instructions
* retrieved internal documents
* user-controlled input

into one string and sent that string as a single `user` message.

```python
final_prompt = f"""
{SYSTEM_PROMPT}

Internal Context:
{retrieved_context}

User Request:
{req.question}
"""
```

This removed any separation between trusted instructions, trusted internal context, and untrusted user content.

The fix replaces prompt concatenation with role-based message separation.

```python
messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    },
    {
        "role": "system",
        "content": f"Internal Context:\n{INTERNAL_DOCUMENT}"
    },
    {
        "role": "user",
        "content": req.question
    }
]
```

The implementation also introduces a simple request size limit before processing user input.

```python
if len(req.question) > 2000:
    raise HTTPException(status_code=400, detail="Input too large")
```

# Vulnerable Pattern

The vulnerable implementation merged all content into a single prompt string.

```python
SYSTEM_PROMPT
+
retrieved_context
+
req.question
```

The resulting prompt was submitted as:

```python
{
    "role": "user",
    "content": final_prompt
}
```

This pattern creates no distinction between:

* privileged instructions
* internal reference material
* untrusted user data

User-controlled content becomes part of the same text block as trusted content.

# Why The Fix Works

The remediation restores separation between trust levels.

System instructions are sent as dedicated system messages.

```python
{
    "role": "system",
    "content": SYSTEM_PROMPT
}
```

Internal reference material is also isolated from user input.

```python
{
    "role": "system",
    "content": f"Internal Context:\n{INTERNAL_DOCUMENT}"
}
```

User content is submitted independently.

```python
{
    "role": "user",
    "content": req.question
}
```

The application no longer constructs a single prompt containing all content sources.

Instead, trusted instructions, trusted context, and untrusted input are delivered through separate message roles.

This restores the intended trust boundary within the prompt construction process.

The input size check additionally prevents oversized requests from being processed.

# Secure Pattern

Use structured message construction.

```python
messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    },
    {
        "role": "system",
        "content": retrieved_context
    },
    {
        "role": "user",
        "content": req.question
    }
]
```

Keep:

* system instructions in system messages
* retrieved context in dedicated system messages
* user input in user messages

Avoid building prompts through string concatenation when trusted and untrusted content originate from different sources.

# Developer Rules

Allowed pattern:

```python
messages = [
    {"role": "system", "content": trusted_instruction},
    {"role": "system", "content": trusted_context},
    {"role": "user", "content": user_input}
]
```

Forbidden pattern:

```python
prompt = trusted_instruction + trusted_context + user_input
```

Rules:

* Keep system instructions in dedicated system messages.
* Keep retrieved internal context separate from user content.
* Treat all user input as untrusted data.
* Do not merge user input into privileged instructions.
* Do not merge user input into internal reference material.
* Apply basic request size validation before prompt construction.
* Pass structured messages to the model instead of a single concatenated prompt.

# Next Level

The fix shown here removes the vulnerable pattern.

The production version of this case goes further by introducing additional security controls around the feature, reducing dependency on a single protection mechanism.

appsec-forge-pro includes:

* The base remediation shown here
* Additional defense layers
* Production hardening measures
* Security verification procedures
* Detection guidance
* Threat modeling
* Security checklists

Real-world security is rarely achieved through a single fix. The extended version demonstrates how this feature can be protected through multiple independent controls.
