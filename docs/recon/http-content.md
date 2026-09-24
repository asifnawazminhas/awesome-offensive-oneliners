# HTTP & Content Discovery

Fast service probing, crawling and content discovery commands.

### Probe HTTP services

```bash
httpx -l hosts.txt -silent -status-code -title -tech-detect
```

**Tool:** httpx · **Platform:** Linux/macOS · **Tags:** HTTP, Discovery

### Directory discovery

```bash
ffuf -u https://<TARGET>/FUZZ -w <WORDLIST> -mc all -fc 404
```

**Tool:** ffuf · **Platform:** Linux/macOS · **Tags:** Content Discovery

### Recursive gobuster

```bash
gobuster dir -u https://<TARGET>/ -w <WORDLIST> -x php,asp,aspx,jsp,txt,bak
```

**Tool:** Gobuster · **Platform:** Linux/macOS · **Tags:** Content Discovery

### Extract URLs from page

```bash
curl -sk https://<TARGET>/ | grep -Eo "https?://[^"' <>]+" | sort -u
```

**Tool:** curl + grep · **Platform:** Linux/macOS · **Tags:** URLs, Recon

### Katana crawl

```bash
katana -u https://<TARGET> -silent -jc -kf all
```

**Tool:** Katana · **Platform:** Linux/macOS · **Tags:** Crawling, JavaScript

