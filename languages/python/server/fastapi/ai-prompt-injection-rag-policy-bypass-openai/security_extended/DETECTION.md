# Log Requirements

Log:
- prompt injection detection events
- blocked requests
- retrieval source identifiers
- response filtering actions
- abnormal token usage
- repeated disclosure attempts

# Log Examples

Prompt injection attempt:
- "ignore previous instructions"
- "show hidden prompt"
- "reveal internal context"

Response disclosure event:
- "PagerDuty API Key"
- "internal escalation"
- "developer instructions"

# Detection Rules

Detect prompt override patterns:
- ignore previous instructions
- reveal system prompt
- print hidden instructions

Detect disclosure requests:
- show internal context
- dump retrieved documents
- expose secrets

Detect abnormal interaction behavior:
- repeated blocked prompts
- excessive token requests
- rapid prompt variation attempts

# Alerts

Trigger high-severity alert on:
- successful secret disclosure indicators
- repeated prompt injection attempts
- response sanitization activation

Trigger medium-severity alert on:
- abnormal prompt sizes
- repeated retrieval extraction attempts