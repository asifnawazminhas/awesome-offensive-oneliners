# Arjun

Arjun one-liners for HTTP parameter discovery across methods and target lists.

<div class="ol-section-kicker"><span>TOOL</span><strong>5 one-liners</strong></div>

## GET parameters

```bash
arjun -u https://<TARGET>/<ENDPOINT> -m GET
```

**Tool:** Arjun · **Platform:** Linux · **Tags:** parameters, web · **Context:** No auth

## POST parameters

```bash
arjun -u https://<TARGET>/<ENDPOINT> -m POST
```

**Tool:** Arjun · **Platform:** Linux · **Tags:** parameters, POST · **Context:** No auth

## JSON parameters

```bash
arjun -u https://<TARGET>/<ENDPOINT> -m JSON
```

**Tool:** Arjun · **Platform:** Linux · **Tags:** parameters, JSON · **Context:** No auth

## Target list

```bash
arjun -i urls.txt -oT arjun.txt
```

**Tool:** Arjun · **Platform:** Linux · **Tags:** parameters, list · **Context:** No auth

## Custom headers

```bash
arjun -u https://<TARGET>/<ENDPOINT> --headers "Authorization: Bearer <TOKEN>"
```

**Tool:** Arjun · **Platform:** Linux · **Tags:** parameters, auth · **Context:** Authenticated

---

**Related:** Parameters · API Authorization · ffuf
