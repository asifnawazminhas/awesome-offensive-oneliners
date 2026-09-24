# Web Recon

Quick web fingerprinting and discovery commands.

### HTTP fingerprinting

```bash
httpx -u https://<TARGET> -status-code -title -tech-detect -server -ip -cname
```

**Tool:** httpx · **Platform:** Linux/macOS · **Tags:** HTTP, Fingerprinting

### Headers only

```bash
curl -skI https://<TARGET>/
```

**Tool:** curl · **Platform:** Linux/macOS · **Tags:** HTTP, Headers

### Follow redirects

```bash
curl -skL -D - https://<TARGET>/ -o /dev/null
```

**Tool:** curl · **Platform:** Linux/macOS · **Tags:** HTTP, Redirects

### TLS certificate summary

```bash
openssl s_client -connect <TARGET>:443 -servername <TARGET> </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates -ext subjectAltName
```

**Tool:** OpenSSL · **Platform:** Linux/macOS · **Tags:** TLS, Certificate

### Robots and sitemap

```bash
for p in robots.txt sitemap.xml; do echo "=== $p ==="; curl -sk https://<TARGET>/$p; done
```

**Tool:** curl · **Platform:** Linux/macOS · **Tags:** Recon, Content

### Technology detection with whatweb

```bash
whatweb -a 3 https://<TARGET>
```

**Tool:** WhatWeb · **Platform:** Linux · **Tags:** Fingerprinting, Web

