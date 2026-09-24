# DNS & SPN Discovery

DNS, SRV and SPN one-liners for quickly mapping Active Directory services.

<div class="ol-section-kicker"><span>AD</span><strong>8 one-liners</strong></div>

## Locate LDAP domain controllers

```bash
dig +short SRV _ldap._tcp.dc._msdcs.<DOMAIN>
```

**Tool:** dig · **Platform:** Linux/macOS · **Tags:** AD, DNS, DC discovery · **Context:** No auth · **Noise:** Quiet

## Locate Kerberos services

```bash
dig +short SRV _kerberos._tcp.<DOMAIN>
```

**Tool:** dig · **Platform:** Linux/macOS · **Tags:** AD, DNS, Kerberos · **Context:** No auth · **Noise:** Quiet

## Resolve DCs with nslookup

```powershell
nslookup -type=SRV _ldap._tcp.dc._msdcs.<DOMAIN>
```

**Tool:** nslookup · **Platform:** Windows · **Tags:** AD, DNS, DC discovery · **Context:** No auth · **Noise:** Quiet

## Query all SPNs with setspn

```powershell
setspn -Q */*
```

**Tool:** setspn · **Platform:** Windows · **Tags:** AD, SPN, Kerberos · **Context:** Domain user · **Noise:** Quiet

## Find user SPNs with PowerView

```powershell
Get-DomainUser -SPN | Select-Object samaccountname,serviceprincipalname
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, SPN, Kerberoasting · **Context:** Domain user · **Noise:** Quiet

## Find computer SPNs with PowerView

```powershell
Get-DomainComputer -Properties dNSHostName,servicePrincipalName | Select-Object dNSHostName,servicePrincipalName
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, SPN, computers · **Context:** Domain user · **Noise:** Quiet

## Query SPNs over LDAP

```bash
ldapsearch -x -H ldap://<DC_IP> -D "<DOMAIN>\<USER>" -w '<PASSWORD>' -b "<BASE_DN>" "(servicePrincipalName=*)" sAMAccountName servicePrincipalName
```

**Tool:** ldapsearch · **Platform:** Linux · **Tags:** AD, LDAP, SPN · **Context:** Domain user · **Noise:** Quiet

## Enumerate SPNs with NetExec

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --query "(servicePrincipalName=*)" "sAMAccountName servicePrincipalName"
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** AD, LDAP, SPN · **Context:** Domain user · **Noise:** Quiet

---

**Related:** Kerberos · Domain Discovery · LDAP Filters
