# SMB, shares and sessions

Find reachable SMB hosts, shares, sessions and logged-on users.

<div class="ol-section-kicker"><span>AD</span></div>

## NetExec SMB discovery

```bash
nxc smb <CIDR>
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user


## NetExec authenticated SMB sweep

```bash
nxc smb <CIDR> -u <USER> -p '<PASSWORD>'
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user


## NetExec pass-the-hash validation

```bash
nxc smb <CIDR> -u <USER> -H <HASH>
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user


## NetExec shares

```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --shares
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user


## NetExec sessions

```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --sessions
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user


## NetExec logged-on users

```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --loggedon-users
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user


## smbclient list shares

```bash
smbclient -L //<TARGET>/ -U '<DOMAIN>/<USER>%<PASSWORD>'
```

**Tool:** smbclient · **Platform:** Linux/macOS · **Context:** Domain user


## PowerView shares

```powershell
Get-DomainComputer | Get-NetShare
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user

---

**Related:** [Overview](./) · [Sid History](sid-history.md) · [Trusts](trusts.md)
