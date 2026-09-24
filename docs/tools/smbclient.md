# smbclient

smbclient one-liners for share enumeration and file operations.

<div class="ol-section-kicker"><span>TOOL</span><strong>5 one-liners</strong></div>

## Anonymous share list

```bash
smbclient -L //<TARGET> -N
```

**Tool:** smbclient · **Platform:** Linux · **Tags:** SMB, shares · **Context:** No auth

## Authenticated share list

```bash
smbclient -L //<TARGET> -U '<DOMAIN>/<USER>%<PASSWORD>'
```

**Tool:** smbclient · **Platform:** Linux · **Tags:** SMB, shares · **Context:** Domain user

## Connect to share

```bash
smbclient //<TARGET>/<SHARE> -U '<DOMAIN>/<USER>%<PASSWORD>'
```

**Tool:** smbclient · **Platform:** Linux · **Tags:** SMB, share · **Context:** Domain user

## Recursive list

```bash
smbclient //<TARGET>/<SHARE> -U '<DOMAIN>/<USER>%<PASSWORD>' -c 'recurse;ls'
```

**Tool:** smbclient · **Platform:** Linux · **Tags:** SMB, files · **Context:** Domain user

## Download file

```bash
smbclient //<TARGET>/<SHARE> -U '<DOMAIN>/<USER>%<PASSWORD>' -c 'get <REMOTE_FILE> <LOCAL_FILE>'
```

**Tool:** smbclient · **Platform:** Linux · **Tags:** SMB, transfer · **Context:** Domain user

---

**Related:** SMB, Shares & Sessions · NetExec · File Transfer
