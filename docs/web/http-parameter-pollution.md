---
hide:
  - toc
---
# HTTP Parameter Pollution

Duplicate-parameter probes for parser differences and precedence.

<div class="ol-section-kicker"><span>WEB</span><strong>HPP</strong></div>

## Duplicate GET parameter
```bash
curl -sk 'https://<TARGET>/endpoint?id=1&id=2'
```
**Tool:** curl · **Platform:** Any · **Tags:** HPP, GET · **Context:** No auth

## Reverse duplicate order
```bash
curl -sk 'https://<TARGET>/endpoint?id=2&id=1'
```
**Tool:** curl · **Platform:** Any · **Tags:** HPP, Parser · **Context:** No auth

## Duplicate POST parameter
```bash
curl -sk -X POST https://<TARGET>/endpoint -d 'id=1&id=2'
```
**Tool:** curl · **Platform:** Any · **Tags:** HPP, POST · **Context:** No auth

## Array-style duplicate
```bash
curl -sk 'https://<TARGET>/endpoint?id[]=1&id[]=2'
```
**Tool:** curl · **Platform:** Any · **Tags:** Arrays, HPP · **Context:** No auth

## Mixed query and body
```bash
curl -sk -X POST 'https://<TARGET>/endpoint?id=1' -d 'id=2'
```
**Tool:** curl · **Platform:** Any · **Tags:** Query, Body, HPP · **Context:** No auth

**Related:** [Parameters](parameters.md) · [API Authorization](api-authz.md) · [Injection](injection.md)
