# Nmap

Compact Nmap one-liners for host discovery, service detection and common protocol enumeration.

<div class="ol-section-kicker"><span>TOOL</span><strong>6 one-liners</strong></div>

## Fast service scan

```bash
nmap -Pn -sV --top-ports 1000 <TARGET>
```

**Tool:** Nmap · **Platform:** Linux · **Tags:** ports, services · **Context:** No auth

## All TCP ports

```bash
nmap -Pn -p- --min-rate 1000 <TARGET>
```

**Tool:** Nmap · **Platform:** Linux · **Tags:** ports, TCP · **Context:** No auth

## Service scripts

```bash
nmap -Pn -sV -sC -p <PORTS> <TARGET>
```

**Tool:** Nmap · **Platform:** Linux · **Tags:** services, NSE · **Context:** No auth

## SMB discovery

```bash
nmap -Pn -p445 --script smb-protocols,smb2-security-mode,smb2-time <TARGET>
```

**Tool:** Nmap · **Platform:** Linux · **Tags:** SMB, NSE · **Context:** No auth

## TLS enumeration

```bash
nmap -Pn -p443 --script ssl-cert,ssl-enum-ciphers <TARGET>
```

**Tool:** Nmap · **Platform:** Linux · **Tags:** TLS, NSE · **Context:** No auth

## HTTP title and headers

```bash
nmap -Pn -p80,443,8080,8443 --script http-title,http-headers <TARGET>
```

**Tool:** Nmap · **Platform:** Linux · **Tags:** HTTP, NSE · **Context:** No auth

---

**Related:** Ports & Services · TLS & Certificates · SMB
