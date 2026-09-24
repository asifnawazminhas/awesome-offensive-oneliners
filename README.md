# Awesome Offensive OneLiners

A practical collection of copyable one-line commands for penetration testing, Active Directory, web security, reconnaissance and offensive security operations.

**Website:** https://oneliners.asifnawazminhas.com/

The project stays intentionally scan-first: one command, one objective, brief context only where it helps you use the one-liner correctly.

## Local development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

## Build

```bash
mkdocs build --strict
```

See `docs/contributing.md` for contributions and `docs/conventions.md` for placeholder conventions.


## Deep red-team one-liners

The Red Team section also includes focused pages for download cradles, LOLBin/local execution, reverse shells, staging paths and SMB file transfer. Entries stay scan-first and copyable, with only short operational notes where useful.

## Coverage highlights

- Active Directory with NetExec, PowerView, Impacket, Kerberos, delegation, ACLs, AD CS and BloodHound.
- Recon with Subfinder, Amass, crt.sh, PureDNS, DNS resolution, HTTP probing, Shodan and pipelines.
- Web with dedicated VHost discovery, content discovery, parameter discovery/fuzzing, technology hunting and common web attack surfaces.
- Windows and Linux local enumeration, application-control checks, privilege-escalation checks and red-team execution/transfer references.

The website contains 360+ scan-first one-liners across 70+ focused pages.
