---
hide:
  - toc
---

# NetExec

Fast NetExec reference grouped around common SMB and LDAP tasks.

<div class="ol-section-kicker"><span>TOOLS</span></div>

## SMB discovery

```bash
nxc smb <CIDR>
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user


## SMB password authentication

```bash
nxc smb <TARGETS> -u <USER> -p '<PASSWORD>'
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user


## SMB NTLM authentication

```bash
nxc smb <TARGETS> -u <USER> -H <HASH>
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user


## SMB shares

```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --shares
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user


## SMB sessions

```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --sessions
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user


## SMB logged-on users

```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --loggedon-users
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user


## SMB password policy

```bash
nxc smb <DC_IP> -u <USER> -p '<PASSWORD>' --pass-pol
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user


## LDAP users

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --users
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user


## LDAP groups

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --groups
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user


## LDAP computers

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --computers
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user


## Kerberoast

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --kerberoasting kerberoast.txt
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user


## AS-REP roast

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --asreproast asrep.txt
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user


## SMB local administrators
```bash
nxc smb <TARGETS> -u <USER> -p '<PASSWORD>' --local-groups 544
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** SMB, Local Administrators · **Context:** Domain user

## SMB disks
```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --disks
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** SMB, Disks · **Context:** Domain user

## SMB users
```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --users
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** SMB, Users · **Context:** Domain user

## SMB groups
```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --groups
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** SMB, Groups · **Context:** Domain user

## SMB RID brute
```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --rid-brute
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** SMB, RID, Users · **Context:** Domain user

## SMB spider share
```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --spider <SHARE> --pattern '<PATTERN>'
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** SMB, Spider, Files · **Context:** Domain user

## LDAP password-not-required users
```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --password-not-required
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** LDAP, Accounts · **Context:** Domain user

## LDAP trusted-for-delegation
```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --trusted-for-delegation
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** LDAP, Delegation · **Context:** Domain user

## LDAP admin count
```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --admin-count
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** LDAP, adminCount · **Context:** Domain user

## LDAP active users
```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --active-users
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** LDAP, Users · **Context:** Domain user

## WinRM authentication check
```bash
nxc winrm <TARGETS> -u <USER> -p '<PASSWORD>'
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** WinRM, Authentication · **Context:** Valid user

## RDP authentication check
```bash
nxc rdp <TARGETS> -u <USER> -p '<PASSWORD>'
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** RDP, Authentication · **Context:** Valid user

## MSSQL authentication check
```bash
nxc mssql <TARGETS> -u <USER> -p '<PASSWORD>'
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** MSSQL, Authentication · **Context:** Valid user


---

**Related:** [Overview](./) · [Naabu](naabu.md) · [Nmap](nmap.md)
