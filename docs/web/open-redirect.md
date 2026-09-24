# Open Redirect

One-liners for finding and validating redirect parameters.

<div class="ol-section-kicker"><span>WEB</span><strong>5 one-liners</strong></div>

## Find redirect-like parameters

```bash
gau <DOMAIN> | grep -Ei "(url|uri|redirect|return|next|continue|dest|destination|callback)=" | sort -u
```

**Tool:** gau · **Platform:** Linux · **Tags:** Web, redirect, parameters · **Context:** No auth · **Noise:** Moderate

## Direct redirect probe

```bash
curl -skI "https://<TARGET>/<PATH>?next=https://example.org" | grep -i "^Location:"
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, open redirect · **Context:** No auth · **Noise:** Moderate

## Scheme-relative probe

```bash
curl -skI "https://<TARGET>/<PATH>?next=//example.org" | grep -i "^Location:"
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, open redirect · **Context:** No auth · **Noise:** Moderate

## Encoded redirect probe

```bash
curl -skI "https://<TARGET>/<PATH>?next=https%3A%2F%2Fexample.org" | grep -i "^Location:"
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, open redirect, encoding · **Context:** No auth · **Noise:** Moderate

## ffuf redirect parameter values

```bash
ffuf -u "https://<TARGET>/<PATH>?next=FUZZ" -w <REDIRECT_PAYLOADS> -mc 301,302,303,307,308
```

**Tool:** ffuf · **Platform:** Linux · **Tags:** Web, open redirect, fuzzing · **Context:** No auth · **Noise:** Moderate

---

**Related:** Parameters · OAuth/OIDC · Cache Poisoning
