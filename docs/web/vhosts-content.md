# Virtual hosts and content discovery

Discover alternate virtual hosts, directories, files and endpoints.

<div class="ol-section-kicker"><span>WEB</span></div>

## ffuf virtual-host discovery

```bash
ffuf -w <WORDLIST> -u http://<TARGET>/ -H "Host: FUZZ.<DOMAIN>" -ac
```

**Tool:** ffuf · **Platform:** Linux/macOS · **Tags:** VHost, Discovery


## ffuf vhost interesting codes

```bash
ffuf -w <WORDLIST> -u https://<TARGET>/ -H "Host: FUZZ.<DOMAIN>" -mc 200,204,301,302,307,401,403 -ac
```

**Tool:** ffuf · **Platform:** Linux/macOS


## Gobuster virtual hosts

```bash
gobuster vhost -u https://<TARGET> -w <WORDLIST> --append-domain
```

**Tool:** gobuster · **Platform:** Linux/macOS


## ffuf directory discovery

```bash
ffuf -w <WORDLIST> -u https://<TARGET>/FUZZ -ac
```

**Tool:** ffuf · **Platform:** Linux/macOS


## ffuf extensions

```bash
ffuf -w <WORDLIST> -u https://<TARGET>/FUZZ -e .php,.asp,.aspx,.jsp,.json,.txt,.bak,.old,.zip -ac
```

**Tool:** ffuf · **Platform:** Linux/macOS


## Gobuster directory discovery

```bash
gobuster dir -u https://<TARGET> -w <WORDLIST> -x php,asp,aspx,jsp,json,txt,bak -k
```

**Tool:** gobuster · **Platform:** Linux/macOS


## Feroxbuster recursive discovery

```bash
feroxbuster -u https://<TARGET> -w <WORDLIST> -x php,asp,aspx,jsp,json,txt,bak -k
```

**Tool:** feroxbuster · **Platform:** Linux/macOS


## Dirsearch common extensions

```bash
dirsearch -u https://<TARGET> -e php,asp,aspx,jsp,json,txt,bak,old,zip --random-agent
```

**Tool:** dirsearch · **Platform:** Linux/macOS
