# dnsx

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

High-signal dnsx one-liners for resolving, enriching and filtering DNS results.

<div class="ol-section-kicker"><span>TOOL</span><strong>5 one-liners</strong></div>

## Resolve A records

```bash
dnsx -l subdomains.txt -a -resp-only -silent
```

**Tool:** dnsx · **Platform:** Linux · **Tags:** DNS, A records · **Context:** No auth · **Noise:** Quiet

## Resolve CNAMEs

```bash
dnsx -l subdomains.txt -cname -resp -silent
```

**Tool:** dnsx · **Platform:** Linux · **Tags:** DNS, CNAME · **Context:** No auth · **Noise:** Quiet

## Resolve all common records

```bash
dnsx -l subdomains.txt -a -aaaa -cname -mx -ns -txt -resp -silent
```

**Tool:** dnsx · **Platform:** Linux · **Tags:** DNS, records · **Context:** No auth · **Noise:** Quiet

## PTR lookups

```bash
dnsx -l ips.txt -ptr -resp-only -silent
```

**Tool:** dnsx · **Platform:** Linux · **Tags:** DNS, PTR · **Context:** No auth · **Noise:** Quiet

## Wildcard filtering

```bash
dnsx -l subdomains.txt -wd <DOMAIN> -silent
```

**Tool:** dnsx · **Platform:** Linux · **Tags:** DNS, wildcard · **Context:** No auth · **Noise:** Quiet

---

**Related:** DNS Resolution · Reverse DNS · Subfinder
