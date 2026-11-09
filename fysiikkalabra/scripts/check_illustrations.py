#!/usr/bin/env python3
"""Static illustration inventory for all Finnish FY1-FY8 lessons.

Run from any directory:
    python scripts/check_illustrations.py
    python scripts/check_illustrations.py --report docs/illustration-inventory.md

This does not check physical correctness or rendered visual quality.
"""
import argparse
import ast
from collections import Counter
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
MODULES = [f"FY{n}" for n in range(1, 9)]
SVG = re.compile(r"<svg\b[^>]*>.*?</svg>", re.S)
IMG = re.compile(r"<img\b[^>]*>", re.S)
ATTR = re.compile(r"""([\w:-]+)\s*=\s*["']([^"']*)["']""")


def attributes(tag):
    return {key.lower(): html.unescape(val) for key, val in ATTR.findall(tag)}


def mapped_figures(path, problems):
    if not path.is_file():
        problems.append(f"{path}: missing figures.py")
        return None
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except SyntaxError as exc:
        problems.append(f"{path}: Python syntax error: {exc}")
        return None
    for stmt in tree.body:
        if isinstance(stmt, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "FIGURES" for t in stmt.targets
        ):
            if not isinstance(stmt.value, ast.Dict):
                problems.append(f"{path}: FIGURES mapping needs manual inspection")
                return None
            keys = [k.value for k in stmt.value.keys
                    if isinstance(k, ast.Constant) and isinstance(k.value, str)]
            for key, count in Counter(keys).items():
                if count > 1:
                    problems.append(f"{path}: duplicate FIGURES key {key}")
            return set(keys)
    problems.append(f"{path}: no FIGURES dictionary")
    return None


def inspect():
    rows, problems = [], []
    for module in MODULES:
        base = ROOT / "content" / "fi" / module
        if not base.is_dir():
            problems.append(f"{base}: missing module")
            continue
        folders = sorted(
            (p for p in base.iterdir() if p.is_dir() and re.fullmatch(r"fy\d+-\d+", p.name)),
            key=lambda p: int(p.name.split("-")[-1]))
        for folder in folders:
            lesson = folder / "lesson.md"
            if not lesson.is_file():
                problems.append(f"{lesson}: missing lesson")
                continue
            source = ROOT / "lessons" / module / folder.name / "figures.py"
            text = lesson.read_text(encoding="utf-8")
            svgs, imgs = SVG.findall(text), IMG.findall(text)
            names = []
            for svg in svgs:
                tag = svg[:svg.index(">") + 1]
                a = attributes(tag)
                name = a.get("data-fig")
                if not name:
                    problems.append(f"{lesson}: untracked inline svg")
                else:
                    names.append(name)
                if a.get("role") != "img" or not a.get("aria-label", "").strip():
                    problems.append(f"{lesson}: svg {name} lacks image role or alt description")
            for tag in imgs:
                if "alt" not in attributes(tag):
                    problems.append(f"{lesson}: img without alt")
            for name, count in Counter(names).items():
                if count > 1:
                    problems.append(f"{lesson}: duplicate data-fig {name}")
            if names.count("hero") != 1:
                problems.append(f"{lesson}: {names.count('hero')} hero figures, expected 1")
            keys = mapped_figures(source, problems)
            if keys is not None:
                for name in sorted(set(names) - keys):
                    problems.append(f"{lesson}: data-fig {name} not in figures.py FIGURES")
            title_match = re.search(r"^#\s+(.+)$", text, re.M)
            rows.append({
                "module": module, "id": folder.name,
                "title": title_match.group(1) if title_match else folder.name,
                "svg": len(svgs), "img": len(imgs), "hero": names.count("hero"),
                "source_figures": len(keys) if keys is not None else None,
            })
    return rows, problems


def report(rows, problems):
    lines = [
        "# FY1-FY8: Kuvituksen rakenteellinen inventaario", "",
        "Generoitu komennolla python scripts/check_illustrations.py --report docs/illustration-inventory.md.",
        "",
        "Rajaus: suomenkielisten oppituntien lesson.md-tiedostojen SVG- ja img-elementit. "
        "Tehtavien kuvat, simulaatioiden sisaiset kuvat, kaannokset ja lopullinen selainulkoasu "
        "eivat sisally lukuihin. Maara ei mittaa pedagogista tai fysikaalista laatua.", "",
        "| Moduuli | Tunnit | SVG | img | Aloituskuvat |",
        "|---|---:|---:|---:|---:|",
    ]
    for module in MODULES:
        a = [r for r in rows if r["module"] == module]
        lines.append(f"| {module} | {len(a)} | {sum(r['svg'] for r in a)} | "
                     f"{sum(r['img'] for r in a)} | {sum(r['hero'] for r in a)} |")
    lines.append(f"| Yhteensa | {len(rows)} | {sum(r['svg'] for r in rows)} | "
                 f"{sum(r['img'] for r in rows)} | {sum(r['hero'] for r in rows)} |")
    lines += ["", "## Oppitunnit", "", "| Oppitunti | Otsikko | SVG | img |",
              "|---|---|---:|---:|"]
    for r in rows:
        title = r["title"].replace("|", "/").replace("\n", " ")
        lines.append(f"| {r['id']} | {title} | {r['svg']} | {r['img']} |")
    lines += ["", "## Rakenteelliset poikkeamat", ""]
    lines.extend("- " + p for p in problems)
    if not problems:
        lines.append("Ei automaattisesti havaittuja poikkeamia.")
    lines += ["", "## Erillinen asiantuntijatarkastus", "",
              "- Vertaa SVG-kuvaa renderoituun selainkuvaan ja testaa eri nayttokoot.",
              "- Tarkista fysikaalisten nuolten alku, suunta ja merkitys.",
              "- Tarkista aaltojen, sahkokenttien ja energiakaavioiden fysikaalinen geometria.",
              "- Tarkista tehtavakuvat ja simulaatiot erillisella inventaariolla.", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=pathlib.Path)
    args = parser.parse_args()
    rows, problems = inspect()
    for module in MODULES:
        a = [r for r in rows if r["module"] == module]
        print(f"{module}: {len(a)} lessons; {sum(r['svg'] for r in a)} SVG; "
              f"{sum(r['img'] for r in a)} img")
    if args.report:
        out = args.report if args.report.is_absolute() else ROOT / args.report
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(report(rows, problems), encoding="utf-8")
        print(f"Report written: {out}")
    for p in problems:
        print("ERROR:", p, file=sys.stderr)
    print(f"TOTAL: {len(rows)} lessons, {len(problems)} structural issues")
    return int(bool(problems))


if __name__ == "__main__":
    sys.exit(main())
