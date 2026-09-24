# Certificate SAN Discovery

One-liners for extracting SANs and pivoting from TLS certificates to hostnames.

<div class="ol-section-kicker"><span>REC</span><strong>4 one-liners</strong></div>

## OpenSSL SAN extraction

```bash
echo | openssl s_client -connect <TARGET>:443 -servername <TARGET> 2>/dev/null | openssl x509 -noout -ext subjectAltName | grep -Eo "DNS:[^, ]+" | cut -d: -f2 | sort -u
```

**Tool:** OpenSSL · **Platform:** Any · **Tags:** Recon, TLS, SAN · **Context:** No auth · **Noise:** Quiet

## httpx certificate SANs

```bash
httpx -u https://<TARGET> -tls-grab -json -silent | jq -r ' .tls.subject_an[]? '
```

**Tool:** httpx,jq · **Platform:** Linux · **Tags:** Recon, TLS, SAN · **Context:** No auth · **Noise:** Quiet

## crt.sh domain SANs

```bash
curl -s "https://crt.sh/?q=%25.<DOMAIN>&output=json" | jq -r ' .[].name_value ' | tr "\r" "\n" | sed 's/^\*\.//' | sort -u
```

**Tool:** curl,jq · **Platform:** Any · **Tags:** Recon, CT, SAN · **Context:** No auth · **Noise:** Quiet

## Nmap certificate SANs

```bash
nmap -Pn -p443 --script ssl-cert <TARGET>
```

**Tool:** Nmap · **Platform:** Linux · **Tags:** Recon, TLS, SAN · **Context:** No auth · **Noise:** Quiet

---

**Related:** TLS & Certificates · Passive Subdomains · Shodan
