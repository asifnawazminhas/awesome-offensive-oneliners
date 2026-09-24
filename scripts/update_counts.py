from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

# Matches the compact cards used on section index pages, for example:
#
# <div class="ol-mini-card">
#   <strong><a href="enumeration/">Enumeration</a></strong>
#   <span>0 commands · host and environment discovery</span>
# </div>
#
# The script resolves enumeration/ -> enumeration.md and counts
# the fenced command blocks in that page.

CARD_RE = re.compile(
    r'(?P<prefix><div\s+class="ol-mini-card"[^>]*>.*?'
    r'<a\s+href="(?P<href>[^"]+)"[^>]*>.*?</a>.*?'
    r'<span[^>]*>)'
    r'(?P<count>\d+)'
    r'(?P<suffix>\s+commands\b.*?</span>.*?</div>)',
    re.IGNORECASE | re.DOTALL,
)


def count_code_blocks(path: Path) -> int:
    """
    Count fenced code blocks in a Markdown page.

    In this repository, each fenced code block represents one command /
    one-liner entry, which matches the existing section-card counting model.
    """
    text = path.read_text(encoding="utf-8")

    fences = sum(
        1
        for line in text.splitlines()
        if line.lstrip().startswith("```")
    )

    return fences // 2


def resolve_card_target(index_path: Path, href: str) -> Path | None:
    """
    Resolve a section-card href to the Markdown file behind it.

    Examples:
        enumeration/ -> enumeration.md
        kerberos/    -> kerberos.md
        tools/foo/   -> tools/foo.md when applicable
    """
    href = href.strip()

    if not href:
        return None

    if href.startswith(("http://", "https://", "#", "mailto:")):
        return None

    clean = (
        href
        .split("#", 1)[0]
        .split("?", 1)[0]
        .rstrip("/")
    )

    if not clean:
        return None

    base = index_path.parent

    # Normal project pattern:
    # enumeration/ -> enumeration.md
    sibling_md = (base / clean).with_suffix(".md")

    if sibling_md.exists():
        return sibling_md

    # Support explicit Markdown links too.
    explicit = base / clean

    if explicit.suffix == ".md" and explicit.exists():
        return explicit

    # Fallback if a card ever links to an actual subdirectory.
    nested_index = base / clean / "index.md"

    if nested_index.exists():
        return nested_index

    return None


def update_index(index_path: Path) -> tuple[int, int]:
    original = index_path.read_text(encoding="utf-8")

    updates = 0
    unresolved = 0

    def replace(match: re.Match) -> str:
        nonlocal updates, unresolved

        href = match.group("href")
        old_count = int(match.group("count"))

        target = resolve_card_target(index_path, href)

        if target is None:
            unresolved += 1

            print(
                f"[WARN] Could not resolve card target in "
                f"{index_path.relative_to(DOCS)}: {href}"
            )

            return match.group(0)

        new_count = count_code_blocks(target)

        if new_count != old_count:
            print(
                f"[UPDATE] "
                f"{index_path.relative_to(DOCS)} -> "
                f"{target.relative_to(DOCS)}: "
                f"{old_count} -> {new_count} commands"
            )

            updates += 1

        return (
            f'{match.group("prefix")}'
            f'{new_count}'
            f'{match.group("suffix")}'
        )

    updated = CARD_RE.sub(replace, original)

    if updated != original:
        index_path.write_text(updated, encoding="utf-8")

    return updates, unresolved


def main() -> None:
    total_updates = 0
    total_unresolved = 0

    indexes = sorted(DOCS.rglob("index.md"))

    for index_path in indexes:
        updates, unresolved = update_index(index_path)

        total_updates += updates
        total_unresolved += unresolved

    print(
        f"[DONE] Scanned {len(indexes)} index pages; "
        f"updated {total_updates} card count(s); "
        f"unresolved {total_unresolved}."
    )


if __name__ == "__main__":
    main()
