---
hide:
  - toc
---

# Parameter Discovery & Fuzzing

Hidden parameter discovery, archived parameter mining, reflection triage and value fuzzing.

<div class="ol-section-kicker"><span>WEB</span><strong>PARAMS</strong></div>

## Arjun GET parameters

```bash
arjun -u https://<TARGET>/endpoint -m GET -oJ params.json
```

**Tool:** Arjun · **Platform:** Linux/macOS · **Tags:** Parameters, GET · **Context:** No auth

## Arjun POST parameters

```bash
arjun -u https://<TARGET>/endpoint -m POST -oJ params-post.json
```

**Tool:** Arjun · **Platform:** Linux/macOS · **Tags:** Parameters, POST · **Context:** No auth

## ParamSpider archived parameters

```bash
paramspider -d <DOMAIN>
```

**Tool:** ParamSpider · **Platform:** Linux/macOS · **Tags:** Parameters, Archives · **Context:** No auth

## x8 parameter discovery

```bash
x8 -u https://<TARGET>/endpoint -w <PARAM_WORDLIST>
```

**Tool:** x8 · **Platform:** Linux/macOS · **Tags:** Parameters, Discovery · **Context:** No auth

## ffuf GET parameter names

```bash
ffuf -u 'https://<TARGET>/endpoint?FUZZ=test' -w <PARAM_WORDLIST> -ac -rate 50
```

**Tool:** ffuf · **Platform:** Linux/macOS · **Tags:** Parameters, Discovery · **Context:** No auth

## ffuf POST parameter names

```bash
ffuf -u https://<TARGET>/endpoint -X POST -d 'FUZZ=test' -H 'Content-Type: application/x-www-form-urlencoded' -w <PARAM_WORDLIST> -ac -rate 50
```

**Tool:** ffuf · **Platform:** Linux/macOS · **Tags:** Parameters, POST · **Context:** No auth

## ffuf parameter value fuzzing

```bash
ffuf -u 'https://<TARGET>/endpoint?id=FUZZ' -w <PAYLOADS> -mc 200,500 -rate 50
```

**Tool:** ffuf · **Platform:** Linux/macOS · **Tags:** Parameters, Fuzzing · **Context:** No auth

## wfuzz parameter value fuzzing

```bash
wfuzz -c -z file,<PAYLOADS> --hc 404 'https://<TARGET>/endpoint?id=FUZZ'
```

**Tool:** wfuzz · **Platform:** Linux/macOS · **Tags:** Parameters, Fuzzing · **Context:** No auth

## ffuf POST body fuzzing

```bash
ffuf -u https://<TARGET>/endpoint -X POST -d 'id=FUZZ' -H 'Content-Type: application/x-www-form-urlencoded' -w <PAYLOADS> -mc 200,500 -rate 50
```

**Tool:** ffuf · **Platform:** Linux/macOS · **Tags:** POST, Fuzzing · **Context:** No auth

## gau parameterized URLs

```bash
gau <DOMAIN> | grep '=' | uro | sort -u
```

**Tool:** gau + uro · **Platform:** Linux/macOS · **Tags:** Archives, Parameters · **Context:** No auth

## waybackurls parameterized URLs

```bash
echo <DOMAIN> | waybackurls | grep '=' | uro | sort -u
```

**Tool:** waybackurls + uro · **Platform:** Linux/macOS · **Tags:** Archives, Parameters · **Context:** No auth

## gau with gf XSS patterns

```bash
gau <DOMAIN> | gf xss | uro | sort -u
```

**Tool:** gau + gf + uro · **Platform:** Linux/macOS · **Tags:** XSS, Parameters · **Context:** No auth

## Normalize parameter values

```bash
cat urls.txt | grep '=' | uro | qsreplace FUZZ | sort -u
```

**Tool:** qsreplace + uro · **Platform:** Linux/macOS · **Tags:** Normalize, Parameters · **Context:** No auth

## Reflection triage with kxss

```bash
cat urls.txt | grep '=' | uro | kxss
```

**Tool:** kxss · **Platform:** Linux/macOS · **Tags:** XSS, Reflection · **Context:** No auth

## Katana to kxss

```bash
katana -u https://<TARGET> -silent | uro | grep '=' | kxss
```

**Tool:** katana + uro + kxss · **Platform:** Linux/macOS · **Tags:** Pipeline, Reflection · **Context:** No auth

---

**Related:** [Overview](./) · [Open Redirect](open-redirect.md) · [Path Traversal Lfi](path-traversal-lfi.md)
