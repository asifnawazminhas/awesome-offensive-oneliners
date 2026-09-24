# UAC State

One-liners for reading User Account Control configuration and current elevation context.

<div class="ol-section-kicker"><span>WIN</span><strong>5 one-liners</strong></div>

## EnableLUA

```powershell
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA
```

**Tool:** reg.exe · **Platform:** Windows · **Tags:** UAC · **Context:** User

## ConsentPromptBehaviorAdmin

```powershell
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v ConsentPromptBehaviorAdmin
```

**Tool:** reg.exe · **Platform:** Windows · **Tags:** UAC · **Context:** User

## PromptOnSecureDesktop

```powershell
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v PromptOnSecureDesktop
```

**Tool:** reg.exe · **Platform:** Windows · **Tags:** UAC · **Context:** User

## Token elevation type

```powershell
whoami /groups | findstr /i "Mandatory Label"
```

**Tool:** whoami · **Platform:** Windows · **Tags:** UAC, token · **Context:** User

## Current admin membership

```powershell
net localgroup administrators | findstr /i /c:"%USERNAME%"
```

**Tool:** net.exe · **Platform:** Windows · **Tags:** UAC, admin · **Context:** User

---

**Related:** Tokens & Privileges · Environment · Execution Control
