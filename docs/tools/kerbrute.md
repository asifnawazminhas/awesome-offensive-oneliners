# Kerbrute

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

Kerbrute one-liners for Kerberos-based user validation and authentication checks.

<div class="ol-section-kicker"><span>TOOL</span><strong>3 one-liners</strong></div>

## User enumeration

```bash
kerbrute userenum -d <DOMAIN> --dc <DC_IP> users.txt
```

**Tool:** Kerbrute · **Platform:** Linux · **Tags:** Kerberos, user enumeration · **Context:** No auth · **Noise:** Moderate

## Password spray

```bash
kerbrute passwordspray -d <DOMAIN> --dc <DC_IP> users.txt '<PASSWORD>'
```

**Tool:** Kerbrute · **Platform:** Linux · **Tags:** Kerberos, password spray · **Context:** No auth · **Noise:** Moderate

## Brute one user

```bash
kerbrute bruteuser -d <DOMAIN> --dc <DC_IP> passwords.txt <USER>
```

**Tool:** Kerbrute · **Platform:** Linux · **Tags:** Kerberos, authentication · **Context:** No auth · **Noise:** Moderate

---

**Related:** Kerberos · Domain Password Policy · Users & Groups
