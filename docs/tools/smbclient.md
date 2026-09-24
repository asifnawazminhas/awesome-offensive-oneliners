# smbclient

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

smbclient one-liners for share enumeration and file operations.

<div class="ol-section-kicker"><span>TOOL</span><strong>5 one-liners</strong></div>

## Anonymous share list

```bash
smbclient -L //<TARGET> -N
```

**Tool:** smbclient · **Platform:** Linux · **Tags:** SMB, shares · **Context:** No auth · **Noise:** Moderate

## Authenticated share list

```bash
smbclient -L //<TARGET> -U '<DOMAIN>/<USER>%<PASSWORD>'
```

**Tool:** smbclient · **Platform:** Linux · **Tags:** SMB, shares · **Context:** Domain user · **Noise:** Moderate

## Connect to share

```bash
smbclient //<TARGET>/<SHARE> -U '<DOMAIN>/<USER>%<PASSWORD>'
```

**Tool:** smbclient · **Platform:** Linux · **Tags:** SMB, share · **Context:** Domain user · **Noise:** Moderate

## Recursive list

```bash
smbclient //<TARGET>/<SHARE> -U '<DOMAIN>/<USER>%<PASSWORD>' -c 'recurse;ls'
```

**Tool:** smbclient · **Platform:** Linux · **Tags:** SMB, files · **Context:** Domain user · **Noise:** Moderate

## Download file

```bash
smbclient //<TARGET>/<SHARE> -U '<DOMAIN>/<USER>%<PASSWORD>' -c 'get <REMOTE_FILE> <LOCAL_FILE>'
```

**Tool:** smbclient · **Platform:** Linux · **Tags:** SMB, transfer · **Context:** Domain user · **Noise:** Moderate

---

**Related:** SMB, Shares & Sessions · NetExec · File Transfer
