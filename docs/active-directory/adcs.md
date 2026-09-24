# Active Directory Certificate Services

Discover certificate services, templates and common AD CS exposure.

<div class="ol-section-kicker"><span>AD</span></div>

## Certipy find

```bash
certipy find -u '<USER>@<DOMAIN>' -p '<PASSWORD>' -dc-ip <DC_IP>
```

**Tool:** Certipy · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Moderate


## Certipy vulnerable templates

```bash
certipy find -u '<USER>@<DOMAIN>' -p '<PASSWORD>' -dc-ip <DC_IP> -vulnerable
```

**Tool:** Certipy · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Moderate


## Certipy JSON output

```bash
certipy find -u '<USER>@<DOMAIN>' -p '<PASSWORD>' -dc-ip <DC_IP> -json
```

**Tool:** Certipy · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Moderate


## Certify enumerate

```cmd
Certify.exe find
```

**Tool:** Certify · **Platform:** Windows · **Context:** Domain user · **Noise:** Moderate


## Certify vulnerable templates

```cmd
Certify.exe find /vulnerable
```

**Tool:** Certify · **Platform:** Windows · **Context:** Domain user · **Noise:** Moderate


## PowerShell enterprise CAs

```powershell
Get-ChildItem Cert:\LocalMachine\CA | Select Subject,Thumbprint
```

**Tool:** PowerShell · **Platform:** Windows · **Context:** Domain user · **Noise:** Moderate

---

**Related:** [Overview](./) · [Acls](acls.md) · [Bloodhound](bloodhound.md)
