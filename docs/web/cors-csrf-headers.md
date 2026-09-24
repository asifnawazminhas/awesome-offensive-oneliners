# CORS, CSRF and headers

Fast policy checks without turning the page into a tutorial.

<div class="ol-section-kicker"><span>WEB</span></div>

## CORS arbitrary Origin check

```bash
curl -skI https://<TARGET>/ -H 'Origin: https://example.invalid' | grep -Ei 'access-control-allow-origin|access-control-allow-credentials'
```

**Tool:** curl · **Platform:** Cross-platform


## CORS null Origin check

```bash
curl -skI https://<TARGET>/ -H 'Origin: null' | grep -Ei 'access-control-allow-origin|access-control-allow-credentials'
```

**Tool:** curl · **Platform:** Cross-platform


## Preflight check

```bash
curl -sk -X OPTIONS https://<TARGET>/api/endpoint -H 'Origin: https://example.invalid' -H 'Access-Control-Request-Method: POST' -i
```

**Tool:** curl · **Platform:** Cross-platform


## Cookie SameSite flags

```bash
curl -skI https://<TARGET>/ | grep -i set-cookie
```

**Tool:** curl · **Platform:** Cross-platform


## Clickjacking header check

```bash
curl -skI https://<TARGET>/ | grep -Ei 'x-frame-options|frame-ancestors'
```

**Tool:** curl · **Platform:** Cross-platform
