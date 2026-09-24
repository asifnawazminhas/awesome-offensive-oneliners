---
hide:
  - toc
---
# AD DNS Deep Discovery

Fast DNS and directory-backed discovery for Active Directory.

<div class="ol-section-kicker"><span>AD</span><strong>DNS</strong></div>

## Enumerate AD SRV records
```bash
dig +short SRV _ldap._tcp.dc._msdcs.<DOMAIN>
```
**Tool:** dig · **Platform:** Linux/macOS · **Tags:** DNS, SRV, DC · **Context:** No auth · **Noise:** Quiet

## Kerberos SRV records
```bash
dig +short SRV _kerberos._tcp.<DOMAIN>
```
**Tool:** dig · **Platform:** Linux/macOS · **Tags:** DNS, Kerberos · **Context:** No auth · **Noise:** Quiet

## Global Catalog SRV records
```bash
dig +short SRV _ldap._tcp.gc._msdcs.<DOMAIN>
```
**Tool:** dig · **Platform:** Linux/macOS · **Tags:** DNS, Global Catalog · **Context:** No auth · **Noise:** Quiet

## DNS zone via PowerView
```powershell
Get-DomainDNSZone
```
**Tool:** PowerView · **Platform:** Windows · **Tags:** DNS, AD · **Context:** Domain user · **Noise:** Quiet

## DNS records via PowerView
```powershell
Get-DomainDNSRecord -ZoneName <DOMAIN>
```
**Tool:** PowerView · **Platform:** Windows · **Tags:** DNS, Records · **Context:** Domain user · **Noise:** Quiet

## AD-integrated DNS nodes via LDAP
```bash
ldapsearch -x -H ldap://<DC_IP> -D '<DOMAIN>\\<USER>' -w '<PASSWORD>' -b 'DC=DomainDnsZones,DC=<DOMAIN_PART>,DC=<TLD>' '(objectClass=dnsNode)' name
```
**Tool:** ldapsearch · **Platform:** Linux · **Tags:** LDAP, DNS, AD-integrated DNS · **Context:** Domain user · **Noise:** Quiet

## DNS A records with dnsx
```bash
printf '%s\n' <DOMAIN> | dnsx -silent -a -resp
```
**Tool:** dnsx · **Platform:** Linux/macOS · **Tags:** DNS, A Record · **Context:** No auth · **Noise:** Quiet

## DNS CNAME records with dnsx
```bash
dnsx -l hosts.txt -silent -cname -resp
```
**Tool:** dnsx · **Platform:** Linux/macOS · **Tags:** DNS, CNAME · **Context:** No auth · **Noise:** Quiet

**Related:** [DNS & SPN Discovery](dns-spn.md) · [Domain Discovery](domain-discovery.md) · [LDAP Filters](ldap-filters.md)
