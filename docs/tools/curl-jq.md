# curl & jq

Small HTTP and JSON one-liners that are useful everywhere.

### GET JSON

```bash
curl -sk https://<TARGET>/api | jq
```

**Tool:** curl + jq · **Platform:** Linux/macOS · **Tags:** HTTP, JSON

### POST JSON

```bash
curl -sk -X POST https://<TARGET>/api -H "Content-Type: application/json" -d '{"key":"value"}' | jq
```

**Tool:** curl + jq · **Platform:** Linux/macOS · **Tags:** HTTP, JSON

### Extract JSON field

```bash
curl -sk https://<TARGET>/api | jq -r '.items[].name'
```

**Tool:** curl + jq · **Platform:** Linux/macOS · **Tags:** JSON, Parsing

### Save response headers

```bash
curl -skD headers.txt https://<TARGET>/ -o body.html
```

**Tool:** curl · **Platform:** Linux/macOS · **Tags:** HTTP, Headers

### Send custom Host header

```bash
curl -ski https://<IP>/ -H "Host: <HOSTNAME>"
```

**Tool:** curl · **Platform:** Linux/macOS · **Tags:** HTTP, Host Header

### Send Referer header

```bash
curl -ski https://<TARGET>/ -H "Referer: https://example.com/"
```

**Tool:** curl · **Platform:** Linux/macOS · **Tags:** HTTP, Referer

