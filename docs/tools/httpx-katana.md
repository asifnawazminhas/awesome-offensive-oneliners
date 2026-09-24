# httpx and Katana

Probe HTTP services and crawl endpoints with minimal output.

<div class="ol-section-kicker"><span>TOOLS</span></div>

## httpx fingerprint

```bash
httpx -l hosts.txt -silent -status-code -title -tech-detect
```

**Tool:** httpx · **Platform:** Linux/macOS · **Context:** No auth


## httpx JSON

```bash
httpx -l hosts.txt -silent -json -o httpx.json
```

**Tool:** httpx · **Platform:** Linux/macOS · **Context:** No auth


## Katana crawl

```bash
katana -u https://<TARGET> -silent
```

**Tool:** katana · **Platform:** Linux/macOS · **Context:** No auth


## Katana JavaScript only

```bash
katana -u https://<TARGET> -silent | grep -Ei '\.js($|\?)' | sort -u
```

**Tool:** katana · **Platform:** Linux/macOS · **Context:** No auth


## Katana parameterized URLs

```bash
katana -u https://<TARGET> -silent | uro | grep '=' | sort -u
```

**Tool:** katana + uro · **Platform:** Linux/macOS · **Context:** No auth

---

**Related:** [Overview](./) · [Hashcat](hashcat.md) · [Impacket](impacket.md)
