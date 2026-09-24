# TLS & Certificates

TLS, certificate and SAN discovery one-liners for web targets.

<div class="ol-section-kicker"><span>WEB</span><strong>6 one-liners</strong></div>

## Show certificate subject and issuer

```bash
echo | openssl s_client -connect <TARGET>:443 -servername <TARGET> 2>/dev/null | openssl x509 -noout -subject -issuer -dates
```

**Tool:** OpenSSL · **Platform:** Any · **Tags:** TLS, certificate · **Context:** No auth · **Noise:** Moderate

## Extract SANs

```bash
echo | openssl s_client -connect <TARGET>:443 -servername <TARGET> 2>/dev/null | openssl x509 -noout -ext subjectAltName
```

**Tool:** OpenSSL · **Platform:** Any · **Tags:** TLS, SAN, recon · **Context:** No auth · **Noise:** Moderate

## Show certificate fingerprint

```bash
echo | openssl s_client -connect <TARGET>:443 -servername <TARGET> 2>/dev/null | openssl x509 -noout -fingerprint -sha256
```

**Tool:** OpenSSL · **Platform:** Any · **Tags:** TLS, fingerprint · **Context:** No auth · **Noise:** Moderate

## Enumerate TLS ciphers

```bash
nmap -Pn -p443 --script ssl-enum-ciphers <TARGET>
```

**Tool:** Nmap · **Platform:** Linux · **Tags:** TLS, ciphers · **Context:** No auth · **Noise:** Moderate

## Test TLS versions

```bash
for v in -tls1 -tls1_1 -tls1_2 -tls1_3; do echo | openssl s_client $v -connect <TARGET>:443 -servername <TARGET> 2>&1 | grep -m1 Protocol; done
```

**Tool:** OpenSSL · **Platform:** Any · **Tags:** TLS, versions · **Context:** No auth · **Noise:** Moderate

## httpx TLS metadata

```bash
httpx -u https://<TARGET> -tls-grab -silent
```

**Tool:** httpx · **Platform:** Linux · **Tags:** TLS, certificate, recon · **Context:** No auth · **Noise:** Moderate

---

**Related:** Certificate SAN Recon · Technologies · HTTP Probing
