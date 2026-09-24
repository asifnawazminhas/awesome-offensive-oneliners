# Active Directory Certificate Services

Discovery and certificate workflow one-liners for AD CS assessments.

### Discover certificate authorities

```bash
certipy find -u <USER>@<DOMAIN> -p <PASSWORD> -dc-ip <DC_IP>
```

**Tool:** Certipy · **Platform:** Linux · **Tags:** AD CS, Discovery

### Find vulnerable templates

```bash
certipy find -u <USER>@<DOMAIN> -p <PASSWORD> -dc-ip <DC_IP> -vulnerable -stdout
```

**Tool:** Certipy · **Platform:** Linux · **Tags:** AD CS, Templates

### Export BloodHound-ready AD CS data

```bash
certipy find -u <USER>@<DOMAIN> -p <PASSWORD> -dc-ip <DC_IP> -bloodhound
```

**Tool:** Certipy · **Platform:** Linux · **Tags:** AD CS, BloodHound

### Request certificate

```bash
certipy req -u <USER>@<DOMAIN> -p <PASSWORD> -ca <CA_NAME> -template <TEMPLATE> -dc-ip <DC_IP>
```

**Tool:** Certipy · **Platform:** Linux · **Tags:** AD CS, Certificate

### Authenticate with PFX

```bash
certipy auth -pfx <CERTIFICATE>.pfx -dc-ip <DC_IP>
```

**Tool:** Certipy · **Platform:** Linux · **Tags:** AD CS, PKINIT

