# naabu

Fast naabu one-liners for port discovery before deeper service enumeration.

<div class="ol-section-kicker"><span>TOOL</span><strong>5 one-liners</strong></div>

## Top ports

```bash
naabu -host <TARGET> -top-ports 100 -silent
```

**Tool:** naabu · **Platform:** Linux · **Tags:** ports, recon · **Context:** No auth

## Specific ports

```bash
naabu -host <TARGET> -p 80,443,445,3389,5985,5986 -silent
```

**Tool:** naabu · **Platform:** Linux · **Tags:** ports, recon · **Context:** No auth

## List input

```bash
naabu -list hosts.txt -top-ports 1000 -silent
```

**Tool:** naabu · **Platform:** Linux · **Tags:** ports, recon · **Context:** No auth

## Feed httpx

```bash
naabu -list hosts.txt -p 80,443,8080,8443 -silent | httpx -silent
```

**Tool:** naabu,httpx · **Platform:** Linux · **Tags:** ports, HTTP, pipeline · **Context:** No auth

## Exclude CDN

```bash
naabu -list hosts.txt -exclude-cdn -top-ports 1000 -silent
```

**Tool:** naabu · **Platform:** Linux · **Tags:** ports, CDN · **Context:** No auth

---

**Related:** Ports & Services · Nmap · httpx
