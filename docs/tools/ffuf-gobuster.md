# ffuf and Gobuster

High-frequency discovery commands for content, parameters and virtual hosts.

<div class="ol-section-kicker"><span>TOOLS</span></div>

## ffuf directories

```bash
ffuf -w <WORDLIST> -u https://<TARGET>/FUZZ -ac
```

**Tool:** ffuf · **Platform:** Linux/macOS


## ffuf vhosts

```bash
ffuf -w <WORDLIST> -u https://<TARGET>/ -H "Host: FUZZ.<DOMAIN>" -ac
```

**Tool:** ffuf · **Platform:** Linux/macOS


## ffuf GET parameters

```bash
ffuf -w <WORDLIST> -u 'https://<TARGET>/page?FUZZ=test' -ac
```

**Tool:** ffuf · **Platform:** Linux/macOS


## Gobuster directories

```bash
gobuster dir -u https://<TARGET> -w <WORDLIST> -k
```

**Tool:** gobuster · **Platform:** Linux/macOS


## Gobuster vhosts

```bash
gobuster vhost -u https://<TARGET> -w <WORDLIST> --append-domain
```

**Tool:** gobuster · **Platform:** Linux/macOS
