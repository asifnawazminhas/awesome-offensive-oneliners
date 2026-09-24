---
hide:
  - toc
---
# Fine-Grained Password Policies

One-liners for Password Settings Objects and resultant password policy.

<div class="ol-section-kicker"><span>AD</span><strong>FGPP</strong></div>

## List Password Settings Objects
```powershell
Get-ADFineGrainedPasswordPolicy -Filter * | Select-Object Name,Precedence,MinPasswordLength,LockoutThreshold,MaxPasswordAge
```
**Tool:** ActiveDirectory module · **Platform:** Windows · **Tags:** FGPP, Password Policy · **Context:** Domain user · **Noise:** Quiet

## Resultant policy for a user
```powershell
Get-ADUserResultantPasswordPolicy -Identity '<USER>'
```
**Tool:** ActiveDirectory module · **Platform:** Windows · **Tags:** FGPP, User · **Context:** Domain user · **Noise:** Quiet

## PSO subjects
```powershell
Get-ADFineGrainedPasswordPolicySubject -Identity '<PSO_NAME>'
```
**Tool:** ActiveDirectory module · **Platform:** Windows · **Tags:** FGPP, Subjects · **Context:** Domain user · **Noise:** Quiet

## LDAP enumerate PSOs
```bash
ldapsearch -x -H ldap://<DC_IP> -D '<DOMAIN>\\<USER>' -w '<PASSWORD>' -b 'CN=Password Settings Container,CN=System,<BASE_DN>' '(objectClass=msDS-PasswordSettings)' cn msDS-PasswordSettingsPrecedence msDS-MinimumPasswordLength msDS-LockoutThreshold
```
**Tool:** ldapsearch · **Platform:** Linux · **Tags:** LDAP, FGPP · **Context:** Domain user · **Noise:** Quiet

## NetExec domain password policy
```bash
nxc smb <DC_IP> -u '<USER>' -p '<PASSWORD>' --pass-pol
```
**Tool:** NetExec · **Platform:** Linux · **Tags:** Password Policy, SMB · **Context:** Domain user · **Noise:** Quiet

**Related:** [Password Policy](password-policy.md) · [LDAP Filters](ldap-filters.md) · [Account Hygiene](account-hygiene.md)
