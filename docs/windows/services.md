# Service Enumeration

Windows service one-liners for paths, accounts, start modes and permissions triage.

<div class="ol-section-kicker"><span>WIN</span><strong>6 one-liners</strong></div>

## Service paths and accounts

```powershell
Get-CimInstance Win32_Service | Select Name,StartName,StartMode,State,PathName
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** services · **Context:** User

## Unquoted service paths

```powershell
Get-CimInstance Win32_Service | Where-Object {$_.PathName -match " " -and $_.PathName -notmatch '^"'} | Select Name,StartName,PathName
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** services, unquoted path · **Context:** User

## Auto-start services

```powershell
Get-CimInstance Win32_Service | Where-Object {$_.StartMode -eq "Auto"} | Select Name,StartName,State,PathName
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** services · **Context:** User

## Services running as SYSTEM

```powershell
Get-CimInstance Win32_Service | Where-Object {$_.StartName -eq "LocalSystem"} | Select Name,State,PathName
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** services, SYSTEM · **Context:** User

## Service ACL with sc.exe

```powershell
sc.exe sdshow <SERVICE>
```

**Tool:** sc.exe · **Platform:** Windows · **Tags:** services, ACL · **Context:** User

## Service configuration

```powershell
sc.exe qc <SERVICE>
```

**Tool:** sc.exe · **Platform:** Windows · **Tags:** services · **Context:** User

---

**Related:** Writable Paths · Privilege Escalation · Scheduled Tasks
