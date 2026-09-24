# Reverse DNS

One-liners for PTR enumeration and reverse-DNS enrichment.

<div class="ol-section-kicker"><span>REC</span><strong>5 one-liners</strong></div>

## Single PTR lookup

```bash
dig -x <IP> +short
```

**Tool:** dig · **Platform:** Any · **Tags:** Recon, DNS, PTR · **Context:** No auth · **Noise:** Quiet

## Host reverse lookup

```bash
host <IP>
```

**Tool:** host · **Platform:** Any · **Tags:** Recon, DNS, PTR · **Context:** No auth · **Noise:** Quiet

## dnsx PTR list

```bash
dnsx -l ips.txt -ptr -resp-only -silent
```

**Tool:** dnsx · **Platform:** Linux · **Tags:** Recon, DNS, PTR · **Context:** No auth · **Noise:** Quiet

## Parallel PTR with xargs

```bash
cat ips.txt | xargs -I{} -P50 sh -c 'printf "{} "; dig -x {} +short'
```

**Tool:** dig,xargs · **Platform:** Linux · **Tags:** Recon, DNS, PTR · **Context:** No auth · **Noise:** Quiet

## Nmap reverse DNS sweep

```bash
nmap -sL <CIDR> | grep "Nmap scan report"
```

**Tool:** Nmap · **Platform:** Linux · **Tags:** Recon, DNS, PTR · **Context:** No auth · **Noise:** Quiet

---

**Related:** ASN & CIDR · DNS Resolution · Ports & Services
