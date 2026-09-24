# Kerbrute

Kerbrute one-liners for Kerberos-based user validation and authentication checks.

<div class="ol-section-kicker"><span>TOOL</span><strong>3 one-liners</strong></div>

## User enumeration

```bash
kerbrute userenum -d <DOMAIN> --dc <DC_IP> users.txt
```

**Tool:** Kerbrute · **Platform:** Linux · **Tags:** Kerberos, user enumeration · **Context:** No auth

## Password spray

```bash
kerbrute passwordspray -d <DOMAIN> --dc <DC_IP> users.txt '<PASSWORD>'
```

**Tool:** Kerbrute · **Platform:** Linux · **Tags:** Kerberos, password spray · **Context:** No auth

## Brute one user

```bash
kerbrute bruteuser -d <DOMAIN> --dc <DC_IP> passwords.txt <USER>
```

**Tool:** Kerbrute · **Platform:** Linux · **Tags:** Kerberos, authentication · **Context:** No auth

---

**Related:** Kerberos · Domain Password Policy · Users & Groups
