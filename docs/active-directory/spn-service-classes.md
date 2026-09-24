---
hide:
  - toc
---
# SPN Service-Class Discovery

One-liners for locating specific SPN service classes.

<div class="ol-section-kicker"><span>AD</span><strong>SPN</strong></div>

## All user SPNs
```powershell
Get-DomainUser -SPN | Select-Object samaccountname,serviceprincipalname
```
**Tool:** PowerView · **Platform:** Windows · **Tags:** SPN, Users · **Context:** Domain user · **Noise:** Quiet

## MSSQL SPNs
```powershell
Get-DomainUser -SPN | Where-Object {$_.serviceprincipalname -match 'MSSQLSvc/'} | Select-Object samaccountname,serviceprincipalname
```
**Tool:** PowerView · **Platform:** Windows · **Tags:** MSSQL, SPN · **Context:** Domain user · **Noise:** Quiet

## HTTP SPNs
```powershell
Get-DomainUser -SPN | Where-Object {$_.serviceprincipalname -match '^HTTP/'} | Select-Object samaccountname,serviceprincipalname
```
**Tool:** PowerView · **Platform:** Windows · **Tags:** HTTP, SPN · **Context:** Domain user · **Noise:** Quiet

## CIFS SPNs
```powershell
Get-DomainComputer -SPN | Where-Object {$_.serviceprincipalname -match '^cifs/'} | Select-Object dnshostname,serviceprincipalname
```
**Tool:** PowerView · **Platform:** Windows · **Tags:** CIFS, SPN · **Context:** Domain user · **Noise:** Quiet

## LDAP SPNs
```powershell
Get-DomainComputer -SPN | Where-Object {$_.serviceprincipalname -match '^ldap/'} | Select-Object dnshostname,serviceprincipalname
```
**Tool:** PowerView · **Platform:** Windows · **Tags:** LDAP, SPN · **Context:** Domain user · **Noise:** Quiet

## setspn query by class
```cmd
setspn -Q MSSQLSvc/*
```
**Tool:** setspn · **Platform:** Windows · **Tags:** MSSQL, SPN · **Context:** Domain user · **Noise:** Quiet

## LDAP SPN filter
```bash
ldapsearch -x -H ldap://<DC_IP> -D '<DOMAIN>\\<USER>' -w '<PASSWORD>' -b '<BASE_DN>' '(&(objectCategory=person)(servicePrincipalName=MSSQLSvc/*))' sAMAccountName servicePrincipalName
```
**Tool:** ldapsearch · **Platform:** Linux · **Tags:** LDAP, MSSQL, SPN · **Context:** Domain user · **Noise:** Quiet

**Related:** [Kerberos](kerberos.md) · [MSSQL](mssql.md) · [DNS & SPN Discovery](dns-spn.md)
