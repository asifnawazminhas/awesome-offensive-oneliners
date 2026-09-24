# Red Team Discovery

Compact discovery commands useful during authorised red team operations.

### Domain identity

```powershell
whoami /user && whoami /groups
```

**Tool:** Windows · **Platform:** Windows · **Tags:** Identity, Discovery · **Context:** User · **Noise:** Moderate

### Domain controller discovery

```powershell
nltest /dsgetdc:<DOMAIN>
```

**Tool:** nltest · **Platform:** Windows · **Tags:** AD, DC Discovery · **Context:** User · **Noise:** Moderate

### Current logon sessions

```powershell
quser
```

**Tool:** Windows · **Platform:** Windows · **Tags:** Sessions, Discovery · **Context:** User · **Noise:** Moderate

### ARP neighbors

```powershell
arp -a
```

**Tool:** Windows · **Platform:** Windows · **Tags:** Network, Discovery · **Context:** User · **Noise:** Moderate

### SMB shares

```powershell
net view \<HOST>
```

**Tool:** Windows · **Platform:** Windows · **Tags:** SMB, Shares · **Context:** User · **Noise:** Moderate

### Linux neighbors

```bash
ip neigh
```

**Tool:** iproute2 · **Platform:** Linux · **Tags:** Network, Discovery · **Context:** User · **Noise:** Moderate

---

**Related:** [Overview](./) · [Download Cradles](download-cradles.md)
