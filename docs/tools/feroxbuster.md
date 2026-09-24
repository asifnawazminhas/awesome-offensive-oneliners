# Feroxbuster

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

Feroxbuster one-liners for recursive web content discovery.

<div class="ol-section-kicker"><span>TOOL</span><strong>5 one-liners</strong></div>

## Basic recursive scan

```bash
feroxbuster -u https://<TARGET> -w <WORDLIST>
```

**Tool:** Feroxbuster · **Platform:** Linux · **Tags:** content discovery, web · **Context:** No auth · **Noise:** Moderate

## Extensions

```bash
feroxbuster -u https://<TARGET> -w <WORDLIST> -x php,html,js,txt,json
```

**Tool:** Feroxbuster · **Platform:** Linux · **Tags:** content discovery, extensions · **Context:** No auth · **Noise:** Moderate

## Authenticated cookie

```bash
feroxbuster -u https://<TARGET> -w <WORDLIST> -H "Cookie: <COOKIE>"
```

**Tool:** Feroxbuster · **Platform:** Linux · **Tags:** content discovery, auth · **Context:** Authenticated · **Noise:** Moderate

## Rate limit

```bash
feroxbuster -u https://<TARGET> -w <WORDLIST> --rate-limit 10
```

**Tool:** Feroxbuster · **Platform:** Linux · **Tags:** content discovery, rate limit · **Context:** No auth · **Noise:** Moderate

## No recursion

```bash
feroxbuster -u https://<TARGET> -w <WORDLIST> -n
```

**Tool:** Feroxbuster · **Platform:** Linux · **Tags:** content discovery · **Context:** No auth · **Noise:** Moderate

---

**Related:** Content Discovery · ffuf · Gobuster
