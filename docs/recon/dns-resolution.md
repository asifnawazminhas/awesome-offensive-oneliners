# DNS resolution

Resolve, validate and inspect discovered names.

<div class="ol-section-kicker"><span>RECON</span></div>

## Resolve subdomains with dnsx

```bash
dnsx -l subdomains.txt -silent -a -resp
```

**Tool:** dnsx · **Platform:** Linux/macOS


## Keep only resolvable names

```bash
dnsx -l subdomains.txt -silent > resolved.txt
```

**Tool:** dnsx · **Platform:** Linux/macOS


## Resolve A records

```bash
while read -r h; do dig +short A "$h" | sed "s#^#$h #"; done < subdomains.txt
```

**Tool:** dig · **Platform:** Linux/macOS


## Enumerate nameservers

```bash
dig +short NS <DOMAIN>
```

**Tool:** dig · **Platform:** Cross-platform


## Enumerate MX records

```bash
dig +short MX <DOMAIN>
```

**Tool:** dig · **Platform:** Cross-platform


## Enumerate TXT records

```bash
dig +short TXT <DOMAIN>
```

**Tool:** dig · **Platform:** Cross-platform


## Find domain controllers via SRV

```bash
dig +short SRV _ldap._tcp.dc._msdcs.<DOMAIN>
```

**Tool:** dig · **Platform:** Cross-platform · **Tags:** AD, SRV


## Reverse lookup a network

```bash
dnsx -l ips.txt -silent -ptr -resp
```

**Tool:** dnsx · **Platform:** Linux/macOS


## Wildcard check

```bash
for i in {1..3}; do dig +short "$(openssl rand -hex 6).<DOMAIN>"; done
```

**Tool:** dig + openssl · **Platform:** Linux/macOS · **Tags:** Wildcard
