# PATH Hijacking Checks

One-liners for finding writable PATH entries and scripts invoking commands without absolute paths.

<div class="ol-section-kicker"><span>LNX</span><strong>4 one-liners</strong></div>

## PATH entries

```bash
tr : '\n' <<< "$PATH"
```

**Tool:** bash · **Platform:** Linux · **Tags:** PATH · **Context:** User

## Writable PATH directories

```bash
tr : '\n' <<< "$PATH" | while read d; do [ -d "$d" ] && [ -w "$d" ] && echo "$d"; done
```

**Tool:** bash · **Platform:** Linux · **Tags:** PATH, writable · **Context:** User

## PATH ownership and permissions

```bash
tr : '\n' <<< "$PATH" | xargs -r ls -ld 2>/dev/null
```

**Tool:** ls · **Platform:** Linux · **Tags:** PATH, permissions · **Context:** User

## Scripts with bare command names

```bash
grep -RHE "(^|[;&| ])(cp|mv|tar|rsync|curl|wget|python|perl|bash|sh)([ ;|&]|$)" /etc/cron* /usr/local/bin 2>/dev/null
```

**Tool:** grep · **Platform:** Linux · **Tags:** PATH, scripts · **Context:** User

---

**Related:** Cron · Sudo Checks · Writable Services
