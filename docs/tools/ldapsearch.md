# ldapsearch

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

LDAP one-liners for Active Directory enumeration from Linux.

<div class="ol-section-kicker"><span>TOOL</span><strong>5 one-liners</strong></div>

## RootDSE

```bash
ldapsearch -x -H ldap://<DC_IP> -s base -b "" defaultNamingContext namingContexts
```

**Tool:** ldapsearch · **Platform:** Linux · **Tags:** LDAP, AD · **Context:** No auth · **Noise:** Moderate

## Domain users

```bash
ldapsearch -x -H ldap://<DC_IP> -D "<DOMAIN>\<USER>" -w '<PASSWORD>' -b "<BASE_DN>" "(&(objectCategory=person)(objectClass=user))" sAMAccountName
```

**Tool:** ldapsearch · **Platform:** Linux · **Tags:** LDAP, users · **Context:** Domain user · **Noise:** Moderate

## Computers

```bash
ldapsearch -x -H ldap://<DC_IP> -D "<DOMAIN>\<USER>" -w '<PASSWORD>' -b "<BASE_DN>" "(objectCategory=computer)" dNSHostName operatingSystem
```

**Tool:** ldapsearch · **Platform:** Linux · **Tags:** LDAP, computers · **Context:** Domain user · **Noise:** Moderate

## Groups

```bash
ldapsearch -x -H ldap://<DC_IP> -D "<DOMAIN>\<USER>" -w '<PASSWORD>' -b "<BASE_DN>" "(objectClass=group)" cn member
```

**Tool:** ldapsearch · **Platform:** Linux · **Tags:** LDAP, groups · **Context:** Domain user · **Noise:** Moderate

## SPNs

```bash
ldapsearch -x -H ldap://<DC_IP> -D "<DOMAIN>\<USER>" -w '<PASSWORD>' -b "<BASE_DN>" "(servicePrincipalName=*)" sAMAccountName servicePrincipalName
```

**Tool:** ldapsearch · **Platform:** Linux · **Tags:** LDAP, SPN · **Context:** Domain user · **Noise:** Moderate

---

**Related:** LDAP Filters · DNS & SPN Discovery · Password Policy
