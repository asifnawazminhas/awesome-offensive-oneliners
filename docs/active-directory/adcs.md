# Active Directory Certificate Services

Discover certificate services, templates and common AD CS exposure.

<div class="ol-section-kicker"><span>AD</span></div>

## Certipy find

```bash
certipy find -u '<USER>@<DOMAIN>' -p '<PASSWORD>' -dc-ip <DC_IP>
```

**Tool:** Certipy · **Platform:** Linux/macOS


## Certipy vulnerable templates

```bash
certipy find -u '<USER>@<DOMAIN>' -p '<PASSWORD>' -dc-ip <DC_IP> -vulnerable
```

**Tool:** Certipy · **Platform:** Linux/macOS


## Certipy JSON output

```bash
certipy find -u '<USER>@<DOMAIN>' -p '<PASSWORD>' -dc-ip <DC_IP> -json
```

**Tool:** Certipy · **Platform:** Linux/macOS


## Certify enumerate

```cmd
Certify.exe find
```

**Tool:** Certify · **Platform:** Windows


## Certify vulnerable templates

```cmd
Certify.exe find /vulnerable
```

**Tool:** Certify · **Platform:** Windows


## PowerShell enterprise CAs

```powershell
Get-ChildItem Cert:\LocalMachine\CA | Select Subject,Thumbprint
```

**Tool:** PowerShell · **Platform:** Windows
