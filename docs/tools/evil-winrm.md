# Evil-WinRM

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

<div class="ol-section-kicker"><span>TOOL</span><strong>EVIL-WINRM</strong></div>

## Password authentication
```bash
evil-winrm -i <TARGET> -u '<USER>' -p '<PASSWORD>'
```
**Tool:** Evil-WinRM · **Platform:** Linux/macOS · **Tags:** WinRM, Authentication · **Context:** Valid user · **Noise:** Moderate

## NTLM hash authentication
```bash
evil-winrm -i <TARGET> -u '<USER>' -H '<NT_HASH>'
```
**Tool:** Evil-WinRM · **Platform:** Linux/macOS · **Tags:** WinRM, NTLM · **Context:** Valid user · **Noise:** Moderate

## SSL WinRM
```bash
evil-winrm -i <TARGET> -u '<USER>' -p '<PASSWORD>' -S
```
**Tool:** Evil-WinRM · **Platform:** Linux/macOS · **Tags:** WinRM, HTTPS · **Context:** Valid user · **Noise:** Moderate

## Load local PowerShell scripts
```bash
evil-winrm -i <TARGET> -u '<USER>' -p '<PASSWORD>' -s ./scripts
```
**Tool:** Evil-WinRM · **Platform:** Linux/macOS · **Tags:** WinRM, Scripts · **Context:** Valid user · **Noise:** Moderate
