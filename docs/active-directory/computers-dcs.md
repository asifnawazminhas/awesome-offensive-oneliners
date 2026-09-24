# Computers and domain controllers

Enumerate hosts, operating systems and domain-controller properties.

<div class="ol-section-kicker"><span>AD</span></div>

## PowerView computers

```powershell
Get-DomainComputer | Select-Object dnshostname,operatingsystem
```

**Tool:** PowerView · **Platform:** Windows


## PowerView servers only

```powershell
Get-DomainComputer -LDAPFilter '(operatingSystem=*Server*)' | Select dnshostname,operatingsystem
```

**Tool:** PowerView · **Platform:** Windows


## NetExec LDAP computers

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --computers
```

**Tool:** NetExec · **Platform:** Linux/macOS


## NetExec SMB host discovery

```bash
nxc smb <CIDR>
```

**Tool:** NetExec · **Platform:** Linux/macOS


## PowerView domain controllers

```powershell
Get-DomainController | Select-Object Name,IPAddress,OperatingSystem,SiteName
```

**Tool:** PowerView · **Platform:** Windows


## Native DC discovery

```cmd
nltest /dsgetdc:<DOMAIN>
```

**Tool:** nltest · **Platform:** Windows
