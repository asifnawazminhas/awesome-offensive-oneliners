# Lateral Movement

Credential validation and remote access commands for scoped lateral movement testing.

### Test SMB credentials across hosts

```bash
nxc smb <CIDR> -u <USER> -p <PASSWORD> --continue-on-success
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** SMB, Credential Validation · **Context:** User · **Noise:** Loud

### Test WinRM credentials

```bash
nxc winrm <CIDR> -u <USER> -p <PASSWORD>
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** WinRM, Credential Validation · **Context:** User · **Noise:** Loud

### Test RDP credentials

```bash
nxc rdp <CIDR> -u <USER> -p <PASSWORD>
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** RDP, Credential Validation · **Context:** User · **Noise:** Loud

### Copy file over SMB

```bash
smbclient //<HOST>/<SHARE> -U <DOMAIN>/<USER>%<PASSWORD> -c "put <FILE>"
```

**Tool:** smbclient · **Platform:** Linux · **Tags:** SMB, File Transfer · **Context:** User · **Noise:** Loud

### RDP session

```bash
xfreerdp /v:<HOST> /u:<USER> /p:<PASSWORD> /dynamic-resolution /cert:ignore
```

**Tool:** FreeRDP · **Platform:** Linux · **Tags:** RDP, Remote Access · **Context:** User · **Noise:** Loud

---

**Related:** [Overview](./) · [Execution](execution.md) · [Lolbins](lolbins.md)
