# Masscan

<div class="ol-section-kicker"><span>TOOL</span><strong>MASSCAN</strong></div>

## Common ports
```bash
masscan <CIDR> -p80,443,445,3389 --rate 1000
```
**Tool:** Masscan · **Platform:** Linux · **Tags:** Ports, Discovery · **Context:** Network access

## Top-range scan
```bash
masscan <CIDR> -p1-10000 --rate 1000
```
**Tool:** Masscan · **Platform:** Linux · **Tags:** Ports, Range · **Context:** Network access

## Save list output
```bash
masscan <CIDR> -p1-65535 --rate 1000 -oL masscan.txt
```
**Tool:** Masscan · **Platform:** Linux · **Tags:** Output, Ports · **Context:** Network access

## Extract IP:port pairs
```bash
awk '/open/{print $4":"$3}' masscan.txt
```
**Tool:** awk · **Platform:** Linux/macOS · **Tags:** Parsing, Masscan · **Context:** Local
