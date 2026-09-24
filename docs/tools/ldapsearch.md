# ldapsearch

LDAP one-liners for Active Directory enumeration from Linux.

<div class="ol-section-kicker"><span>TOOL</span><strong>5 one-liners</strong></div>

## RootDSE

```bash
ldapsearch -x -H ldap://<DC_IP> -s base -b "" defaultNamingContext namingContexts
```

**Tool:** ldapsearch · **Platform:** Linux · **Tags:** LDAP, AD · **Context:** No auth

## Domain users

```bash
ldapsearch -x -H ldap://<DC_IP> -D "<DOMAIN>\<USER>" -w '<PASSWORD>' -b "<BASE_DN>" "(&(objectCategory=person)(objectClass=user))" sAMAccountName
```

**Tool:** ldapsearch · **Platform:** Linux · **Tags:** LDAP, users · **Context:** Domain user

## Computers

```bash
ldapsearch -x -H ldap://<DC_IP> -D "<DOMAIN>\<USER>" -w '<PASSWORD>' -b "<BASE_DN>" "(objectCategory=computer)" dNSHostName operatingSystem
```

**Tool:** ldapsearch · **Platform:** Linux · **Tags:** LDAP, computers · **Context:** Domain user

## Groups

```bash
ldapsearch -x -H ldap://<DC_IP> -D "<DOMAIN>\<USER>" -w '<PASSWORD>' -b "<BASE_DN>" "(objectClass=group)" cn member
```

**Tool:** ldapsearch · **Platform:** Linux · **Tags:** LDAP, groups · **Context:** Domain user

## SPNs

```bash
ldapsearch -x -H ldap://<DC_IP> -D "<DOMAIN>\<USER>" -w '<PASSWORD>' -b "<BASE_DN>" "(servicePrincipalName=*)" sAMAccountName servicePrincipalName
```

**Tool:** ldapsearch · **Platform:** Linux · **Tags:** LDAP, SPN · **Context:** Domain user

---

**Related:** LDAP Filters · DNS & SPN Discovery · Password Policy
