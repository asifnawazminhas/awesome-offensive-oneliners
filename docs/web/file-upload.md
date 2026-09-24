# File Upload Testing

One-liners for quickly probing upload handlers, MIME checks and resulting file paths.

<div class="ol-section-kicker"><span>WEB</span><strong>6 one-liners</strong></div>

## Multipart upload with curl

```bash
curl -sk -F "file=@<FILE>" https://<TARGET>/<UPLOAD_ENDPOINT>
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, file upload · **Context:** Authenticated · **Noise:** Moderate

## Override multipart MIME type

```bash
curl -sk -F "file=@<FILE>;type=image/jpeg" https://<TARGET>/<UPLOAD_ENDPOINT>
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, file upload, MIME · **Context:** Authenticated · **Noise:** Moderate

## Custom filename in multipart

```bash
curl -sk -F "file=@<FILE>;filename=<NAME>" https://<TARGET>/<UPLOAD_ENDPOINT>
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, file upload, filename · **Context:** Authenticated · **Noise:** Moderate

## Upload with bearer token

```bash
curl -sk -H "Authorization: Bearer <TOKEN>" -F "file=@<FILE>" https://<TARGET>/<UPLOAD_ENDPOINT>
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, file upload, API · **Context:** Authenticated · **Noise:** Moderate

## Probe common upload paths

```bash
ffuf -u https://<TARGET>/FUZZ -w <WORDLIST> -mc 200,301,302,401,403
```

**Tool:** ffuf · **Platform:** Linux · **Tags:** Web, file upload, discovery · **Context:** No auth · **Noise:** Moderate

## Check uploaded file URL

```bash
curl -skI https://<TARGET>/<UPLOAD_PATH>/<NAME>
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, file upload, validation · **Context:** No auth · **Noise:** Moderate

---

**Related:** Content Discovery · HTTP Methods · Authentication
