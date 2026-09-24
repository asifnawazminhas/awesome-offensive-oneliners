# Nuclei

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

Small one-liners for template-driven validation and technology detection.

<div class="ol-section-kicker"><span>TOOLS</span></div>

## Default scan

```bash
nuclei -l urls.txt -silent
```

**Tool:** nuclei · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate


## Technology templates

```bash
nuclei -l urls.txt -tags tech -silent
```

**Tool:** nuclei · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate


## Severity filter

```bash
nuclei -l urls.txt -severity medium,high,critical -silent
```

**Tool:** nuclei · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate


## JSONL output

```bash
nuclei -l urls.txt -jsonl -o nuclei.jsonl
```

**Tool:** nuclei · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate


## Specific template directory

```bash
nuclei -u https://<TARGET> -t <TEMPLATE_DIR> -silent
```

**Tool:** nuclei · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate

---

**Related:** [Overview](./) · [Nmap](nmap.md) · [Powerview Rubeus](powerview-rubeus.md)
