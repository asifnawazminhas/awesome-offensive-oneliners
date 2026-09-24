from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
docs = root / "docs"
index = docs / "index.md"
exclude = {docs / "index.md", docs / "contributing.md", docs / "conventions.md"}
md_files = [p for p in docs.rglob("*.md") if p not in exclude]
code_blocks = sum(p.read_text(encoding="utf-8").count("```") // 2 for p in md_files)
pages = len(md_files)
one = f"{(code_blocks // 10) * 10}+"
pg = f"{(pages // 10) * 10}+"
text = index.read_text(encoding="utf-8")
text = re.sub(r'<!-- ONELINER_COUNT -->.*?<!-- /ONELINER_COUNT -->', f'<!-- ONELINER_COUNT -->{one}<!-- /ONELINER_COUNT -->', text)
text = re.sub(r'<!-- PAGE_COUNT -->.*?<!-- /PAGE_COUNT -->', f'<!-- PAGE_COUNT -->{pg}<!-- /PAGE_COUNT -->', text)
index.write_text(text, encoding="utf-8")
print(f"Homepage stats: {one} one-liners, {pg} pages ({code_blocks} code blocks, {pages} Markdown files)")
