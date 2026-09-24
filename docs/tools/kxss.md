# kxss

kxss one-liners for reflected parameter triage.

<div class="ol-section-kicker"><span>TOOL</span><strong>4 one-liners</strong></div>

## URL list

```bash
cat urls.txt | kxss
```

**Tool:** kxss · **Platform:** Linux · **Tags:** XSS, parameters · **Context:** No auth

## gau to kxss

```bash
gau <DOMAIN> | grep "=" | uro | kxss
```

**Tool:** gau,uro,kxss · **Platform:** Linux · **Tags:** XSS, pipeline · **Context:** No auth

## Katana to kxss

```bash
katana -u https://<TARGET> -silent | grep "=" | uro | kxss
```

**Tool:** Katana,uro,kxss · **Platform:** Linux · **Tags:** XSS, pipeline · **Context:** No auth

## Subdomains to kxss

```bash
subfinder -d <DOMAIN> -silent | httpx -silent | katana -silent | grep "=" | uro | kxss
```

**Tool:** subfinder,httpx,Katana,kxss · **Platform:** Linux · **Tags:** XSS, pipeline · **Context:** No auth

---

**Related:** XSS · Parameters · Katana
