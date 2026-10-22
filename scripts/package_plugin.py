"""Validate the plugin source and build a portable ZIP using the Python standard library."""
from pathlib import Path
import json
import re
import zipfile

root = Path(__file__).resolve().parent.parent
manifest = json.loads((root / "plugin.json").read_text(encoding="utf-8"))
legacy = json.loads((root / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
assert manifest["$schema"] == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
assert manifest["name"] == legacy["name"]
assert manifest["version"] == legacy["version"]
assert manifest["extensions"]["com.openai"]["interface"] == legacy["interface"]
assert len(legacy["interface"]["shortDescription"]) <= 30
skill_files = sorted((root / "skills").glob("*/SKILL.md"))
assert skill_files, "No skill entrypoints"
names = []
for path in skill_files:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), path
    # These published sources use a JSON object as valid YAML frontmatter.
    metadata = json.loads(text.split("---", 2)[1])
    assert metadata["name"] == path.parent.name
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", metadata["name"])
    assert 0 < len(metadata["description"]) <= 1024
    assert len(text.encode("utf-8")) <= 1024 * 1024
    names.append(metadata["name"])
assert len(names) == len(set(names)), "Duplicate skill names"
for path in (root / "skills").rglob("*.md"):
    text = path.read_text(encoding="utf-8")
    for link in re.findall(r"\]\(([^)]+)\)", text):
        if ":" in link or link.startswith("#"):
            continue
        target = (path.parent / link.split("#")[0]).resolve()
        assert target.is_relative_to(root), (path, link)
        assert target.is_file(), (path, link)
archive_dir = root / "dist"
archive_dir.mkdir(exist_ok=True)
archive = archive_dir / (manifest["name"] + "-" + manifest["version"] + ".zip")
files = [root / "plugin.json", root / ".codex-plugin/plugin.json", root / "LICENSE"]
files.extend(p for p in (root / "skills").rglob("*") if p.is_file())
with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as z:
    for path in sorted(files):
        z.write(path, path.relative_to(root).as_posix())
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert "plugin.json" in z.namelist()
    assert "LICENSE" in z.namelist()
print("Validated:", manifest["name"], manifest["version"])
print("Skills:", ", ".join(names))
print("Package:", archive)
