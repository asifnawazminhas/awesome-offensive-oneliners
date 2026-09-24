# ffuf and Gobuster

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

High-frequency discovery commands for content, parameters and virtual hosts.

<div class="ol-section-kicker"><span>TOOLS</span></div>

## ffuf directories

```bash
ffuf -w <WORDLIST> -u https://<TARGET>/FUZZ -ac
```

**Tool:** ffuf · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate


## ffuf vhosts

```bash
ffuf -w <WORDLIST> -u https://<TARGET>/ -H "Host: FUZZ.<DOMAIN>" -ac
```

**Tool:** ffuf · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate


## ffuf GET parameters

```bash
ffuf -w <WORDLIST> -u 'https://<TARGET>/page?FUZZ=test' -ac
```

**Tool:** ffuf · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate


## Gobuster directories

```bash
gobuster dir -u https://<TARGET> -w <WORDLIST> -k
```

**Tool:** gobuster · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate


## Gobuster vhosts

```bash
gobuster vhost -u https://<TARGET> -w <WORDLIST> --append-domain
```

**Tool:** gobuster · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate

---

**Related:** [Overview](./) · [Feroxbuster](feroxbuster.md) · [Gau](gau.md)
