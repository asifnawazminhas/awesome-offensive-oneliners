# gau

GetAllURLs one-liners for historical endpoint and parameter collection.

<div class="ol-section-kicker"><span>TOOL</span><strong>5 one-liners</strong></div>

## Domain URLs

```bash
gau <DOMAIN>
```

**Tool:** gau · **Platform:** Linux · **Tags:** URLs, recon · **Context:** No auth

## Include subdomains

```bash
gau --subs <DOMAIN>
```

**Tool:** gau · **Platform:** Linux · **Tags:** URLs, subdomains · **Context:** No auth

## Filter extensions

```bash
gau <DOMAIN> --blacklist png,jpg,jpeg,gif,svg,woff,css | uro
```

**Tool:** gau,uro · **Platform:** Linux · **Tags:** URLs, filtering · **Context:** No auth

## Parameterized URLs

```bash
gau <DOMAIN> | grep "=" | uro
```

**Tool:** gau,uro · **Platform:** Linux · **Tags:** URLs, parameters · **Context:** No auth

## JavaScript URLs

```bash
gau <DOMAIN> | grep -Ei "\.js($|\?)" | sort -u
```

**Tool:** gau · **Platform:** Linux · **Tags:** URLs, JavaScript · **Context:** No auth

---

**Related:** Historical URLs · Parameters · JavaScript
