# Cron Checks

One-liners for cron jobs, writable scripts and scheduled root execution paths.

<div class="ol-section-kicker"><span>LNX</span><strong>5 one-liners</strong></div>

## System cron

```bash
cat /etc/crontab 2>/dev/null
```

**Tool:** cat · **Platform:** Linux · **Tags:** cron · **Context:** User · **Noise:** Quiet

## Cron directories

```bash
ls -la /etc/cron.* 2>/dev/null
```

**Tool:** ls · **Platform:** Linux · **Tags:** cron · **Context:** User · **Noise:** Quiet

## Current user crontab

```bash
crontab -l 2>/dev/null
```

**Tool:** crontab · **Platform:** Linux · **Tags:** cron · **Context:** User · **Noise:** Quiet

## All cron entries

```bash
grep -RHEv "^#|^$" /etc/crontab /etc/cron.d/* 2>/dev/null
```

**Tool:** grep · **Platform:** Linux · **Tags:** cron · **Context:** User · **Noise:** Quiet

## Writable files referenced by cron

```bash
grep -RHEv "^#|^$" /etc/crontab /etc/cron.d/* 2>/dev/null | grep -Eo "/[^ ]+" | while read f; do [ -w "$f" ] && echo "$f"; done
```

**Tool:** grep · **Platform:** Linux · **Tags:** cron, writable · **Context:** User · **Noise:** Quiet

---

**Related:** systemd · Writable Services · PATH Hijacking
