# Linux Enumeration

Fast Linux host enumeration commands.

### Current user and groups

```bash
id
```

**Tool:** Linux · **Platform:** Linux · **Tags:** Identity, Enumeration · **Context:** User · **Noise:** Quiet

### Kernel and OS

```bash
uname -a && cat /etc/os-release
```

**Tool:** Linux · **Platform:** Linux · **Tags:** OS, Enumeration · **Context:** User · **Noise:** Quiet

### Listening sockets

```bash
ss -lntup
```

**Tool:** iproute2 · **Platform:** Linux · **Tags:** Network, Ports · **Context:** User · **Noise:** Quiet

### Network interfaces

```bash
ip -br addr
```

**Tool:** iproute2 · **Platform:** Linux · **Tags:** Network, Interfaces · **Context:** User · **Noise:** Quiet

### Routing table

```bash
ip route
```

**Tool:** iproute2 · **Platform:** Linux · **Tags:** Network, Routes · **Context:** User · **Noise:** Quiet

### Sudo permissions

```bash
sudo -l
```

**Tool:** sudo · **Platform:** Linux · **Tags:** Privilege Escalation, sudo · **Context:** User · **Noise:** Quiet

### SUID files

```bash
find / -perm -4000 -type f 2>/dev/null
```

**Tool:** find · **Platform:** Linux · **Tags:** Privilege Escalation, SUID · **Context:** User · **Noise:** Quiet

### Cron jobs

```bash
grep -R "" /etc/cron* 2>/dev/null | head -n 100
```

**Tool:** grep · **Platform:** Linux · **Tags:** Cron, Enumeration · **Context:** User · **Noise:** Quiet

---

**Related:** [Overview](./) · [Cron](cron.md) · [Networking Files](networking-files.md)
