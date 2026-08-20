## Context

A microservice is deployed in Docker on a host (VM / bare metal). For simplifying operations (CI/CD, debugging, dynamic container execution), the container is granted access to the Docker daemon via the Unix socket `/var/run/docker.sock`. This pattern is often used in CI agents, internal tools, or admin panels.

## Root Cause

A developer mounts the Docker socket inside the container:

* to launch child containers
* to manage container lifecycle
* for debugging purposes

However, the Docker daemon runs with root privileges. Anyone who gains access to the socket effectively obtains root access to the host.

## Attack Scenario

1. An attacker gains access to the container (RCE, SSRF → internal service, leaked credentials).
2. Finds the mounted `/var/run/docker.sock`.
3. Uses the Docker API to run a container with the host root filesystem mounted.
4. Gains access to the host filesystem → extracts secrets, SSH keys, tokens.
5. Establishes persistence or escalates the attack (lateral movement, persistence).

## Impact

* One of the most common anti-patterns in Docker / CI systems
* Enables full host compromise via a “container”
* Frequently found in GitLab Runner, Jenkins agents, and internal tooling
* Bypasses most container isolation mechanisms
