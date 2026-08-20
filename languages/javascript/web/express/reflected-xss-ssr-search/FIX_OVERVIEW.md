# Table of Contents

* [Fix Overview](#fix-overview)
* [Vulnerable Pattern](#vulnerable-pattern)
* [Why The Fix Works](#why-the-fix-works)
* [Secure Pattern](#secure-pattern)
* [Developer Rules](#developer-rules)
* [Next level](#next-level)

# Fix Overview

The application rendered user-controlled input directly into an HTML response using template literals.

The fix introduces centralized HTML output encoding through the `escapeHtml()` function before user data is inserted into the response.

Instead of rendering raw input:

```js
<p>You searched for: ${query}</p>
```

the application now renders encoded input:

```js
const safeQuery = escapeHtml(query);

<p>You searched for: ${safeQuery}</p>
```

The remediation focuses on output encoding at the rendering boundary.

# Vulnerable Pattern

User input from `req.query.q` was embedded directly into HTML:

```js
const query = req.query.q || '';

const html = `
    <h1>Search Results</h1>
    <p>You searched for: ${query}</p>
`;
```

The application relied on string concatenation and template literals without any encoding step.

No transformation was applied before the value became part of the HTML document.

# Why The Fix Works

The fix applies HTML encoding before rendering:

```js
function escapeHtml(str) {
    return str
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");
}
```

User input is processed through:

```js
const safeQuery = escapeHtml(query);
```

The encoded value is then rendered:

```js
<p>You searched for: ${safeQuery}</p>
```

Characters that have special meaning in HTML are converted into their encoded representations before insertion into the response.

As a result, the browser receives encoded text instead of raw HTML markup.

# Secure Pattern

Encode untrusted data immediately before inserting it into an HTML response.

Use a dedicated encoding function:

```js
const safeQuery = escapeHtml(query);
```

Render only the encoded value:

```js
<p>${safeQuery}</p>
```

The rendering layer becomes responsible for converting untrusted input into safe HTML output.

# Developer Rules

Allowed:

* Treat all request data as untrusted.
* Encode user input before inserting it into HTML.
* Use a centralized encoding function such as `escapeHtml()`.
* Render encoded values instead of raw values.
* Apply encoding at the point where HTML is generated.

Forbidden:

* Rendering `req.query`, `req.body`, or other user-controlled values directly into HTML.
* Embedding raw user input inside template literals used for HTML generation.
* Skipping output encoding when building HTML responses.
* Duplicating ad-hoc encoding logic throughout the application.

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
