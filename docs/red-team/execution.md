# Red Team Execution

Remote execution one-liners for authorised environments.

### Remote PowerShell command

```powershell
Invoke-Command -ComputerName <HOST> -ScriptBlock { hostname; whoami }
```

**Tool:** PowerShell Remoting · **Platform:** Windows · **Tags:** Execution, WinRM · **Context:** User · **Noise:** Moderate

### WinRM with evil-winrm

```bash
evil-winrm -i <HOST> -u <USER> -p <PASSWORD>
```

**Tool:** Evil-WinRM · **Platform:** Linux · **Tags:** WinRM, Remote Access · **Context:** User · **Noise:** Moderate

### WMI command with Impacket

```bash
wmiexec.py <DOMAIN>/<USER>:<PASSWORD>@<HOST>
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** WMI, Remote Execution · **Context:** User · **Noise:** Moderate

### SMB exec with Impacket

```bash
psexec.py <DOMAIN>/<USER>:<PASSWORD>@<HOST>
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** SMB, Remote Execution · **Context:** User · **Noise:** Moderate

### NetExec command execution

```bash
nxc smb <HOST> -u <USER> -p <PASSWORD> -x "whoami"
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** SMB, Execution · **Context:** User · **Noise:** Moderate

---

**Related:** [Overview](./) · [Download Cradles](download-cradles.md) · [Lateral Movement](lateral-movement.md)
