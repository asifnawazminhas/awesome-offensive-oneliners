---
hide:
  - toc
---

# Windows Privilege Escalation Checks

Fast local checks for common Windows privilege-escalation conditions.

<div class="ol-section-kicker"><span>WIN</span><strong>PRIVESC</strong></div>

## Identity and privileges

```cmd
whoami /all
```

**Tool:** Windows · **Platform:** Windows · **Tags:** Identity, Privileges · **Context:** User · **Noise:** Quiet

## Token privileges of interest

```cmd
whoami /priv | findstr /i "SeImpersonate SeAssignPrimaryToken SeDebug SeBackup SeRestore"
```

**Tool:** Windows · **Platform:** Windows · **Tags:** Token, Privileges · **Context:** User · **Noise:** Quiet

## Unquoted service paths

```cmd
wmic service get name,displayname,startmode,pathname | findstr /i /v "C:\Windows\\" | findstr /i /v "\""
```

**Tool:** WMIC · **Platform:** Windows · **Tags:** Services, Unquoted Path · **Context:** User · **Noise:** Quiet

## Writable service permissions with AccessChk

```cmd
accesschk.exe -uwcqv "Everyone" * /accepteula
```

**Tool:** AccessChk · **Platform:** Windows · **Tags:** Services, Permissions · **Context:** User · **Noise:** Quiet

## Scheduled tasks

```cmd
schtasks /query /fo LIST /v
```

**Tool:** schtasks · **Platform:** Windows · **Tags:** Scheduled Tasks · **Context:** User · **Noise:** Quiet

## AlwaysInstallElevated HKLM

```cmd
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

**Tool:** reg.exe · **Platform:** Windows · **Tags:** MSI, Policy · **Context:** User · **Noise:** Quiet

## AlwaysInstallElevated HKCU

```cmd
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

**Tool:** reg.exe · **Platform:** Windows · **Tags:** MSI, Policy · **Context:** User · **Noise:** Quiet

## Unattended installation files

```cmd
dir /s /b C:\*unattend*.xml C:\*sysprep*.inf C:\*sysprep*.xml 2>nul
```

**Tool:** cmd.exe · **Platform:** Windows · **Tags:** Files, Credentials · **Context:** User · **Noise:** Quiet

## Stored credentials

```cmd
cmdkey /list
```

**Tool:** cmdkey · **Platform:** Windows · **Tags:** Credentials · **Context:** User · **Noise:** Quiet

## Writable application directory

```cmd
icacls "C:\Program Files\<APP>"
```

**Tool:** icacls · **Platform:** Windows · **Tags:** ACL, Writable Path · **Context:** User · **Noise:** Quiet

## PATH entries and ACLs

```powershell
$env:Path -split ';' | Where-Object { $_ } | ForEach-Object { "`n$_"; icacls $_ 2>$null }
```

**Tool:** PowerShell + icacls · **Platform:** Windows · **Tags:** PATH, DLL Search · **Context:** User · **Noise:** Quiet

---

**Related:** [Overview](./) · [Powershell](powershell.md) · [Scheduled Tasks](scheduled-tasks.md)
