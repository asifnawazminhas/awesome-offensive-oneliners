---
hide:
  - toc
---
# DNS Quality Checks

Wildcard detection, resolver validation and clean-resolution helpers.

<div class="ol-section-kicker"><span>REC</span><strong>DNS</strong></div>

## Random-label wildcard check
```bash
for i in 1 2 3; do dig +short "$(openssl rand -hex 6).<DOMAIN>" A; done
```
**Tool:** dig/openssl · **Platform:** Linux/macOS · **Tags:** Wildcard DNS · **Context:** No auth

## dnsx wildcard filtering
```bash
dnsx -l subdomains.txt -silent -wd <DOMAIN>
```
**Tool:** dnsx · **Platform:** Linux/macOS · **Tags:** Wildcard, DNS · **Context:** No auth

## Validate resolver list with massdns
```bash
massdns -r resolvers.txt -t A -o S -w resolver-test.txt known-hosts.txt
```
**Tool:** massdns · **Platform:** Linux/macOS · **Tags:** Resolvers, Validation · **Context:** Local

## PureDNS resolve with trusted resolvers
```bash
puredns resolve subdomains.txt -r resolvers.txt --resolvers-trusted resolvers-trusted.txt -w resolved.txt
```
**Tool:** PureDNS · **Platform:** Linux/macOS · **Tags:** DNS, Resolvers · **Context:** Local

## Remove unresolved candidates
```bash
dnsx -l subdomains.txt -silent -a -resp-only | sort -u
```
**Tool:** dnsx · **Platform:** Linux/macOS · **Tags:** DNS, Validation · **Context:** No auth

**Related:** [DNS Resolution](dns-resolution.md) · [Passive Subdomains](passive-subdomains.md) · [Permutation Pipelines](permutations-advanced.md)
