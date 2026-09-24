# Certify

Certify one-liners for AD CS discovery from Windows hosts.

<div class="ol-section-kicker"><span>TOOL</span><strong>4 one-liners</strong></div>

## Find vulnerable templates

```powershell
Certify.exe find /vulnerable
```

**Tool:** Certify · **Platform:** Windows · **Tags:** AD CS, templates · **Context:** Domain user

## Find all CA and templates

```powershell
Certify.exe find
```

**Tool:** Certify · **Platform:** Windows · **Tags:** AD CS, discovery · **Context:** Domain user

## Current user context

```powershell
Certify.exe find /currentuser
```

**Tool:** Certify · **Platform:** Windows · **Tags:** AD CS, current user · **Context:** Domain user

## Specific CA

```powershell
Certify.exe find /ca:<CA_NAME>
```

**Tool:** Certify · **Platform:** Windows · **Tags:** AD CS, CA · **Context:** Domain user

---

**Related:** AD CS · Certipy · BloodHound
