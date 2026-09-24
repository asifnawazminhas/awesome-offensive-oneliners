# SID History

One-liners for finding accounts with SIDHistory and resolving inherited identifiers.

<div class="ol-section-kicker"><span>AD</span><strong>4 one-liners</strong></div>

## PowerView SIDHistory users

```powershell
Get-DomainUser -Properties samaccountname,sidhistory | Where-Object {$_.sidhistory}
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, SIDHistory · **Context:** Domain user

## PowerView SIDHistory groups

```powershell
Get-DomainGroup -Properties samaccountname,sidhistory | Where-Object {$_.sidhistory}
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, SIDHistory · **Context:** Domain user

## LDAP SIDHistory users

```bash
ldapsearch -x -H ldap://<DC_IP> -D "<DOMAIN>\<USER>" -w '<PASSWORD>' -b "<BASE_DN>" "(sIDHistory=*)" sAMAccountName sIDHistory
```

**Tool:** ldapsearch · **Platform:** Linux · **Tags:** AD, LDAP, SIDHistory · **Context:** Domain user

## NetExec SIDHistory query

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --query "(sIDHistory=*)" "sAMAccountName sIDHistory"
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** AD, SIDHistory · **Context:** Domain user

---

**Related:** Trusts · Users & Groups · LDAP Filters
