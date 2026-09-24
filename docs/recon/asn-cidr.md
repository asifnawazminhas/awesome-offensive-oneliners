# ASN & CIDR Discovery

One-liners for turning organization names, domains and ASNs into routable ranges.

<div class="ol-section-kicker"><span>REC</span><strong>5 one-liners</strong></div>

## WHOIS ASN lookup

```bash
whois -h whois.radb.net -- "-i origin AS<ASN>" | grep -Eo "([0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]+" | sort -u
```

**Tool:** whois · **Platform:** Linux · **Tags:** Recon, ASN, CIDR · **Context:** No auth · **Noise:** Moderate

## BGPView ASN prefixes

```bash
curl -s https://api.bgpview.io/asn/<ASN>/prefixes | jq -r ' .data.ipv4_prefixes[].prefix, .data.ipv6_prefixes[].prefix '
```

**Tool:** curl,jq · **Platform:** Any · **Tags:** Recon, ASN, CIDR · **Context:** No auth · **Noise:** Moderate

## RIPE ASN prefixes

```bash
curl -s "https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS<ASN>" | jq -r ' .data.prefixes[].prefix '
```

**Tool:** curl,jq · **Platform:** Any · **Tags:** Recon, ASN, RIPE · **Context:** No auth · **Noise:** Moderate

## ASN from IP

```bash
whois <IP> | grep -Ei "origin|aut-num" | head
```

**Tool:** whois · **Platform:** Any · **Tags:** Recon, ASN · **Context:** No auth · **Noise:** Moderate

## CIDR host expansion

```bash
mapcidr -cidr <CIDR> -silent
```

**Tool:** mapcidr · **Platform:** Linux · **Tags:** Recon, CIDR · **Context:** No auth · **Noise:** Moderate

---

**Related:** ASN to IP · Ports & Services · Cloud Assets
