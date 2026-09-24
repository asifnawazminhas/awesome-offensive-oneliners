# Cloud Asset Discovery

One-liners for identifying cloud-hosted endpoints and common public cloud naming patterns.

<div class="ol-section-kicker"><span>REC</span><strong>5 one-liners</strong></div>

## AWS S3 hostnames from URLs

```bash
grep -Eio "[A-Za-z0-9._-]+\.s3[.-][A-Za-z0-9.-]*amazonaws\.com|s3[.-][A-Za-z0-9.-]*amazonaws\.com/[A-Za-z0-9._/-]+" urls.txt | sort -u
```

**Tool:** grep · **Platform:** Linux · **Tags:** Recon, AWS, S3 · **Context:** No auth · **Noise:** Moderate

## Azure Blob hostnames

```bash
grep -Eio "[A-Za-z0-9-]+\.blob\.core\.windows\.net" urls.txt | sort -u
```

**Tool:** grep · **Platform:** Linux · **Tags:** Recon, Azure, Blob · **Context:** No auth · **Noise:** Moderate

## GCS hostnames

```bash
grep -Eio "storage\.googleapis\.com/[A-Za-z0-9._/-]+|[A-Za-z0-9._-]+\.storage\.googleapis\.com" urls.txt | sort -u
```

**Tool:** grep · **Platform:** Linux · **Tags:** Recon, GCP, storage · **Context:** No auth · **Noise:** Moderate

## Cloudfront endpoints

```bash
grep -Eio "[a-z0-9]+\.cloudfront\.net" urls.txt | sort -u
```

**Tool:** grep · **Platform:** Linux · **Tags:** Recon, AWS, CloudFront · **Context:** No auth · **Noise:** Moderate

## DNS CNAME cloud clues

```bash
dnsx -l subdomains.txt -cname -resp-only -silent | grep -Ei "amazonaws|azure|windows.net|cloudfront|googleapis|herokudns|fastly|akamai"
```

**Tool:** dnsx · **Platform:** Linux · **Tags:** Recon, cloud, CNAME · **Context:** No auth · **Noise:** Moderate

---

**Related:** DNS Resolution · CNAMEs · Passive Combinations
