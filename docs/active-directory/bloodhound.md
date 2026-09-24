# BloodHound collection

Collect graph data quickly from Linux or Windows.

<div class="ol-section-kicker"><span>AD</span></div>

## BloodHound.py collection

```bash
bloodhound-python -u <USER> -p '<PASSWORD>' -d <DOMAIN> -ns <DC_IP> -c All
```

**Tool:** bloodhound-python · **Platform:** Linux/macOS · **Context:** Domain user


## BloodHound.py DC-only collection

```bash
bloodhound-python -u <USER> -p '<PASSWORD>' -d <DOMAIN> -ns <DC_IP> -c DCOnly
```

**Tool:** bloodhound-python · **Platform:** Linux/macOS · **Context:** Domain user


## SharpHound all collection

```cmd
SharpHound.exe -c All --zipfilename bloodhound.zip
```

**Tool:** SharpHound · **Platform:** Windows · **Context:** Domain user


## SharpHound domain-controller only

```cmd
SharpHound.exe -c DCOnly --zipfilename dconly.zip
```

**Tool:** SharpHound · **Platform:** Windows · **Context:** Domain user


## SharpHound loop collection

```cmd
SharpHound.exe -c Session --Loop --LoopDuration 00:30:00 --LoopInterval 00:01:00
```

**Tool:** SharpHound · **Platform:** Windows · **Context:** Domain user

---

**Related:** [Overview](./) · [Ad Cs](adcs.md) · [Computers Dcs](computers-dcs.md)
