# Certipy & BloodHound

Fast collection and discovery one-liners.

### Certipy vulnerable templates

```bash
certipy find -u <USER>@<DOMAIN> -p <PASSWORD> -dc-ip <DC_IP> -vulnerable -stdout
```

**Tool:** Certipy · **Platform:** Linux · **Tags:** AD CS, Templates

### Certipy full find

```bash
certipy find -u <USER>@<DOMAIN> -p <PASSWORD> -dc-ip <DC_IP> -enabled -stdout
```

**Tool:** Certipy · **Platform:** Linux · **Tags:** AD CS, Discovery

### BloodHound Python all collection

```bash
bloodhound-python -u <USER> -p <PASSWORD> -d <DOMAIN> -ns <DC_IP> -c All
```

**Tool:** bloodhound-python · **Platform:** Linux · **Tags:** BloodHound, Collection

### SharpHound all collection

```powershell
SharpHound.exe -c All --zipfilename bloodhound.zip
```

**Tool:** SharpHound · **Platform:** Windows · **Tags:** BloodHound, Collection

