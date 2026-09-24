# alterx

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

<div class="ol-section-kicker"><span>TOOL</span><strong>ALTERX</strong></div>

## Default permutations
```bash
printf '%s\n' app.<DOMAIN> | alterx -silent
```
**Tool:** alterx · **Platform:** Linux/macOS · **Tags:** Subdomains, Permutations · **Context:** Local · **Noise:** Moderate

## Pipe to dnsx
```bash
cat subdomains.txt | alterx -silent | dnsx -silent
```
**Tool:** alterx/dnsx · **Platform:** Linux/macOS · **Tags:** Permutations, DNS · **Context:** No auth · **Noise:** Moderate

## Prefix pattern
```bash
printf '%s\n' app.<DOMAIN> | alterx -p '{{prefix}}-{{word}}.{{suffix}}' -silent
```
**Tool:** alterx · **Platform:** Linux/macOS · **Tags:** Patterns, Subdomains · **Context:** Local · **Noise:** Moderate

## Append environments
```bash
printf '%s\n' app.<DOMAIN> | alterx -p '{{word}}-{{suffix}}' -pp suffixes.txt -silent
```
**Tool:** alterx · **Platform:** Linux/macOS · **Tags:** Environments, Permutations · **Context:** Local · **Noise:** Moderate
