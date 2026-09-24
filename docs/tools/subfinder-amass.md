# Subfinder and Amass

Passive subdomain discovery with lightweight, composable output.

<div class="ol-section-kicker"><span>TOOLS</span></div>

## Subfinder silent

```bash
subfinder -d <DOMAIN> -silent
```

**Tool:** subfinder · **Platform:** Linux/macOS · **Context:** No auth


## Subfinder all providers

```bash
subfinder -d <DOMAIN> -all -silent
```

**Tool:** subfinder · **Platform:** Linux/macOS · **Context:** No auth


## Subfinder recursive

```bash
subfinder -d <DOMAIN> -recursive -silent
```

**Tool:** subfinder · **Platform:** Linux/macOS · **Context:** No auth


## Amass passive

```bash
amass enum -passive -d <DOMAIN>
```

**Tool:** Amass · **Platform:** Linux/macOS · **Context:** No auth


## Merge results

```bash
(subfinder -d <DOMAIN> -silent; amass enum -passive -d <DOMAIN>) | sort -u
```

**Tool:** subfinder + Amass · **Platform:** Linux/macOS · **Context:** No auth

---

**Related:** [Overview](./) · [Smbclient](smbclient.md) · [Waybackurls](waybackurls.md)
