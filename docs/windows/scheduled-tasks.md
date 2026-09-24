# Scheduled Tasks

One-liners for discovering scheduled tasks, actions and privileged execution context.

<div class="ol-section-kicker"><span>WIN</span><strong>5 one-liners</strong></div>

## Verbose scheduled tasks

```powershell
schtasks /query /fo LIST /v
```

**Tool:** schtasks · **Platform:** Windows · **Tags:** scheduled tasks · **Context:** User · **Noise:** Quiet

## PowerShell task actions

```powershell
Get-ScheduledTask | Select TaskName,TaskPath,State,@{n="Actions";e={$_.Actions.Execute -join ";"}}
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** scheduled tasks · **Context:** User · **Noise:** Quiet

## Tasks running as SYSTEM

```powershell
Get-ScheduledTask | Where-Object {$_.Principal.UserId -match "SYSTEM"} | Select TaskName,TaskPath,State
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** scheduled tasks, SYSTEM · **Context:** User · **Noise:** Quiet

## Task details

```powershell
Get-ScheduledTask -TaskName "<TASK>" | Get-ScheduledTaskInfo
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** scheduled tasks · **Context:** User · **Noise:** Quiet

## Export task XML

```powershell
schtasks /query /tn "<TASK>" /xml
```

**Tool:** schtasks · **Platform:** Windows · **Tags:** scheduled tasks, XML · **Context:** User · **Noise:** Quiet

---

**Related:** Services · Writable Paths · Privilege Escalation
