# LDAP Filters

Useful LDAP one-liners for targeted Active Directory searches.

<div class="ol-section-kicker"><span>AD</span><strong>6 one-liners</strong></div>

## Disabled users

```bash
ldapsearch -x -H ldap://<DC_IP> -D "<DOMAIN>\<USER>" -w '<PASSWORD>' -b "<BASE_DN>" "(&(objectCategory=person)(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=2))" sAMAccountName
```

**Tool:** ldapsearch · **Platform:** Linux · **Tags:** AD, LDAP, users · **Context:** Domain user

## Users without pre-auth

```bash
ldapsearch -x -H ldap://<DC_IP> -D "<DOMAIN>\<USER>" -w '<PASSWORD>' -b "<BASE_DN>" "(&(objectCategory=person)(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=4194304))" sAMAccountName
```

**Tool:** ldapsearch · **Platform:** Linux · **Tags:** AD, LDAP, AS-REP · **Context:** Domain user

## Trusted-for-delegation computers

```bash
ldapsearch -x -H ldap://<DC_IP> -D "<DOMAIN>\<USER>" -w '<PASSWORD>' -b "<BASE_DN>" "(&(objectCategory=computer)(userAccountControl:1.2.840.113556.1.4.803:=524288))" dNSHostName
```

**Tool:** ldapsearch · **Platform:** Linux · **Tags:** AD, LDAP, delegation · **Context:** Domain user

## SPN users

```bash
ldapsearch -x -H ldap://<DC_IP> -D "<DOMAIN>\<USER>" -w '<PASSWORD>' -b "<BASE_DN>" "(&(objectCategory=person)(objectClass=user)(servicePrincipalName=*))" sAMAccountName servicePrincipalName
```

**Tool:** ldapsearch · **Platform:** Linux · **Tags:** AD, LDAP, SPN · **Context:** Domain user

## Domain admins by group DN

```bash
ldapsearch -x -H ldap://<DC_IP> -D "<DOMAIN>\<USER>" -w '<PASSWORD>' -b "<BASE_DN>" "(memberOf=CN=Domain Admins,CN=Users,<BASE_DN>)" sAMAccountName
```

**Tool:** ldapsearch · **Platform:** Linux · **Tags:** AD, LDAP, groups · **Context:** Domain user

## Computers by OS

```bash
ldapsearch -x -H ldap://<DC_IP> -D "<DOMAIN>\<USER>" -w '<PASSWORD>' -b "<BASE_DN>" "(&(objectCategory=computer)(operatingSystem=*Server*))" dNSHostName operatingSystem
```

**Tool:** ldapsearch · **Platform:** Linux · **Tags:** AD, LDAP, computers · **Context:** Domain user

---

**Related:** DNS & SPN Discovery · Password Policy · Tools: ldapsearch
