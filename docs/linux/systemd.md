# systemd Checks

One-liners for services, unit files, timers and writable systemd paths.

<div class="ol-section-kicker"><span>LNX</span><strong>6 one-liners</strong></div>

## Running services

```bash
systemctl --type=service --state=running --no-pager
```

**Tool:** systemctl · **Platform:** Linux · **Tags:** systemd, services · **Context:** User · **Noise:** Quiet

## Enabled services

```bash
systemctl list-unit-files --type=service --state=enabled --no-pager
```

**Tool:** systemctl · **Platform:** Linux · **Tags:** systemd, services · **Context:** User · **Noise:** Quiet

## Timers

```bash
systemctl list-timers --all --no-pager
```

**Tool:** systemctl · **Platform:** Linux · **Tags:** systemd, timers · **Context:** User · **Noise:** Quiet

## Unit file for service

```bash
systemctl cat <SERVICE>
```

**Tool:** systemctl · **Platform:** Linux · **Tags:** systemd, service · **Context:** User · **Noise:** Quiet

## Writable unit files

```bash
find /etc/systemd /usr/lib/systemd /lib/systemd -type f -writable 2>/dev/null
```

**Tool:** find · **Platform:** Linux · **Tags:** systemd, writable · **Context:** User · **Noise:** Quiet

## Writable service ExecStart targets

```bash
grep -RHE "^ExecStart=" /etc/systemd/system /lib/systemd/system /usr/lib/systemd/system 2>/dev/null | cut -d= -f2-
```

**Tool:** grep · **Platform:** Linux · **Tags:** systemd, services · **Context:** User · **Noise:** Quiet

---

**Related:** Writable Services · Cron · PATH Hijacking
