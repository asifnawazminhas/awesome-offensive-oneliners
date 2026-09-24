---
hide:
  - toc
---
# GraphQL Introspection Variants

Short GraphQL discovery and introspection one-liners.

<div class="ol-section-kicker"><span>WEB</span><strong>GRAPHQL</strong></div>

## Typename baseline
```bash
curl -sk https://<TARGET>/graphql -H 'Content-Type: application/json' -d '{"query":"{__typename}"}'
```
**Tool:** curl · **Platform:** Any · **Tags:** GraphQL, Baseline · **Context:** No auth · **Noise:** Moderate

## Query type fields
```bash
curl -sk https://<TARGET>/graphql -H 'Content-Type: application/json' -d '{"query":"{__schema{queryType{fields{name}}}}"}'
```
**Tool:** curl · **Platform:** Any · **Tags:** GraphQL, Introspection · **Context:** No auth · **Noise:** Moderate

## Mutation type fields
```bash
curl -sk https://<TARGET>/graphql -H 'Content-Type: application/json' -d '{"query":"{__schema{mutationType{fields{name}}}}"}'
```
**Tool:** curl · **Platform:** Any · **Tags:** GraphQL, Mutation · **Context:** No auth · **Noise:** Moderate

## Types and fields
```bash
curl -sk https://<TARGET>/graphql -H 'Content-Type: application/json' -d '{"query":"{__schema{types{name fields{name}}}}"}'
```
**Tool:** curl · **Platform:** Any · **Tags:** GraphQL, Schema · **Context:** No auth · **Noise:** Moderate

## GET-based GraphQL
```bash
curl -skG https://<TARGET>/graphql --data-urlencode 'query={__typename}'
```
**Tool:** curl · **Platform:** Any · **Tags:** GraphQL, GET · **Context:** No auth · **Noise:** Moderate

**Related:** [APIs & GraphQL](api-graphql.md) · [API Authorization](api-authz.md) · [Authentication](authentication.md)
