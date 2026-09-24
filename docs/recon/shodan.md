# Shodan one-liners

Fast internet-exposure queries and CLI lookups.

<div class="ol-section-kicker"><span>RECON</span></div>

## Host details

```bash
shodan host <IP>
```

**Tool:** Shodan CLI · **Platform:** Cross-platform · **Context:** No auth


## Search hostname

```bash
shodan search --fields ip_str,port,org,hostnames 'hostname:<DOMAIN>'
```

**Tool:** Shodan CLI · **Platform:** Cross-platform · **Context:** No auth


## Search SSL certificate CN

```bash
shodan search --fields ip_str,port,hostnames 'ssl.cert.subject.cn:<DOMAIN>'
```

**Tool:** Shodan CLI · **Platform:** Cross-platform · **Context:** No auth


## Search organisation

```bash
shodan search --fields ip_str,port,product 'org:"<ORG>"'
```

**Tool:** Shodan CLI · **Platform:** Cross-platform · **Context:** No auth


## Search by HTTP title

```bash
shodan search --fields ip_str,port,hostnames 'http.title:"<TITLE>"'
```

**Tool:** Shodan CLI · **Platform:** Cross-platform · **Context:** No auth


## Download query results

```bash
shodan download results 'hostname:<DOMAIN>'
```

**Tool:** Shodan CLI · **Platform:** Cross-platform · **Context:** No auth


## Parse downloaded results

```bash
shodan parse --fields ip_str,port,hostnames results.json.gz
```

**Tool:** Shodan CLI · **Platform:** Cross-platform · **Context:** No auth

---

**Related:** [Overview](./) · [Screenshots](screenshots.md) · [Urls History](urls-history.md)
