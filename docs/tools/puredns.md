# PureDNS

<div class="ol-section-kicker"><span>TOOL</span><strong>PUREDNS</strong></div>

## Resolve candidates
```bash
puredns resolve subdomains.txt -r resolvers.txt -w resolved.txt
```
**Tool:** PureDNS · **Platform:** Linux/macOS · **Tags:** DNS, Resolution · **Context:** No auth

## Brute-force subdomains
```bash
puredns bruteforce subdomains.txt <DOMAIN> -r resolvers.txt -w brute.txt
```
**Tool:** PureDNS · **Platform:** Linux/macOS · **Tags:** DNS, Bruteforce · **Context:** No auth

## Trusted resolver verification
```bash
puredns resolve subdomains.txt -r resolvers.txt --resolvers-trusted trusted.txt -w resolved.txt
```
**Tool:** PureDNS · **Platform:** Linux/macOS · **Tags:** DNS, Resolvers · **Context:** No auth

## Wildcard detection
```bash
puredns resolve subdomains.txt -r resolvers.txt --write-wildcards wildcards.txt -w resolved.txt
```
**Tool:** PureDNS · **Platform:** Linux/macOS · **Tags:** DNS, Wildcards · **Context:** No auth
