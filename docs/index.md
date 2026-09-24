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

<div class="ol-category-grid">
<a class="ol-category-card" href="active-directory/">
  <div class="ol-category-head"><span class="ol-category-icon">AD</span><span class="ol-category-count">32</span></div>
  <strong>Active Directory</strong>
  <p>domain enumeration, Kerberos, delegation, AD CS and graph-based analysis.</p>
  <span class="ol-card-cta">Explore →</span>
</a>
<a class="ol-category-card" href="windows/">
  <div class="ol-category-head"><span class="ol-category-icon">WIN</span><span class="ol-category-count">26</span></div>
  <strong>Windows</strong>
  <p>host discovery, application control checks, services, registry and PowerShell.</p>
  <span class="ol-card-cta">Explore →</span>
</a>
<a class="ol-category-card" href="linux/">
  <div class="ol-category-head"><span class="ol-category-icon">LNX</span><span class="ol-category-count">20</span></div>
  <strong>Linux</strong>
  <p>host enumeration, privilege escalation checks, networking and file operations.</p>
  <span class="ol-card-cta">Explore →</span>
</a>
<a class="ol-category-card" href="web/">
  <div class="ol-category-head"><span class="ol-category-icon">WEB</span><span class="ol-category-count">21</span></div>
  <strong>Web</strong>
  <p>web reconnaissance, authentication checks, API testing and injection workflows.</p>
  <span class="ol-card-cta">Explore →</span>
</a>
<a class="ol-category-card" href="recon/">
  <div class="ol-category-head"><span class="ol-category-icon">REC</span><span class="ol-category-count">17</span></div>
  <strong>Recon</strong>
  <p>Fast discovery commands for DNS, subdomains, HTTP services and Nmap.</p>
  <span class="ol-card-cta">Explore →</span>
</a>
<a class="ol-category-card" href="red-team/">
  <div class="ol-category-head"><span class="ol-category-icon">RT</span><span class="ol-category-count">22</span></div>
  <strong>Red Team</strong>
  <p>Operational one-liners for discovery, execution, lateral movement and tunneling in authorised environments.</p>
  <span class="ol-card-cta">Explore →</span>
</a>
<a class="ol-category-card" href="credentials/">
  <div class="ol-category-head"><span class="ol-category-icon">CREDS</span><span class="ol-category-count">14</span></div>
  <strong>Credentials</strong>
  <p>Kerberos, hashes, NTLM and DPAPI-oriented testing.</p>
  <span class="ol-card-cta">Explore →</span>
</a>
<a class="ol-category-card" href="tools/">
  <div class="ol-category-head"><span class="ol-category-icon">TOOLS</span><span class="ol-category-count">31</span></div>
  <strong>Tools</strong>
  <p>commonly used offensive security tools.</p>
  <span class="ol-card-cta">Explore →</span>
</a>
</div>

## Quick launch

<div class="ol-quick-grid">

<div class="ol-quick-card" markdown>

### Find constrained delegation

```powershell
Get-DomainComputer -TrustedToAuth -Properties DnsHostName,msDS-AllowedToDelegateTo
```

**Tool:** PowerView · **Platform:** Windows · **Tags:** Kerberos, Delegation, Enumeration

</div>

<div class="ol-quick-card" markdown>

### Discover live web services

```bash
httpx -l hosts.txt -silent -status-code -title -tech-detect
```

**Tool:** httpx · **Platform:** Linux/macOS · **Tags:** Recon, HTTP, Fingerprinting

</div>

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
