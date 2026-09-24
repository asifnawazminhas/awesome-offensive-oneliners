# Nuclei

Small one-liners for template-driven validation and technology detection.

<div class="ol-section-kicker"><span>TOOLS</span></div>

## Default scan

```bash
nuclei -l urls.txt -silent
```

**Tool:** nuclei · **Platform:** Linux/macOS


## Technology templates

```bash
nuclei -l urls.txt -tags tech -silent
```

**Tool:** nuclei · **Platform:** Linux/macOS


## Severity filter

```bash
nuclei -l urls.txt -severity medium,high,critical -silent
```

**Tool:** nuclei · **Platform:** Linux/macOS


## JSONL output

```bash
nuclei -l urls.txt -jsonl -o nuclei.jsonl
```

**Tool:** nuclei · **Platform:** Linux/macOS


## Specific template directory

```bash
nuclei -u https://<TARGET> -t <TEMPLATE_DIR> -silent
```

**Tool:** nuclei · **Platform:** Linux/macOS
