# AMSI State

One-liners for checking AMSI-related providers, logs and PowerShell integration clues.

<div class="ol-section-kicker"><span>WIN</span><strong>4 one-liners</strong></div>

## AMSI provider registry

```powershell
reg query "HKLM\SOFTWARE\Microsoft\AMSI\Providers" /s
```

**Tool:** reg.exe · **Platform:** Windows · **Tags:** AMSI, providers · **Context:** User

## Loaded AMSI module in PowerShell

```powershell
Get-Process -Id $PID -Module -ErrorAction SilentlyContinue | Where-Object {$_.ModuleName -ieq "amsi.dll"}
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** AMSI, PowerShell · **Context:** User

## AMSI DLL on disk

```powershell
Get-Item "$env:WINDIR\System32\amsi.dll" | Select FullName,VersionInfo
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** AMSI · **Context:** User

## Defender AMSI-related events

```powershell
Get-WinEvent -LogName "Microsoft-Windows-Windows Defender/Operational" -MaxEvents 100 | Where-Object {$_.Message -match "AMSI"} | Select TimeCreated,Id,Message
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** AMSI, Defender · **Context:** User

---

**Related:** Defender & ASR · PowerShell Logging · Execution Control
