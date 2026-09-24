# gau

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

GetAllURLs one-liners for historical endpoint and parameter collection.

<div class="ol-section-kicker"><span>TOOL</span><strong>5 one-liners</strong></div>

## Domain URLs

```bash
gau <DOMAIN>
```

**Tool:** gau · **Platform:** Linux · **Tags:** URLs, recon · **Context:** No auth · **Noise:** Quiet

## Include subdomains

```bash
gau --subs <DOMAIN>
```

**Tool:** gau · **Platform:** Linux · **Tags:** URLs, subdomains · **Context:** No auth · **Noise:** Quiet

## Filter extensions

```bash
gau <DOMAIN> --blacklist png,jpg,jpeg,gif,svg,woff,css | uro
```

**Tool:** gau,uro · **Platform:** Linux · **Tags:** URLs, filtering · **Context:** No auth · **Noise:** Quiet

## Parameterized URLs

```bash
gau <DOMAIN> | grep "=" | uro
```

**Tool:** gau,uro · **Platform:** Linux · **Tags:** URLs, parameters · **Context:** No auth · **Noise:** Quiet

## JavaScript URLs

```bash
gau <DOMAIN> | grep -Ei "\.js($|\?)" | sort -u
```

**Tool:** gau · **Platform:** Linux · **Tags:** URLs, JavaScript · **Context:** No auth · **Noise:** Quiet

---

**Related:** Historical URLs · Parameters · JavaScript
