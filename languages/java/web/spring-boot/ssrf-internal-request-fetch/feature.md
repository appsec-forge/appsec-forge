# SSRF — Java — Spring Boot REST API

## Context
Internal microservice fetches external resources (URLs) on behalf of clients (e.g., webhook validation, metadata fetch, URL preview).

## Root Cause
User-controlled URL is directly used in server-side HTTP request without validation, allowing access to internal network resources.

## Attack Scenario
Attacker submits a crafted URL pointing to internal services (e.g., http://localhost:8080/admin or cloud metadata endpoint). Server performs request and returns sensitive data.

## Impact
Exposure of internal services, credentials (e.g., cloud metadata), lateral movement inside infrastructure, potential full environment compromise.