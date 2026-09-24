# Ports and services

Quick service discovery before deeper enumeration.

<div class="ol-section-kicker"><span>RECON</span></div>

## Naabu top ports

```bash
naabu -list hosts.txt -top-ports 1000 -silent
```

**Tool:** naabu · **Platform:** Linux/macOS


## Naabu to Nmap service scan

```bash
naabu -list hosts.txt -top-ports 1000 -silent | nmap -sV -iL -
```

**Tool:** naabu + nmap · **Platform:** Linux/macOS · **Tags:** Pipeline


## Nmap all TCP ports

```bash
nmap -Pn -p- --min-rate 2000 -T4 <TARGET>
```

**Tool:** nmap · **Platform:** Cross-platform


## Nmap service detection

```bash
nmap -Pn -sV -sC -p <PORTS> <TARGET>
```

**Tool:** nmap · **Platform:** Cross-platform


## Masscan fast sweep

```bash
masscan <CIDR> -p1-65535 --rate 5000 -oL masscan.txt
```

**Tool:** masscan · **Platform:** Linux


## Extract open host:port pairs from Nmap grepable

```bash
awk '/Ports:/{ip=$2; for(i=1;i<=NF;i++) if($i ~ /open\//) print ip,$i}' nmap.gnmap
```

**Tool:** awk · **Platform:** Linux/macOS
