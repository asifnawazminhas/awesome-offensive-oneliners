# Placeholder conventions

Use these placeholders consistently before copying a command.

| Placeholder | Meaning |
|---|---|
| `<TARGET>` | hostname, IP or URL target |
| `<DOMAIN>` | DNS or Active Directory domain |
| `<DC_IP>` | domain controller IP |
| `<USER>` | username |
| `<PASSWORD>` | password |
| `<HASH>` | NTLM or other hash |
| `<WORDLIST>` | wordlist path |
| `<FILE>` | input/output file |
| `<PORT>` | TCP/UDP port |
| `<CIDR>` | network range |
| `<URL>` | complete URL |

Keep replacements shell-safe and quote values when required.


## Context labels

Context labels are intentionally compact and describe the typical access level needed to use a one-liner.

| Label | Meaning |
|---|---|
| `No auth` | no authenticated session required |
| `User` | standard local, application or shell user context |
| `Domain user` | authenticated Active Directory domain account |
| `Local admin` | local administrator privileges required |
| `SYSTEM` | Windows SYSTEM context required |

Treat these as quick operator hints, not guarantees: product configuration and delegated rights can change what is available.
