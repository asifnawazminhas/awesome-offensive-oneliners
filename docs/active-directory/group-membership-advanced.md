---
hide:
  - toc
---
# Advanced Group Membership

Nested memberships, foreign principals and privileged-group pivots.

<div class="ol-section-kicker"><span>AD</span><strong>GROUPS</strong></div>

## Recursive group members with PowerView
```powershell
Get-DomainGroupMember -Identity '<GROUP>' -Recurse | Select-Object MemberName,MemberDomain,MemberObjectClass
```
**Tool:** PowerView · **Platform:** Windows · **Tags:** Groups, Recursive · **Context:** Domain user

## User group memberships
```powershell
Get-DomainGroup -MemberIdentity '<USER>' | Select-Object samaccountname
```
**Tool:** PowerView · **Platform:** Windows · **Tags:** Groups, Membership · **Context:** Domain user

## LDAP nested membership matching rule
```bash
ldapsearch -x -H ldap://<DC_IP> -D '<DOMAIN>\\<USER>' -w '<PASSWORD>' -b '<BASE_DN>' '(&(objectCategory=person)(memberOf:1.2.840.113556.1.4.1941:=CN=<GROUP>,OU=<OU>,DC=<DOMAIN>,DC=<TLD>))' sAMAccountName
```
**Tool:** ldapsearch · **Platform:** Linux · **Tags:** LDAP, Nested Groups · **Context:** Domain user

## Foreign security principals
```powershell
Get-DomainObject -LDAPFilter '(objectClass=foreignSecurityPrincipal)' | Select-Object name,distinguishedname
```
**Tool:** PowerView · **Platform:** Windows · **Tags:** Foreign Security Principal, Trusts · **Context:** Domain user

## Members containing foreign SIDs
```powershell
Get-DomainGroup -Properties member | Where-Object {$_.member -match 'CN=S-1-5-21-'} | Select-Object samaccountname,member
```
**Tool:** PowerView · **Platform:** Windows · **Tags:** Foreign SID, Groups · **Context:** Domain user

## Protected Users membership
```powershell
Get-DomainGroupMember -Identity 'Protected Users' | Select-Object MemberName,MemberDomain
```
**Tool:** PowerView · **Platform:** Windows · **Tags:** Protected Users, Groups · **Context:** Domain user

**Related:** [Users & Groups](users-groups.md) · [Trusts](trusts.md) · [SID History](sid-history.md)
