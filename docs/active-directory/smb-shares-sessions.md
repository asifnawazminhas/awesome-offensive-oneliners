# SMB, shares and sessions

Find reachable SMB hosts, shares, sessions and logged-on users.

<div class="ol-section-kicker"><span>AD</span></div>

## NetExec SMB discovery

```bash
nxc smb <CIDR>
```

**Tool:** NetExec · **Platform:** Linux/macOS


## NetExec authenticated SMB sweep

```bash
nxc smb <CIDR> -u <USER> -p '<PASSWORD>'
```

**Tool:** NetExec · **Platform:** Linux/macOS


## NetExec pass-the-hash validation

```bash
nxc smb <CIDR> -u <USER> -H <HASH>
```

**Tool:** NetExec · **Platform:** Linux/macOS


## NetExec shares

```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --shares
```

**Tool:** NetExec · **Platform:** Linux/macOS


## NetExec sessions

```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --sessions
```

**Tool:** NetExec · **Platform:** Linux/macOS


## NetExec logged-on users

```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --loggedon-users
```

**Tool:** NetExec · **Platform:** Linux/macOS


## smbclient list shares

```bash
smbclient -L //<TARGET>/ -U '<DOMAIN>/<USER>%<PASSWORD>'
```

**Tool:** smbclient · **Platform:** Linux/macOS


## PowerView shares

```powershell
Get-DomainComputer | Get-NetShare
```

**Tool:** PowerView · **Platform:** Windows
