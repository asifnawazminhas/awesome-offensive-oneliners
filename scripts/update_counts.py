from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

COUNT_PATTERN = re.compile(
    r'(<span\s+data-count-page="([^"]+)">)(\d+)(\s+commands\b[^<]*</span>)',
    re.IGNORECASE
)

FENCE_PATTERN = re.compile(
    r"^```(?:bash|sh|shell|powershell|ps1|cmd|bat|console|text)?\s*$",
    re.MULTILINE | re.IGNORECASE,
)


def count_command_blocks(path: Path) -> int:
    if not path.exists():
        print(f"[WARN] Missing page: {path}")
        return 0

    text = path.read_text(encoding="utf-8")

    count = 0
    in_fence = False

    for line in text.splitlines():
        stripped = line.strip()

        if stripped.startswith("```"):
            if not in_fence:
                language = stripped[3:].strip().lower()

                if language in {
                    "",
                    "bash",
                    "sh",
                    "shell",
                    "powershell",
                    "ps1",
                    "cmd",
                    "bat",
                    "console",
                    "text",
                }:
                    count += 1

                in_fence = True
            else:
                in_fence = False

    return count


def update_index(index_path: Path) -> bool:
    original = index_path.read_text(encoding="utf-8")
    index_dir = index_path.parent

    changed = False

    def replace(match: re.Match) -> str:
        nonlocal changed

        prefix = match.group(1)
        relative_page = match.group(2)
        old_count = match.group(3)
        suffix = match.group(4)

        target = index_dir / relative_page
        new_count = count_command_blocks(target)

        if str(new_count) != old_count:
            print(
                f"[UPDATE] {index_path.relative_to(DOCS)}: "
                f"{relative_page} {old_count} -> {new_count}"
            )
            changed = True

        return f"{prefix}{new_count}{suffix}"

    updated = COUNT_PATTERN.sub(replace, original)

    if changed:
        index_path.write_text(updated, encoding="utf-8")

    return changed


def main():
    indexes = list(DOCS.rglob("index.md"))

    updated_files = 0

    for index_path in indexes:
        if update_index(index_path):
            updated_files += 1

    print(f"[DONE] Updated {updated_files} index file(s).")


if __name__ == "__main__":
    main()
