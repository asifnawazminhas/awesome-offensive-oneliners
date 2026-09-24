# curl & jq

Small HTTP and JSON one-liners that are useful everywhere.

### GET JSON

```bash
curl -sk https://<TARGET>/api | jq
```

**Tool:** curl + jq · **Platform:** Linux/macOS · **Tags:** HTTP, JSON · **Context:** User

### POST JSON

```bash
curl -sk -X POST https://<TARGET>/api -H "Content-Type: application/json" -d '{"key":"value"}' | jq
```

**Tool:** curl + jq · **Platform:** Linux/macOS · **Tags:** HTTP, JSON · **Context:** User

### Extract JSON field

```bash
curl -sk https://<TARGET>/api | jq -r '.items[].name'
```

**Tool:** curl + jq · **Platform:** Linux/macOS · **Tags:** JSON, Parsing · **Context:** User

### Save response headers

```bash
curl -skD headers.txt https://<TARGET>/ -o body.html
```

**Tool:** curl · **Platform:** Linux/macOS · **Tags:** HTTP, Headers · **Context:** User

### Send custom Host header

```bash
curl -ski https://<IP>/ -H "Host: <HOSTNAME>"
```

**Tool:** curl · **Platform:** Linux/macOS · **Tags:** HTTP, Host Header · **Context:** User

### Send Referer header

```bash
curl -ski https://<TARGET>/ -H "Referer: https://example.com/"
```

**Tool:** curl · **Platform:** Linux/macOS · **Tags:** HTTP, Referer · **Context:** User

---

**Related:** [Overview](./) · [Certipy Bloodhound](certipy-bloodhound.md) · [Dnsx](dnsx.md)
