# Computers and domain controllers

Enumerate hosts, operating systems and domain-controller properties.

<div class="ol-section-kicker"><span>AD</span></div>

## PowerView computers

```powershell
Get-DomainComputer | Select-Object dnshostname,operatingsystem
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user


## PowerView servers only

```powershell
Get-DomainComputer -LDAPFilter '(operatingSystem=*Server*)' | Select dnshostname,operatingsystem
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user


## NetExec LDAP computers

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --computers
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user


## NetExec SMB host discovery

```bash
nxc smb <CIDR>
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user


## PowerView domain controllers

```powershell
Get-DomainController | Select-Object Name,IPAddress,OperatingSystem,SiteName
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user


## Native DC discovery

```cmd
nltest /dsgetdc:<DOMAIN>
```

**Tool:** nltest · **Platform:** Windows · **Context:** Domain user

---

**Related:** [Overview](./) · [Bloodhound](bloodhound.md) · [Delegation](delegation.md)
