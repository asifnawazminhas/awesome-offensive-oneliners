# Injection Testing

Compact automation-oriented commands for common web injection testing.

### SQLMap basic GET test

```bash
sqlmap -u "https://<TARGET>/<PATH>?id=1" --batch --level=2 --risk=1
```

**Tool:** sqlmap · **Platform:** Linux · **Tags:** SQLi, Automation

### Dalfox reflected XSS scan

```bash
dalfox url "https://<TARGET>/<PATH>?q=test" --silence
```

**Tool:** Dalfox · **Platform:** Linux · **Tags:** XSS, Automation

### Nuclei web templates

```bash
nuclei -u https://<TARGET> -severity low,medium,high,critical
```

**Tool:** Nuclei · **Platform:** Linux/macOS · **Tags:** Web, Templates

### ffuf parameter value fuzzing

```bash
ffuf -u "https://<TARGET>/<PATH>?id=FUZZ" -w <WORDLIST> -mc all -fc 404
```

**Tool:** ffuf · **Platform:** Linux/macOS · **Tags:** Fuzzing, Parameters

