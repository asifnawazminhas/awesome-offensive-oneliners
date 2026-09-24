# Delegation

<span class="ol-search-aliases">kcd constrained delegation unconstrained delegation TrustedToAuth msDS-AllowedToDelegateTo kerberos delegation</span>

Find unconstrained, constrained and resource-based delegation configuration.

<div class="ol-section-kicker"><span>AD</span></div>

## PowerView unconstrained computers

```powershell
Get-DomainComputer -Unconstrained | Select dnshostname,useraccountcontrol
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user · **Noise:** Moderate


## PowerView constrained delegation

```powershell
Get-DomainComputer -TrustedToAuth -Properties DnsHostName,msDS-AllowedToDelegateTo
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user · **Noise:** Moderate


## PowerView user constrained delegation

```powershell
Get-DomainUser -TrustedToAuth -Properties samaccountname,msDS-AllowedToDelegateTo
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user · **Noise:** Moderate


## PowerView RBCD targets

```powershell
Get-DomainComputer -LDAPFilter '(msDS-AllowedToActOnBehalfOfOtherIdentity=*)' -Properties dnshostname,msDS-AllowedToActOnBehalfOfOtherIdentity
```

**Tool:** PowerView · **Platform:** Windows · **Context:** Domain user · **Noise:** Moderate


## NetExec trusted-for-delegation

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --trusted-for-delegation
```

**Tool:** NetExec · **Platform:** Linux/macOS · **Context:** Domain user · **Noise:** Moderate


## LDAP constrained-delegation query

```bash
ldapsearch -x -H ldap://<DC_IP> -D '<USER>@<DOMAIN>' -w '<PASSWORD>' -b '<BASE_DN>' '(msDS-AllowedToDelegateTo=*)' sAMAccountName msDS-AllowedToDelegateTo
```

**Tool:** ldapsearch · **Platform:** Linux/macOS · **Context:** No auth · **Noise:** Moderate

---

**Related:** [Overview](./) · [Computers Dcs](computers-dcs.md) · [Dns Spn](dns-spn.md)
