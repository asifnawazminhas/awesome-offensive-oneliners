# XSS and reflection triage

Prioritise reflected parameters and simple encoding behaviour.

<div class="ol-section-kicker"><span>WEB</span></div>

## kxss reflection scan

```bash
cat urls.txt | grep = | uro | kxss
```

**Tool:** kxss · **Platform:** Linux/macOS · **Context:** No auth


## Replace all values with marker

```bash
cat urls.txt | grep = | uro | qsreplace 'xssMARK' | sort -u
```

**Tool:** qsreplace · **Platform:** Linux/macOS · **Context:** No auth


## curl reflection check

```bash
curl -sk 'https://<TARGET>/page?q=xssMARK' | grep -n 'xssMARK'
```

**Tool:** curl · **Platform:** Cross-platform · **Context:** No auth


## Dalfox URL mode

```bash
dalfox url 'https://<TARGET>/page?q=test' --silence
```

**Tool:** Dalfox · **Platform:** Linux/macOS · **Context:** No auth


## Dalfox pipe mode

```bash
cat urls.txt | dalfox pipe --silence
```

**Tool:** Dalfox · **Platform:** Linux/macOS · **Context:** No auth

---

**Related:** [Overview](./) · [Websockets](websockets.md)
