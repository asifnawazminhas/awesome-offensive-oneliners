# Subdomain permutations

Generate and resolve likely mutations from discovered names.

<div class="ol-section-kicker"><span>RECON</span></div>

## Alterx permutations to live DNS

```bash
cat subdomains.txt | alterx -silent | dnsx -silent | sort -u
```

**Tool:** alterx + dnsx · **Platform:** Linux/macOS · **Tags:** Pipeline


## Alterx with custom patterns

```bash
alterx -l subdomains.txt -p '{{word}}-dev.{{suffix}},{{word}}-staging.{{suffix}}' -silent | dnsx -silent
```

**Tool:** alterx · **Platform:** Linux/macOS


## Simple environment mutations

```bash
sed -E 's/^([^.]+)\./\1-{dev,test,stage,staging,prod}./' subdomains.txt
```

**Tool:** sed · **Platform:** Linux/macOS


## MassDNS resolve permutations

```bash
massdns -r resolvers.txt -t A -o S -w massdns.out permutations.txt
```

**Tool:** massdns · **Platform:** Linux/macOS
