# Permutation Pipelines

Higher-coverage subdomain permutation one-liners with resolution and deduplication.

<div class="ol-section-kicker"><span>REC</span><strong>5 one-liners</strong></div>

## alterx to dnsx

```bash
cat subdomains.txt | alterx -silent | dnsx -silent
```

**Tool:** alterx,dnsx · **Platform:** Linux · **Tags:** Recon, subdomains, permutations · **Context:** No auth · **Noise:** Moderate

## alterx plus original set

```bash
(cat subdomains.txt; cat subdomains.txt | alterx -silent) | sort -u | dnsx -silent
```

**Tool:** alterx,dnsx · **Platform:** Linux · **Tags:** Recon, subdomains, permutations · **Context:** No auth · **Noise:** Moderate

## dnsgen to massdns

```bash
dnsgen subdomains.txt | massdns -r resolvers.txt -t A -o S -w resolved.txt
```

**Tool:** dnsgen,massdns · **Platform:** Linux · **Tags:** Recon, subdomains, permutations · **Context:** No auth · **Noise:** Moderate

## altdns permutations

```bash
altdns -i subdomains.txt -o permutations.txt -w words.txt
```

**Tool:** altdns · **Platform:** Linux · **Tags:** Recon, subdomains, permutations · **Context:** No auth · **Noise:** Moderate

## puredns resolve permutations

```bash
cat permutations.txt | puredns resolve -r resolvers.txt -w resolved.txt
```

**Tool:** puredns · **Platform:** Linux · **Tags:** Recon, DNS, permutations · **Context:** No auth · **Noise:** Moderate

---

**Related:** Permutations · DNS Resolution · Passive Subdomains
