# Trust Discovery

One-liners for mapping domain and forest trust relationships.

<div class="ol-section-kicker"><span>AD</span><strong>7 one-liners</strong></div>

## PowerView domain trusts

```powershell
Get-DomainTrust
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, trusts · **Context:** Domain user

## PowerView forest trusts

```powershell
Get-ForestTrust
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, forest, trusts · **Context:** Domain user

## Native domain trusts

```powershell
nltest /domain_trusts
```

**Tool:** nltest · **Platform:** Windows · **Tags:** AD, trusts · **Context:** Domain user

## Native trusted domains

```powershell
nltest /trusted_domains
```

**Tool:** nltest · **Platform:** Windows · **Tags:** AD, trusts · **Context:** Domain user

## List forest domains

```powershell
Get-ForestDomain
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, forest · **Context:** Domain user

## LDAP trustedDomain objects

```bash
ldapsearch -x -H ldap://<DC_IP> -D "<DOMAIN>\<USER>" -w '<PASSWORD>' -b "<BASE_DN>" "(objectClass=trustedDomain)" cn trustDirection trustType trustAttributes
```

**Tool:** ldapsearch · **Platform:** Linux · **Tags:** AD, LDAP, trusts · **Context:** Domain user

## NetExec LDAP trust query

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --query "(objectClass=trustedDomain)" "cn trustDirection trustType trustAttributes"
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** AD, LDAP, trusts · **Context:** Domain user

---

**Related:** ACLs · SID History · BloodHound
