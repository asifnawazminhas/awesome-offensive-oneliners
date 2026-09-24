# Subfinder and Amass

Passive subdomain discovery with lightweight, composable output.

<div class="ol-section-kicker"><span>TOOLS</span></div>

## Subfinder silent

```bash
subfinder -d <DOMAIN> -silent
```

**Tool:** subfinder · **Platform:** Linux/macOS


## Subfinder all providers

```bash
subfinder -d <DOMAIN> -all -silent
```

**Tool:** subfinder · **Platform:** Linux/macOS


## Subfinder recursive

```bash
subfinder -d <DOMAIN> -recursive -silent
```

**Tool:** subfinder · **Platform:** Linux/macOS


## Amass passive

```bash
amass enum -passive -d <DOMAIN>
```

**Tool:** Amass · **Platform:** Linux/macOS


## Merge results

```bash
(subfinder -d <DOMAIN> -silent; amass enum -passive -d <DOMAIN>) | sort -u
```

**Tool:** subfinder + Amass · **Platform:** Linux/macOS
