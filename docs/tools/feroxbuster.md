# Feroxbuster

Feroxbuster one-liners for recursive web content discovery.

<div class="ol-section-kicker"><span>TOOL</span><strong>5 one-liners</strong></div>

## Basic recursive scan

```bash
feroxbuster -u https://<TARGET> -w <WORDLIST>
```

**Tool:** Feroxbuster · **Platform:** Linux · **Tags:** content discovery, web · **Context:** No auth

## Extensions

```bash
feroxbuster -u https://<TARGET> -w <WORDLIST> -x php,html,js,txt,json
```

**Tool:** Feroxbuster · **Platform:** Linux · **Tags:** content discovery, extensions · **Context:** No auth

## Authenticated cookie

```bash
feroxbuster -u https://<TARGET> -w <WORDLIST> -H "Cookie: <COOKIE>"
```

**Tool:** Feroxbuster · **Platform:** Linux · **Tags:** content discovery, auth · **Context:** Authenticated

## Rate limit

```bash
feroxbuster -u https://<TARGET> -w <WORDLIST> --rate-limit 10
```

**Tool:** Feroxbuster · **Platform:** Linux · **Tags:** content discovery, rate limit · **Context:** No auth

## No recursion

```bash
feroxbuster -u https://<TARGET> -w <WORDLIST> -n
```

**Tool:** Feroxbuster · **Platform:** Linux · **Tags:** content discovery · **Context:** No auth

---

**Related:** Content Discovery · ffuf · Gobuster
