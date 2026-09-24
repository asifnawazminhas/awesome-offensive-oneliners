# wfuzz

<div class="ol-section-kicker"><span>TOOL</span><strong>WFUZZ</strong></div>

## Directory fuzzing
```bash
wfuzz -c -w wordlist.txt --hc 404 https://<TARGET>/FUZZ
```
**Tool:** wfuzz · **Platform:** Linux/macOS · **Tags:** Content Discovery · **Context:** No auth

## VHost fuzzing
```bash
wfuzz -c -w subdomains.txt -H 'Host: FUZZ.<DOMAIN>' --hh <BASELINE_BYTES> http://<IP>/
```
**Tool:** wfuzz · **Platform:** Linux/macOS · **Tags:** VHost, Host Header · **Context:** No auth

## GET parameter fuzzing
```bash
wfuzz -c -w payloads.txt --hc 404 'https://<TARGET>/endpoint?id=FUZZ'
```
**Tool:** wfuzz · **Platform:** Linux/macOS · **Tags:** Parameters, Fuzzing · **Context:** No auth

## POST parameter fuzzing
```bash
wfuzz -c -w payloads.txt -d 'id=FUZZ' https://<TARGET>/endpoint
```
**Tool:** wfuzz · **Platform:** Linux/macOS · **Tags:** POST, Fuzzing · **Context:** No auth

## Header fuzzing
```bash
wfuzz -c -w values.txt -H 'X-Forwarded-For: FUZZ' https://<TARGET>/
```
**Tool:** wfuzz · **Platform:** Linux/macOS · **Tags:** Headers, Fuzzing · **Context:** No auth
