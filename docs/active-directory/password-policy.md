# Domain Password Policy

One-liners for reading domain password and lockout policy.

<div class="ol-section-kicker"><span>AD</span><strong>5 one-liners</strong></div>

## Native domain password policy

```powershell
net accounts /domain
```

**Tool:** net.exe · **Platform:** Windows · **Tags:** AD, password policy · **Context:** Domain user · **Noise:** Quiet

## PowerView policy

```powershell
Get-DomainPolicyData | Select-Object -ExpandProperty SystemAccess
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, password policy · **Context:** Domain user · **Noise:** Quiet

## NetExec password policy

```bash
nxc smb <DC_IP> -u <USER> -p '<PASSWORD>' --pass-pol
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** AD, password policy · **Context:** Domain user · **Noise:** Quiet

## LDAP default domain policy

```bash
ldapsearch -x -H ldap://<DC_IP> -D "<DOMAIN>\<USER>" -w '<PASSWORD>' -b "<BASE_DN>" -s base "(objectClass=domain)" minPwdLength pwdHistoryLength lockoutThreshold maxPwdAge minPwdAge
```

**Tool:** ldapsearch · **Platform:** Linux · **Tags:** AD, LDAP, password policy · **Context:** Domain user · **Noise:** Quiet

## Fine-grained password policies

```powershell
Get-ADFineGrainedPasswordPolicy -Filter *
```

**Tool:** ActiveDirectory · **Platform:** Windows · **Tags:** AD, FGPP, password policy · **Context:** Domain user · **Noise:** Quiet

---

**Related:** Users & Groups · LDAP Filters · NetExec
