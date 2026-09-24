# Hash Testing

Common offline password audit one-liners.

### NTLM hashcat

```bash
hashcat -m 1000 <HASHFILE> <WORDLIST>
```

**Tool:** Hashcat · **Platform:** Linux/Windows · **Tags:** NTLM, Cracking · **Context:** User

### NetNTLMv2 hashcat

```bash
hashcat -m 5600 <HASHFILE> <WORDLIST>
```

**Tool:** Hashcat · **Platform:** Linux/Windows · **Tags:** NetNTLMv2, Cracking · **Context:** User

### SHA-256 hashcat

```bash
hashcat -m 1400 <HASHFILE> <WORDLIST>
```

**Tool:** Hashcat · **Platform:** Linux/Windows · **Tags:** SHA256, Cracking · **Context:** User

### John auto-detect

```bash
john <HASHFILE> --wordlist=<WORDLIST>
```

**Tool:** John the Ripper · **Platform:** Linux/macOS · **Tags:** Hashes, Cracking · **Context:** User

### Show cracked John results

```bash
john <HASHFILE> --show
```

**Tool:** John the Ripper · **Platform:** Linux/macOS · **Tags:** Hashes, Results · **Context:** User

---

**Related:** [Overview](./) · [Kerberos](kerberos.md)
