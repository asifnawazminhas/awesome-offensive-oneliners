# Writable Paths

One-liners for identifying user-writable directories and files in trusted or privileged locations.

<div class="ol-section-kicker"><span>WIN</span><strong>5 one-liners</strong></div>

## Writable directories under Program Files

```powershell
Get-ChildItem "C:\Program Files","C:\Program Files (x86)" -Directory -Recurse -ErrorAction SilentlyContinue | Where-Object {try{ $t=Join-Path $_.FullName ([IO.Path]::GetRandomFileName()); [IO.File]::WriteAllText($t,"x"); Remove-Item $t -Force; $true }catch{$false}} | Select -Expand FullName
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** writable paths · **Context:** User

## ACLs containing Users write rights

```powershell
icacls C:\ProgramData | findstr /i "Users Everyone"
```

**Tool:** icacls · **Platform:** Windows · **Tags:** ACL, writable paths · **Context:** User

## PATH entries

```powershell
$env:PATH -split ';'
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** PATH · **Context:** User

## ACLs for PATH entries

```powershell
$env:PATH -split ';' | ForEach-Object { if(Test-Path $_){ Write-Host "=== $_ ==="; icacls $_ } }
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** PATH, ACL · **Context:** User

## Writable temp locations

```powershell
Get-Item $env:TEMP,$env:TMP,"C:\Windows\Temp","C:\ProgramData" | Select FullName,@{n="Writable";e={try{$f=Join-Path $_.FullName ([IO.Path]::GetRandomFileName());New-Item $f -ItemType File -Force|Out-Null;Remove-Item $f -Force;$true}catch{$false}}}
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** writable paths, temp · **Context:** User

---

**Related:** Services · Scheduled Tasks · Execution Control
