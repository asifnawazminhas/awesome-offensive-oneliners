---
hide:
  - toc
---

# Subdomain Enumeration

Passive, active and resolver-backed subdomain discovery one-liners.

<div class="ol-section-kicker"><span>RECON</span><strong>SUBDOMAINS</strong></div>

## Subfinder basic

```bash
subfinder -d <DOMAIN> -silent
```

**Tool:** subfinder · **Platform:** Linux/macOS · **Tags:** Passive, Subdomains · **Context:** No auth

## Subfinder all configured sources

```bash
subfinder -d <DOMAIN> -all -silent -o subfinder.txt
```

**Tool:** subfinder · **Platform:** Linux/macOS · **Tags:** API, Passive · **Context:** No auth

## Subfinder selected API-backed sources

```bash
subfinder -d <DOMAIN> -s shodan,censys,virustotal,github -silent
```

**Tool:** subfinder · **Platform:** Linux/macOS · **Tags:** API, Passive · **Context:** No auth

Configured provider keys live in `~/.config/subfinder/provider-config.yaml`.

## List Subfinder sources

```bash
subfinder -ls
```

**Tool:** subfinder · **Platform:** Linux/macOS · **Tags:** Sources, API · **Context:** No auth

## Subfinder recursive sources

```bash
subfinder -d <DOMAIN> -recursive -silent
```

**Tool:** subfinder · **Platform:** Linux/macOS · **Tags:** Recursive, Passive · **Context:** No auth

## Amass passive

```bash
amass enum -passive -d <DOMAIN> -o amass.txt
```

**Tool:** Amass · **Platform:** Linux/macOS · **Tags:** OSINT, Passive · **Context:** No auth

## Amass active brute-force

```bash
amass enum -active -brute -d <DOMAIN> -o amass-active.txt
```

**Tool:** Amass · **Platform:** Linux/macOS · **Tags:** Active, Brute Force · **Context:** No auth

## Assetfinder subdomains

```bash
assetfinder --subs-only <DOMAIN> | sort -u
```

**Tool:** assetfinder · **Platform:** Linux/macOS · **Context:** No auth

## Findomain quiet enumeration

```bash
findomain -t <DOMAIN> -q | sort -u
```

**Tool:** findomain · **Platform:** Linux/macOS · **Context:** No auth

## Certificate Transparency via crt.sh

```bash
curl -s 'https://crt.sh/?q=%25.<DOMAIN>&output=json' | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u
```

**Tool:** curl + jq · **Platform:** Linux/macOS · **Tags:** CT, Certificates · **Context:** No auth

## PureDNS brute-force

```bash
puredns bruteforce <SUBDOMAIN_WORDLIST> <DOMAIN> -r <RESOLVERS> -w puredns.txt
```

**Tool:** puredns · **Platform:** Linux/macOS · **Tags:** DNS, Brute Force · **Context:** No auth

## GitHub code search for domain references

```bash
gh search code '<DOMAIN>' --limit 100 --json repository,path,url | jq -r '.[] | [.repository.nameWithOwner,.path,.url] | @tsv'
```

**Tool:** GitHub CLI · **Platform:** Cross-platform · **Tags:** OSINT, GitHub · **Context:** No auth

## Combine multiple sources

```bash
(subfinder -d <DOMAIN> -silent; assetfinder --subs-only <DOMAIN>; findomain -t <DOMAIN> -q) | sort -u > all-subs.txt
```

**Tool:** Multiple · **Platform:** Linux/macOS · **Tags:** Pipeline, Dedupe · **Context:** No auth

## Subfinder directly to live HTTP services

```bash
subfinder -d <DOMAIN> -silent | httpx -silent -status-code -title -tech-detect
```

**Tool:** subfinder + httpx · **Platform:** Linux/macOS · **Tags:** Pipeline, HTTP · **Context:** No auth

---

**Related:** [Overview](./) · [Passive Combinations](passive-combinations.md) · [Permutations Advanced](permutations-advanced.md)
