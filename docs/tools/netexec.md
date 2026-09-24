---
hide:
  - toc
---

# NetExec

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

<span class="ol-search-aliases">nxc netexec crackmapexec cme smb ldap winrm mssql rdp</span>

Fast NetExec reference grouped around common SMB and LDAP tasks.

<div class="ol-section-kicker"><span>TOOLS</span></div>

## SMB discovery

```bash
nxc smb <CIDR>
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Moderate


## SMB password authentication

```bash
nxc smb <TARGETS> -u <USER> -p '<PASSWORD>'
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Moderate


## SMB NTLM authentication

```bash
nxc smb <TARGETS> -u <USER> -H <HASH>
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Moderate


## SMB shares

```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --shares
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Moderate


## SMB sessions

```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --sessions
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Moderate


## SMB logged-on users

```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --loggedon-users
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Moderate


## SMB password policy

```bash
nxc smb <DC_IP> -u <USER> -p '<PASSWORD>' --pass-pol
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Moderate


## LDAP users

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --users
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Moderate


## LDAP groups

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --groups
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Moderate


## LDAP computers

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --computers
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Moderate


## Kerberoast

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --kerberoasting kerberoast.txt
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Moderate


## AS-REP roast

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --asreproast asrep.txt
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Moderate


## SMB local administrators
```bash
nxc smb <TARGETS> -u <USER> -p '<PASSWORD>' --local-groups 544
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** SMB, Local Administrators · **Context:** Domain user · **Noise:** Moderate

## SMB disks
```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --disks
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** SMB, Disks · **Context:** Domain user · **Noise:** Moderate

## SMB users
```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --users
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** SMB, Users · **Context:** Domain user · **Noise:** Moderate

## SMB groups
```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --groups
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** SMB, Groups · **Context:** Domain user · **Noise:** Moderate

## SMB RID brute
```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --rid-brute
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** SMB, RID, Users · **Context:** Domain user · **Noise:** Moderate

## SMB spider share
```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --spider <SHARE> --pattern '<PATTERN>'
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** SMB, Spider, Files · **Context:** Domain user · **Noise:** Moderate

## LDAP password-not-required users
```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --password-not-required
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** LDAP, Accounts · **Context:** Domain user · **Noise:** Moderate

## LDAP trusted-for-delegation
```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --trusted-for-delegation
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** LDAP, Delegation · **Context:** Domain user · **Noise:** Moderate

## LDAP admin count
```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --admin-count
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** LDAP, adminCount · **Context:** Domain user · **Noise:** Moderate

## LDAP active users
```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --active-users
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** LDAP, Users · **Context:** Domain user · **Noise:** Moderate

## WinRM authentication check
```bash
nxc winrm <TARGETS> -u <USER> -p '<PASSWORD>'
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** WinRM, Authentication · **Context:** Valid user · **Noise:** Moderate

## RDP authentication check
```bash
nxc rdp <TARGETS> -u <USER> -p '<PASSWORD>'
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** RDP, Authentication · **Context:** Valid user · **Noise:** Moderate

## MSSQL authentication check
```bash
nxc mssql <TARGETS> -u <USER> -p '<PASSWORD>'
```
**Tool:** NetExec · **Platform:** Linux/macOS · **Tags:** MSSQL, Authentication · **Context:** Valid user · **Noise:** Moderate


---

**Related:** [Overview](./) · [Naabu](naabu.md) · [Nmap](nmap.md)
