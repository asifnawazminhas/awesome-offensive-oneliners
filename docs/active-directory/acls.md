# ACL Discovery

ACL-focused one-liners for finding interesting delegated rights and object control.

<div class="ol-section-kicker"><span>AD</span><strong>7 one-liners</strong></div>

## Find interesting ACLs

```powershell
Find-InterestingDomainAcl -ResolveGUIDs
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, ACL · **Context:** Domain user · **Noise:** Quiet

## ACLs for one object

```powershell
Get-DomainObjectAcl -Identity <OBJECT> -ResolveGUIDs
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, ACL · **Context:** Domain user · **Noise:** Quiet

## ACLs for one principal

```powershell
Get-DomainObjectAcl -ResolveGUIDs | Where-Object {$_.SecurityIdentifier -eq "<SID>"}
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, ACL · **Context:** Domain user · **Noise:** Quiet

## Find GenericAll

```powershell
Find-InterestingDomainAcl -ResolveGUIDs | Where-Object {$_.ActiveDirectoryRights -match "GenericAll"}
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, ACL, GenericAll · **Context:** Domain user · **Noise:** Quiet

## Find GenericWrite

```powershell
Find-InterestingDomainAcl -ResolveGUIDs | Where-Object {$_.ActiveDirectoryRights -match "GenericWrite"}
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, ACL, GenericWrite · **Context:** Domain user · **Noise:** Quiet

## Find WriteDacl or WriteOwner

```powershell
Find-InterestingDomainAcl -ResolveGUIDs | Where-Object {$_.ActiveDirectoryRights -match "WriteDacl|WriteOwner"}
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, ACL · **Context:** Domain user · **Noise:** Quiet

## BloodHound ACL collection

```bash
bloodhound-python -u <USER> -p '<PASSWORD>' -d <DOMAIN> -ns <DC_IP> -c ACL,ObjectProps
```

**Tool:** BloodHound · **Platform:** Linux · **Tags:** AD, ACL, BloodHound · **Context:** Domain user · **Noise:** Quiet

---

**Related:** BloodHound · Users & Groups · RBCD
