"""Write a lesson's figures from its figures.py into lesson.md. Usage: python scripts/figures.py <lesson-id> [--check]

figures.py in the lesson folder defines FIGURES = {name: function returning the SVG string} with scripts/figlib.py.
Each `<svg ... data-fig="<name>" ...>...</svg>` block in lesson.md is replaced by the figure of that name; a name
without a block in lesson.md is reported, so a new figure is placed by hand once (paste `<svg data-fig="name"></svg>`
on its own line after the paragraph it explains) and kept in step from then on. --check only reports whether
lesson.md is up to date (exit 1 if not). --tag a,b,c names the existing figures of lesson.md in order (data-fig),
once, before figures.py takes them over."""
import sys, re, pathlib, importlib.util
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from lint_lesson import find_lesson

folder = find_lesson(sys.argv[1])
if "--tag" in sys.argv:
    names = sys.argv[sys.argv.index("--tag") + 1].split(","); md = folder / "lesson.md"; parts = md.read_text().split("<svg ")
    if len(parts) - 1 != len(names): sys.exit(f"lesson.md has {len(parts) - 1} figures, {len(names)} names given")
    md.write_text(parts[0] + "".join(f'<svg data-fig="{nm}" ' + p for nm, p in zip(names, parts[1:]))); sys.exit(0)
spec = importlib.util.spec_from_file_location("figures", folder / "figures.py")
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
md = folder / "lesson.md"; text = md.read_text(); new = text
for name, fn in mod.FIGURES.items():
    pat = re.compile(r'<svg\b[^>]*\bdata-fig="' + re.escape(name) + r'"[^>]*>.*?</svg>', re.S)
    if not pat.search(new): print(f"no <svg data-fig=\"{name}\"> in lesson.md: place it after its paragraph"); continue
    svg = fn()
    if 'data-fig=' not in svg: svg = svg.replace("<svg ", f'<svg data-fig="{name}" ', 1)
    new = pat.sub(lambda m: svg, new, count=1)
if "--check" in sys.argv:
    print("lesson.md figures up to date" if new == text else "lesson.md figures differ from figures.py"); sys.exit(0 if new == text else 1)
if new != text: md.write_text(new); print(f"wrote {len(mod.FIGURES)} figure(s) into {md}")
else: print("figures up to date")
