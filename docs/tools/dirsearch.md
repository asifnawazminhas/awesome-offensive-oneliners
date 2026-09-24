# dirsearch

<div class="ol-section-kicker"><span>TOOL</span><strong>DIRSEARCH</strong></div>

## Basic content discovery
```bash
dirsearch -u https://<TARGET>/
```
**Tool:** dirsearch · **Platform:** Python · **Tags:** Content Discovery · **Context:** No auth

## Extensions
```bash
dirsearch -u https://<TARGET>/ -e php,asp,aspx,jsp,html,js,json,txt
```
**Tool:** dirsearch · **Platform:** Python · **Tags:** Extensions, Content Discovery · **Context:** No auth

## Custom wordlist
```bash
dirsearch -u https://<TARGET>/ -w wordlist.txt
```
**Tool:** dirsearch · **Platform:** Python · **Tags:** Wordlist · **Context:** No auth

## Exclude status codes
```bash
dirsearch -u https://<TARGET>/ --exclude-status 404,429
```
**Tool:** dirsearch · **Platform:** Python · **Tags:** Filtering · **Context:** No auth

## Save output
```bash
dirsearch -u https://<TARGET>/ --format=json -o dirsearch.json
```
**Tool:** dirsearch · **Platform:** Python · **Tags:** Output, JSON · **Context:** No auth
