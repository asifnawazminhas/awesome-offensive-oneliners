# Users and groups

Enumerate accounts, groups, memberships and common account properties.

<div class="ol-section-kicker"><span>AD</span></div>

## PowerView all users

```powershell
Get-DomainUser | Select-Object samaccountname
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user · **Noise:** Quiet


## PowerView enabled users

```powershell
Get-DomainUser -LDAPFilter '(!(userAccountControl:1.2.840.113556.1.4.803:=2))' | Select samaccountname
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user · **Noise:** Quiet


## PowerView privileged descriptions

```powershell
Get-DomainUser -Properties samaccountname,description | Where-Object description | Format-Table -Auto
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user · **Noise:** Quiet


## NetExec LDAP users

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --users
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Quiet


## NetExec LDAP groups

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --groups
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Quiet


## Impacket GetADUsers

```bash
GetADUsers.py -all '<DOMAIN>/<USER>:<PASSWORD>' -dc-ip <DC_IP>
```

**Tool:** Impacket · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Quiet


## Native domain users

```cmd
net user /domain
```

**Tool:** net.exe · **Platform:** Windows · **Context:** Domain user · **Noise:** Quiet


## Native domain admins

```cmd
net group "Domain Admins" /domain
```

**Tool:** net.exe · **Platform:** Windows · **Context:** Domain user · **Noise:** Quiet


## PowerView members of a group

```powershell
Get-DomainGroupMember -Identity 'Domain Admins' -Recurse
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user · **Noise:** Quiet

---

**Related:** [Overview](./) · [Trusts](trusts.md) · [Winrm Rdp](winrm-rdp.md)
