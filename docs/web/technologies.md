# Technology fingerprinting

Identify common frameworks, CMS products and management interfaces quickly.

<div class="ol-section-kicker"><span>WEB</span></div>

## httpx technology detection

```bash
httpx -l urls.txt -silent -status-code -title -tech-detect
```

**Tool:** httpx · **Platform:** Linux/macOS · **Context:** No auth


## WhatWeb fingerprint

```bash
whatweb -a 3 https://<TARGET>
```

**Tool:** WhatWeb · **Platform:** Linux/macOS · **Context:** No auth


## Nuclei technology tags

```bash
nuclei -l urls.txt -tags tech -silent
```

**Tool:** nuclei · **Platform:** Linux/macOS · **Context:** No auth


## Wappalyzer CLI

```bash
wappalyzer https://<TARGET>
```

**Tool:** Wappalyzer · **Platform:** Cross-platform · **Context:** No auth


## Server headers

```bash
curl -skI https://<TARGET> | grep -Ei '^(server|x-powered-by|via|x-generator|x-aspnet-version):'
```

**Tool:** curl · **Platform:** Cross-platform · **Context:** No auth

---

**Related:** [Overview](./) · [Ssrf Ssti](ssrf-ssti.md) · [Tls Certificates](tls-certificates.md)
