# Red Team Discovery

Compact discovery commands useful during authorised red team operations.

### Domain identity

```powershell
whoami /user && whoami /groups
```

**Tool:** Windows · **Platform:** Windows · **Tags:** Identity, Discovery

### Domain controller discovery

```powershell
nltest /dsgetdc:<DOMAIN>
```

**Tool:** nltest · **Platform:** Windows · **Tags:** AD, DC Discovery

### Current logon sessions

```powershell
quser
```

**Tool:** Windows · **Platform:** Windows · **Tags:** Sessions, Discovery

### ARP neighbors

```powershell
arp -a
```

**Tool:** Windows · **Platform:** Windows · **Tags:** Network, Discovery

### SMB shares

```powershell
net view \<HOST>
```

**Tool:** Windows · **Platform:** Windows · **Tags:** SMB, Shares

### Linux neighbors

```bash
ip neigh
```

**Tool:** iproute2 · **Platform:** Linux · **Tags:** Network, Discovery

