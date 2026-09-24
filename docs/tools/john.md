# John the Ripper

John one-liners for identifying, cracking and displaying common password hashes.

<div class="ol-section-kicker"><span>TOOL</span><strong>6 one-liners</strong></div>

## Auto-format crack

```bash
john hashes.txt --wordlist=<WORDLIST>
```

**Tool:** John · **Platform:** Any · **Tags:** hash cracking · **Context:** User

## Show cracked

```bash
john hashes.txt --show
```

**Tool:** John · **Platform:** Any · **Tags:** hash cracking · **Context:** User

## List formats

```bash
john --list=formats
```

**Tool:** John · **Platform:** Any · **Tags:** hash cracking, formats · **Context:** User

## NT hash format

```bash
john hashes.txt --format=NT --wordlist=<WORDLIST>
```

**Tool:** John · **Platform:** Any · **Tags:** hash cracking, NTLM · **Context:** User

## SSH key conversion

```bash
ssh2john <KEY_FILE> > ssh.hash && john ssh.hash --wordlist=<WORDLIST>
```

**Tool:** ssh2john,John · **Platform:** Any · **Tags:** SSH, hash cracking · **Context:** User

## ZIP conversion

```bash
zip2john <ARCHIVE.zip> > zip.hash && john zip.hash --wordlist=<WORDLIST>
```

**Tool:** zip2john,John · **Platform:** Any · **Tags:** ZIP, hash cracking · **Context:** User

---

**Related:** Hashes · Hashcat · Credentials
