# Environment Checks

One-liners for quickly profiling Windows version, architecture, domain and security context.

<div class="ol-section-kicker"><span>WIN</span><strong>6 one-liners</strong></div>

## OS build

```powershell
Get-ComputerInfo | Select WindowsProductName,WindowsVersion,OsBuildNumber,OsArchitecture
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** environment, OS · **Context:** User · **Noise:** Quiet

## Compact systeminfo

```powershell
systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type" /C:"Domain"
```

**Tool:** systeminfo · **Platform:** Windows · **Tags:** environment, OS, domain · **Context:** User · **Noise:** Quiet

## Current domain

```powershell
(Get-CimInstance Win32_ComputerSystem).Domain
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** domain, environment · **Context:** User · **Noise:** Quiet

## Network adapters

```powershell
Get-NetIPConfiguration | Select InterfaceAlias,IPv4Address,IPv4DefaultGateway,DNSServer
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** network, environment · **Context:** User · **Noise:** Quiet

## Proxy settings

```powershell
netsh winhttp show proxy
```

**Tool:** netsh · **Platform:** Windows · **Tags:** proxy, environment · **Context:** User · **Noise:** Quiet

## PowerShell version

```powershell
$PSVersionTable
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** PowerShell, environment · **Context:** User · **Noise:** Quiet

---

**Related:** Enumeration · Defender & ASR · App Control
