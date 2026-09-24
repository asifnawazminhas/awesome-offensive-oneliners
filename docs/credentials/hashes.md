# Hash Testing

Common offline password audit one-liners.

### NTLM hashcat

```bash
hashcat -m 1000 <HASHFILE> <WORDLIST>
```

**Tool:** Hashcat · **Platform:** Linux/Windows · **Tags:** NTLM, Cracking · **Context:** User · **Noise:** Moderate

### NetNTLMv2 hashcat

```bash
hashcat -m 5600 <HASHFILE> <WORDLIST>
```

**Tool:** Hashcat · **Platform:** Linux/Windows · **Tags:** NetNTLMv2, Cracking · **Context:** User · **Noise:** Moderate

### SHA-256 hashcat

```bash
hashcat -m 1400 <HASHFILE> <WORDLIST>
```

**Tool:** Hashcat · **Platform:** Linux/Windows · **Tags:** SHA256, Cracking · **Context:** User · **Noise:** Moderate

### John auto-detect

```bash
john <HASHFILE> --wordlist=<WORDLIST>
```

**Tool:** John the Ripper · **Platform:** Linux/macOS · **Tags:** Hashes, Cracking · **Context:** User · **Noise:** Moderate

### Show cracked John results

```bash
john <HASHFILE> --show
```

**Tool:** John the Ripper · **Platform:** Linux/macOS · **Tags:** Hashes, Results · **Context:** User · **Noise:** Moderate

---

**Related:** [Overview](./) · [Kerberos](kerberos.md)
