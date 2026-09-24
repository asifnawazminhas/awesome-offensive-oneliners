---
hide:
  - toc
---
# LDAP Paging

One-liners for large AD result sets and server-side paging.

<div class="ol-section-kicker"><span>AD</span><strong>LDAP</strong></div>

## ldapsearch paged results
```bash
ldapsearch -x -H ldap://<DC_IP> -D '<DOMAIN>\\<USER>' -w '<PASSWORD>' -b '<BASE_DN>' -E pr=1000/noprompt '(objectClass=user)' sAMAccountName
```
**Tool:** ldapsearch · **Platform:** Linux · **Tags:** LDAP, Paging, Users · **Context:** Domain user · **Noise:** Quiet

## Paged computers
```bash
ldapsearch -x -H ldap://<DC_IP> -D '<DOMAIN>\\<USER>' -w '<PASSWORD>' -b '<BASE_DN>' -E pr=1000/noprompt '(objectCategory=computer)' dNSHostName
```
**Tool:** ldapsearch · **Platform:** Linux · **Tags:** LDAP, Paging, Computers · **Context:** Domain user · **Noise:** Quiet

## PowerView all users with selected properties
```powershell
Get-DomainUser -Properties samaccountname,distinguishedname,lastlogon,pwdlastset | Select-Object samaccountname,distinguishedname,lastlogon,pwdlastset
```
**Tool:** PowerView · **Platform:** Windows · **Tags:** LDAP, Users · **Context:** Domain user · **Noise:** Quiet

## PowerView LDAP filter
```powershell
Get-DomainObject -LDAPFilter '(&(objectCategory=person)(objectClass=user))' -Properties samaccountname,distinguishedname
```
**Tool:** PowerView · **Platform:** Windows · **Tags:** LDAP, Filter · **Context:** Domain user · **Noise:** Quiet

**Related:** [LDAP Filters](ldap-filters.md) · [LDAP & Native](ldap-native.md) · [Account Hygiene](account-hygiene.md)
