# OpenSSL

<div class="ol-section-kicker"><span>TOOL</span><strong>OPENSSL</strong></div>

## Inspect TLS certificate
```bash
openssl s_client -connect <TARGET>:443 -servername <TARGET> </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates
```
**Tool:** OpenSSL · **Platform:** Linux/macOS · **Tags:** TLS, Certificate · **Context:** No auth

## Certificate SANs
```bash
openssl s_client -connect <TARGET>:443 -servername <TARGET> </dev/null 2>/dev/null | openssl x509 -noout -ext subjectAltName
```
**Tool:** OpenSSL · **Platform:** Linux/macOS · **Tags:** TLS, SAN · **Context:** No auth

## TLS 1.2 support
```bash
openssl s_client -connect <TARGET>:443 -servername <TARGET> -tls1_2 </dev/null
```
**Tool:** OpenSSL · **Platform:** Linux/macOS · **Tags:** TLS 1.2 · **Context:** No auth

## TLS 1.3 support
```bash
openssl s_client -connect <TARGET>:443 -servername <TARGET> -tls1_3 </dev/null
```
**Tool:** OpenSSL · **Platform:** Linux/macOS · **Tags:** TLS 1.3 · **Context:** No auth

## Show negotiated cipher
```bash
openssl s_client -connect <TARGET>:443 -servername <TARGET> </dev/null 2>/dev/null | grep -E 'Protocol|Cipher'
```
**Tool:** OpenSSL · **Platform:** Linux/macOS · **Tags:** TLS, Cipher · **Context:** No auth
