# HTTP probing

Turn DNS names and IPs into useful HTTP targets.

<div class="ol-section-kicker"><span>RECON</span></div>

## Probe live HTTP services

```bash
httpx -l subdomains.txt -silent -status-code -title -tech-detect
```

**Tool:** httpx · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate


## Probe common web ports

```bash
httpx -l subdomains.txt -ports 80,443,8080,8443,8000,8888 -silent -status-code -title
```

**Tool:** httpx · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate


## Follow redirects

```bash
httpx -l subdomains.txt -silent -follow-redirects -status-code -title -location
```

**Tool:** httpx · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate


## JSON output

```bash
httpx -l subdomains.txt -silent -json -o httpx.json
```

**Tool:** httpx · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate


## Show server and content length

```bash
httpx -l subdomains.txt -silent -server -content-length -status-code
```

**Tool:** httpx · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate


## Filter interesting status codes

```bash
httpx -l subdomains.txt -silent -mc 200,204,301,302,307,401,403,500 -status-code -title
```

**Tool:** httpx · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate


## Screenshot live hosts

```bash
httpx -l urls.txt -silent -screenshot -system-chrome
```

**Tool:** httpx · **Platform:** Linux/macOS · **Tags:** Screenshots · **Context:** No auth · **Noise:** Moderate

---

**Related:** [Overview](./) · [Favicon Hunting](favicon-hunting.md) · [Javascript](javascript.md)
