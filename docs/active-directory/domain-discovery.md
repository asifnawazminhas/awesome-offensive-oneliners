# Domain discovery

One-liners to identify the domain, domain controllers, policy and LDAP context.

<div class="ol-section-kicker"><span>AD</span></div>

## PowerView current domain

```powershell
Get-Domain
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user


## PowerView domain controllers

```powershell
Get-DomainController
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user


## Native current domain

```powershell
[System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()
```

**Tool:** PowerShell/.NET · **Platform:** Windows


## Native domain controller list

```cmd
nltest /dclist:<DOMAIN>
```

**Tool:** nltest · **Platform:** Windows


## DNS domain-controller SRV

```cmd
nslookup -type=SRV _ldap._tcp.dc._msdcs.<DOMAIN>
```

**Tool:** nslookup · **Platform:** Windows


## NetExec LDAP users sanity check

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --users
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user


## NetExec password policy

```bash
nxc smb <DC_IP> -u <USER> -p '<PASSWORD>' --pass-pol
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user


## Native domain policy

```cmd
net accounts /domain
```

**Tool:** net.exe · **Platform:** Windows · **Context:** Domain user
