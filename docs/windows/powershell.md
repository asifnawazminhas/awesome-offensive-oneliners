# PowerShell

Small, reusable PowerShell one-liners for assessment work.

### Download a file

```powershell
Invoke-WebRequest -Uri "http://<HOST>/<FILE>" -OutFile "$env:TEMP\<FILE>"
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** HTTP, Download · **Context:** User · **Noise:** Quiet

### Download text in memory

```powershell
(Invoke-WebRequest -UseBasicParsing -Uri "http://<HOST>/<FILE>").Content
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** HTTP, Memory · **Context:** User · **Noise:** Quiet

### SHA256 file hash

```powershell
Get-FileHash <FILE> -Algorithm SHA256
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** Hashing, Files · **Context:** User · **Noise:** Quiet

### Search files recursively

```powershell
Get-ChildItem <PATH> -Recurse -File -ErrorAction SilentlyContinue | Select-String -Pattern "<TEXT>"
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** Search, Files · **Context:** User · **Noise:** Quiet

### Test TCP port

```powershell
Test-NetConnection <HOST> -Port <PORT>
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** Network, TCP · **Context:** User · **Noise:** Quiet

### Resolve DNS

```powershell
Resolve-DnsName <HOSTNAME>
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** DNS, Network · **Context:** User · **Noise:** Quiet

---

**Related:** [Overview](./) · [Powershell Logging](powershell-logging.md) · [Privilege Escalation](privilege-escalation.md)
