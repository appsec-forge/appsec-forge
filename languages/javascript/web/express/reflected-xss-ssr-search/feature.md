## Context

A SaaS dashboard built on Node.js + Express serves dynamic HTML pages for internal analytics. The frontend uses server-side rendering (SSR) with template literals and partial user input (search, filters, comments).

## Root Cause

User-controlled input (query parameters or form data) is directly embedded into HTML responses without proper output encoding. Developers rely on manual string concatenation instead of templating engines with auto-escaping.

## Attack Scenario

An attacker sends a crafted link with a malicious script in a query parameter (e.g., search). When a logged-in user opens it, the script executes in their browser, stealing session cookies or performing actions via CSRF.

## Impact

Reflected XSS in SSR apps remains one of the most common production issues. It often appears in dashboards, admin panels, and internal tools where developers skip strict output encoding, assuming a trusted audience.
