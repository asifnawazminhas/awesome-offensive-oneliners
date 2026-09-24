---
hide:
  - toc
---
# NetExec Database & Workspace Helpers

Useful NetExec database and protocol-workspace one-liners.

<div class="ol-section-kicker"><span>AD</span><strong>NXC</strong></div>

## Open NetExec database shell
```bash
nxcdb
```
**Tool:** NetExec · **Platform:** Linux · **Tags:** Database, Workspace · **Context:** Local

## List NetExec workspaces
```bash
nxcdb -h
```
**Tool:** NetExec · **Platform:** Linux · **Tags:** Database, Help · **Context:** Local

## SMB host discovery
```bash
nxc smb <CIDR>
```
**Tool:** NetExec · **Platform:** Linux · **Tags:** SMB, Discovery · **Context:** No auth

## LDAP authenticated baseline
```bash
nxc ldap <DC_IP> -u '<USER>' -p '<PASSWORD>'
```
**Tool:** NetExec · **Platform:** Linux · **Tags:** LDAP, Authentication · **Context:** Domain user

## Export LDAP users
```bash
nxc ldap <DC_IP> -u '<USER>' -p '<PASSWORD>' --users | tee nxc-users.txt
```
**Tool:** NetExec · **Platform:** Linux · **Tags:** LDAP, Users, Export · **Context:** Domain user

## Export SMB shares
```bash
nxc smb <TARGETS> -u '<USER>' -p '<PASSWORD>' --shares | tee nxc-shares.txt
```
**Tool:** NetExec · **Platform:** Linux · **Tags:** SMB, Shares, Export · **Context:** Domain user

**Related:** [NetExec Modules](netexec-modules.md) · [SMB, Shares & Sessions](smb-shares-sessions.md) · [LDAP Filters](ldap-filters.md)
