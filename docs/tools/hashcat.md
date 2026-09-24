# Hashcat

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

Hashcat one-liners for common hashes encountered during authorized assessments.

<div class="ol-section-kicker"><span>TOOL</span><strong>6 one-liners</strong></div>

## NTLM

```bash
hashcat -m 1000 hashes.txt <WORDLIST>
```

**Tool:** Hashcat · **Platform:** Any · **Tags:** hash cracking, NTLM · **Context:** User · **Noise:** Quiet

## NetNTLMv2

```bash
hashcat -m 5600 hashes.txt <WORDLIST>
```

**Tool:** Hashcat · **Platform:** Any · **Tags:** hash cracking, NetNTLMv2 · **Context:** User · **Noise:** Quiet

## Kerberos TGS etype 23

```bash
hashcat -m 13100 hashes.txt <WORDLIST>
```

**Tool:** Hashcat · **Platform:** Any · **Tags:** hash cracking, Kerberos · **Context:** User · **Noise:** Quiet

## AS-REP etype 23

```bash
hashcat -m 18200 hashes.txt <WORDLIST>
```

**Tool:** Hashcat · **Platform:** Any · **Tags:** hash cracking, Kerberos · **Context:** User · **Noise:** Quiet

## Show cracked

```bash
hashcat -m <MODE> hashes.txt --show
```

**Tool:** Hashcat · **Platform:** Any · **Tags:** hash cracking · **Context:** User · **Noise:** Quiet

## Rule attack

```bash
hashcat -m <MODE> hashes.txt <WORDLIST> -r <RULE_FILE>
```

**Tool:** Hashcat · **Platform:** Any · **Tags:** hash cracking, rules · **Context:** User · **Noise:** Quiet

---

**Related:** Hashes · Kerberos · John
