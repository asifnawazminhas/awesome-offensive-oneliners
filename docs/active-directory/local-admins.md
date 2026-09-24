# Local Admin Discovery

One-liners for identifying local administrator relationships across Windows estates.

<div class="ol-section-kicker"><span>AD</span><strong>6 one-liners</strong></div>

## Current local Administrators

```powershell
net localgroup administrators
```

**Tool:** net.exe · **Platform:** Windows · **Tags:** local admins · **Context:** User

## PowerShell local Administrators

```powershell
Get-LocalGroupMember -Group Administrators
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** local admins · **Context:** User

## PowerView local admin access

```powershell
Find-LocalAdminAccess
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, local admins · **Context:** Domain user

## NetExec admin validation

```bash
nxc smb <TARGETS> -u <USER> -p '<PASSWORD>'
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** AD, local admins, SMB · **Context:** Domain user

## NetExec local admins

```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --local-groups Administrators
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** AD, local groups · **Context:** Domain user

## BloodHound local admin collection

```bash
bloodhound-python -u <USER> -p '<PASSWORD>' -d <DOMAIN> -ns <DC_IP> -c LocalAdmin
```

**Tool:** BloodHound · **Platform:** Linux · **Tags:** AD, local admin · **Context:** Domain user

---

**Related:** Sessions · SMB, Shares & Sessions · BloodHound
