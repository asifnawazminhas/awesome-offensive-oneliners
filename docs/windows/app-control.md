# Windows Application Control

One-liners for AppLocker, WDAC, CLM and Defender visibility.

### Effective AppLocker policy

```powershell
Get-AppLockerPolicy -Effective | Select-Object -ExpandProperty RuleCollections
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** AppLocker, Policy

### AppLocker XML

```powershell
(Get-AppLockerPolicy -Effective).ToXml()
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** AppLocker, XML

### PowerShell language mode

```powershell
$ExecutionContext.SessionState.LanguageMode
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** CLM, PowerShell

### WDAC policy files

```powershell
Get-ChildItem "$env:WINDIR\System32\CodeIntegrity" -File | Select-Object Name,Length,LastWriteTime,FullName
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** WDAC, Code Integrity

### AppLocker EXE events

```powershell
Get-WinEvent -LogName "Microsoft-Windows-AppLocker/EXE and DLL" -MaxEvents 30 | Select-Object TimeCreated,Id,Message
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** AppLocker, Events

### Code Integrity events

```powershell
Get-WinEvent -LogName "Microsoft-Windows-CodeIntegrity/Operational" -MaxEvents 30 | Select-Object TimeCreated,Id,Message
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** WDAC, Events

### Defender ASR rules

```powershell
Get-MpPreference | Select-Object AttackSurfaceReductionRules_Ids,AttackSurfaceReductionRules_Actions
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** Defender, ASR

