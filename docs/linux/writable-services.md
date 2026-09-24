# Writable Service Paths

One-liners for identifying writable binaries, scripts and config files used by privileged services.

<div class="ol-section-kicker"><span>LNX</span><strong>5 one-liners</strong></div>

## Root processes and binaries

```bash
ps -eo user,pid,comm,args | awk '$1=="root"'
```

**Tool:** ps · **Platform:** Linux · **Tags:** services, root processes · **Context:** User · **Noise:** Quiet

## Writable executables in /usr/local

```bash
find /usr/local -type f -writable -executable 2>/dev/null
```

**Tool:** find · **Platform:** Linux · **Tags:** writable, services · **Context:** User · **Noise:** Quiet

## Writable init scripts

```bash
find /etc/init.d /etc/systemd/system -type f -writable 2>/dev/null
```

**Tool:** find · **Platform:** Linux · **Tags:** services, writable · **Context:** User · **Noise:** Quiet

## Writable root-owned scripts

```bash
find / -xdev -type f -user root -writable 2>/dev/null | head -100
```

**Tool:** find · **Platform:** Linux · **Tags:** writable, root · **Context:** User · **Noise:** Quiet

## Service command lines

```bash
systemctl list-units --type=service --state=running --no-pager --no-legend | awk '{print $1}' | xargs -r -n1 systemctl show -p User -p ExecStart
```

**Tool:** systemctl · **Platform:** Linux · **Tags:** services, discovery · **Context:** User · **Noise:** Quiet

---

**Related:** systemd · Cron · PATH Hijacking
