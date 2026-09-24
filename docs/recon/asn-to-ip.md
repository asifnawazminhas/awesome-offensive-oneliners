# ASN to IP Pipelines

One-liners for converting ASNs into target IPs and probing resulting services.

<div class="ol-section-kicker"><span>REC</span><strong>4 one-liners</strong></div>

## ASN prefixes to file

```bash
curl -s "https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS<ASN>" | jq -r ' .data.prefixes[].prefix ' > cidrs.txt
```

**Tool:** curl,jq · **Platform:** Any · **Tags:** Recon, ASN, CIDR · **Context:** No auth

## CIDRs to hosts

```bash
cat cidrs.txt | mapcidr -silent > ips.txt
```

**Tool:** mapcidr · **Platform:** Linux · **Tags:** Recon, CIDR, IPs · **Context:** No auth

## ASN to HTTP services

```bash
curl -s "https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS<ASN>" | jq -r ' .data.prefixes[].prefix ' | mapcidr -silent | httpx -silent
```

**Tool:** RIPE,mapcidr,httpx · **Platform:** Linux · **Tags:** Recon, ASN, HTTP · **Context:** No auth

## ASN to common web ports

```bash
cat cidrs.txt | mapcidr -silent | naabu -p 80,443,8080,8443 -silent
```

**Tool:** mapcidr,naabu · **Platform:** Linux · **Tags:** Recon, ASN, ports · **Context:** No auth

---

**Related:** ASN & CIDR · HTTP Probing · Ports & Services
