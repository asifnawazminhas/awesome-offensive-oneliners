# BloodHound

Collection one-liners for BloodHound-oriented analysis.

### Collect default BloodHound data

```bash
bloodhound-python -u <USER> -p <PASSWORD> -d <DOMAIN> -ns <DC_IP> -c All
```

**Tool:** bloodhound-python · **Platform:** Linux · **Tags:** BloodHound, Collection

### Collect with SharpHound

```powershell
SharpHound.exe -c All --zipfilename bloodhound.zip
```

**Tool:** SharpHound · **Platform:** Windows · **Tags:** BloodHound, Collection

### Collect DC-only data

```powershell
SharpHound.exe -c DCOnly --zipfilename dconly.zip
```

**Tool:** SharpHound · **Platform:** Windows · **Tags:** BloodHound, Collection

### BloodHound CE collector

```bash
bloodhound-ce-python -u <USER> -p <PASSWORD> -d <DOMAIN> -ns <DC_IP> -c All
```

**Tool:** BloodHound CE Python · **Platform:** Linux · **Tags:** BloodHound, Collection

