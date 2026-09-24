# Active Directory Enumeration

Core domain discovery one-liners.

### Current domain

```powershell
Get-Domain
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, Domain, Enumeration

### Domain users

```powershell
Get-DomainUser | Select-Object samaccountname
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, Users, Enumeration

### Domain groups

```powershell
Get-DomainGroup | Select-Object samaccountname
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, Groups, Enumeration

### Domain computers

```powershell
Get-DomainComputer | Select-Object dnshostname,operatingsystem
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, Computers, Enumeration

### Domain controllers

```powershell
Get-DomainController | Select-Object name,IPAddress,OSVersion
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, DC, Enumeration

### Domain trusts

```powershell
Get-DomainTrust
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, Trusts

### Group members

```powershell
Get-DomainGroupMember -Identity "<GROUP>" -Recurse
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, Groups

### Find local admin access

```powershell
Find-LocalAdminAccess
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, Local Admin

### LDAP users with NetExec

```bash
nxc ldap <DC> -u <USER> -p <PASSWORD> --users
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** LDAP, Users

### LDAP groups with NetExec

```bash
nxc ldap <DC> -u <USER> -p <PASSWORD> --groups
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** LDAP, Groups

