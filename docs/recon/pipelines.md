# Recon pipelines

Small pipelines that move from one discovery stage to the next.

<div class="ol-section-kicker"><span>RECON</span></div>

## Domain to live web services

```bash
subfinder -d <DOMAIN> -silent | dnsx -silent | httpx -silent -status-code -title -tech-detect
```

**Tool:** subfinder + dnsx + httpx · **Platform:** Linux/macOS · **Tags:** Pipeline · **Context:** No auth · **Noise:** Moderate


## Domain to open web ports

```bash
subfinder -d <DOMAIN> -silent | naabu -top-ports 1000 -silent | httpx -silent -status-code -title
```

**Tool:** subfinder + naabu + httpx · **Platform:** Linux/macOS · **Tags:** Pipeline · **Context:** No auth · **Noise:** Moderate


## Live sites to URLs

```bash
subfinder -d <DOMAIN> -silent | httpx -silent | katana -silent | uro | sort -u
```

**Tool:** subfinder + httpx + katana + uro · **Platform:** Linux/macOS · **Tags:** Pipeline · **Context:** No auth · **Noise:** Moderate


## URLs to parameterized candidates

```bash
katana -u <URL> -silent | uro | grep '=' | sort -u
```

**Tool:** katana + uro · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate


## URLs to reflected parameter candidates

```bash
cat urls.txt | grep '=' | uro | kxss
```

**Tool:** uro + kxss · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate


## Subdomains to screenshots

```bash
subfinder -d <DOMAIN> -silent | httpx -silent -screenshot -system-chrome
```

**Tool:** subfinder + httpx · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate

---

**Related:** [Overview](./) · [Permutations](permutations.md) · [Ports Services](ports-services.md)
