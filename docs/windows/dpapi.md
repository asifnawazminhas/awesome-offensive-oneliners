# DPAPI Discovery

One-liners for locating Windows DPAPI material and checking common credential stores.

<div class="ol-section-kicker"><span>WIN</span><strong>5 one-liners</strong></div>

## List user Protect directory

```powershell
Get-ChildItem "$env:APPDATA\Microsoft\Protect" -Force -Recurse -ErrorAction SilentlyContinue
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** DPAPI, Protect · **Context:** User · **Noise:** Quiet

## List Credential Manager blobs

```powershell
Get-ChildItem "$env:LOCALAPPDATA\Microsoft\Credentials","$env:APPDATA\Microsoft\Credentials" -Force -ErrorAction SilentlyContinue
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** DPAPI, credentials · **Context:** User · **Noise:** Quiet

## List Vault files

```powershell
Get-ChildItem "$env:LOCALAPPDATA\Microsoft\Vault" -Force -Recurse -ErrorAction SilentlyContinue
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** DPAPI, vault · **Context:** User · **Noise:** Quiet

## Stored credential targets

```powershell
cmdkey /list
```

**Tool:** cmdkey · **Platform:** Windows · **Tags:** credentials, DPAPI · **Context:** User · **Noise:** Quiet

## Browser profile locations

```powershell
Get-ChildItem "$env:LOCALAPPDATA\Google\Chrome\User Data","$env:LOCALAPPDATA\Microsoft\Edge\User Data" -ErrorAction SilentlyContinue
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** browser, DPAPI · **Context:** User · **Noise:** Quiet

---

**Related:** Credentials · Tokens & Privileges · Environment
