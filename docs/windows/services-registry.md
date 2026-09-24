# Windows Services & Registry

Useful service and registry inspection one-liners.

### Automatic services

```powershell
Get-CimInstance Win32_Service | Where-Object StartMode -eq Auto | Select-Object Name,State,StartName,PathName
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** Services

### Unquoted service paths

```powershell
Get-CimInstance Win32_Service | Where-Object {$_.PathName -match " " -and $_.PathName -notmatch "^""} | Select-Object Name,StartName,PathName
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** Services, Paths

### CurrentVersion registry

```powershell
Get-ItemProperty -LiteralPath 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion' | Select-Object ProductName,DisplayVersion,CurrentBuild,SystemRoot
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** Registry, OS

### AlwaysInstallElevated

```powershell
Get-ItemProperty 'HKLM:\Software\Policies\Microsoft\Windows\Installer','HKCU:\Software\Policies\Microsoft\Windows\Installer' -ErrorAction SilentlyContinue | Select-Object AlwaysInstallElevated
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** Registry, MSI

### Writable service binaries

```powershell
Get-CimInstance Win32_Service | ForEach-Object { $_.PathName }
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** Services, Paths

Use the output as input to your normal ACL review workflow.

