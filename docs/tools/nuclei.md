# Nuclei

Small one-liners for template-driven validation and technology detection.

<div class="ol-section-kicker"><span>TOOLS</span></div>

## Default scan

```bash
nuclei -l urls.txt -silent
```

**Tool:** nuclei · **Platform:** Linux/macOS · **Context:** No auth


## Technology templates

```bash
nuclei -l urls.txt -tags tech -silent
```

**Tool:** nuclei · **Platform:** Linux/macOS · **Context:** No auth


## Severity filter

```bash
nuclei -l urls.txt -severity medium,high,critical -silent
```

**Tool:** nuclei · **Platform:** Linux/macOS · **Context:** No auth


## JSONL output

```bash
nuclei -l urls.txt -jsonl -o nuclei.jsonl
```

**Tool:** nuclei · **Platform:** Linux/macOS · **Context:** No auth


## Specific template directory

```bash
nuclei -u https://<TARGET> -t <TEMPLATE_DIR> -silent
```

**Tool:** nuclei · **Platform:** Linux/macOS · **Context:** No auth

---

**Related:** [Overview](./) · [Nmap](nmap.md) · [Powerview Rubeus](powerview-rubeus.md)
