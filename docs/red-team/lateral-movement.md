# Lateral Movement

Credential validation and remote access commands for scoped lateral movement testing.

### Test SMB credentials across hosts

```bash
nxc smb <CIDR> -u <USER> -p <PASSWORD> --continue-on-success
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** SMB, Credential Validation

### Test WinRM credentials

```bash
nxc winrm <CIDR> -u <USER> -p <PASSWORD>
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** WinRM, Credential Validation

### Test RDP credentials

```bash
nxc rdp <CIDR> -u <USER> -p <PASSWORD>
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** RDP, Credential Validation

### Copy file over SMB

```bash
smbclient //<HOST>/<SHARE> -U <DOMAIN>/<USER>%<PASSWORD> -c "put <FILE>"
```

**Tool:** smbclient · **Platform:** Linux · **Tags:** SMB, File Transfer

### RDP session

```bash
xfreerdp /v:<HOST> /u:<USER> /p:<PASSWORD> /dynamic-resolution /cert:ignore
```

**Tool:** FreeRDP · **Platform:** Linux · **Tags:** RDP, Remote Access

