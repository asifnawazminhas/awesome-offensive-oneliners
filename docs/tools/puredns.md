# PureDNS

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

<div class="ol-section-kicker"><span>TOOL</span><strong>PUREDNS</strong></div>

## Resolve candidates
```bash
puredns resolve subdomains.txt -r resolvers.txt -w resolved.txt
```
**Tool:** PureDNS · **Platform:** Linux/macOS · **Tags:** DNS, Resolution · **Context:** No auth · **Noise:** Moderate

## Brute-force subdomains
```bash
puredns bruteforce subdomains.txt <DOMAIN> -r resolvers.txt -w brute.txt
```
**Tool:** PureDNS · **Platform:** Linux/macOS · **Tags:** DNS, Bruteforce · **Context:** No auth · **Noise:** Moderate

## Trusted resolver verification
```bash
puredns resolve subdomains.txt -r resolvers.txt --resolvers-trusted trusted.txt -w resolved.txt
```
**Tool:** PureDNS · **Platform:** Linux/macOS · **Tags:** DNS, Resolvers · **Context:** No auth · **Noise:** Moderate

## Wildcard detection
```bash
puredns resolve subdomains.txt -r resolvers.txt --write-wildcards wildcards.txt -w resolved.txt
```
**Tool:** PureDNS · **Platform:** Linux/macOS · **Tags:** DNS, Wildcards · **Context:** No auth · **Noise:** Moderate
