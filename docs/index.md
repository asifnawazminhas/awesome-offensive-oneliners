<div class="ol-hero" markdown>

<div class="ol-eyebrow">$ one command at a time</div>

# Awesome Offensive OneLiners

A practical collection of copyable one-line commands for penetration testing, Active Directory, red teaming, web security and offensive security operations.

<div class="ol-actions">
<a class="ol-button primary" href="active-directory/">Browse commands</a>
<a class="ol-button" href="https://github.com/asifnawazminhas/awesome-offensive-oneliners" target="_blank" rel="noopener">View on GitHub</a>
</div>

</div>

<div class="ol-stats">
  <div class="ol-stat"><strong>8</strong><span>major sections</span></div>
  <div class="ol-stat"><strong>30+</strong><span>focused pages</span></div>
  <div class="ol-stat"><strong>100+</strong><span>practical commands</span></div>
  <div class="ol-stat"><strong>/</strong><span>press to search</span></div>
</div>

## Jump in

<div class="grid cards" markdown>

-   :material-domain:{ .lg .middle } **Active Directory**

    ---

    Enumeration, Kerberos, delegation, AD CS and BloodHound.

    [:octicons-arrow-right-24: Open section](active-directory/)

-   :material-microsoft-windows:{ .lg .middle } **Windows**

    ---

    Enumeration, application control, services, registry and PowerShell.

    [:octicons-arrow-right-24: Open section](windows/)

-   :material-linux:{ .lg .middle } **Linux**

    ---

    Enumeration, privilege escalation, networking and file operations.

    [:octicons-arrow-right-24: Open section](linux/)

-   :material-web:{ .lg .middle } **Web**

    ---

    Recon, authentication, APIs and injection testing.

    [:octicons-arrow-right-24: Open section](web/)

-   :material-radar:{ .lg .middle } **Recon**

    ---

    DNS, subdomains, HTTP discovery and Nmap.

    [:octicons-arrow-right-24: Open section](recon/)

-   :material-target:{ .lg .middle } **Red Team**

    ---

    Discovery, execution, lateral movement and tunneling.

    [:octicons-arrow-right-24: Open section](red-team/)

-   :material-key:{ .lg .middle } **Credentials**

    ---

    Kerberos, hashes, NTLM and DPAPI.

    [:octicons-arrow-right-24: Open section](credentials/)

-   :material-tools:{ .lg .middle } **Tools**

    ---

    NetExec, Impacket, PowerView, Rubeus, Certipy, BloodHound, curl and jq.

    [:octicons-arrow-right-24: Open section](tools/)

</div>

## Quick examples

### Find constrained delegation

```powershell
Get-DomainComputer -TrustedToAuth -Properties DnsHostName,msDS-AllowedToDelegateTo
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** Kerberos, Delegation, Enumeration

### Discover live web services

```bash
httpx -l hosts.txt -silent -status-code -title -tech-detect
```

**Tool:** httpx · **Platform:** Linux/macOS · **Tags:** Recon, HTTP, Fingerprinting

### Enumerate SMB hosts with NetExec

```bash
nxc smb <CIDR> --gen-relay-list relay.txt
```

**Tool:** NetExec · **Platform:** Linux · **Tags:** SMB, Discovery, Relay

!!! note "Project principle"
    One command. One objective. Minimal noise. Replace placeholders such as `<TARGET>`, `<DOMAIN>`, `<USER>` and `<PASSWORD>` before use.
