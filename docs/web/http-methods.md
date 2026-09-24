# HTTP Methods

One-liners for discovering allowed methods and method-dependent behavior.

<div class="ol-section-kicker"><span>WEB</span><strong>6 one-liners</strong></div>

## OPTIONS methods

```bash
curl -sk -i -X OPTIONS https://<TARGET>/<PATH>
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, HTTP methods · **Context:** No auth · **Noise:** Moderate

## HEAD request

```bash
curl -skI https://<TARGET>/<PATH>
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, HTTP, HEAD · **Context:** No auth · **Noise:** Moderate

## TRACE probe

```bash
curl -sk -i -X TRACE https://<TARGET>/<PATH>
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, TRACE · **Context:** No auth · **Noise:** Moderate

## PUT probe

```bash
curl -sk -i -X PUT https://<TARGET>/<PATH>/<NAME> --data-binary 'test'
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, PUT · **Context:** Authenticated · **Noise:** Moderate

## DELETE probe

```bash
curl -sk -i -X DELETE https://<TARGET>/<PATH>/<RESOURCE>
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, DELETE · **Context:** Authenticated · **Noise:** Moderate

## Nmap methods script

```bash
nmap -Pn -p443 --script http-methods --script-args http-methods.url-path='/<PATH>' <TARGET>
```

**Tool:** Nmap · **Platform:** Linux · **Tags:** Web, HTTP methods · **Context:** No auth · **Noise:** Moderate

---

**Related:** File Upload · Request Smuggling · APIs & GraphQL
