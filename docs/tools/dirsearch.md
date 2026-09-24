# dirsearch

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

<div class="ol-section-kicker"><span>TOOL</span><strong>DIRSEARCH</strong></div>

## Basic content discovery
```bash
dirsearch -u https://<TARGET>/
```
**Tool:** dirsearch · **Platform:** Python · **Tags:** Content Discovery · **Context:** No auth · **Noise:** Moderate

## Extensions
```bash
dirsearch -u https://<TARGET>/ -e php,asp,aspx,jsp,html,js,json,txt
```
**Tool:** dirsearch · **Platform:** Python · **Tags:** Extensions, Content Discovery · **Context:** No auth · **Noise:** Moderate

## Custom wordlist
```bash
dirsearch -u https://<TARGET>/ -w wordlist.txt
```
**Tool:** dirsearch · **Platform:** Python · **Tags:** Wordlist · **Context:** No auth · **Noise:** Moderate

## Exclude status codes
```bash
dirsearch -u https://<TARGET>/ --exclude-status 404,429
```
**Tool:** dirsearch · **Platform:** Python · **Tags:** Filtering · **Context:** No auth · **Noise:** Moderate

## Save output
```bash
dirsearch -u https://<TARGET>/ --format=json -o dirsearch.json
```
**Tool:** dirsearch · **Platform:** Python · **Tags:** Output, JSON · **Context:** No auth · **Noise:** Moderate
