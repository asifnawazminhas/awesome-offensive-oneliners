# PowerShell

Small, reusable PowerShell one-liners for assessment work.

### Download a file

```powershell
Invoke-WebRequest -Uri "http://<HOST>/<FILE>" -OutFile "$env:TEMP\<FILE>"
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** HTTP, Download

### Download text in memory

```powershell
(Invoke-WebRequest -UseBasicParsing -Uri "http://<HOST>/<FILE>").Content
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** HTTP, Memory

### SHA256 file hash

```powershell
Get-FileHash <FILE> -Algorithm SHA256
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** Hashing, Files

### Search files recursively

```powershell
Get-ChildItem <PATH> -Recurse -File -ErrorAction SilentlyContinue | Select-String -Pattern "<TEXT>"
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** Search, Files

### Test TCP port

```powershell
Test-NetConnection <HOST> -Port <PORT>
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** Network, TCP

### Resolve DNS

```powershell
Resolve-DnsName <HOSTNAME>
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** DNS, Network

