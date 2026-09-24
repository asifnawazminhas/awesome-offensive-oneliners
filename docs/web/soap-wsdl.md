---
hide:
  - toc
---
# SOAP & WSDL Enumeration

Quick SOAP and WSDL discovery one-liners.

<div class="ol-section-kicker"><span>WEB</span><strong>SOAP</strong></div>

## Common WSDL query
```bash
curl -sk 'https://<TARGET>/service?wsdl'
```
**Tool:** curl · **Platform:** Any · **Tags:** SOAP, WSDL · **Context:** No auth · **Noise:** Moderate

## WSDL path probe
```bash
curl -skI https://<TARGET>/service.wsdl
```
**Tool:** curl · **Platform:** Any · **Tags:** WSDL, Discovery · **Context:** No auth · **Noise:** Moderate

## Discover WSDL references
```bash
curl -sk https://<TARGET>/ | grep -Eoi 'https?://[^" ]+\.wsdl|[^" ]+\?wsdl' | sort -u
```
**Tool:** curl/grep · **Platform:** Linux/macOS · **Tags:** WSDL, Discovery · **Context:** No auth · **Noise:** Moderate

## SOAPAction baseline
```bash
curl -sk -X POST https://<TARGET>/service -H 'Content-Type: text/xml; charset=utf-8' -H 'SOAPAction: "<ACTION>"' --data-binary @request.xml
```
**Tool:** curl · **Platform:** Any · **Tags:** SOAP, SOAPAction · **Context:** No auth · **Noise:** Moderate

## SOAP 1.2 baseline
```bash
curl -sk -X POST https://<TARGET>/service -H 'Content-Type: application/soap+xml; charset=utf-8; action="<ACTION>"' --data-binary @request.xml
```
**Tool:** curl · **Platform:** Any · **Tags:** SOAP, SOAP 1.2 · **Context:** No auth · **Noise:** Moderate

**Related:** [XXE](xxe.md) · [JSON / XML Content-Type Switching](content-type-switching.md) · [APIs & GraphQL](api-graphql.md)
