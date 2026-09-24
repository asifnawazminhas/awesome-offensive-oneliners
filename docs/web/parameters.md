# Parameter discovery

Find hidden GET/POST parameters and feed interesting URLs into reflection testing.

<div class="ol-section-kicker"><span>WEB</span></div>

## ffuf GET parameter names

```bash
ffuf -w <WORDLIST> -u 'https://<TARGET>/page?FUZZ=test' -ac
```

**Tool:** ffuf · **Platform:** Linux/macOS


## ffuf POST parameter names

```bash
ffuf -w <WORDLIST> -u https://<TARGET>/endpoint -X POST -d 'FUZZ=test' -H 'Content-Type: application/x-www-form-urlencoded' -ac
```

**Tool:** ffuf · **Platform:** Linux/macOS


## Arjun GET parameters

```bash
arjun -u https://<TARGET>/page -m GET
```

**Tool:** Arjun · **Platform:** Linux/macOS


## Arjun POST parameters

```bash
arjun -u https://<TARGET>/endpoint -m POST
```

**Tool:** Arjun · **Platform:** Linux/macOS


## Collect parameterized URLs

```bash
cat urls.txt | grep '=' | uro | sort -u
```

**Tool:** uro · **Platform:** Linux/macOS


## Normalize parameter values

```bash
cat urls.txt | grep = | uro | qsreplace FUZZ | sort -u
```

**Tool:** qsreplace + uro · **Platform:** Linux/macOS


## Reflection triage with kxss

```bash
cat urls.txt | grep = | uro | kxss
```

**Tool:** kxss · **Platform:** Linux/macOS


## Katana to kxss

```bash
katana -u https://<TARGET> -silent | uro | grep '=' | kxss
```

**Tool:** katana + uro + kxss · **Platform:** Linux/macOS · **Tags:** Pipeline
