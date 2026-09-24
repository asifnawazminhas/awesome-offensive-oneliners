# NetExec

Common NetExec one-liners across SMB, LDAP, WinRM and MSSQL.

### SMB host discovery

```bash
nxc smb <CIDR>
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** SMB, Discovery

### SMB authenticated check

```bash
nxc smb <CIDR> -u <USER> -p <PASSWORD>
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** SMB, Authentication

### SMB shares

```bash
nxc smb <HOST> -u <USER> -p <PASSWORD> --shares
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** SMB, Shares

### SMB sessions

```bash
nxc smb <HOST> -u <USER> -p <PASSWORD> --sessions
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** SMB, Sessions

### LDAP users

```bash
nxc ldap <DC> -u <USER> -p <PASSWORD> --users
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** LDAP, Users

### LDAP groups

```bash
nxc ldap <DC> -u <USER> -p <PASSWORD> --groups
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** LDAP, Groups

### WinRM authentication

```bash
nxc winrm <HOST> -u <USER> -p <PASSWORD>
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** WinRM, Authentication

### MSSQL authentication

```bash
nxc mssql <HOST> -u <USER> -p <PASSWORD>
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** MSSQL, Authentication

