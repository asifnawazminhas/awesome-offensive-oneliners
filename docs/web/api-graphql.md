# APIs and GraphQL

Quick endpoint, schema and HTTP-method checks.

<div class="ol-section-kicker"><span>WEB</span></div>

## Pretty-print JSON

```bash
curl -sk https://<TARGET>/api/endpoint | jq .
```

**Tool:** curl + jq · **Platform:** Cross-platform


## OPTIONS methods

```bash
curl -sk -X OPTIONS -i https://<TARGET>/api/endpoint
```

**Tool:** curl · **Platform:** Cross-platform


## JSON POST

```bash
curl -sk https://<TARGET>/api/endpoint -H 'Content-Type: application/json' -d '{"key":"value"}'
```

**Tool:** curl · **Platform:** Cross-platform


## Bearer token request

```bash
curl -sk https://<TARGET>/api/me -H 'Authorization: Bearer <TOKEN>'
```

**Tool:** curl · **Platform:** Cross-platform


## GraphQL typename probe

```bash
curl -sk https://<TARGET>/graphql -H 'Content-Type: application/json' --data '{"query":"{__typename}"}'
```

**Tool:** curl · **Platform:** Cross-platform


## GraphQL introspection type names

```bash
curl -sk https://<TARGET>/graphql -H 'Content-Type: application/json' --data '{"query":"{__schema{types{name}}}"}' | jq -r '.data.__schema.types[].name'
```

**Tool:** curl + jq · **Platform:** Cross-platform


## Discover API paths from URLs

```bash
cat urls.txt | grep -Ei '/(api|graphql|v[0-9]+)/' | sort -u
```

**Tool:** grep · **Platform:** Linux/macOS
