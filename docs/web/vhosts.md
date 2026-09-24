# Virtual Host Discovery

Name-based virtual-host discovery one-liners for hosts that share the same IP address.

<div class="ol-section-kicker"><span>WEB</span><strong>VHOST</strong></div>

## ffuf Host-header fuzzing

```bash
ffuf -u http://<IP>/ -H "Host: FUZZ.<DOMAIN>" -w <WORDLIST> -ac
```

**Tool:** ffuf · **Platform:** Linux/macOS · **Tags:** VHost, Host Header, Discovery

## ffuf vhost with response-size filter

```bash
ffuf -u http://<IP>/ -H "Host: FUZZ.<DOMAIN>" -w <WORDLIST> -fs <BASELINE_SIZE>
```

**Tool:** ffuf · **Platform:** Linux/macOS · **Tags:** VHost, Filtering

## ffuf vhost interesting status codes

```bash
ffuf -u https://<IP>/ -H "Host: FUZZ.<DOMAIN>" -w <WORDLIST> -mc 200,204,301,302,307,401,403 -ac
```

**Tool:** ffuf · **Platform:** Linux/macOS · **Tags:** VHost, HTTP

## Gobuster vhost mode

```bash
gobuster vhost -u https://<DOMAIN> -w <WORDLIST> --append-domain
```

**Tool:** gobuster · **Platform:** Linux/macOS · **Tags:** VHost, Discovery

## wfuzz Host-header discovery

```bash
wfuzz -c -w <WORDLIST> -H "Host: FUZZ.<DOMAIN>" --hh <BASELINE_CHARS> http://<IP>/
```

**Tool:** wfuzz · **Platform:** Linux/macOS · **Tags:** VHost, Host Header

## Manual curl vhost probe

```bash
curl -sk -H 'Host: <VHOST>.<DOMAIN>' http://<IP>/ -o /dev/null -w '%{http_code} %{size_download}\n'
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** VHost, Manual Validation

## Compare default and candidate response hashes

```bash
for h in invalid.<DOMAIN> admin.<DOMAIN>; do printf '%s ' "$h"; curl -sk -H "Host: $h" http://<IP>/ | sha256sum | cut -d' ' -f1; done
```

**Tool:** curl + sha256sum · **Platform:** Linux/macOS · **Tags:** VHost, Differential

## Resolve discovered vhosts locally

```bash
while read -r h; do printf '%s\t%s\n' '<IP>' "$h"; done < vhosts.txt
```

**Tool:** shell · **Platform:** Linux/macOS · **Tags:** Hosts File, Validation
