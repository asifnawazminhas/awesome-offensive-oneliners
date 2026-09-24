# Nmap

Common Nmap one-liners for service discovery and targeted enumeration.

### Fast top ports

```bash
nmap -sV --top-ports 1000 -T4 <TARGET>
```

**Tool:** Nmap · **Platform:** Linux/macOS/Windows · **Tags:** Ports, Services

### All TCP ports

```bash
nmap -p- --min-rate 2000 -T4 <TARGET>
```

**Tool:** Nmap · **Platform:** Linux/macOS/Windows · **Tags:** TCP, Ports

### Service and scripts

```bash
nmap -sC -sV -p <PORTS> <TARGET>
```

**Tool:** Nmap · **Platform:** Linux/macOS/Windows · **Tags:** Services, NSE

### UDP top ports

```bash
sudo nmap -sU --top-ports 100 -T4 <TARGET>
```

**Tool:** Nmap · **Platform:** Linux/macOS · **Tags:** UDP, Ports

### SMB scripts

```bash
nmap -p445 --script "smb2-*" <TARGET>
```

**Tool:** Nmap · **Platform:** Linux/macOS/Windows · **Tags:** SMB, NSE

### HTTP scripts

```bash
nmap -p80,443 --script "http-title,http-headers,http-methods" <TARGET>
```

**Tool:** Nmap · **Platform:** Linux/macOS/Windows · **Tags:** HTTP, NSE

