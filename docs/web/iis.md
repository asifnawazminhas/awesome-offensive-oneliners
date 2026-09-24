# IIS Enumeration

One-liners for fingerprinting IIS and common Microsoft web application surfaces.

<div class="ol-section-kicker"><span>WEB</span><strong>6 one-liners</strong></div>

## Server header

```bash
curl -skI https://<TARGET>/ | grep -i "^Server:"
```

**Tool:** curl · **Platform:** Any · **Tags:** IIS, fingerprinting · **Context:** No auth

## ASP.NET headers

```bash
curl -skI https://<TARGET>/ | grep -Ei "X-AspNet-Version|X-Powered-By|ASP.NET"
```

**Tool:** curl · **Platform:** Any · **Tags:** IIS, ASP.NET · **Context:** No auth

## Common IIS files

```bash
ffuf -u https://<TARGET>/FUZZ -w <IIS_WORDLIST> -mc 200,301,302,401,403
```

**Tool:** ffuf · **Platform:** Linux · **Tags:** IIS, content discovery · **Context:** No auth

## Shortname scan with nuclei

```bash
nuclei -u https://<TARGET> -tags iis -silent
```

**Tool:** Nuclei · **Platform:** Linux · **Tags:** IIS · **Context:** No auth

## WebDAV OPTIONS probe

```bash
curl -sk -i -X OPTIONS https://<TARGET>/ | grep -Ei "Allow:|DAV:"
```

**Tool:** curl · **Platform:** Any · **Tags:** IIS, WebDAV · **Context:** No auth

## IIS tilde character probe

```bash
curl -skI "https://<TARGET>/*~1*/a.aspx"
```

**Tool:** curl · **Platform:** Any · **Tags:** IIS, shortname · **Context:** No auth

---

**Related:** Content Discovery · HTTP Methods · Popular Software
