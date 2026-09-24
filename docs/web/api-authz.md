# API Authorization

One-liners for object-level and function-level authorization comparisons.

<div class="ol-section-kicker"><span>WEB</span><strong>5 one-liners</strong></div>

## Compare two object IDs

```bash
for id in <ID1> <ID2>; do curl -sk -H "Authorization: Bearer <TOKEN>" "https://<TARGET>/api/items/$id" -w "\n$id %{http_code} %{size_download}\n"; done
```

**Tool:** curl · **Platform:** Any · **Tags:** API, authorization, IDOR · **Context:** Authenticated · **Noise:** Moderate

## Compare unauthenticated and authenticated

```bash
curl -sk -o /tmp/noauth -w "%{http_code} %{size_download}\n" https://<TARGET>/api/<ENDPOINT>; curl -sk -H "Authorization: Bearer <TOKEN>" -o /tmp/auth -w "%{http_code} %{size_download}\n" https://<TARGET>/api/<ENDPOINT>
```

**Tool:** curl · **Platform:** Any · **Tags:** API, authorization · **Context:** Authenticated · **Noise:** Moderate

## Method authorization matrix

```bash
for m in GET POST PUT PATCH DELETE; do curl -sk -o /dev/null -w "$m %{http_code} %{size_download}\n" -X $m -H "Authorization: Bearer <TOKEN>" https://<TARGET>/api/<ENDPOINT>; done
```

**Tool:** curl · **Platform:** Any · **Tags:** API, authorization, methods · **Context:** Authenticated · **Noise:** Moderate

## Swap bearer tokens

```bash
for t in "<TOKEN_A>" "<TOKEN_B>"; do curl -sk -H "Authorization: Bearer $t" https://<TARGET>/api/<ENDPOINT>/<OBJECT_ID> -w " %{http_code} %{size_download}\n"; done
```

**Tool:** curl · **Platform:** Any · **Tags:** API, authorization, BOLA · **Context:** Authenticated · **Noise:** Moderate

## ffuf object identifiers

```bash
ffuf -u https://<TARGET>/api/items/FUZZ -w <IDS> -H "Authorization: Bearer <TOKEN>" -mc all -fs <BASELINE_SIZE>
```

**Tool:** ffuf · **Platform:** Linux · **Tags:** API, authorization, IDOR · **Context:** Authenticated · **Noise:** Moderate

---

**Related:** APIs & GraphQL · Authentication · HTTP Methods
