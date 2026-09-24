# JavaScript discovery

Find JavaScript assets and quickly mine endpoints and secrets candidates.

<div class="ol-section-kicker"><span>RECON</span></div>

## Katana JavaScript discovery

```bash
katana -u <URL> -silent | grep -Ei '\.js($|\?)' | sort -u
```

**Tool:** katana · **Platform:** Linux/macOS


## Download discovered JavaScript

```bash
mkdir -p js && cat js-urls.txt | while read -r u; do curl -ks "$u" -o "js/$(echo "$u" | sha1sum | cut -d\  -f1).js"; done
```

**Tool:** curl · **Platform:** Linux/macOS


## Extract absolute URLs from JavaScript

```bash
rg -o 'https?://[^"''' )]+' js/ | sort -u
```

**Tool:** ripgrep · **Platform:** Linux/macOS


## Extract API-looking paths

```bash
rg -o '/(api|v[0-9]+|graphql)/[A-Za-z0-9_./?=&%:-]+' js/ | sort -u
```

**Tool:** ripgrep · **Platform:** Linux/macOS


## Search JavaScript for secret keywords

```bash
rg -n -i '(api[_-]?key|secret|token|authorization|client[_-]?secret|access[_-]?key)' js/
```

**Tool:** ripgrep · **Platform:** Linux/macOS


## LinkFinder against one JavaScript file

```bash
python3 linkfinder.py -i <URL> -o cli
```

**Tool:** LinkFinder · **Platform:** Linux/macOS
