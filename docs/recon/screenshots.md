# Web Screenshots

One-liners for visual triage of large HTTP target sets.

<div class="ol-section-kicker"><span>REC</span><strong>5 one-liners</strong></div>

## gowitness file scan

```bash
gowitness scan file -f urls.txt --screenshot-path screenshots
```

**Tool:** gowitness · **Platform:** Linux · **Tags:** Recon, screenshots, HTTP · **Context:** No auth · **Noise:** Moderate

## gowitness CIDR scan

```bash
gowitness scan cidr --cidr <CIDR> --screenshot-path screenshots
```

**Tool:** gowitness · **Platform:** Linux · **Tags:** Recon, screenshots, CIDR · **Context:** No auth · **Noise:** Moderate

## EyeWitness URL list

```bash
python3 EyeWitness.py --web -f urls.txt --no-prompt
```

**Tool:** EyeWitness · **Platform:** Linux · **Tags:** Recon, screenshots, HTTP · **Context:** No auth · **Noise:** Moderate

## aquatone from stdin

```bash
cat hosts.txt | aquatone -out aquatone
```

**Tool:** Aquatone · **Platform:** Linux · **Tags:** Recon, screenshots, HTTP · **Context:** No auth · **Noise:** Moderate

## httpx screenshot

```bash
httpx -l urls.txt -screenshot -screenshot-timeout 10 -silent
```

**Tool:** httpx · **Platform:** Linux · **Tags:** Recon, screenshots, HTTP · **Context:** No auth · **Noise:** Moderate

---

**Related:** HTTP Probing · Technologies · Favicon Hunting
