# Passive Source Combinations

High-coverage passive subdomain pipelines that combine multiple independent sources.

<div class="ol-section-kicker"><span>REC</span><strong>5 one-liners</strong></div>

## Subfinder + assetfinder

```bash
(subfinder -d <DOMAIN> -silent; assetfinder --subs-only <DOMAIN>) | sort -u
```

**Tool:** subfinder,assetfinder · **Platform:** Linux · **Tags:** Recon, subdomains, passive · **Context:** No auth

## Subfinder + Amass + crt.sh

```bash
(subfinder -d <DOMAIN> -silent; amass enum -passive -d <DOMAIN>; curl -s "https://crt.sh/?q=%25.<DOMAIN>&output=json" | jq -r ' .[].name_value ') | sed 's/^\*\.//' | sort -u
```

**Tool:** subfinder,Amass,crt.sh · **Platform:** Linux · **Tags:** Recon, subdomains, passive · **Context:** No auth

## Passive to DNS-resolved

```bash
(subfinder -d <DOMAIN> -silent; assetfinder --subs-only <DOMAIN>) | sort -u | dnsx -silent
```

**Tool:** subfinder,assetfinder,dnsx · **Platform:** Linux · **Tags:** Recon, subdomains, DNS · **Context:** No auth

## Passive to live HTTP

```bash
(subfinder -d <DOMAIN> -silent; amass enum -passive -d <DOMAIN>) | sort -u | dnsx -silent | httpx -silent -title -status-code -tech-detect
```

**Tool:** subfinder,Amass,dnsx,httpx · **Platform:** Linux · **Tags:** Recon, pipeline · **Context:** No auth

## Passive plus permutations

```bash
(subfinder -d <DOMAIN> -silent; assetfinder --subs-only <DOMAIN>) | sort -u | tee passive.txt | alterx -silent | dnsx -silent
```

**Tool:** subfinder,assetfinder,alterx,dnsx · **Platform:** Linux · **Tags:** Recon, pipeline, permutations · **Context:** No auth

---

**Related:** Passive Subdomains · Permutations · DNS Resolution
