---
hide:
  - toc
---
# Constrained Language Mode Checks

One-liners for determining what PowerShell CLM permits, blocks and logs.

<div class="ol-section-kicker"><span>WIN</span><strong>CLM</strong></div>

## Current language mode
```powershell
$ExecutionContext.SessionState.LanguageMode
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** CLM, LanguageMode · **Context:** User

## Add-Type capability
```powershell
try { Add-Type -TypeDefinition 'public class T { public static int X(){return 1;} }'; [T]::X() } catch { $_.Exception.Message }
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** CLM, Add-Type · **Context:** User

## Non-core .NET method check
```powershell
try { [System.Reflection.Assembly]::Load('System.Xml') | Out-Null; 'Assembly API available' } catch { $_.Exception.Message }
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** CLM, .NET · **Context:** User

## COM object check
```powershell
try { New-Object -ComObject WScript.Shell | Out-Null; 'COM available' } catch { $_.Exception.Message }
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** CLM, COM · **Context:** User

## P/Invoke-style type definition check
```powershell
try { Add-Type -MemberDefinition '[DllImport("kernel32.dll")] public static extern uint GetCurrentProcessId();' -Name Native -Namespace CLMTest; [CLMTest.Native]::GetCurrentProcessId() } catch { $_.Exception.Message }
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** CLM, PInvoke · **Context:** User

## ScriptBlock logging state
```powershell
Get-ItemProperty 'HKLM:\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging' -ErrorAction SilentlyContinue
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** PowerShell, Logging · **Context:** User

## PowerShell 4104 events
```powershell
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-PowerShell/Operational';Id=4104} -MaxEvents 20 | Select-Object TimeCreated,Message
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** ScriptBlock Logging, 4104 · **Context:** User

## AppLocker PowerShell-related events
```powershell
Get-WinEvent -LogName 'Microsoft-Windows-AppLocker/MSI and Script' -MaxEvents 30 | Select-Object TimeCreated,Id,Message
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** AppLocker, Scripts · **Context:** User

## WDAC Code Integrity correlation
```powershell
Get-WinEvent -LogName 'Microsoft-Windows-CodeIntegrity/Operational' -MaxEvents 30 | Select-Object TimeCreated,Id,Message
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** WDAC, Code Integrity · **Context:** User

**Related:** [App Control](app-control.md) · [Execution Control Validation](execution-control.md) · [PowerShell Logging](powershell-logging.md)
