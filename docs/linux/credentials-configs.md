# Credential & Config Discovery

One-liners for locating common configuration files, histories and credential-bearing environment values.

<div class="ol-section-kicker"><span>LNX</span><strong>5 one-liners</strong></div>

## Credential-like files in home

```bash
find ~ -maxdepth 4 -type f \( -iname "*.env" -o -iname "*.ini" -o -iname "*.conf" -o -iname "*.yaml" -o -iname "*.yml" -o -iname "*.json" \) 2>/dev/null
```

**Tool:** find · **Platform:** Linux · **Tags:** credentials, configs · **Context:** User

## Secret keywords in config files

```bash
grep -RIniE "(password|passwd|secret|token|api[_-]?key|client[_-]?secret)" ~ /etc 2>/dev/null | head -100
```

**Tool:** grep · **Platform:** Linux · **Tags:** credentials, configs · **Context:** User

## Shell histories

```bash
find ~ -maxdepth 2 -type f -name ".*history" -print -exec tail -n 50 {} \; 2>/dev/null
```

**Tool:** find · **Platform:** Linux · **Tags:** credentials, history · **Context:** User

## Environment secret keywords

```bash
env | grep -Ei "(password|passwd|secret|token|key|credential)"
```

**Tool:** env · **Platform:** Linux · **Tags:** credentials, environment · **Context:** User

## SSH private keys

```bash
find ~ -type f \( -name "id_rsa" -o -name "id_ed25519" -o -name "*.pem" \) -maxdepth 4 2>/dev/null
```

**Tool:** find · **Platform:** Linux · **Tags:** SSH, credentials · **Context:** User

---

**Related:** Enumeration · Container Detection · Networking & Files
