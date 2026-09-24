# LOLBin Discovery

One-liners for discovering commonly available signed Windows utilities used during assessments.

<div class="ol-section-kicker"><span>WIN</span><strong>5 one-liners</strong></div>

## Core LOLBins availability

```powershell
"certutil","mshta","rundll32","regsvr32","msiexec","cscript","wscript","wmic","bitsadmin" | ForEach-Object {Get-Command $_ -ErrorAction SilentlyContinue | Select Name,Source}
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** LOLBins, discovery · **Context:** User

## MSBuild paths

```powershell
Get-ChildItem "$env:WINDIR\Microsoft.NET" -Filter MSBuild.exe -Recurse -ErrorAction SilentlyContinue | Select -Expand FullName
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** MSBuild, LOLBins · **Context:** User

## InstallUtil paths

```powershell
Get-ChildItem "$env:WINDIR\Microsoft.NET" -Filter InstallUtil.exe -Recurse -ErrorAction SilentlyContinue | Select -Expand FullName
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** InstallUtil, LOLBins · **Context:** User

## curl version

```powershell
curl.exe --version
```

**Tool:** curl · **Platform:** Windows · **Tags:** LOLBins, transfer · **Context:** User

## WMIC presence

```powershell
where.exe wmic.exe
```

**Tool:** where.exe · **Platform:** Windows · **Tags:** WMIC, LOLBins · **Context:** User

---

**Related:** Execution Control · Download Cradles · App Control
