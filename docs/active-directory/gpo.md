# GPO Enumeration

One-liners for discovering Group Policy objects, links and applied settings.

<div class="ol-section-kicker"><span>AD</span><strong>7 one-liners</strong></div>

## List GPOs with PowerView

```powershell
Get-DomainGPO | Select-Object displayName,name
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, GPO · **Context:** Domain user

## Find GPO by name

```powershell
Get-DomainGPO -Identity "<GPO_NAME>"
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, GPO · **Context:** Domain user

## Map GPOs to OUs

```powershell
Get-DomainOU | Select-Object name,gplink
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, GPO, OU · **Context:** Domain user

## Applied GPOs for current host

```powershell
gpresult /r
```

**Tool:** gpresult · **Platform:** Windows · **Tags:** AD, GPO · **Context:** User

## Export detailed GPO result

```powershell
gpresult /h C:\Windows\Temp\gp.html
```

**Tool:** gpresult · **Platform:** Windows · **Tags:** AD, GPO · **Context:** User

## List GPOs with native module

```powershell
Get-GPO -All | Select DisplayName,Id,GpoStatus
```

**Tool:** GroupPolicy · **Platform:** Windows · **Tags:** AD, GPO · **Context:** Domain user

## LDAP GPO objects

```bash
ldapsearch -x -H ldap://<DC_IP> -D "<DOMAIN>\<USER>" -w '<PASSWORD>' -b "CN=Policies,CN=System,<BASE_DN>" "(objectClass=groupPolicyContainer)" displayName name
```

**Tool:** ldapsearch · **Platform:** Linux · **Tags:** AD, LDAP, GPO · **Context:** Domain user

---

**Related:** ACLs · Domain Discovery · BloodHound
