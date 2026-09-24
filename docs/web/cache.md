# Cache Poisoning & Deception

One-liners for identifying cache layers and varying common unkeyed inputs.

<div class="ol-section-kicker"><span>WEB</span><strong>5 one-liners</strong></div>

## Inspect cache headers

```bash
curl -skI https://<TARGET>/ | grep -Ei "^(age|cache-control|via|x-cache|x-cache-hits|x-served-by|x-varnish|cf-cache-status)"
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, cache · **Context:** No auth · **Noise:** Moderate

## Probe X-Forwarded-Host

```bash
curl -sk -H "X-Forwarded-Host: cache-test.example" https://<TARGET>/ | grep -F "cache-test.example"
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, cache poisoning, headers · **Context:** No auth · **Noise:** Moderate

## Probe X-Original-URL

```bash
curl -sk -H "X-Original-URL: /robots.txt" https://<TARGET>/
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, cache, headers · **Context:** No auth · **Noise:** Moderate

## Probe path extension deception

```bash
curl -skI https://<TARGET>/<ACCOUNT_PATH>/style.css
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, cache deception · **Context:** Authenticated · **Noise:** Moderate

## Repeat and watch Age header

```bash
for i in 1 2 3; do curl -skI https://<TARGET>/ | grep -i "^Age:"; sleep 1; done
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, cache validation · **Context:** No auth · **Noise:** Moderate

---

**Related:** Request Smuggling · Headers · Open Redirect
