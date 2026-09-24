# Passive subdomain discovery

Fast passive discovery using the most common tools and API-backed sources.

<div class="ol-section-kicker"><span>RECON</span></div>

## Subfinder basic

```bash
subfinder -d <DOMAIN> -silent
```

**Tool:** subfinder · **Platform:** Linux/macOS · **Tags:** Subdomains, Passive

Fast passive subdomain enumeration.


## Subfinder all configured sources

```bash
subfinder -d <DOMAIN> -all -silent
```

**Tool:** subfinder · **Platform:** Linux/macOS · **Tags:** API, Passive

Use every configured provider, including API-backed sources.


## Subfinder recursive sources

```bash
subfinder -d <DOMAIN> -recursive -silent
```

**Tool:** subfinder · **Platform:** Linux/macOS · **Tags:** Recursive, Passive


## Subfinder save output

```bash
subfinder -d <DOMAIN> -silent -o subfinder.txt
```

**Tool:** subfinder · **Platform:** Linux/macOS


## Amass passive

```bash
amass enum -passive -d <DOMAIN> -o amass.txt
```

**Tool:** Amass · **Platform:** Linux/macOS · **Tags:** OSINT, Passive


## Assetfinder only subdomains

```bash
assetfinder --subs-only <DOMAIN> | sort -u
```

**Tool:** assetfinder · **Platform:** Linux/macOS


## Findomain quiet enumeration

```bash
findomain -t <DOMAIN> -q | sort -u
```

**Tool:** findomain · **Platform:** Linux/macOS


## Certificate Transparency via crt.sh

```bash
curl -s 'https://crt.sh/?q=%25.<DOMAIN>&output=json' | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u
```

**Tool:** curl + jq · **Platform:** Linux/macOS · **Tags:** CT, Certificates


## GitHub code search for domain references

```bash
gh search code '<DOMAIN>' --limit 100 --json repository,path,url | jq -r '.[] | [.repository.nameWithOwner,.path,.url] | @tsv'
```

**Tool:** GitHub CLI · **Platform:** Cross-platform · **Tags:** OSINT, GitHub



## List Subfinder sources

```bash
subfinder -ls
```

**Tool:** subfinder · **Platform:** Linux/macOS · **Tags:** Sources, API

Shows built-in passive sources so you can see which API-backed providers are available.

## Run selected API-backed sources

```bash
subfinder -d <DOMAIN> -s shodan,censys,virustotal,github -silent
```

**Tool:** subfinder · **Platform:** Linux/macOS · **Tags:** API, Passive

Uses selected providers configured in `~/.config/subfinder/provider-config.yaml`.

## Combine passive sources

```bash
cat subfinder.txt amass.txt findomain.txt 2>/dev/null | sed '/^$/d' | sort -u > subdomains.txt
```

**Tool:** coreutils · **Platform:** Linux/macOS · **Tags:** Pipeline
