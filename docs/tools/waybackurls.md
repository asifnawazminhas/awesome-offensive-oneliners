# waybackurls

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

Wayback Machine URL collection one-liners.

<div class="ol-section-kicker"><span>TOOL</span><strong>4 one-liners</strong></div>

## Domain URLs

```bash
echo <DOMAIN> | waybackurls
```

**Tool:** waybackurls · **Platform:** Linux · **Tags:** URLs, Wayback · **Context:** No auth · **Noise:** Quiet

## From multiple domains

```bash
cat domains.txt | waybackurls | sort -u
```

**Tool:** waybackurls · **Platform:** Linux · **Tags:** URLs, Wayback · **Context:** No auth · **Noise:** Quiet

## Parameterized URLs

```bash
echo <DOMAIN> | waybackurls | grep "=" | uro
```

**Tool:** waybackurls,uro · **Platform:** Linux · **Tags:** URLs, parameters · **Context:** No auth · **Noise:** Quiet

## JavaScript files

```bash
echo <DOMAIN> | waybackurls | grep -Ei "\.js($|\?)" | sort -u
```

**Tool:** waybackurls · **Platform:** Linux · **Tags:** URLs, JavaScript · **Context:** No auth · **Noise:** Quiet

---

**Related:** Historical URLs · gau · Parameters
