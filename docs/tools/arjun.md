# Arjun

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

Arjun one-liners for HTTP parameter discovery across methods and target lists.

<div class="ol-section-kicker"><span>TOOL</span><strong>5 one-liners</strong></div>

## GET parameters

```bash
arjun -u https://<TARGET>/<ENDPOINT> -m GET
```

**Tool:** Arjun · **Platform:** Linux · **Tags:** parameters, web · **Context:** No auth · **Noise:** Moderate

## POST parameters

```bash
arjun -u https://<TARGET>/<ENDPOINT> -m POST
```

**Tool:** Arjun · **Platform:** Linux · **Tags:** parameters, POST · **Context:** No auth · **Noise:** Moderate

## JSON parameters

```bash
arjun -u https://<TARGET>/<ENDPOINT> -m JSON
```

**Tool:** Arjun · **Platform:** Linux · **Tags:** parameters, JSON · **Context:** No auth · **Noise:** Moderate

## Target list

```bash
arjun -i urls.txt -oT arjun.txt
```

**Tool:** Arjun · **Platform:** Linux · **Tags:** parameters, list · **Context:** No auth · **Noise:** Moderate

## Custom headers

```bash
arjun -u https://<TARGET>/<ENDPOINT> --headers "Authorization: Bearer <TOKEN>"
```

**Tool:** Arjun · **Platform:** Linux · **Tags:** parameters, auth · **Context:** Authenticated · **Noise:** Moderate

---

**Related:** Parameters · API Authorization · ffuf
