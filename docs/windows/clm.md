---
hide:
  - toc
---
# Constrained Language Mode Checks

<span class="ol-search-aliases">clm constrained language mode powershell language mode wdac applocker</span>

One-liners for determining what PowerShell CLM permits, blocks and logs.

<div class="ol-section-kicker"><span>WIN</span><strong>CLM</strong></div>

## Current language mode
```powershell
$ExecutionContext.SessionState.LanguageMode
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** CLM, LanguageMode · **Context:** User · **Noise:** Quiet

## Add-Type capability
```powershell
try { Add-Type -TypeDefinition 'public class T { public static int X(){return 1;} }'; [T]::X() } catch { $_.Exception.Message }
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** CLM, Add-Type · **Context:** User · **Noise:** Quiet

## Non-core .NET method check
```powershell
try { [System.Reflection.Assembly]::Load('System.Xml') | Out-Null; 'Assembly API available' } catch { $_.Exception.Message }
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** CLM, .NET · **Context:** User · **Noise:** Quiet

## COM object check
```powershell
try { New-Object -ComObject WScript.Shell | Out-Null; 'COM available' } catch { $_.Exception.Message }
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** CLM, COM · **Context:** User · **Noise:** Quiet

## P/Invoke-style type definition check
```powershell
try { Add-Type -MemberDefinition '[DllImport("kernel32.dll")] public static extern uint GetCurrentProcessId();' -Name Native -Namespace CLMTest; [CLMTest.Native]::GetCurrentProcessId() } catch { $_.Exception.Message }
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** CLM, PInvoke · **Context:** User · **Noise:** Quiet

## ScriptBlock logging state
```powershell
Get-ItemProperty 'HKLM:\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging' -ErrorAction SilentlyContinue
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** PowerShell, Logging · **Context:** User · **Noise:** Quiet

## PowerShell 4104 events
```powershell
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-PowerShell/Operational';Id=4104} -MaxEvents 20 | Select-Object TimeCreated,Message
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** ScriptBlock Logging, 4104 · **Context:** User · **Noise:** Quiet

## AppLocker PowerShell-related events
```powershell
Get-WinEvent -LogName 'Microsoft-Windows-AppLocker/MSI and Script' -MaxEvents 30 | Select-Object TimeCreated,Id,Message
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** AppLocker, Scripts · **Context:** User · **Noise:** Quiet

## WDAC Code Integrity correlation
```powershell
Get-WinEvent -LogName 'Microsoft-Windows-CodeIntegrity/Operational' -MaxEvents 30 | Select-Object TimeCreated,Id,Message
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** WDAC, Code Integrity · **Context:** User · **Noise:** Quiet


## Invoke-Expression availability
```powershell
try { Invoke-Expression '$x=1'; "IEX available: $x" } catch { $_.Exception.Message }
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** CLM, IEX, Capability · **Context:** User · **Noise:** Quiet

## Script method definition check
```powershell
try { $o=New-Object PSObject; $o | Add-Member ScriptMethod X { 1 }; $o.X() } catch { $_.Exception.Message }
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** CLM, ScriptMethod, Capability · **Context:** User · **Noise:** Quiet

## Type conversion check
```powershell
try { [System.Net.IPAddress]'127.0.0.1' } catch { $_.Exception.Message }
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** CLM, Type Conversion · **Context:** User · **Noise:** Quiet

## PowerShell version and edition
```powershell
$PSVersionTable | Select-Object PSVersion,PSEdition,CLRVersion
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** PowerShell, Version, CLM · **Context:** User · **Noise:** Quiet

## System lockdown policy indicator
```powershell
[System.Management.Automation.Security.SystemPolicy]::GetSystemLockdownPolicy()
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** CLM, System Policy, Lockdown · **Context:** User · **Requires:** API availability varies by PowerShell build · **Noise:** Quiet

## Module import check
```powershell
try { Import-Module Microsoft.PowerShell.Management -ErrorAction Stop; 'Module import available' } catch { $_.Exception.Message }
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** CLM, Modules, Capability · **Context:** User · **Noise:** Quiet

**Related:** [App Control](app-control.md) · [Execution Control Validation](execution-control.md) · [PowerShell Logging](powershell-logging.md)
