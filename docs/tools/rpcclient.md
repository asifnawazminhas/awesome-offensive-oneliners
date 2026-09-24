# rpcclient

<div class="ol-section-kicker"><span>TOOL</span><strong>RPCCLIENT</strong></div>

## Anonymous connection
```bash
rpcclient -U '' -N //<TARGET>
```
**Tool:** rpcclient · **Platform:** Linux · **Tags:** SMB, RPC · **Context:** No auth

## Authenticated connection
```bash
rpcclient -U '<DOMAIN>/<USER>%<PASSWORD>' //<TARGET>
```
**Tool:** rpcclient · **Platform:** Linux · **Tags:** RPC, Authentication · **Context:** Domain user

## Enumerate domain users
```bash
rpcclient -U '<DOMAIN>/<USER>%<PASSWORD>' //<TARGET> -c 'enumdomusers'
```
**Tool:** rpcclient · **Platform:** Linux · **Tags:** Users, RPC · **Context:** Domain user

## Enumerate domain groups
```bash
rpcclient -U '<DOMAIN>/<USER>%<PASSWORD>' //<TARGET> -c 'enumdomgroups'
```
**Tool:** rpcclient · **Platform:** Linux · **Tags:** Groups, RPC · **Context:** Domain user

## Query domain info
```bash
rpcclient -U '<DOMAIN>/<USER>%<PASSWORD>' //<TARGET> -c 'querydominfo'
```
**Tool:** rpcclient · **Platform:** Linux · **Tags:** Domain, RPC · **Context:** Domain user
