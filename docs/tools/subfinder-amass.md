# Subfinder and Amass

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

Passive subdomain discovery with lightweight, composable output.

<div class="ol-section-kicker"><span>TOOLS</span></div>

## Subfinder silent

```bash
subfinder -d <DOMAIN> -silent
```

**Tool:** subfinder · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Quiet


## Subfinder all providers

```bash
subfinder -d <DOMAIN> -all -silent
```

**Tool:** subfinder · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Quiet


## Subfinder recursive

```bash
subfinder -d <DOMAIN> -recursive -silent
```

**Tool:** subfinder · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Quiet


## Amass passive

```bash
amass enum -passive -d <DOMAIN>
```

**Tool:** Amass · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Quiet


## Merge results

```bash
(subfinder -d <DOMAIN> -silent; amass enum -passive -d <DOMAIN>) | sort -u
```

**Tool:** subfinder + Amass · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Quiet

---

**Related:** [Overview](./) · [Smbclient](smbclient.md) · [Waybackurls](waybackurls.md)
