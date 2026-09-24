# Awesome Offensive OneLiners

A practical collection of copyable one-line commands for penetration testing, Active Directory, red teaming, web security and offensive security operations.

**Website:** https://oneliners.asifnawazminhas.com/

## Project at a glance

- 840+ practical one-liners
- 140+ focused pages
- 8 major sections
- Search-first navigation with context labels and related-command links

## Philosophy

**One command. One objective. Minimal noise.**

The project prioritises scan-first one-liners, short metadata, useful tool alternatives, context labels, and related-command navigation instead of long tutorials.

## Coverage

- Active Directory: discovery, DNS/SPNs, ACLs, GPOs, trusts, RBCD, MSSQL, WinRM/RDP, sessions, local admins, password policy, LDAP and more
- Web: VHosts, parameters, uploads, traversal/LFI, APIs, authorization, WebSockets, request smuggling, cache, TLS, IIS and more
- Recon: passive sources, ASN/CIDR, cloud assets, DNS, permutations, screenshots, favicon pivots, code search and pipelines
- Windows: tokens, DPAPI, services, scheduled tasks, writable paths, Defender/ASR, UAC, PowerShell logging, AMSI and execution controls
- Linux: sudo, capabilities, systemd, cron, containers, NFS, writable services, PATH hijacking and credentials/configs
- Tools: NetExec, PowerView, Impacket, Certify, ldapsearch, dnsx, naabu, Nmap, gau, waybackurls, Feroxbuster, Arjun, kxss, Hashcat, John and more

## Local development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Open `http://127.0.0.1:8000/`.

## Build

```bash
mkdocs build --strict
```

## Responsible use

Use these commands only in systems and environments where you have explicit authorization to test.


## Recent coverage

Expanded AD DNS/SPN/group/account discovery, modern web parser/header checks, recon quality pipelines, CLM validation, LOLBin coverage, Sliver C2, and additional operator tool references.


## Coverage

The library spans Active Directory, Windows, Linux, Web, Recon, Cloud, Kubernetes, Red Team, Credentials and operator tooling. Entries stay one-liner first, with compact Context, Requires, Noise and version-sensitive notes where useful.
