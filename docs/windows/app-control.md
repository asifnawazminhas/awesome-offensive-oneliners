---
hide:
  - toc
---

# Windows Application Control

One-liners for AppLocker, WDAC, Code Integrity, CLM and Defender visibility.

<div class="ol-section-kicker"><span>WIN</span><strong>APP CONTROL</strong></div>

## Effective AppLocker policy

```powershell
Get-AppLockerPolicy -Effective -Xml
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** AppLocker, Policy · **Context:** User

## Local AppLocker policy

```powershell
Get-AppLockerPolicy -Local -Xml
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** AppLocker, Local Policy · **Context:** User

## AppLocker Identity service

```powershell
Get-Service AppIDSvc
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** AppLocker, Service · **Context:** User

## AppLocker EXE and DLL events

```powershell
Get-WinEvent -LogName 'Microsoft-Windows-AppLocker/EXE and DLL' -MaxEvents 30 | Select-Object TimeCreated,Id,Message
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** AppLocker, Events · **Context:** User

## Test a path against effective policy

```powershell
Test-AppLockerPolicy -PolicyObject (Get-AppLockerPolicy -Effective) -Path 'C:\Windows\Tasks\test.exe' -User 'Everyone'
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** AppLocker, Test · **Context:** User

## WDAC registry policy

```cmd
reg query "HKLM\SYSTEM\CurrentControlSet\Control\CI\Policy"
```

**Tool:** reg.exe · **Platform:** Windows · **Tags:** WDAC, Code Integrity · **Context:** User

## Active WDAC policy files

```powershell
Get-ChildItem "$env:WINDIR\System32\CodeIntegrity\CiPolicies\Active" -File -ErrorAction SilentlyContinue | Select-Object Name,Length,LastWriteTime,FullName
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** WDAC, Policy Files · **Context:** User

## Code Integrity events

```powershell
Get-WinEvent -LogName 'Microsoft-Windows-CodeIntegrity/Operational' -MaxEvents 30 | Select-Object TimeCreated,Id,Message
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** WDAC, Events · **Context:** User

## CiTool deployed policies

```cmd
citool.exe --list-policies
```

**Tool:** CiTool · **Platform:** Windows 11 / Server · **Tags:** WDAC, Policy · **Context:** User

## PowerShell language mode

```powershell
$ExecutionContext.SessionState.LanguageMode
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** CLM, PowerShell · **Context:** User

## CLM .NET capability check

```powershell
try { [System.Diagnostics.Process]::GetCurrentProcess() | Out-Null; 'Type access available' } catch { $_.Exception.Message }
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** CLM, Validation · **Context:** User

## Defender ASR rules

```powershell
Get-MpPreference | Select-Object AttackSurfaceReductionRules_Ids,AttackSurfaceReductionRules_Actions
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** Defender, ASR · **Context:** User

---

**Related:** [Overview](./) · [Constrained Language Mode](clm.md) · [AMSI State](amsi-state.md) · [Defender & ASR](defender-asr.md)
