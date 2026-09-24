# John the Ripper

<div class="ol-version-note">Syntax can drift between releases. Confirm with the tool's local <code>--version</code> and <code>--help</code> output.</div>

John one-liners for identifying, cracking and displaying common password hashes.

<div class="ol-section-kicker"><span>TOOL</span><strong>6 one-liners</strong></div>

## Auto-format crack

```bash
john hashes.txt --wordlist=<WORDLIST>
```

**Tool:** John · **Platform:** Any · **Tags:** hash cracking · **Context:** User · **Noise:** Quiet

## Show cracked

```bash
john hashes.txt --show
```

**Tool:** John · **Platform:** Any · **Tags:** hash cracking · **Context:** User · **Noise:** Quiet

## List formats

```bash
john --list=formats
```

**Tool:** John · **Platform:** Any · **Tags:** hash cracking, formats · **Context:** User · **Noise:** Quiet

## NT hash format

```bash
john hashes.txt --format=NT --wordlist=<WORDLIST>
```

**Tool:** John · **Platform:** Any · **Tags:** hash cracking, NTLM · **Context:** User · **Noise:** Quiet

## SSH key conversion

```bash
ssh2john <KEY_FILE> > ssh.hash && john ssh.hash --wordlist=<WORDLIST>
```

**Tool:** ssh2john,John · **Platform:** Any · **Tags:** SSH, hash cracking · **Context:** User · **Noise:** Quiet

## ZIP conversion

```bash
zip2john <ARCHIVE.zip> > zip.hash && john zip.hash --wordlist=<WORDLIST>
```

**Tool:** zip2john,John · **Platform:** Any · **Tags:** ZIP, hash cracking · **Context:** User · **Noise:** Quiet

---

**Related:** Hashes · Hashcat · Credentials
