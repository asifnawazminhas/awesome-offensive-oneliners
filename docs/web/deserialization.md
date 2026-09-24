# Deserialization Discovery

Fast one-liners for spotting serialized formats and common deserialization surfaces.

<div class="ol-section-kicker"><span>WEB</span><strong>5 one-liners</strong></div>

## Find Java serialization magic in files

```bash
grep -RIl $'\xAC\xED\x00\x05' . 2>/dev/null
```

**Tool:** grep · **Platform:** Linux · **Tags:** Web, deserialization, Java · **Context:** User

## Find PHP serialized parameters

```bash
grep -RIE "(^|[=:\"'])O:[0-9]+:\"|a:[0-9]+:\{" urls.txt
```

**Tool:** grep · **Platform:** Linux · **Tags:** Web, deserialization, PHP · **Context:** User

## Decode base64-looking cookie

```bash
echo '<COOKIE>' | base64 -d 2>/dev/null | strings
```

**Tool:** base64 · **Platform:** Any · **Tags:** Web, cookies, deserialization · **Context:** Authenticated

## Search responses for Java class names

```bash
curl -sk https://<TARGET>/ | grep -Eo "java\.[A-Za-z0-9_.]+|javax\.[A-Za-z0-9_.]+" | sort -u
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, Java, fingerprinting · **Context:** No auth

## Nuclei deserialization templates

```bash
nuclei -u https://<TARGET> -tags deserialization -silent
```

**Tool:** Nuclei · **Platform:** Linux · **Tags:** Web, deserialization · **Context:** No auth

---

**Related:** Technologies · Popular Software · APIs & GraphQL
