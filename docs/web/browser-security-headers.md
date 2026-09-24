---
hide:
  - toc
---
# Browser Security Headers & Cookies

Fast CSP, cookie and SameSite checks.

<div class="ol-section-kicker"><span>WEB</span><strong>HEADERS</strong></div>

## Security headers summary
```bash
curl -skI https://<TARGET>/ | grep -Ei 'content-security-policy|strict-transport-security|x-frame-options|x-content-type-options|referrer-policy|permissions-policy'
```
**Tool:** curl · **Platform:** Any · **Tags:** Headers, CSP, HSTS · **Context:** No auth

## CSP only
```bash
curl -skI https://<TARGET>/ | grep -i '^content-security-policy:'
```
**Tool:** curl · **Platform:** Any · **Tags:** CSP · **Context:** No auth

## All Set-Cookie headers
```bash
curl -skD - https://<TARGET>/ -o /dev/null | grep -i '^set-cookie:'
```
**Tool:** curl · **Platform:** Any · **Tags:** Cookies · **Context:** No auth

## Missing Secure flag candidates
```bash
curl -skD - https://<TARGET>/ -o /dev/null | grep -i '^set-cookie:' | grep -vi '; *secure'
```
**Tool:** curl · **Platform:** Any · **Tags:** Cookies, Secure · **Context:** No auth

## Missing HttpOnly candidates
```bash
curl -skD - https://<TARGET>/ -o /dev/null | grep -i '^set-cookie:' | grep -vi '; *httponly'
```
**Tool:** curl · **Platform:** Any · **Tags:** Cookies, HttpOnly · **Context:** No auth

## SameSite values
```bash
curl -skD - https://<TARGET>/ -o /dev/null | grep -i '^set-cookie:' | grep -Eio 'SameSite=(Strict|Lax|None)'
```
**Tool:** curl · **Platform:** Any · **Tags:** Cookies, SameSite · **Context:** No auth

## Cookies without SameSite
```bash
curl -skD - https://<TARGET>/ -o /dev/null | grep -i '^set-cookie:' | grep -vi 'samesite='
```
**Tool:** curl · **Platform:** Any · **Tags:** Cookies, SameSite · **Context:** No auth

**Related:** [CORS, CSRF & Headers](cors-csrf-headers.md) · [Authentication](authentication.md) · [XSS](xss.md)
