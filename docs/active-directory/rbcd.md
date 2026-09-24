# RBCD Discovery

Resource-based constrained delegation discovery one-liners.

<div class="ol-section-kicker"><span>AD</span><strong>5 one-liners</strong></div>

## PowerView RBCD attribute

```powershell
Get-DomainComputer -Properties dNSHostName,msDS-AllowedToActOnBehalfOfOtherIdentity | Where-Object {$_.'msDS-AllowedToActOnBehalfOfOtherIdentity'}
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, RBCD, delegation · **Context:** Domain user

## LDAP RBCD objects

```bash
ldapsearch -x -H ldap://<DC_IP> -D "<DOMAIN>\<USER>" -w '<PASSWORD>' -b "<BASE_DN>" "(msDS-AllowedToActOnBehalfOfOtherIdentity=*)" dNSHostName msDS-AllowedToActOnBehalfOfOtherIdentity
```

**Tool:** ldapsearch · **Platform:** Linux · **Tags:** AD, LDAP, RBCD · **Context:** Domain user

## NetExec RBCD LDAP query

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --query "(msDS-AllowedToActOnBehalfOfOtherIdentity=*)" "dNSHostName msDS-AllowedToActOnBehalfOfOtherIdentity"
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** AD, LDAP, RBCD · **Context:** Domain user

## Find writable computer ACLs

```powershell
Find-InterestingDomainAcl -ResolveGUIDs | Where-Object {$_.ObjectAceType -match "Computer" -and $_.ActiveDirectoryRights -match "GenericWrite|GenericAll|WriteDacl|WriteOwner"}
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, ACL, RBCD · **Context:** Domain user

## Check machine account quota

```powershell
Get-DomainObject -Identity "DC=<DOMAIN_COMPONENT>" -Properties ms-DS-MachineAccountQuota
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, MAQ, RBCD · **Context:** Domain user

---

**Related:** Delegation · ACLs · Machine Account Quota
