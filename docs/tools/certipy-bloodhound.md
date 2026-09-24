# Certipy & BloodHound

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

Fast collection and discovery one-liners.

### Certipy vulnerable templates

```bash
certipy find -u <USER>@<DOMAIN> -p <PASSWORD> -dc-ip <DC_IP> -vulnerable -stdout
```

**Tool:** Certipy · **Platform:** Linux · **Tags:** AD CS, Templates · **Context:** Domain user · **Noise:** Moderate

### Certipy full find

```bash
certipy find -u <USER>@<DOMAIN> -p <PASSWORD> -dc-ip <DC_IP> -enabled -stdout
```

**Tool:** Certipy · **Platform:** Linux · **Tags:** AD CS, Discovery · **Context:** Domain user · **Noise:** Moderate

### BloodHound Python all collection

```bash
bloodhound-python -u <USER> -p <PASSWORD> -d <DOMAIN> -ns <DC_IP> -c All
```

**Tool:** bloodhound-python · **Platform:** Linux · **Tags:** BloodHound, Collection · **Context:** Domain user · **Noise:** Moderate

### SharpHound all collection

```powershell
SharpHound.exe -c All --zipfilename bloodhound.zip
```

**Tool:** SharpHound · **Platform:** Windows · **Tags:** BloodHound, Collection · **Context:** Domain user · **Noise:** Moderate

---

**Related:** [Overview](./) · [Certify](certify.md) · [Curl Jq](curl-jq.md)
