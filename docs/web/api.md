# API Testing

Fast API inspection and request-building commands.

### GET JSON

```bash
curl -sk https://<TARGET>/api/<PATH> | jq
```

**Tool:** curl + jq · **Platform:** Linux/macOS · **Tags:** API, JSON

### POST JSON

```bash
curl -sk -X POST https://<TARGET>/api/<PATH> -H "Content-Type: application/json" -d '{"key":"value"}'
```

**Tool:** curl · **Platform:** Linux/macOS · **Tags:** API, POST

### OPTIONS methods

```bash
curl -ski -X OPTIONS https://<TARGET>/api/<PATH>
```

**Tool:** curl · **Platform:** Linux/macOS · **Tags:** API, Methods

### Pretty-print OpenAPI

```bash
curl -sk https://<TARGET>/openapi.json | jq .
```

**Tool:** curl + jq · **Platform:** Linux/macOS · **Tags:** API, OpenAPI

### GraphQL introspection endpoint check

```bash
curl -sk -X POST https://<TARGET>/graphql -H "Content-Type: application/json" -d '{"query":"{__typename}"}'
```

**Tool:** curl · **Platform:** Linux/macOS · **Tags:** GraphQL, API

