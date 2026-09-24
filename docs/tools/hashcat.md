# Hashcat

Hashcat one-liners for common hashes encountered during authorized assessments.

<div class="ol-section-kicker"><span>TOOL</span><strong>6 one-liners</strong></div>

## NTLM

```bash
hashcat -m 1000 hashes.txt <WORDLIST>
```

**Tool:** Hashcat · **Platform:** Any · **Tags:** hash cracking, NTLM · **Context:** User

## NetNTLMv2

```bash
hashcat -m 5600 hashes.txt <WORDLIST>
```

**Tool:** Hashcat · **Platform:** Any · **Tags:** hash cracking, NetNTLMv2 · **Context:** User

## Kerberos TGS etype 23

```bash
hashcat -m 13100 hashes.txt <WORDLIST>
```

**Tool:** Hashcat · **Platform:** Any · **Tags:** hash cracking, Kerberos · **Context:** User

## AS-REP etype 23

```bash
hashcat -m 18200 hashes.txt <WORDLIST>
```

**Tool:** Hashcat · **Platform:** Any · **Tags:** hash cracking, Kerberos · **Context:** User

## Show cracked

```bash
hashcat -m <MODE> hashes.txt --show
```

**Tool:** Hashcat · **Platform:** Any · **Tags:** hash cracking · **Context:** User

## Rule attack

```bash
hashcat -m <MODE> hashes.txt <WORDLIST> -r <RULE_FILE>
```

**Tool:** Hashcat · **Platform:** Any · **Tags:** hash cracking, rules · **Context:** User

---

**Related:** Hashes · Kerberos · John
