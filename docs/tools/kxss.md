# kxss

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

kxss one-liners for reflected parameter triage.

<div class="ol-section-kicker"><span>TOOL</span><strong>4 one-liners</strong></div>

## URL list

```bash
cat urls.txt | kxss
```

**Tool:** kxss · **Platform:** Linux · **Tags:** XSS, parameters · **Context:** No auth · **Noise:** Moderate

## gau to kxss

```bash
gau <DOMAIN> | grep "=" | uro | kxss
```

**Tool:** gau,uro,kxss · **Platform:** Linux · **Tags:** XSS, pipeline · **Context:** No auth · **Noise:** Moderate

## Katana to kxss

```bash
katana -u https://<TARGET> -silent | grep "=" | uro | kxss
```

**Tool:** Katana,uro,kxss · **Platform:** Linux · **Tags:** XSS, pipeline · **Context:** No auth · **Noise:** Moderate

## Subdomains to kxss

```bash
subfinder -d <DOMAIN> -silent | httpx -silent | katana -silent | grep "=" | uro | kxss
```

**Tool:** subfinder,httpx,Katana,kxss · **Platform:** Linux · **Tags:** XSS, pipeline · **Context:** No auth · **Noise:** Moderate

---

**Related:** XSS · Parameters · Katana
