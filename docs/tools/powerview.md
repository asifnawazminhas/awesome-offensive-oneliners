---
hide:
  - toc
---

# PowerView

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

Fast PowerView reference for domain discovery and relationships.

<div class="ol-section-kicker"><span>TOOLS</span></div>

## Domain

```powershell
Get-Domain
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user · **Noise:** Quiet


## Domain controllers

```powershell
Get-DomainController
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user · **Noise:** Quiet


## Users

```powershell
Get-DomainUser | Select samaccountname
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user · **Noise:** Quiet


## Groups

```powershell
Get-DomainGroup | Select samaccountname
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user · **Noise:** Quiet


## Computers

```powershell
Get-DomainComputer | Select dnshostname,operatingsystem
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user · **Noise:** Quiet


## SPN users

```powershell
Get-DomainUser -SPN
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user · **Noise:** Quiet


## AS-REP candidates

```powershell
Get-DomainUser -PreauthNotRequired
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user · **Noise:** Quiet


## Constrained delegation

```powershell
Get-DomainComputer -TrustedToAuth -Properties DnsHostName,msDS-AllowedToDelegateTo
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user · **Noise:** Quiet


## Unconstrained delegation

```powershell
Get-DomainComputer -Unconstrained
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user · **Noise:** Quiet


## Domain trusts

```powershell
Get-DomainTrust
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user · **Noise:** Quiet


## Interesting ACLs

```powershell
Find-InterestingDomainAcl -ResolveGUIDs
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user · **Noise:** Quiet

---

**Related:** [Overview](./) · [Powerview Rubeus](powerview-rubeus.md) · [Smbclient](smbclient.md)
