from pathlib import Path
import re
import subprocess
from datetime import datetime, timezone

root = Path(__file__).resolve().parents[1]
docs = root / "docs"
index = docs / "index.md"
changelog = docs / "changelog.md"
exclude = {docs / "index.md", docs / "contributing.md", docs / "conventions.md", docs / "start-here.md", docs / "changelog.md"}
md_files = [p for p in docs.rglob("*.md") if p not in exclude and not p.name == "index.md"]
code_blocks = sum(p.read_text(encoding="utf-8").count("```") // 2 for p in md_files)
pages = len(md_files)
try:
    stamp = subprocess.check_output(["git", "log", "-1", "--format=%cs"], cwd=root, text=True).strip()
except Exception:
    stamp = datetime.now(timezone.utc).date().isoformat()

def update(path: Path):
    text = path.read_text(encoding="utf-8")
    text = re.sub(r'<!-- ONELINER_COUNT -->.*?<!-- /ONELINER_COUNT -->', f'<!-- ONELINER_COUNT -->{code_blocks}<!-- /ONELINER_COUNT -->', text)
    text = re.sub(r'<!-- PAGE_COUNT -->.*?<!-- /PAGE_COUNT -->', f'<!-- PAGE_COUNT -->{pages}<!-- /PAGE_COUNT -->', text)
    text = re.sub(r'<!-- LAST_UPDATED -->.*?<!-- /LAST_UPDATED -->', f'<!-- LAST_UPDATED -->{stamp}<!-- /LAST_UPDATED -->', text)
    path.write_text(text, encoding="utf-8")

update(index)
if changelog.exists(): update(changelog)
print(f"Homepage stats: {code_blocks} one-liners, {pages} focused pages, last updated {stamp}")
