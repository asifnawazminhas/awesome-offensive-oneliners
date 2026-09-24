# WinRM & RDP Discovery

One-liners for identifying remote management exposure and access.

<div class="ol-section-kicker"><span>AD</span><strong>7 one-liners</strong></div>

## Probe WinRM with NetExec

```bash
nxc winrm <TARGETS> -u <USER> -p '<PASSWORD>'
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** AD, WinRM · **Context:** Domain user · **Noise:** Quiet

## Probe RDP with NetExec

```bash
nxc rdp <TARGETS> -u <USER> -p '<PASSWORD>'
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** AD, RDP · **Context:** Domain user · **Noise:** Quiet

## Test WinRM TCP port

```powershell
Test-NetConnection <HOST> -Port 5985
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** WinRM, discovery · **Context:** User · **Noise:** Quiet

## Test WinRM TLS port

```powershell
Test-NetConnection <HOST> -Port 5986
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** WinRM, TLS · **Context:** User · **Noise:** Quiet

## Test RDP port

```powershell
Test-NetConnection <HOST> -Port 3389
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** RDP, discovery · **Context:** User · **Noise:** Quiet

## Nmap WinRM and RDP

```bash
nmap -Pn -p 3389,5985,5986 <TARGET>
```

**Tool:** Nmap · **Platform:** Linux · **Tags:** RDP, WinRM · **Context:** No auth · **Noise:** Quiet

## Enumerate RDP NLA

```bash
nmap -Pn -p3389 --script rdp-enum-encryption <TARGET>
```

**Tool:** Nmap · **Platform:** Linux · **Tags:** RDP, NLA · **Context:** No auth · **Noise:** Quiet

---

**Related:** Local Admin Discovery · Sessions · Lateral Movement
