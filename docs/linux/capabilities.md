# Linux Capabilities

One-liners for discovering binaries with file capabilities and high-value capability assignments.

<div class="ol-section-kicker"><span>LNX</span><strong>4 one-liners</strong></div>

## All file capabilities

```bash
getcap -r / 2>/dev/null
```

**Tool:** getcap · **Platform:** Linux · **Tags:** capabilities, privilege escalation · **Context:** User

## High-value capabilities

```bash
getcap -r / 2>/dev/null | grep -Ei "cap_setuid|cap_setgid|cap_dac_override|cap_sys_admin|cap_sys_ptrace|cap_chown"
```

**Tool:** getcap · **Platform:** Linux · **Tags:** capabilities, privilege escalation · **Context:** User

## Current process capabilities

```bash
grep -E "^Cap(Inh|Prm|Eff|Bnd|Amb):" /proc/self/status
```

**Tool:** procfs · **Platform:** Linux · **Tags:** capabilities, process · **Context:** User

## Decode current capabilities

```bash
capsh --decode=$(awk '/CapEff/{print $2}' /proc/self/status)
```

**Tool:** capsh · **Platform:** Linux · **Tags:** capabilities, process · **Context:** User

---

**Related:** Sudo Checks · SUID/SGID · Containers
