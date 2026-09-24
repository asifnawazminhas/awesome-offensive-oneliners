# Sudo Checks

One-liners for sudo rights, sudoers configuration and common privilege escalation candidates.

<div class="ol-section-kicker"><span>LNX</span><strong>5 one-liners</strong></div>

## Current sudo rights

```bash
sudo -l
```

**Tool:** sudo · **Platform:** Linux · **Tags:** sudo, privilege escalation · **Context:** User

## Sudo version

```bash
sudo --version | head -1
```

**Tool:** sudo · **Platform:** Linux · **Tags:** sudo, version · **Context:** User

## Read sudoers includes

```bash
grep -RHEv "^#|^$" /etc/sudoers /etc/sudoers.d/* 2>/dev/null
```

**Tool:** grep · **Platform:** Linux · **Tags:** sudo, configuration · **Context:** User

## Find NOPASSWD rules

```bash
grep -RHi "NOPASSWD" /etc/sudoers /etc/sudoers.d 2>/dev/null
```

**Tool:** grep · **Platform:** Linux · **Tags:** sudo, NOPASSWD · **Context:** User

## Check env_keep

```bash
grep -RHi "env_keep" /etc/sudoers /etc/sudoers.d 2>/dev/null
```

**Tool:** grep · **Platform:** Linux · **Tags:** sudo, environment · **Context:** User

---

**Related:** GTFOBins · PATH Hijacking · Capabilities
