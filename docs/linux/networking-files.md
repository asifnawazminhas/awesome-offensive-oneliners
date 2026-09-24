# Linux Networking & Files

File transfer, search and network utility one-liners.

### Serve current directory

```bash
python3 -m http.server 8000
```

**Tool:** Python · **Platform:** Linux/macOS/Windows · **Tags:** HTTP, File Transfer · **Context:** User · **Noise:** Quiet

### Download with curl

```bash
curl -fL http://<HOST>/<FILE> -o <FILE>
```

**Tool:** curl · **Platform:** Linux/macOS · **Tags:** HTTP, Download · **Context:** User · **Noise:** Quiet

### Download with wget

```bash
wget http://<HOST>/<FILE> -O <FILE>
```

**Tool:** wget · **Platform:** Linux · **Tags:** HTTP, Download · **Context:** User · **Noise:** Quiet

### Recursive text search

```bash
grep -Rni --exclude-dir={proc,sys,dev} "<TEXT>" / 2>/dev/null
```

**Tool:** grep · **Platform:** Linux · **Tags:** Search, Files · **Context:** User · **Noise:** Quiet

### Find recently modified files

```bash
find <PATH> -type f -mtime -1 -print 2>/dev/null
```

**Tool:** find · **Platform:** Linux · **Tags:** Files, Timeline · **Context:** User · **Noise:** Quiet

### DNS lookup

```bash
dig +short <HOSTNAME>
```

**Tool:** dig · **Platform:** Linux/macOS · **Tags:** DNS, Recon · **Context:** User · **Noise:** Quiet

---

**Related:** [Overview](./) · [Enumeration](enumeration.md) · [Nfs](nfs.md)
