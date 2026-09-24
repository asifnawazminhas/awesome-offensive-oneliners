# alterx

<div class="ol-section-kicker"><span>TOOL</span><strong>ALTERX</strong></div>

## Default permutations
```bash
printf '%s\n' app.<DOMAIN> | alterx -silent
```
**Tool:** alterx · **Platform:** Linux/macOS · **Tags:** Subdomains, Permutations · **Context:** Local

## Pipe to dnsx
```bash
cat subdomains.txt | alterx -silent | dnsx -silent
```
**Tool:** alterx/dnsx · **Platform:** Linux/macOS · **Tags:** Permutations, DNS · **Context:** No auth

## Prefix pattern
```bash
printf '%s\n' app.<DOMAIN> | alterx -p '{{prefix}}-{{word}}.{{suffix}}' -silent
```
**Tool:** alterx · **Platform:** Linux/macOS · **Tags:** Patterns, Subdomains · **Context:** Local

## Append environments
```bash
printf '%s\n' app.<DOMAIN> | alterx -p '{{word}}-{{suffix}}' -pp suffixes.txt -silent
```
**Tool:** alterx · **Platform:** Linux/macOS · **Tags:** Environments, Permutations · **Context:** Local
