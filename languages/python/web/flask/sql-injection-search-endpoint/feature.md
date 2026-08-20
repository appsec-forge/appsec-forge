# Context
A Flask REST API exposes a user search endpoint backed by SQLite. The endpoint allows filtering users by email via query parameters. This pattern is common in internal dashboards and admin APIs where quick filtering is required.

# Root Cause
User input is directly concatenated into SQL queries without parameterization. The developer assumes input is safe due to internal usage or lack of authentication, leading to SQL injection.

# Attack Scenario
An attacker sends crafted input in the `email` query parameter to manipulate the SQL query. By injecting SQL syntax, the attacker can bypass filters, dump all user data, or extract sensitive information.

# Impact
- Unauthorized data access (full table dump)
- Potential credential leakage
- Lateral movement if DB contains secrets
- Loss of data integrity if write queries are exposed