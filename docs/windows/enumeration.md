# Windows Enumeration

Fast local host enumeration commands.

### Current identity

```powershell
whoami /all
```

**Tool:** Windows · **Platform:** Windows · **Tags:** Identity, Privileges

### OS information

```powershell
Get-ComputerInfo | Select-Object WindowsProductName,WindowsVersion,OsBuildNumber,OsArchitecture
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** OS, Enumeration

### Network configuration

```powershell
Get-NetIPConfiguration
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** Network, Enumeration

### Listening TCP ports

```powershell
Get-NetTCPConnection -State Listen | Sort-Object LocalPort | Format-Table -AutoSize
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** Network, Ports

### Local administrators

```powershell
Get-LocalGroupMember -Group Administrators
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** Groups, Local Admin

### Installed hotfixes

```powershell
Get-HotFix | Sort-Object InstalledOn -Descending
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** Patches, Enumeration

### Scheduled tasks

```powershell
Get-ScheduledTask | Where-Object State -ne Disabled | Select-Object TaskName,TaskPath,State
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** Scheduled Tasks

### Environment variables

```powershell
Get-ChildItem Env: | Sort-Object Name
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** Environment

