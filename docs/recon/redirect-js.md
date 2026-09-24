---
hide:
  - toc
---
# Redirect Chains & Historical JavaScript

One-liners for redirect paths and archived JavaScript discovery.

<div class="ol-section-kicker"><span>REC</span><strong>HTTP</strong></div>

## curl redirect chain
```bash
curl -skIL https://<TARGET>/ | grep -Ei '^(HTTP/|location:)'
```
**Tool:** curl · **Platform:** Any · **Tags:** Redirects, HTTP · **Context:** No auth

## httpx redirect locations
```bash
httpx -l urls.txt -silent -status-code -location -follow-redirects
```
**Tool:** httpx · **Platform:** Linux/macOS · **Tags:** Redirects, HTTP · **Context:** No auth

## Historical JavaScript with gau
```bash
gau <DOMAIN> | grep -Ei '\.js($|\?)' | sort -u
```
**Tool:** gau · **Platform:** Linux/macOS · **Tags:** JavaScript, Historical URLs · **Context:** No auth

## Historical JavaScript with waybackurls
```bash
printf '%s\n' <DOMAIN> | waybackurls | grep -Ei '\.js($|\?)' | sort -u
```
**Tool:** waybackurls · **Platform:** Linux/macOS · **Tags:** JavaScript, Wayback · **Context:** No auth

## Live-check historical JS
```bash
gau <DOMAIN> | grep -Ei '\.js($|\?)' | sort -u | httpx -silent -mc 200
```
**Tool:** gau/httpx · **Platform:** Linux/macOS · **Tags:** JavaScript, Validation · **Context:** No auth

**Related:** [Historical URLs](urls-history.md) · [JavaScript](javascript.md) · [HTTP Probing](http-probing.md)
