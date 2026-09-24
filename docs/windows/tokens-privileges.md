# Tokens & Privileges

One-liners for checking Windows token privileges, group membership and integrity context.

<div class="ol-section-kicker"><span>WIN</span><strong>6 one-liners</strong></div>

## Token privileges

```powershell
whoami /priv
```

**Tool:** whoami · **Platform:** Windows · **Tags:** tokens, privileges · **Context:** User · **Noise:** Quiet

## Group memberships

```powershell
whoami /groups
```

**Tool:** whoami · **Platform:** Windows · **Tags:** groups, token · **Context:** User · **Noise:** Quiet

## High-value privileges

```powershell
whoami /priv | findstr /i "SeImpersonate SeAssignPrimaryToken SeDebug SeBackup SeRestore SeTakeOwnership SeLoadDriver"
```

**Tool:** whoami · **Platform:** Windows · **Tags:** privileges · **Context:** User · **Noise:** Quiet

## Integrity level

```powershell
whoami /groups | findstr /i "Mandatory Label"
```

**Tool:** whoami · **Platform:** Windows · **Tags:** integrity level · **Context:** User · **Noise:** Quiet

## Current identity

```powershell
[System.Security.Principal.WindowsIdentity]::GetCurrent() | Select Name,ImpersonationLevel
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** token, identity · **Context:** User · **Noise:** Quiet

## Admin role check

```powershell
([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** admin, token · **Context:** User · **Noise:** Quiet

---

**Related:** Privilege Escalation · UAC · DPAPI
