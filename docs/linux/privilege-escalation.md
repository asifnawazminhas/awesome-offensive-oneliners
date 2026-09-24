# Linux Privilege Escalation Checks

Quick checks that help identify common local privilege escalation conditions.

### Writable files in PATH

```bash
IFS=:; for d in $PATH; do find "$d" -maxdepth 1 -type f -writable 2>/dev/null; done
```

**Tool:** find · **Platform:** Linux · **Tags:** PATH, Writable

### Capabilities

```bash
getcap -r / 2>/dev/null
```

**Tool:** getcap · **Platform:** Linux · **Tags:** Capabilities, Privilege Escalation

### World-writable directories

```bash
find / -xdev -type d -perm -0002 2>/dev/null
```

**Tool:** find · **Platform:** Linux · **Tags:** Writable, Directories

### Interesting owner-root files writable by current user

```bash
find / -xdev -user root -writable -type f 2>/dev/null
```

**Tool:** find · **Platform:** Linux · **Tags:** Writable, Privilege Escalation

### Running processes

```bash
ps auxww --sort=-%cpu | head -n 30
```

**Tool:** ps · **Platform:** Linux · **Tags:** Processes, Enumeration

### Systemd services

```bash
systemctl list-units --type=service --state=running --no-pager
```

**Tool:** systemd · **Platform:** Linux · **Tags:** Services, Enumeration

