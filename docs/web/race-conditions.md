# Race Condition Testing

Simple concurrent-request one-liners for detecting duplicate processing and state races.

<div class="ol-section-kicker"><span>WEB</span><strong>4 one-liners</strong></div>

## 20 parallel GET requests

```bash
seq 1 20 | xargs -I{} -P20 curl -sk "https://<TARGET>/<ENDPOINT>" -o /dev/null -w "%{http_code}\n"
```

**Tool:** xargs,curl · **Platform:** Linux · **Tags:** Web, race conditions · **Context:** Authenticated · **Noise:** Moderate

## 20 parallel POST requests

```bash
seq 1 20 | xargs -I{} -P20 curl -sk -X POST https://<TARGET>/<ENDPOINT> -d "<BODY>" -o /dev/null -w "%{http_code} %{size_download}\n"
```

**Tool:** xargs,curl · **Platform:** Linux · **Tags:** Web, race conditions, POST · **Context:** Authenticated · **Noise:** Moderate

## GNU parallel request burst

```bash
seq 1 30 | parallel -j30 curl -sk -o /dev/null -w "%{http_code}\n" https://<TARGET>/<ENDPOINT>
```

**Tool:** parallel,curl · **Platform:** Linux · **Tags:** Web, race conditions · **Context:** Authenticated · **Noise:** Moderate

## Compare response hashes

```bash
seq 1 20 | xargs -I{} -P20 curl -sk https://<TARGET>/<ENDPOINT> | sha256sum | sort | uniq -c
```

**Tool:** curl,sha256sum · **Platform:** Linux · **Tags:** Web, race conditions, diff · **Context:** Authenticated · **Noise:** Moderate

---

**Related:** APIs & GraphQL · Authentication · WebSockets
