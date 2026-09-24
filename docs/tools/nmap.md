# Nmap

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

Compact Nmap one-liners for host discovery, service detection and common protocol enumeration.

<div class="ol-section-kicker"><span>TOOL</span><strong>6 one-liners</strong></div>

## Fast service scan

```bash
nmap -Pn -sV --top-ports 1000 <TARGET>
```

**Tool:** Nmap · **Platform:** Linux · **Tags:** ports, services · **Context:** No auth · **Noise:** Moderate

## All TCP ports

```bash
nmap -Pn -p- --min-rate 1000 <TARGET>
```

**Tool:** Nmap · **Platform:** Linux · **Tags:** ports, TCP · **Context:** No auth · **Noise:** Moderate

## Service scripts

```bash
nmap -Pn -sV -sC -p <PORTS> <TARGET>
```

**Tool:** Nmap · **Platform:** Linux · **Tags:** services, NSE · **Context:** No auth · **Noise:** Moderate

## SMB discovery

```bash
nmap -Pn -p445 --script smb-protocols,smb2-security-mode,smb2-time <TARGET>
```

**Tool:** Nmap · **Platform:** Linux · **Tags:** SMB, NSE · **Context:** No auth · **Noise:** Moderate

## TLS enumeration

```bash
nmap -Pn -p443 --script ssl-cert,ssl-enum-ciphers <TARGET>
```

**Tool:** Nmap · **Platform:** Linux · **Tags:** TLS, NSE · **Context:** No auth · **Noise:** Moderate

## HTTP title and headers

```bash
nmap -Pn -p80,443,8080,8443 --script http-title,http-headers <TARGET>
```

**Tool:** Nmap · **Platform:** Linux · **Tags:** HTTP, NSE · **Context:** No auth · **Noise:** Moderate

---

**Related:** Ports & Services · TLS & Certificates · SMB
