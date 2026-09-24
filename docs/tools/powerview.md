---
hide:
  - toc
---

# PowerView

Fast PowerView reference for domain discovery and relationships.

<div class="ol-section-kicker"><span>TOOLS</span></div>

## Domain

```powershell
Get-Domain
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user


## Domain controllers

```powershell
Get-DomainController
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user


## Users

```powershell
Get-DomainUser | Select samaccountname
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user


## Groups

```powershell
Get-DomainGroup | Select samaccountname
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user


## Computers

```powershell
Get-DomainComputer | Select dnshostname,operatingsystem
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user


## SPN users

```powershell
Get-DomainUser -SPN
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user


## AS-REP candidates

```powershell
Get-DomainUser -PreauthNotRequired
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user


## Constrained delegation

```powershell
Get-DomainComputer -TrustedToAuth -Properties DnsHostName,msDS-AllowedToDelegateTo
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user


## Unconstrained delegation

```powershell
Get-DomainComputer -Unconstrained
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user


## Domain trusts

```powershell
Get-DomainTrust
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user


## Interesting ACLs

```powershell
Find-InterestingDomainAcl -ResolveGUIDs
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user

---

**Related:** [Overview](./) · [Powerview Rubeus](powerview-rubeus.md) · [Smbclient](smbclient.md)
