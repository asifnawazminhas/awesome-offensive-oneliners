# Web Authentication

Authentication and token inspection one-liners.

### Basic auth request

```bash
curl -sk -u <USER>:<PASSWORD> https://<TARGET>/<PATH>
```

**Tool:** curl · **Platform:** Linux/macOS · **Tags:** Authentication, Basic Auth

### Bearer token request

```bash
curl -sk -H "Authorization: Bearer <TOKEN>" https://<TARGET>/<PATH>
```

**Tool:** curl · **Platform:** Linux/macOS · **Tags:** Authentication, Bearer

### Cookie-authenticated request

```bash
curl -sk -H "Cookie: <NAME>=<VALUE>" https://<TARGET>/<PATH>
```

**Tool:** curl · **Platform:** Linux/macOS · **Tags:** Authentication, Cookie

### OIDC discovery

```bash
curl -sk https://<TARGET>/.well-known/openid-configuration | jq
```

**Tool:** curl + jq · **Platform:** Linux/macOS · **Tags:** OIDC, Discovery

### JWKS endpoint

```bash
curl -sk https://<TARGET>/.well-known/jwks.json | jq
```

**Tool:** curl + jq · **Platform:** Linux/macOS · **Tags:** JWT, JWKS

### Decode JWT payload

```bash
python3 -c "import base64,json,sys; p=sys.argv[1].split('.')[1]; print(json.dumps(json.loads(base64.urlsafe_b64decode(p+'='*(-len(p)%4))),indent=2))" <JWT>
```

**Tool:** Python · **Platform:** Linux/macOS · **Tags:** JWT, Decode

