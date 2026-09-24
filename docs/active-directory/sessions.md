# Session Hunting

One-liners for finding logged-on users and active SMB/session relationships.

<div class="ol-section-kicker"><span>AD</span><strong>7 one-liners</strong></div>

## PowerView logged-on users

```powershell
Get-NetLoggedon -ComputerName <HOST>
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, sessions · **Context:** Domain user · **Noise:** Quiet

## PowerView sessions

```powershell
Get-NetSession -ComputerName <HOST>
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, sessions · **Context:** Domain user · **Noise:** Quiet

## NetExec sessions

```bash
nxc smb <TARGETS> -u <USER> -p '<PASSWORD>' --sessions
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** AD, SMB, sessions · **Context:** Domain user · **Noise:** Quiet

## NetExec logged-on users

```bash
nxc smb <TARGETS> -u <USER> -p '<PASSWORD>' --loggedon-users
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** AD, sessions · **Context:** Domain user · **Noise:** Quiet

## Native SMB sessions

```powershell
net session
```

**Tool:** net.exe · **Platform:** Windows · **Tags:** SMB, sessions · **Context:** Local admin · **Noise:** Quiet

## Current interactive users

```powershell
quser
```

**Tool:** quser · **Platform:** Windows · **Tags:** sessions, RDP · **Context:** User · **Noise:** Quiet

## Remote query user

```powershell
quser /server:<HOST>
```

**Tool:** quser · **Platform:** Windows · **Tags:** sessions, RDP · **Context:** Domain user · **Noise:** Quiet

---

**Related:** Local Admin Discovery · BloodHound · Lateral Movement
