# Favicon Hunting

One-liners for hashing favicons and pivoting on repeated web application fingerprints.

<div class="ol-section-kicker"><span>REC</span><strong>5 one-liners</strong></div>

## Download favicon

```bash
curl -sk https://<TARGET>/favicon.ico -o favicon.ico
```

**Tool:** curl · **Platform:** Any · **Tags:** Recon, favicon · **Context:** No auth

## MD5 favicon hash

```bash
md5sum favicon.ico
```

**Tool:** md5sum · **Platform:** Linux · **Tags:** Recon, favicon, hash · **Context:** No auth

## MMH3 hash for Shodan

```bash
python3 -c "import mmh3,base64;print(mmh3.hash(base64.encodebytes(open("favicon.ico","rb").read())))"
```

**Tool:** Python,mmh3 · **Platform:** Linux · **Tags:** Recon, favicon, Shodan · **Context:** No auth

## Shodan favicon search

```bash
shodan search "http.favicon.hash:<MMH3>"
```

**Tool:** Shodan · **Platform:** Any · **Tags:** Recon, favicon, Shodan · **Context:** No auth

## httpx favicon hash

```bash
httpx -u https://<TARGET> -favicon -silent
```

**Tool:** httpx · **Platform:** Linux · **Tags:** Recon, favicon · **Context:** No auth

---

**Related:** Shodan · Technologies · Screenshots
