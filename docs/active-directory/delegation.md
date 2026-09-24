# Delegation

Quick checks for Kerberos delegation configurations.

### Constrained delegation

```powershell
Get-DomainComputer -TrustedToAuth -Properties DnsHostName,msDS-AllowedToDelegateTo
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** Delegation, Kerberos

### Unconstrained delegation

```powershell
Get-DomainComputer -Unconstrained | Select-Object dnshostname,useraccountcontrol
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** Delegation, Kerberos

### Users trusted for delegation

```powershell
Get-DomainUser -TrustedToAuth
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** Delegation, Users

### RBCD attribute search

```powershell
Get-DomainComputer -LDAPFilter "(msDS-AllowedToActOnBehalfOfOtherIdentity=*)" -Properties dnshostname,msDS-AllowedToActOnBehalfOfOtherIdentity
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** RBCD, Delegation

### NetExec delegation module

```bash
nxc ldap <DC> -u <USER> -p <PASSWORD> -M find-delegation
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** Delegation, LDAP

