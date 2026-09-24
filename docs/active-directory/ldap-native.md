# LDAP and native fallbacks

Useful fallbacks when PowerView or NetExec are unavailable.

<div class="ol-section-kicker"><span>AD</span></div>

## ldapsearch users

```bash
ldapsearch -x -H ldap://<DC_IP> -D '<USER>@<DOMAIN>' -w '<PASSWORD>' -b '<BASE_DN>' '(objectClass=user)' sAMAccountName
```

**Tool:** ldapsearch · **Platform:** Linux/macOS · **Context:** No auth


## ldapsearch computers

```bash
ldapsearch -x -H ldap://<DC_IP> -D '<USER>@<DOMAIN>' -w '<PASSWORD>' -b '<BASE_DN>' '(objectClass=computer)' dNSHostName operatingSystem
```

**Tool:** ldapsearch · **Platform:** Linux/macOS · **Context:** No auth


## rpcclient domain users

```bash
rpcclient -U '<DOMAIN>/<USER>%<PASSWORD>' <DC_IP> -c enumdomusers
```

**Tool:** rpcclient · **Platform:** Linux/macOS · **Context:** Domain user


## rpcclient domain groups

```bash
rpcclient -U '<DOMAIN>/<USER>%<PASSWORD>' <DC_IP> -c enumdomgroups
```

**Tool:** rpcclient · **Platform:** Linux/macOS · **Context:** Domain user


## enum4linux-ng

```bash
enum4linux-ng -A -u <USER> -p '<PASSWORD>' <DC_IP>
```

**Tool:** enum4linux-ng · **Platform:** Linux/macOS · **Context:** Domain user

---

**Related:** [Overview](./) · [Ldap Filters](ldap-filters.md) · [Local Admins](local-admins.md)
