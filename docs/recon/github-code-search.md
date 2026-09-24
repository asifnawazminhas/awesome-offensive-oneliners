---
hide:
  - toc
---
# GitHub & GitLab Code Search

Fast code-search one-liners for public exposure and asset discovery.

<div class="ol-section-kicker"><span>REC</span><strong>CODE</strong></div>

## GitHub code search for domain
```bash
gh search code '<DOMAIN>' --limit 100
```
**Tool:** GitHub CLI · **Platform:** Any · **Tags:** GitHub, Code Search · **Context:** Authenticated CLI

## GitHub filename search
```bash
gh search code 'filename:.env <DOMAIN>' --limit 100
```
**Tool:** GitHub CLI · **Platform:** Any · **Tags:** GitHub, .env · **Context:** Authenticated CLI

## GitHub API code search
```bash
curl -s -H 'Authorization: Bearer <GITHUB_TOKEN>' 'https://api.github.com/search/code?q=<DOMAIN>+in:file' | jq -r '.items[].html_url'
```
**Tool:** curl/jq · **Platform:** Any · **Tags:** GitHub API, Code Search · **Context:** API token

## GitLab API project search
```bash
curl -s --header 'PRIVATE-TOKEN: <GITLAB_TOKEN>' 'https://gitlab.com/api/v4/projects?search=<DOMAIN>' | jq -r '.[].web_url'
```
**Tool:** curl/jq · **Platform:** Any · **Tags:** GitLab, Projects · **Context:** API token

## GitLab code-search endpoint
```bash
curl -s --header 'PRIVATE-TOKEN: <GITLAB_TOKEN>' 'https://gitlab.com/api/v4/search?scope=blobs&search=<DOMAIN>' | jq -r '.[].path'
```
**Tool:** curl/jq · **Platform:** Any · **Tags:** GitLab, Code Search · **Context:** API token

**Related:** [Code Search](code-search.md) · [Cloud Assets](cloud-assets.md) · [Passive Combinations](passive-combinations.md)
