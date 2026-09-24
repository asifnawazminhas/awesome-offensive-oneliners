# Awesome Offensive OneLiners

A practical collection of one-line commands for penetration testing, Active Directory, red teaming, web security and offensive security operations.

<div class="grid cards" markdown>

-   :material-microsoft-windows:{ .lg .middle } **Active Directory**

    ---

    Enumeration, Kerberos, delegation, AD CS, lateral movement and domain operations.

-   :material-powershell:{ .lg .middle } **Windows**

    ---

    PowerShell, services, registry, Defender, AppLocker, WDAC and privilege escalation.

-   :material-linux:{ .lg .middle } **Linux**

    ---

    Enumeration, networking, files, processes and privilege escalation.

-   :material-web:{ .lg .middle } **Web**

    ---

    Reconnaissance, HTTP testing, APIs, authentication and common web vulnerabilities.

-   :material-radar:{ .lg .middle } **Recon**

    ---

    DNS, subdomains, ports, services, content discovery and OSINT.

-   :material-target:{ .lg .middle } **Red Team**

    ---

    Discovery, execution, persistence, credential access, lateral movement and C2 operations.

-   :material-key:{ .lg .middle } **Credentials**

    ---

    Kerberos, NTLM, hashes, password cracking, DPAPI and credential testing.

-   :material-tools:{ .lg .middle } **Tools**

    ---

    Nmap, NetExec, Impacket, PowerView, Rubeus, Certipy, BloodHound and more.

</div>

## Quick example

### Find constrained delegation

```powershell
Get-DomainComputer -TrustedToAuth -Properties DnsHostName,msDS-AllowedToDelegateTo
```

**Tool:** PowerView  
**Platform:** Windows  
**Category:** Active Directory  
**Tags:** Kerberos, Delegation, Enumeration

## Project goal

The goal of Awesome Offensive OneLiners is simple:

> One command. One objective. Minimal noise.

The project focuses on commands that are useful during authorised penetration testing, red team exercises, labs and security research.

## Repository

The source code and content are maintained in:

[awesome-offensive-oneliners](https://github.com/asifnawazminhas/awesome-offensive-oneliners){ target="_blank" rel="noopener" }
