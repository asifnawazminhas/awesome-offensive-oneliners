# Content & Endpoint Discovery

Directory, file and endpoint discovery one-liners.

<div class="ol-section-kicker"><span>WEB</span><strong>CONTENT</strong></div>

## ffuf directory discovery

```bash
ffuf -u https://<TARGET>/FUZZ -w <WORDLIST> -ac
```

**Tool:** ffuf · **Platform:** Linux/macOS · **Tags:** Content, Discovery · **Context:** No auth

## ffuf interesting status codes

```bash
ffuf -u https://<TARGET>/FUZZ -w <WORDLIST> -mc 200,204,301,302,307,401,403 -ac
```

**Tool:** ffuf · **Platform:** Linux/macOS · **Tags:** Content, HTTP · **Context:** No auth

## ffuf extension discovery

```bash
ffuf -u https://<TARGET>/FUZZ -w <WORDLIST> -e .php,.asp,.aspx,.jsp,.json,.txt,.bak,.old,.zip -ac
```

**Tool:** ffuf · **Platform:** Linux/macOS · **Tags:** Files, Extensions · **Context:** No auth

## ffuf recursive discovery

```bash
ffuf -u https://<TARGET>/FUZZ -w <WORDLIST> -recursion -recursion-depth 2 -ac
```

**Tool:** ffuf · **Platform:** Linux/macOS · **Tags:** Recursive, Discovery · **Context:** No auth

## Gobuster directory discovery

```bash
gobuster dir -u https://<TARGET> -w <WORDLIST> -x php,asp,aspx,jsp,html,js,json,txt,bak -k
```

**Tool:** gobuster · **Platform:** Linux/macOS · **Tags:** Content, Discovery · **Context:** No auth

## Feroxbuster recursive discovery

```bash
feroxbuster -u https://<TARGET> -w <WORDLIST> -x php,html,js,json,txt,bak -k
```

**Tool:** feroxbuster · **Platform:** Linux/macOS · **Tags:** Recursive, Discovery · **Context:** No auth

## Dirsearch common extensions

```bash
dirsearch -u https://<TARGET> -e php,asp,aspx,jsp,html,js,json,txt,bak,old,zip --random-agent
```

**Tool:** dirsearch · **Platform:** Linux/macOS · **Tags:** Content, Discovery · **Context:** No auth

## Katana crawl endpoints

```bash
katana -u https://<TARGET> -silent -jc -kf all | uro | sort -u
```

**Tool:** katana + uro · **Platform:** Linux/macOS · **Tags:** Crawl, Endpoints · **Context:** No auth

---

**Related:** [Overview](./) · [Cache](cache.md) · [Cors Csrf Headers](cors-csrf-headers.md)
