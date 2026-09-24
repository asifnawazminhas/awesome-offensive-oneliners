---
hide:
  - toc
---
# JSON / XML Content-Type Switching

Fast parser and content-negotiation checks.

<div class="ol-section-kicker"><span>WEB</span><strong>CONTENT TYPE</strong></div>

## JSON request
```bash
curl -sk -X POST https://<TARGET>/api/endpoint -H 'Content-Type: application/json' -d '{"id":1}'
```
**Tool:** curl · **Platform:** Any · **Tags:** JSON, API · **Context:** No auth · **Noise:** Moderate

## Form equivalent
```bash
curl -sk -X POST https://<TARGET>/api/endpoint -H 'Content-Type: application/x-www-form-urlencoded' -d 'id=1'
```
**Tool:** curl · **Platform:** Any · **Tags:** Form, Parser · **Context:** No auth · **Noise:** Moderate

## XML equivalent
```bash
curl -sk -X POST https://<TARGET>/api/endpoint -H 'Content-Type: application/xml' --data-binary '<root><id>1</id></root>'
```
**Tool:** curl · **Platform:** Any · **Tags:** XML, Parser · **Context:** No auth · **Noise:** Moderate

## JSON body with text/plain
```bash
curl -sk -X POST https://<TARGET>/api/endpoint -H 'Content-Type: text/plain' -d '{"id":1}'
```
**Tool:** curl · **Platform:** Any · **Tags:** Content Type, Parser · **Context:** No auth · **Noise:** Moderate

## Accept XML
```bash
curl -sk https://<TARGET>/api/endpoint -H 'Accept: application/xml'
```
**Tool:** curl · **Platform:** Any · **Tags:** Accept, XML · **Context:** No auth · **Noise:** Moderate

**Related:** [APIs & GraphQL](api-graphql.md) · [XXE](xxe.md) · [API Authorization](api-authz.md)
