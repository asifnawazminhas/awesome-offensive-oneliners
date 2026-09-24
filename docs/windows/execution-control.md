# Execution Control Validation

One-liners for correlating AppLocker, WDAC, CLM and Code Integrity state.

<div class="ol-section-kicker"><span>WIN</span><strong>7 one-liners</strong></div>

## Effective AppLocker XML

```powershell
Get-AppLockerPolicy -Effective -Xml
```

**Tool:** AppLocker · **Platform:** Windows · **Tags:** AppLocker, policy · **Context:** User

## AppLocker rule collections

```powershell
[xml]$p=(Get-AppLockerPolicy -Effective).ToXml(); $p.AppLockerPolicy.RuleCollection | Select Type,EnforcementMode
```

**Tool:** AppLocker · **Platform:** Windows · **Tags:** AppLocker, policy · **Context:** User

## Language mode

```powershell
$ExecutionContext.SessionState.LanguageMode
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** CLM, PowerShell · **Context:** User

## WDAC active policies

```powershell
Get-ChildItem "$env:WINDIR\System32\CodeIntegrity\CiPolicies\Active" -ErrorAction SilentlyContinue | Select Name,Length,LastWriteTime
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** WDAC, Code Integrity · **Context:** User

## Code Integrity events

```powershell
Get-WinEvent -LogName "Microsoft-Windows-CodeIntegrity/Operational" -MaxEvents 30 | Select TimeCreated,Id,Message
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** WDAC, events · **Context:** User

## AppLocker EXE/DLL events

```powershell
Get-WinEvent -LogName "Microsoft-Windows-AppLocker/EXE and DLL" -MaxEvents 30 | Select TimeCreated,Id,Message
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** AppLocker, events · **Context:** User

## CITool policy listing

```powershell
citool.exe --list-policies
```

**Tool:** CITool · **Platform:** Windows · **Tags:** WDAC, policy · **Context:** User

---

**Related:** App Control · PowerShell Logging · LOLBin Discovery
