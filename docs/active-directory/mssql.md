# MSSQL Discovery

One-liners for discovering SQL Server SPNs, instances and reachable services.

<div class="ol-section-kicker"><span>AD</span><strong>6 one-liners</strong></div>

## Find MSSQL SPNs

```powershell
Get-DomainUser -SPN | Where-Object {$_.serviceprincipalname -match "MSSQLSvc"} | Select samaccountname,serviceprincipalname
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, MSSQL, SPN · **Context:** Domain user

## Find SQL SPNs with setspn

```powershell
setspn -Q MSSQLSvc/*
```

**Tool:** setspn · **Platform:** Windows · **Tags:** AD, MSSQL, SPN · **Context:** Domain user

## Discover MSSQL with NetExec

```bash
nxc mssql <TARGETS> -u <USER> -p '<PASSWORD>'
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** AD, MSSQL · **Context:** Domain user

## Windows integrated sqlcmd

```powershell
sqlcmd -S <SERVER> -E -Q "SELECT @@version"
```

**Tool:** sqlcmd · **Platform:** Windows · **Tags:** MSSQL · **Context:** Domain user

## SQL auth sqlcmd

```powershell
sqlcmd -S <SERVER> -U <USER> -P '<PASSWORD>' -Q "SELECT SYSTEM_USER,@@servername"
```

**Tool:** sqlcmd · **Platform:** Windows · **Tags:** MSSQL · **Context:** Authenticated

## Impacket MSSQL client

```bash
mssqlclient.py <DOMAIN>/<USER>:<PASSWORD>@<SERVER> -windows-auth
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** AD, MSSQL · **Context:** Domain user

---

**Related:** SPN Discovery · Kerberos · NetExec
