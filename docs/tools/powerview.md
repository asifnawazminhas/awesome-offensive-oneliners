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

**Tool:** PowerView · **Platform:** Windows


## Domain controllers

```powershell
Get-DomainController
```

**Tool:** PowerView · **Platform:** Windows


## Users

```powershell
Get-DomainUser | Select samaccountname
```

**Tool:** PowerView · **Platform:** Windows


## Groups

```powershell
Get-DomainGroup | Select samaccountname
```

**Tool:** PowerView · **Platform:** Windows


## Computers

```powershell
Get-DomainComputer | Select dnshostname,operatingsystem
```

**Tool:** PowerView · **Platform:** Windows


## SPN users

```powershell
Get-DomainUser -SPN
```

**Tool:** PowerView · **Platform:** Windows


## AS-REP candidates

```powershell
Get-DomainUser -PreauthNotRequired
```

**Tool:** PowerView · **Platform:** Windows


## Constrained delegation

```powershell
Get-DomainComputer -TrustedToAuth -Properties DnsHostName,msDS-AllowedToDelegateTo
```

**Tool:** PowerView · **Platform:** Windows


## Unconstrained delegation

```powershell
Get-DomainComputer -Unconstrained
```

**Tool:** PowerView · **Platform:** Windows


## Domain trusts

```powershell
Get-DomainTrust
```

**Tool:** PowerView · **Platform:** Windows


## Interesting ACLs

```powershell
Find-InterestingDomainAcl -ResolveGUIDs
```

**Tool:** PowerView · **Platform:** Windows
