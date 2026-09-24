# Defender & ASR

One-liners for reading Microsoft Defender and Attack Surface Reduction state.

<div class="ol-section-kicker"><span>WIN</span><strong>5 one-liners</strong></div>

## Defender status

```powershell
Get-MpComputerStatus | Select AntivirusEnabled,RealTimeProtectionEnabled,BehaviorMonitorEnabled,IoavProtectionEnabled,AntispywareEnabled
```

**Tool:** Defender · **Platform:** Windows · **Tags:** Defender, status · **Context:** User · **Noise:** Quiet

## Defender exclusions

```powershell
Get-MpPreference | Select ExclusionPath,ExclusionProcess,ExclusionExtension
```

**Tool:** Defender · **Platform:** Windows · **Tags:** Defender, exclusions · **Context:** User · **Noise:** Quiet

## ASR IDs and actions

```powershell
$p=Get-MpPreference; 0..($p.AttackSurfaceReductionRules_Ids.Count-1) | ForEach-Object {[pscustomobject]@{Id=$p.AttackSurfaceReductionRules_Ids[$_];Action=$p.AttackSurfaceReductionRules_Actions[$_]}}
```

**Tool:** Defender · **Platform:** Windows · **Tags:** ASR, policy · **Context:** User · **Noise:** Quiet

## Recent Defender events

```powershell
Get-WinEvent -LogName "Microsoft-Windows-Windows Defender/Operational" -MaxEvents 30 | Select TimeCreated,Id,Message
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** Defender, events · **Context:** User · **Noise:** Quiet

## Defender service

```powershell
Get-Service WinDefend | Select Status,StartType,Name
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** Defender, service · **Context:** User · **Noise:** Quiet

---

**Related:** AMSI State · PowerShell Logging · Execution Control
