# PowerShell Logging

One-liners for checking Script Block, Module and transcription logging policy/state.

<div class="ol-section-kicker"><span>WIN</span><strong>5 one-liners</strong></div>

## Script Block Logging policy

```powershell
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging
```

**Tool:** reg.exe · **Platform:** Windows · **Tags:** PowerShell, logging · **Context:** User · **Noise:** Quiet

## Module Logging policy

```powershell
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ModuleLogging
```

**Tool:** reg.exe · **Platform:** Windows · **Tags:** PowerShell, logging · **Context:** User · **Noise:** Quiet

## Transcription policy

```powershell
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\PowerShell\Transcription
```

**Tool:** reg.exe · **Platform:** Windows · **Tags:** PowerShell, logging · **Context:** User · **Noise:** Quiet

## Recent script block events

```powershell
Get-WinEvent -LogName "Microsoft-Windows-PowerShell/Operational" -FilterXPath "*[System[(EventID=4104)]]" -MaxEvents 20 | Select TimeCreated,Message
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** PowerShell, 4104, logging · **Context:** User · **Noise:** Quiet

## PowerShell operational log state

```powershell
Get-WinEvent -ListLog "Microsoft-Windows-PowerShell/Operational" | Select LogName,IsEnabled,RecordCount
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** PowerShell, logging · **Context:** User · **Noise:** Quiet

---

**Related:** AMSI State · Defender & ASR · PowerShell
