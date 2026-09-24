---
hide:
  - toc
---

# Linux Privilege Escalation Checks

Fast checks for common local privilege-escalation conditions.

<div class="ol-section-kicker"><span>LNX</span><strong>PRIVESC</strong></div>

## sudo rights

```bash
sudo -l
```

**Tool:** sudo · **Platform:** Linux · **Tags:** Sudo, Privileges · **Context:** User · **Noise:** Quiet

## SUID binaries

```bash
find / -perm -4000 -type f 2>/dev/null
```

**Tool:** find · **Platform:** Linux · **Tags:** SUID, Privilege Escalation · **Context:** User · **Noise:** Quiet

## SGID binaries

```bash
find / -perm -2000 -type f 2>/dev/null
```

**Tool:** find · **Platform:** Linux · **Tags:** SGID, Privilege Escalation · **Context:** User · **Noise:** Quiet

## File capabilities

```bash
getcap -r / 2>/dev/null
```

**Tool:** getcap · **Platform:** Linux · **Tags:** Capabilities · **Context:** User · **Noise:** Quiet

## passwd and shadow permissions

```bash
ls -la /etc/passwd /etc/shadow
```

**Tool:** ls · **Platform:** Linux · **Tags:** Credentials, Permissions · **Context:** User · **Noise:** Quiet

## Cron overview

```bash
cat /etc/crontab 2>/dev/null; ls -la /etc/cron.* 2>/dev/null; crontab -l 2>/dev/null
```

**Tool:** cron · **Platform:** Linux · **Tags:** Scheduled Jobs · **Context:** User · **Noise:** Quiet

## World-writable directories

```bash
find / -xdev -type d -perm -0002 2>/dev/null
```

**Tool:** find · **Platform:** Linux · **Tags:** Writable, Directories · **Context:** User · **Noise:** Quiet

## Root-owned files writable by current user

```bash
find / -xdev -user root -writable -type f 2>/dev/null
```

**Tool:** find · **Platform:** Linux · **Tags:** Writable, Files · **Context:** User · **Noise:** Quiet

## Kernel and OS version

```bash
uname -a; cat /etc/os-release
```

**Tool:** uname · **Platform:** Linux · **Tags:** Kernel, OS · **Context:** User · **Noise:** Quiet

## NFS exports

```bash
cat /etc/exports 2>/dev/null
```

**Tool:** NFS · **Platform:** Linux · **Tags:** NFS, no_root_squash · **Context:** User · **Noise:** Quiet

## Docker group membership

```bash
id | grep -E '\b(docker|lxd)\b'
```

**Tool:** id · **Platform:** Linux · **Tags:** Containers, Groups · **Context:** User · **Noise:** Quiet

## Root processes

```bash
ps aux | awk '$1=="root"'
```

**Tool:** ps + awk · **Platform:** Linux · **Tags:** Processes · **Context:** User · **Noise:** Quiet

## Environment and shell history

```bash
env; tail -n 200 ~/.bash_history 2>/dev/null
```

**Tool:** shell · **Platform:** Linux · **Tags:** Environment, History · **Context:** User · **Noise:** Quiet

## Writable PATH files

```bash
IFS=:; for d in $PATH; do find "$d" -maxdepth 1 -type f -writable 2>/dev/null; done
```

**Tool:** find · **Platform:** Linux · **Tags:** PATH, Writable · **Context:** User · **Noise:** Quiet

## Running systemd services

```bash
systemctl list-units --type=service --state=running --no-pager
```

**Tool:** systemd · **Platform:** Linux · **Tags:** Services · **Context:** User · **Noise:** Quiet

---

**Related:** [Overview](./) · [Path Hijacking](path-hijacking.md) · [Sudo](sudo.md)
