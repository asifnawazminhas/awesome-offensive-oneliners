# Historical URLs

Collect archived and indexed URLs, then normalize them.

<div class="ol-section-kicker"><span>RECON</span></div>

## Wayback URLs

```bash
echo <DOMAIN> | waybackurls | sort -u
```

**Tool:** waybackurls · **Platform:** Linux/macOS · **Context:** No auth


## gau URLs

```bash
gau --subs <DOMAIN> | sort -u
```

**Tool:** gau · **Platform:** Linux/macOS · **Context:** No auth


## Combine and normalize URLs

```bash
(echo <DOMAIN> | waybackurls; gau --subs <DOMAIN>) | uro | sort -u > urls.txt
```

**Tool:** waybackurls + gau + uro · **Platform:** Linux/macOS · **Tags:** Pipeline · **Context:** No auth


## Keep parameterized URLs

```bash
cat urls.txt | grep '=' | uro | sort -u
```

**Tool:** grep + uro · **Platform:** Linux/macOS · **Context:** No auth


## Keep JavaScript URLs

```bash
cat urls.txt | grep -Ei '\.js($|\?)' | sort -u
```

**Tool:** grep · **Platform:** Linux/macOS · **Context:** No auth


## Extract extensions from URLs

```bash
cat urls.txt | sed -E 's/.*\.([a-zA-Z0-9]{1,8})([?#].*)?$/\1/' | sort | uniq -c | sort -nr
```

**Tool:** sed · **Platform:** Linux/macOS · **Context:** No auth

---

**Related:** [Overview](./) · [Shodan](shodan.md)
