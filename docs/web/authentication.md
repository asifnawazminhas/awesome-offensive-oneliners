# Authentication and sessions

Fast checks around login flows, cookies, headers and sessions.

<div class="ol-section-kicker"><span>WEB</span></div>

## Inspect response cookies

```bash
curl -skI https://<TARGET>/login | grep -i set-cookie
```

**Tool:** curl · **Platform:** Cross-platform · **Context:** User


## Follow login redirects

```bash
curl -skIL https://<TARGET>/login | grep -Ei '^(HTTP/|location:|set-cookie:)'
```

**Tool:** curl · **Platform:** Cross-platform · **Context:** User


## POST form login

```bash
curl -sk -c cookies.txt -X POST https://<TARGET>/login -d 'username=<USER>&password=<PASSWORD>'
```

**Tool:** curl · **Platform:** Cross-platform · **Context:** User


## Reuse session cookie

```bash
curl -skb cookies.txt https://<TARGET>/account
```

**Tool:** curl · **Platform:** Cross-platform · **Context:** User


## Check security headers

```bash
curl -skI https://<TARGET> | grep -Ei 'strict-transport-security|content-security-policy|x-frame-options|x-content-type-options|referrer-policy'
```

**Tool:** curl · **Platform:** Cross-platform · **Context:** No auth


## Compare authenticated and unauthenticated status

```bash
for c in "" "-b cookies.txt"; do eval curl -sk -o /dev/null -w '%{http_code} %{size_download}\n' $c https://<TARGET>/admin; done
```

**Tool:** curl · **Platform:** Linux/macOS · **Context:** User

---

**Related:** [Overview](./) · [Api Graphql](api-graphql.md) · [Cache](cache.md)
