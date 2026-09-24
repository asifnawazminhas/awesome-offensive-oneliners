---
hide:
  - toc
---
# Deleted AD Objects

One-liners for Recycle Bin visibility and deleted-object enumeration.

<div class="ol-section-kicker"><span>AD</span><strong>DELETED</strong></div>

## Recycle Bin optional feature state
```powershell
Get-ADOptionalFeature 'Recycle Bin Feature' | Select-Object Name,EnabledScopes
```
**Tool:** ActiveDirectory module · **Platform:** Windows · **Tags:** Recycle Bin, AD · **Context:** Domain user

## Deleted users with AD module
```powershell
Get-ADObject -Filter 'isDeleted -eq $true -and objectClass -eq "user"' -IncludeDeletedObjects -Properties sAMAccountName,lastKnownParent | Select-Object Name,sAMAccountName,lastKnownParent
```
**Tool:** ActiveDirectory module · **Platform:** Windows · **Tags:** Deleted Objects, Users · **Context:** Domain user

## All deleted objects
```powershell
Get-ADObject -Filter 'isDeleted -eq $true' -IncludeDeletedObjects -Properties lastKnownParent | Select-Object Name,ObjectClass,lastKnownParent
```
**Tool:** ActiveDirectory module · **Platform:** Windows · **Tags:** Deleted Objects · **Context:** Domain user

## LDAP deleted-object control
```bash
ldapsearch -x -H ldap://<DC_IP> -D '<DOMAIN>\\<USER>' -w '<PASSWORD>' -E '1.2.840.113556.1.4.417' -b '<BASE_DN>' '(isDeleted=TRUE)' distinguishedName lastKnownParent
```
**Tool:** ldapsearch · **Platform:** Linux · **Tags:** LDAP, Deleted Objects · **Context:** Domain user

**Related:** [LDAP Filters](ldap-filters.md) · [Users & Groups](users-groups.md) · [Account Hygiene](account-hygiene.md)
