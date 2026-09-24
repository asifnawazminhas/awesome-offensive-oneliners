# ACLs, GPOs and trusts

High-value relationship discovery using PowerView and native commands.

<div class="ol-section-kicker"><span>AD</span></div>

## PowerView interesting ACLs

```powershell
Find-InterestingDomainAcl -ResolveGUIDs
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user


## PowerView target ACL

```powershell
Get-DomainObjectAcl -Identity <OBJECT> -ResolveGUIDs
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user


## PowerView GPO list

```powershell
Get-DomainGPO | Select displayname,gpcfilesyspath
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user


## PowerView OU GPO links

```powershell
Get-DomainOU -Properties name,gplink
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user


## PowerView trusts

```powershell
Get-DomainTrust
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user


## Native domain trusts

```cmd
nltest /domain_trusts
```

**Tool:** nltest · **Platform:** Windows · **Context:** Domain user


## Forest trusts

```powershell
Get-ForestTrust
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user


## NetExec LDAP domain trusts

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --groups | grep -i trust
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user

---

**Related:** [Overview](./) · [Acls](acls.md)
