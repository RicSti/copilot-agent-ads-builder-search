#!/usr/bin/env python3
"""Packt jeden Skill-Ordner aus skills/ als eigene ZIP nach dist/.

SKILL.md liegt in der ZIP auf oberster Ebene (so zeigt es die Microsoft-Doku
für den Skill-Upload im Agent Builder).

Aufruf aus dem Repo-Ordner:  python3 tools/build_skill_zips.py
"""
import pathlib, re, sys, zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS, DIST = ROOT / "skills", ROOT / "dist"
LIMIT = 20_000  # max. Zeichen für Skill-Anweisungen laut Microsoft
DIST.mkdir(exist_ok=True)
fehler = 0
for skill in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
    md = skill / "SKILL.md"
    text = md.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    name = re.search(r"^name:\s*(.+)$", m.group(1), re.M).group(1).strip() if m else None
    if text.count("\n---\n") > 2 or name != skill.name:
        print(f"FEHLER {skill.name}: Frontmatter fehlt/doppelt oder name passt nicht zum Ordner")
        fehler += 1
        continue
    if len(text) > LIMIT:
        print(f"FEHLER {skill.name}: {len(text)} Zeichen > {LIMIT}")
        fehler += 1
        continue
    ziel = DIST / f"{skill.name}.zip"
    with zipfile.ZipFile(ziel, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(skill.rglob("*")):
            if f.is_file() and f.name != ".DS_Store":
                z.write(f, f.relative_to(skill).as_posix())
    print(f"OK  {ziel.relative_to(ROOT)}  ({len(text)} Zeichen)")
sys.exit(1 if fehler else 0)
