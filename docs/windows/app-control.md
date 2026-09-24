# Windows Application Control

One-liners for AppLocker, WDAC, Code Integrity, CLM and Defender visibility.

<div class="ol-section-kicker"><span>WIN</span><strong>APP CONTROL</strong></div>

## Effective AppLocker policy

```powershell
Get-AppLockerPolicy -Effective -Xml
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** AppLocker, Policy

## Local AppLocker policy

```powershell
Get-AppLockerPolicy -Local -Xml
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** AppLocker, Local Policy

## AppLocker Identity service

```powershell
Get-Service AppIDSvc
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** AppLocker, Service

## AppLocker EXE and DLL events

```powershell
Get-WinEvent -LogName 'Microsoft-Windows-AppLocker/EXE and DLL' -MaxEvents 30 | Select-Object TimeCreated,Id,Message
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** AppLocker, Events

## Test a path against effective policy

```powershell
Test-AppLockerPolicy -PolicyObject (Get-AppLockerPolicy -Effective) -Path 'C:\Windows\Tasks\test.exe' -User 'Everyone'
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** AppLocker, Test

## WDAC registry policy

```cmd
reg query "HKLM\SYSTEM\CurrentControlSet\Control\CI\Policy"
```

**Tool:** reg.exe · **Platform:** Windows · **Tags:** WDAC, Code Integrity

## Active WDAC policy files

```powershell
Get-ChildItem "$env:WINDIR\System32\CodeIntegrity\CiPolicies\Active" -File -ErrorAction SilentlyContinue | Select-Object Name,Length,LastWriteTime,FullName
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** WDAC, Policy Files

## Code Integrity events

```powershell
Get-WinEvent -LogName 'Microsoft-Windows-CodeIntegrity/Operational' -MaxEvents 30 | Select-Object TimeCreated,Id,Message
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** WDAC, Events

## CiTool deployed policies

```cmd
citool.exe --list-policies
```

**Tool:** CiTool · **Platform:** Windows 11 / Server · **Tags:** WDAC, Policy

## PowerShell language mode

```powershell
$ExecutionContext.SessionState.LanguageMode
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** CLM, PowerShell

## CLM .NET capability check

```powershell
try { [System.Diagnostics.Process]::GetCurrentProcess() | Out-Null; 'Type access available' } catch { $_.Exception.Message }
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** CLM, Validation

## Defender ASR rules

```powershell
Get-MpPreference | Select-Object AttackSurfaceReductionRules_Ids,AttackSurfaceReductionRules_Actions
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** Defender, ASR
