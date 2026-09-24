---
hide:
  - toc
---
# AD Account Hygiene

One-liners for adminCount, stale objects, protected users and account state.

<div class="ol-section-kicker"><span>AD</span><strong>ACCOUNTS</strong></div>

## adminCount users
```powershell
Get-DomainUser -LDAPFilter '(adminCount=1)' | Select-Object samaccountname,distinguishedname
```
**Tool:** PowerView · **Platform:** Windows · **Tags:** adminCount, Privileged Users · **Context:** Domain user · **Noise:** Quiet

## Protected Users
```powershell
Get-DomainGroupMember -Identity 'Protected Users' | Select-Object MemberName,MemberDomain
```
**Tool:** PowerView · **Platform:** Windows · **Tags:** Protected Users · **Context:** Domain user · **Noise:** Quiet

## Disabled accounts
```powershell
Get-DomainUser -UACFilter ACCOUNTDISABLE | Select-Object samaccountname,lastlogon
```
**Tool:** PowerView · **Platform:** Windows · **Tags:** Disabled Accounts · **Context:** Domain user · **Noise:** Quiet

## Password never expires
```powershell
Get-DomainUser -UACFilter DONT_EXPIRE_PASSWORD | Select-Object samaccountname,pwdlastset
```
**Tool:** PowerView · **Platform:** Windows · **Tags:** Password Policy, Accounts · **Context:** Domain user · **Noise:** Quiet

## Stale users 90 days
```powershell
$cutoff=(Get-Date).AddDays(-90).ToFileTime(); Get-DomainUser -LDAPFilter "(&(objectCategory=person)(lastLogonTimestamp<=$cutoff))" -Properties samaccountname,lastlogontimestamp | Select-Object samaccountname,@{n='LastLogon';e={[datetime]::FromFileTime($_.lastlogontimestamp)}}
```
**Tool:** PowerView · **Platform:** Windows · **Tags:** Stale Users, LastLogon · **Context:** Domain user · **Noise:** Quiet

## Stale computers 90 days
```powershell
$cutoff=(Get-Date).AddDays(-90).ToFileTime(); Get-DomainComputer -LDAPFilter "(lastLogonTimestamp<=$cutoff)" -Properties dnshostname,lastlogontimestamp | Select-Object dnshostname,@{n='LastLogon';e={[datetime]::FromFileTime($_.lastlogontimestamp)}}
```
**Tool:** PowerView · **Platform:** Windows · **Tags:** Stale Computers, LastLogon · **Context:** Domain user · **Noise:** Quiet

## LDAP stale users
```bash
ldapsearch -x -H ldap://<DC_IP> -D '<DOMAIN>\\<USER>' -w '<PASSWORD>' -b '<BASE_DN>' '(&(objectCategory=person)(objectClass=user))' sAMAccountName lastLogonTimestamp pwdLastSet
```
**Tool:** ldapsearch · **Platform:** Linux · **Tags:** LDAP, Accounts · **Context:** Domain user · **Noise:** Quiet

**Related:** [Users & Groups](users-groups.md) · [Password Policy](password-policy.md) · [LDAP Filters](ldap-filters.md)
