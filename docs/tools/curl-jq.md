# curl & jq

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

Small HTTP and JSON one-liners that are useful everywhere.

### GET JSON

```bash
curl -sk https://<TARGET>/api | jq
```

**Tool:** curl + jq · **Platform:** Linux/macOS · **Tags:** HTTP, JSON · **Context:** User · **Noise:** Moderate

### POST JSON

```bash
curl -sk -X POST https://<TARGET>/api -H "Content-Type: application/json" -d '{"key":"value"}' | jq
```

**Tool:** curl + jq · **Platform:** Linux/macOS · **Tags:** HTTP, JSON · **Context:** User · **Noise:** Moderate

### Extract JSON field

```bash
curl -sk https://<TARGET>/api | jq -r '.items[].name'
```

**Tool:** curl + jq · **Platform:** Linux/macOS · **Tags:** JSON, Parsing · **Context:** User · **Noise:** Moderate

### Save response headers

```bash
curl -skD headers.txt https://<TARGET>/ -o body.html
```

**Tool:** curl · **Platform:** Linux/macOS · **Tags:** HTTP, Headers · **Context:** User · **Noise:** Moderate

### Send custom Host header

```bash
curl -ski https://<IP>/ -H "Host: <HOSTNAME>"
```

**Tool:** curl · **Platform:** Linux/macOS · **Tags:** HTTP, Host Header · **Context:** User · **Noise:** Moderate

### Send Referer header

```bash
curl -ski https://<TARGET>/ -H "Referer: https://example.com/"
```

**Tool:** curl · **Platform:** Linux/macOS · **Tags:** HTTP, Referer · **Context:** User · **Noise:** Moderate

---

**Related:** [Overview](./) · [Certipy Bloodhound](certipy-bloodhound.md) · [Dnsx](dnsx.md)
