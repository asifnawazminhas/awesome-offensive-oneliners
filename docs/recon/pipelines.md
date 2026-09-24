# Recon pipelines

Small pipelines that move from one discovery stage to the next.

<div class="ol-section-kicker"><span>RECON</span></div>

## Domain to live web services

```bash
subfinder -d <DOMAIN> -silent | dnsx -silent | httpx -silent -status-code -title -tech-detect
```

**Tool:** subfinder + dnsx + httpx · **Platform:** Linux/macOS · **Tags:** Pipeline


## Domain to open web ports

```bash
subfinder -d <DOMAIN> -silent | naabu -top-ports 1000 -silent | httpx -silent -status-code -title
```

**Tool:** subfinder + naabu + httpx · **Platform:** Linux/macOS · **Tags:** Pipeline


## Live sites to URLs

```bash
subfinder -d <DOMAIN> -silent | httpx -silent | katana -silent | uro | sort -u
```

**Tool:** subfinder + httpx + katana + uro · **Platform:** Linux/macOS · **Tags:** Pipeline


## URLs to parameterized candidates

```bash
katana -u <URL> -silent | uro | grep '=' | sort -u
```

**Tool:** katana + uro · **Platform:** Linux/macOS


## URLs to reflected parameter candidates

```bash
cat urls.txt | grep '=' | uro | kxss
```

**Tool:** uro + kxss · **Platform:** Linux/macOS


## Subdomains to screenshots

```bash
subfinder -d <DOMAIN> -silent | httpx -silent -screenshot -system-chrome
```

**Tool:** subfinder + httpx · **Platform:** Linux/macOS
