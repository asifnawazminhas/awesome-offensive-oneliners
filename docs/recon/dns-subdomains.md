# DNS & Subdomains

Subdomain enumeration and DNS resolution one-liners.

### Passive subdomains with subfinder

```bash
subfinder -d <DOMAIN> -silent
```

**Tool:** subfinder · **Platform:** Linux/macOS · **Tags:** Subdomains, Passive

### Amass passive enumeration

```bash
amass enum -passive -d <DOMAIN>
```

**Tool:** Amass · **Platform:** Linux/macOS · **Tags:** Subdomains, Passive

### DNS A record

```bash
dig +short A <HOSTNAME>
```

**Tool:** dig · **Platform:** Linux/macOS · **Tags:** DNS, A

### DNS MX records

```bash
dig +short MX <DOMAIN>
```

**Tool:** dig · **Platform:** Linux/macOS · **Tags:** DNS, MX

### DNS TXT records

```bash
dig +short TXT <DOMAIN>
```

**Tool:** dig · **Platform:** Linux/macOS · **Tags:** DNS, TXT

### Resolve list with dnsx

```bash
dnsx -l subdomains.txt -silent -a -resp
```

**Tool:** dnsx · **Platform:** Linux/macOS · **Tags:** DNS, Resolution

