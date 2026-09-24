# httpx and Katana

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

Probe HTTP services and crawl endpoints with minimal output.

<div class="ol-section-kicker"><span>TOOLS</span></div>

## httpx fingerprint

```bash
httpx -l hosts.txt -silent -status-code -title -tech-detect
```

**Tool:** httpx · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate


## httpx JSON

```bash
httpx -l hosts.txt -silent -json -o httpx.json
```

**Tool:** httpx · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate


## Katana crawl

```bash
katana -u https://<TARGET> -silent
```

**Tool:** katana · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate


## Katana JavaScript only

```bash
katana -u https://<TARGET> -silent | grep -Ei '\.js($|\?)' | sort -u
```

**Tool:** katana · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate


## Katana parameterized URLs

```bash
katana -u https://<TARGET> -silent | uro | grep '=' | sort -u
```

**Tool:** katana + uro · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate

---

**Related:** [Overview](./) · [Hashcat](hashcat.md) · [Impacket](impacket.md)
