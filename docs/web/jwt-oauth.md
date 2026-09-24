# JWT and OAuth/OIDC

Inspect tokens and common discovery metadata quickly.

<div class="ol-section-kicker"><span>WEB</span></div>

## Decode JWT header and payload

```bash
python3 -c "import base64,json,sys; t=sys.argv[1].split('.'); print(json.dumps(json.loads(base64.urlsafe_b64decode(t[0]+'==')),indent=2)); print(json.dumps(json.loads(base64.urlsafe_b64decode(t[1]+'==')),indent=2))" '<JWT>'
```

**Tool:** Python · **Platform:** Cross-platform · **Context:** No auth · **Noise:** Moderate


## OIDC discovery document

```bash
curl -sk https://<TARGET>/.well-known/openid-configuration | jq .
```

**Tool:** curl + jq · **Platform:** Cross-platform · **Context:** No auth · **Noise:** Moderate


## Fetch JWKS

```bash
curl -sk https://<TARGET>/.well-known/jwks.json | jq .
```

**Tool:** curl + jq · **Platform:** Cross-platform · **Context:** No auth · **Noise:** Moderate


## Extract OIDC endpoints

```bash
curl -sk https://<TARGET>/.well-known/openid-configuration | jq -r '.authorization_endpoint,.token_endpoint,.userinfo_endpoint,.jwks_uri'
```

**Tool:** curl + jq · **Platform:** Cross-platform · **Context:** User · **Noise:** Moderate


## Inspect JWT algorithm

```bash
python3 -c "import base64,json,sys; print(json.loads(base64.urlsafe_b64decode(sys.argv[1].split('.')[0]+'=='))['alg'])" '<JWT>'
```

**Tool:** Python · **Platform:** Cross-platform · **Context:** No auth · **Noise:** Moderate

---

**Related:** [Overview](./) · [Injection](injection.md) · [Open Redirect](open-redirect.md)
