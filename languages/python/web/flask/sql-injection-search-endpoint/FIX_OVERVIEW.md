# Table of Contents

* [Fix Overview](#fix-overview)
* [Vulnerable Pattern](#vulnerable-pattern)
* [Why The Fix Works](#why-the-fix-works)
* [Secure Pattern](#secure-pattern)
* [Developer Rules](#developer-rules)
* [Next level](#next-level)

# Fix Overview

The original implementation builds an SQL statement by inserting user-controlled data directly into the query string.

```python
query = f"SELECT id, email FROM users WHERE email = '{email}'"
cursor.execute(query)
```

The fix replaces string interpolation with a parameterized query.

```python
query = "SELECT id, email FROM users WHERE email = ?"
cursor.execute(query, (email,))
```

The SQL statement structure becomes static and user input is supplied separately as a bound parameter.

# Vulnerable Pattern

User input is concatenated into SQL code.

```python
query = f"SELECT id, email FROM users WHERE email = '{email}'"
```

The query text is dynamically generated from request data.

Application code is responsible for constructing SQL syntax and embedding user values into that syntax.

# Why The Fix Works

The fixed implementation separates SQL instructions from user-provided values.

```python
query = "SELECT id, email FROM users WHERE email = ?"
cursor.execute(query, (email,))
```

The database receives:

* a fixed SQL statement
* a parameter value bound to the placeholder

The user input is treated as data associated with the placeholder rather than as part of the SQL statement itself.

The query structure remains unchanged regardless of the supplied email value.

# Secure Pattern

Use parameterized statements for all database operations that include external input.

```python
query = "SELECT id, email FROM users WHERE email = ?"
cursor.execute(query, (email,))
```

The SQL statement should contain placeholders.

User-controlled values should be supplied through the parameter binding mechanism provided by the database driver.

# Developer Rules

## Required

* Use parameterized queries for request-derived values.
* Keep SQL statement structure static.
* Pass user input through query parameters.
* Use database driver parameter binding APIs.

## Forbidden

* String interpolation inside SQL statements.
* f-strings that construct SQL queries.
* String concatenation for SQL generation.
* Embedding request parameters directly into SQL text.
* Executing dynamically assembled SQL statements when parameter binding can be used.

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