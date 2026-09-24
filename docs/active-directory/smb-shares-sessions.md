# SMB, shares and sessions

Find reachable SMB hosts, shares, sessions and logged-on users.

<div class="ol-section-kicker"><span>AD</span></div>

## NetExec SMB discovery

```bash
nxc smb <CIDR>
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Quiet


## NetExec authenticated SMB sweep

```bash
nxc smb <CIDR> -u <USER> -p '<PASSWORD>'
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Quiet


## NetExec pass-the-hash validation

```bash
nxc smb <CIDR> -u <USER> -H <HASH>
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Quiet


## NetExec shares

```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --shares
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Quiet


## NetExec sessions

```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --sessions
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Quiet


## NetExec logged-on users

```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --loggedon-users
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Quiet


## smbclient list shares

```bash
smbclient -L //<TARGET>/ -U '<DOMAIN>/<USER>%<PASSWORD>'
```

**Tool:** smbclient · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Quiet


## PowerView shares

```powershell
Get-DomainComputer | Get-NetShare
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user · **Noise:** Quiet

---

**Related:** [Overview](./) · [Sid History](sid-history.md) · [Trusts](trusts.md)
