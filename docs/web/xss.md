# XSS and reflection triage

Prioritise reflected parameters and simple encoding behaviour.

<div class="ol-section-kicker"><span>WEB</span></div>

## kxss reflection scan

```bash
cat urls.txt | grep = | uro | kxss
```

**Tool:** kxss · **Platform:** Linux/macOS


## Replace all values with marker

```bash
cat urls.txt | grep = | uro | qsreplace 'xssMARK' | sort -u
```

**Tool:** qsreplace · **Platform:** Linux/macOS


## curl reflection check

```bash
curl -sk 'https://<TARGET>/page?q=xssMARK' | grep -n 'xssMARK'
```

**Tool:** curl · **Platform:** Cross-platform


## Dalfox URL mode

```bash
dalfox url 'https://<TARGET>/page?q=test' --silence
```

**Tool:** Dalfox · **Platform:** Linux/macOS


## Dalfox pipe mode

```bash
cat urls.txt | dalfox pipe --silence
```

**Tool:** Dalfox · **Platform:** Linux/macOS
