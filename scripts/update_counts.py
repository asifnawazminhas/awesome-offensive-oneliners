from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

CARD_RE = re.compile(
    r'(?P<prefix><div\s+class="ol-mini-card"[^>]*>.*?'
    r'<a\s+href="(?P<href>[^"]+)"[^>]*>.*?</a>.*?'
    r'<span[^>]*>)'
    r'(?P<count>\d+)'
    r'(?P<suffix>\s+commands\b.*?</span>.*?</div>)',
    re.IGNORECASE | re.DOTALL,
)

def count_code_blocks(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    fences = sum(1 for line in text.splitlines() if line.lstrip().startswith("```"))
    return fences // 2

def resolve_card_target(index_path: Path, href: str):
    href = href.strip()
    if not href or href.startswith(("http://", "https://", "#", "mailto:")):
        return None
    clean = href.split("#", 1)[0].split("?", 1)[0].rstrip("/")
    if not clean:
        return None
    base = index_path.parent
    sibling_md = (base / clean).with_suffix(".md")
    if sibling_md.exists():
        return sibling_md
    explicit = base / clean
    if explicit.suffix == ".md" and explicit.exists():
        return explicit
    nested_index = base / clean / "index.md"
    if nested_index.exists():
        return nested_index
    return None

def update_index(index_path: Path):
    original = index_path.read_text(encoding="utf-8")
    updates = unresolved = 0
    def replace(match):
        nonlocal updates, unresolved
        href = match.group("href")
        old_count = int(match.group("count"))
        target = resolve_card_target(index_path, href)
        if target is None:
            unresolved += 1
            print(f"[WARN] Could not resolve {index_path.relative_to(DOCS)}: {href}")
            return match.group(0)
        new_count = count_code_blocks(target)
        if new_count != old_count:
            print(f"[UPDATE] {index_path.relative_to(DOCS)} -> {target.relative_to(DOCS)}: {old_count} -> {new_count}")
            updates += 1
        return f'{match.group("prefix")}{new_count}{match.group("suffix")}'
    updated = CARD_RE.sub(replace, original)
    if updated != original:
        index_path.write_text(updated, encoding="utf-8")
    return updates, unresolved

def main():
    total_updates = total_unresolved = 0
    indexes = sorted(DOCS.rglob("index.md"))
    for index_path in indexes:
        updates, unresolved = update_index(index_path)
        total_updates += updates
        total_unresolved += unresolved
    print(f"[DONE] Scanned {len(indexes)} index pages; updated {total_updates} card count(s); unresolved {total_unresolved}.")

if __name__ == "__main__":
    main()
