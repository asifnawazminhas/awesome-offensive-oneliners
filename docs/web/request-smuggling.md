# HTTP Request Smuggling

One-liners for protocol/version checks and fast smuggling-oriented triage.

<div class="ol-section-kicker"><span>WEB</span><strong>5 one-liners</strong></div>

## Force HTTP/1.1

```bash
curl -sk --http1.1 -I https://<TARGET>/
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, HTTP, smuggling · **Context:** No auth · **Noise:** Moderate

## Force HTTP/2

```bash
curl -sk --http2 -I https://<TARGET>/
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, HTTP2, smuggling · **Context:** No auth · **Noise:** Moderate

## Inspect proxy headers

```bash
curl -skI https://<TARGET>/ | grep -Ei "^(via|server|x-cache|x-served-by|x-forwarded|cf-|x-varnish)"
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, proxy, headers · **Context:** No auth · **Noise:** Moderate

## OPTIONS for intermediary clues

```bash
curl -sk -X OPTIONS -i https://<TARGET>/
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, methods, smuggling · **Context:** No auth · **Noise:** Moderate

## Nuclei HTTP smuggling templates

```bash
nuclei -u https://<TARGET> -tags request-smuggling -silent
```

**Tool:** Nuclei · **Platform:** Linux · **Tags:** Web, smuggling · **Context:** No auth · **Noise:** Moderate

---

**Related:** HTTP Methods · Cache Poisoning · TLS & Certificates
