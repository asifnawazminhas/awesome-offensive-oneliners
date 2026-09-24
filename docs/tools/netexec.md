# NetExec

Fast NetExec reference grouped around common SMB and LDAP tasks.

<div class="ol-section-kicker"><span>TOOLS</span></div>

## SMB discovery

```bash
nxc smb <CIDR>
```

**Tool:** NetExec · **Platform:** Linux/macOS


## SMB password authentication

```bash
nxc smb <TARGETS> -u <USER> -p '<PASSWORD>'
```

**Tool:** NetExec · **Platform:** Linux/macOS


## SMB NTLM authentication

```bash
nxc smb <TARGETS> -u <USER> -H <HASH>
```

**Tool:** NetExec · **Platform:** Linux/macOS


## SMB shares

```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --shares
```

**Tool:** NetExec · **Platform:** Linux/macOS


## SMB sessions

```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --sessions
```

**Tool:** NetExec · **Platform:** Linux/macOS


## SMB logged-on users

```bash
nxc smb <TARGET> -u <USER> -p '<PASSWORD>' --loggedon-users
```

**Tool:** NetExec · **Platform:** Linux/macOS


## SMB password policy

```bash
nxc smb <DC_IP> -u <USER> -p '<PASSWORD>' --pass-pol
```

**Tool:** NetExec · **Platform:** Linux/macOS


## LDAP users

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --users
```

**Tool:** NetExec · **Platform:** Linux/macOS


## LDAP groups

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --groups
```

**Tool:** NetExec · **Platform:** Linux/macOS


## LDAP computers

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --computers
```

**Tool:** NetExec · **Platform:** Linux/macOS


## Kerberoast

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --kerberoasting kerberoast.txt
```

**Tool:** NetExec · **Platform:** Linux/macOS


## AS-REP roast

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --asreproast asrep.txt
```

**Tool:** NetExec · **Platform:** Linux/macOS
