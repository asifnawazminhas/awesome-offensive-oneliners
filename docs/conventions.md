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


## Metadata fields

Entries may include compact metadata when it changes how you use the command:

- **Context** - access level or operating position, such as No auth, User, Domain user, Local admin or SYSTEM.
- **Requires** - a prerequisite such as LDAP access, AWS credentials, `kubectl` context or a specific local binary.
- **Noise** - relative operational visibility: Quiet, Moderate or Loud. This is a heuristic, not a guarantee; telemetry and detections vary by environment.
- **Version** - version-sensitive syntax note. Prefer checking the installed tool with `--version` and `--help` rather than assuming a command is portable across major releases.

## Noise guide

| Label | Meaning |
| --- | --- |
| Quiet | Read-oriented or passive activity with limited request volume. |
| Moderate | Active enumeration, fuzzing, authentication attempts or execution likely to create useful telemetry. |
| Loud | High-volume scanning, broad execution, credential-replication style activity or actions commonly covered by detections. |
