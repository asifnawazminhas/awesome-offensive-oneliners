---
hide:
  - navigation
  - toc
---

<div class="ol-hero" markdown>

<div class="ol-eyebrow">$ one command at a time</div>

# Awesome Offensive OneLiners

A practical collection of copyable one-line commands for penetration testing, Active Directory, red teaming, web security and offensive security operations.

<div class="ol-search-launch" role="button" tabindex="0" aria-label="Open site search">
  <span class="ol-search-icon">⌕</span>
  <span class="ol-search-placeholder">Search commands, tools, techniques...</span>
  <kbd>/</kbd>
</div>

<div class="ol-actions">
<a class="ol-button primary" href="active-directory/">Browse commands</a>
<a class="ol-button" href="https://github.com/asifnawazminhas/awesome-offensive-oneliners" target="_blank" rel="noopener">View on GitHub</a>
</div>

</div>

<div class="ol-stats">
  <div class="ol-stat"><strong>183</strong><span>commands</span></div>
  <div class="ol-stat"><strong>31</strong><span>focused pages</span></div>
  <div class="ol-stat"><strong>8</strong><span>major sections</span></div>
  <div class="ol-stat"><strong>/</strong><span>instant search</span></div>
</div>

## Explore the library

<div class="grid cards ol-library-grid" markdown>

-   :material-domain:{ .lg .middle } **Active Directory** · `32 commands`

    ---

    Domain enumeration, Kerberos, delegation, AD CS and graph-based analysis.

    [:octicons-arrow-right-24: Browse Active Directory](active-directory/)

-   :material-microsoft-windows:{ .lg .middle } **Windows** · `26 commands`

    ---

    Host discovery, application control checks, services, registry and PowerShell.

    [:octicons-arrow-right-24: Browse Windows](windows/)

-   :material-linux:{ .lg .middle } **Linux** · `20 commands`

    ---

    Host enumeration, privilege escalation checks, networking and file operations.

    [:octicons-arrow-right-24: Browse Linux](linux/)

-   :material-web:{ .lg .middle } **Web** · `21 commands`

    ---

    Web reconnaissance, authentication checks, API testing and injection workflows.

    [:octicons-arrow-right-24: Browse Web](web/)

-   :material-radar:{ .lg .middle } **Recon** · `17 commands`

    ---

    DNS, subdomains, HTTP services, content discovery and Nmap.

    [:octicons-arrow-right-24: Browse Recon](recon/)

-   :material-target:{ .lg .middle } **Red Team** · `22 commands`

    ---

    Discovery, execution, lateral movement and tunneling for authorised environments.

    [:octicons-arrow-right-24: Browse Red Team](red-team/)

-   :material-key:{ .lg .middle } **Credentials** · `14 commands`

    ---

    Kerberos, hashes, NTLM and DPAPI-oriented testing.

    [:octicons-arrow-right-24: Browse Credentials](credentials/)

-   :material-tools:{ .lg .middle } **Tools** · `31 commands`

    ---

    NetExec, Impacket, PowerView, Rubeus, Certipy, BloodHound, curl and jq.

    [:octicons-arrow-right-24: Browse Tools](tools/)

</div>

## Quick launch

<div class="grid cards ol-quick-grid" markdown>

-   **Find constrained delegation**

    ```powershell
    Get-DomainComputer -TrustedToAuth -Properties DnsHostName,msDS-AllowedToDelegateTo
    ```

    `PowerView` · `Windows` · `Kerberos`

-   **Discover live web services**

    ```bash
    httpx -l hosts.txt -silent -status-code -title -tech-detect
    ```

    `httpx` · `Linux/macOS` · `Recon`

</div>

<div class="ol-principle">
  <span class="ol-prompt">$_</span>
  <div><strong>One command. One objective. Minimal noise.</strong><br><span>Replace placeholders such as &lt;TARGET&gt;, &lt;DOMAIN&gt;, &lt;USER&gt; and &lt;PASSWORD&gt; before use.</span></div>
</div>

<div class="ol-home-links">
<a href="contributing/">Contributing</a>
<span>·</span>
<a href="https://github.com/asifnawazminhas/awesome-offensive-oneliners/issues" target="_blank" rel="noopener">Report an issue</a>
<span>·</span>
<a href="https://github.com/asifnawazminhas/awesome-offensive-oneliners" target="_blank" rel="noopener">GitHub</a>
</div>
