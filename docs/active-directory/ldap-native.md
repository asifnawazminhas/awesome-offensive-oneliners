# LDAP and native fallbacks

Useful fallbacks when PowerView or NetExec are unavailable.

<div class="ol-section-kicker"><span>AD</span></div>

## ldapsearch users

```bash
ldapsearch -x -H ldap://<DC_IP> -D '<USER>@<DOMAIN>' -w '<PASSWORD>' -b '<BASE_DN>' '(objectClass=user)' sAMAccountName
```

**Tool:** ldapsearch · **Platform:** Linux/macOS


## ldapsearch computers

```bash
ldapsearch -x -H ldap://<DC_IP> -D '<USER>@<DOMAIN>' -w '<PASSWORD>' -b '<BASE_DN>' '(objectClass=computer)' dNSHostName operatingSystem
```

**Tool:** ldapsearch · **Platform:** Linux/macOS


## rpcclient domain users

```bash
rpcclient -U '<DOMAIN>/<USER>%<PASSWORD>' <DC_IP> -c enumdomusers
```

**Tool:** rpcclient · **Platform:** Linux/macOS


## rpcclient domain groups

```bash
rpcclient -U '<DOMAIN>/<USER>%<PASSWORD>' <DC_IP> -c enumdomgroups
```

**Tool:** rpcclient · **Platform:** Linux/macOS


## enum4linux-ng

```bash
enum4linux-ng -A -u <USER> -p '<PASSWORD>' <DC_IP>
```

**Tool:** enum4linux-ng · **Platform:** Linux/macOS
