# Injection triage

Fast one-liners for SQL, command and template-injection candidates.

<div class="ol-section-kicker"><span>WEB</span></div>

## SQLMap single URL

```bash
sqlmap -u 'https://<TARGET>/item?id=1' --batch --level=1 --risk=1
```

**Tool:** sqlmap · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate


## SQLMap request file

```bash
sqlmap -r request.txt --batch --level=1 --risk=1
```

**Tool:** sqlmap · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate


## Collect SQLi-shaped parameters

```bash
cat urls.txt | grep -Ei '[?&](id|uid|item|page|cat|product|order|query)=' | uro
```

**Tool:** grep + uro · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate


## Command-injection marker check

```bash
curl -sk 'https://<TARGET>/ping?host=127.0.0.1%3Bid'
```

**Tool:** curl · **Platform:** Cross-platform · **Context:** No auth · **Noise:** Moderate


## SSTI arithmetic probe

```bash
curl -sk 'https://<TARGET>/?name=%7B%7B7*7%7D%7D' | grep -n '49'
```

**Tool:** curl · **Platform:** Cross-platform · **Context:** No auth · **Noise:** Moderate

---

**Related:** [Overview](./) · [Iis](iis.md) · [Jwt Oauth](jwt-oauth.md)
