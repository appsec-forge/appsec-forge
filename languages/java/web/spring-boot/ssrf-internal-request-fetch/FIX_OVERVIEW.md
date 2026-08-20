# Table of Contents

* [Fix Overview](#fix-overview)
* [Vulnerable Pattern](#vulnerable-pattern)
* [Why The Fix Works](#why-the-fix-works)
* [Secure Pattern](#secure-pattern)
* [Developer Rules](#developer-rules)
* [Next level](#next-level)

# Fix Overview

The vulnerable implementation accepted a user-supplied URL and used it directly to create an outbound request.

```java
URL target = new URL(url);
BufferedReader reader = new BufferedReader(
        new InputStreamReader(target.openStream())
);
```

The fix introduces URL parsing and validation before any network request is performed.

```java
URI uri = new URI(url);
```

The implementation now validates:

* Allowed schemes (`http` and `https`)
* Hostname restrictions for localhost
* Loopback address restrictions for `127.x.x.x`

```java
if (!uri.getScheme().matches("http|https") ||
    uri.getHost().equals("localhost") ||
    uri.getHost().startsWith("127.")) {
    return "Blocked URL";
}
```

Only URLs that pass validation are converted to a request target.

```java
URL target = uri.toURL();
```

# Vulnerable Pattern

Direct use of user input as a request destination.

```java
URL target = new URL(url);
target.openStream();
```

The application performs no validation before creating the outbound request.

The destination is fully controlled by the request parameter.

# Why The Fix Works

The fix introduces validation before any outbound connection is created.

URL parsing is performed first.

```java
URI uri = new URI(url);
```

Only HTTP and HTTPS schemes are accepted.

```java
uri.getScheme().matches("http|https")
```

Requests targeting localhost are rejected.

```java
uri.getHost().equals("localhost")
```

Requests targeting loopback addresses are rejected.

```java
uri.getHost().startsWith("127.")
```

Validation occurs before:

```java
uri.toURL()
```

and before:

```java
target.openStream()
```

As a result, blocked destinations never reach the request execution stage.

# Secure Pattern

Validate user-supplied URLs before creating outbound connections.

Recommended flow:

```java
URI uri = new URI(url);

validateScheme(uri);
validateHost(uri);

URL target = uri.toURL();
```

Validation must occur before:

* URL conversion
* Connection creation
* Stream access

The request should only be executed after all validation checks succeed.

# Developer Rules

Required:

* Parse URLs using `URI` before processing.
* Validate the scheme before creating a connection.
* Allow only explicitly approved schemes.
* Reject `localhost`.
* Reject loopback addresses beginning with `127.`.
* Perform validation before `toURL()`.
* Perform validation before `openStream()`.

Forbidden:

* Creating `URL` objects directly from unvalidated user input.
* Calling `openStream()` on user-controlled destinations.
* Executing outbound requests before validation.
* Accepting arbitrary schemes.
* Allowing localhost targets.
* Allowing loopback targets.

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
