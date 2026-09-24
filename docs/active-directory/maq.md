# Machine Account Quota

One-liners for reading the domain machine-account quota and related computer creation context.

<div class="ol-section-kicker"><span>AD</span><strong>4 one-liners</strong></div>

## PowerView MAQ

```powershell
Get-DomainObject -Identity (Get-Domain).DistinguishedName -Properties ms-DS-MachineAccountQuota | Select ms-DS-MachineAccountQuota
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, MAQ · **Context:** Domain user

## LDAP MAQ

```bash
ldapsearch -x -H ldap://<DC_IP> -D "<DOMAIN>\<USER>" -w '<PASSWORD>' -b "<BASE_DN>" -s base "(objectClass=*)" ms-DS-MachineAccountQuota
```

**Tool:** ldapsearch · **Platform:** Linux · **Tags:** AD, LDAP, MAQ · **Context:** Domain user

## NetExec MAQ query

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --query "(objectClass=domain)" "ms-DS-MachineAccountQuota"
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** AD, LDAP, MAQ · **Context:** Domain user

## List recently created computers

```powershell
Get-DomainComputer -Properties samaccountname,whenCreated | Sort-Object whenCreated -Descending | Select -First 20
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, computers, MAQ · **Context:** Domain user

---

**Related:** RBCD · Computers & DCs · ACLs
