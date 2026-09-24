---
hide:
  - toc
---
# Cloud Naming & Bucket Permutations

Naming-pattern generation for in-scope cloud asset discovery.

<div class="ol-section-kicker"><span>REC</span><strong>CLOUD</strong></div>

## Common bucket permutations
```bash
printf '%s\n' '<ORG>' '<ORG>-dev' '<ORG>-prod' '<ORG>-backup' '<ORG>-assets' '<ORG>-static' '<ORG>-media' | sort -u
```
**Tool:** printf · **Platform:** Linux/macOS · **Tags:** Buckets, Naming · **Context:** Local · **Noise:** Moderate

## alterx cloud permutations
```bash
printf '%s\n' '<ORG>' | alterx -p '{{word}}-{{suffix}}' -pp suffixes.txt -silent
```
**Tool:** alterx · **Platform:** Linux/macOS · **Tags:** Permutations, Cloud · **Context:** Local · **Noise:** Moderate

## AWS hostname pattern search
```bash
printf '%s\n' 's3.amazonaws.com' 's3-website' 'cloudfront.net' | grep -Ff - urls.txt
```
**Tool:** grep · **Platform:** Linux/macOS · **Tags:** AWS, Hostnames · **Context:** Local · **Noise:** Moderate

## Azure hostname pattern search
```bash
grep -Ei '\.(blob|file|queue|table)\.core\.windows\.net|azurewebsites\.net|trafficmanager\.net|azureedge\.net' urls.txt
```
**Tool:** grep · **Platform:** Linux/macOS · **Tags:** Azure, Hostnames · **Context:** Local · **Noise:** Moderate

## GCP hostname pattern search
```bash
grep -Ei 'storage\.googleapis\.com|appspot\.com|cloudfunctions\.net|run\.app' urls.txt
```
**Tool:** grep · **Platform:** Linux/macOS · **Tags:** GCP, Hostnames · **Context:** Local · **Noise:** Moderate

**Related:** [Cloud Assets](cloud-assets.md) · [Permutations](permutations.md) · [Certificate SANs](certificate-sans.md)
