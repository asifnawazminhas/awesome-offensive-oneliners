# GitHub & GitLab Code Search

One-liners for searching public code for target domains, URLs and common secret patterns.

<div class="ol-section-kicker"><span>REC</span><strong>5 one-liners</strong></div>

## GitHub CLI code search

```bash
gh search code "<DOMAIN>" --limit 100
```

**Tool:** GitHub CLI · **Platform:** Any · **Tags:** Recon, GitHub, code search · **Context:** No auth · **Noise:** Quiet

## GitHub API code search

```bash
gh api -H "Accept: application/vnd.github+json" "/search/code?q=<DOMAIN>&per_page=100" | jq -r ' .items[].html_url '
```

**Tool:** GitHub CLI,jq · **Platform:** Any · **Tags:** Recon, GitHub, code search · **Context:** No auth · **Noise:** Quiet

## GitLab project search API

```bash
curl -s "https://gitlab.com/api/v4/projects?search=<ORG>&simple=true&per_page=100" | jq -r ' .[].web_url '
```

**Tool:** curl,jq · **Platform:** Any · **Tags:** Recon, GitLab · **Context:** No auth · **Noise:** Quiet

## Search cloned repos for domain

```bash
rg -n -i "<DOMAIN>" .
```

**Tool:** ripgrep · **Platform:** Any · **Tags:** Recon, source code · **Context:** User · **Noise:** Quiet

## Search common secret keywords

```bash
rg -n -i "(api[_-]?key|client[_-]?secret|access[_-]?token|password|passwd)" .
```

**Tool:** ripgrep · **Platform:** Any · **Tags:** Recon, source code, secrets · **Context:** User · **Noise:** Quiet

---

**Related:** JavaScript · Historical URLs · Cloud Assets
