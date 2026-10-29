"""Unique ids in a built page (teacher 2026-10-29). A figure is drawn once (figures.py) but can appear several times on
one page: in the theory and again in a task that shows it by its id. Its gradients, clip paths, masks and markers
then share their ids, and `url(#id)` may resolve to the wrong copy. `namespace(html)` gives every repeated
definition inside an <svg> a suffix (`fy25-heat` → `fy25-heat-2`) and rewrites that svg's own references to it
(`url(#…)`, `href="#…"`, `xlink:href`, `aria-labelledby`, `aria-describedby`, `for`), so each copy points at its own
definitions; the first copy keeps its ids. The figure sources and the catalog stay as they are (build step only).
`duplicates(html)` lists the ids a page still repeats; build.py refuses to write such a page.

  python scripts/svgids.py site            every built page: exit 1 on a repeated id"""
import collections, pathlib, re, sys

SVG = re.compile(r"<svg\b.*?</svg>", re.S)
ID = re.compile(r'(?<=\sid=")([^"]+)(?=")')
IDREF_ATTRS = ("aria-labelledby", "aria-describedby", "for")


def duplicates(html):
    return sorted(k for k, v in collections.Counter(ID.findall(html)).items() if v > 1)


def _rename(svg, names):
    def ref(i): return names.get(i, i)
    svg = ID.sub(lambda m: ref(m.group(1)), svg)
    svg = re.sub(r"url\(#([^)\s]+)\)", lambda m: f"url(#{ref(m.group(1))})", svg)
    svg = re.sub(r'((?:xlink:)?href)="#([^"]+)"', lambda m: f'{m.group(1)}="#{ref(m.group(2))}"', svg)
    for a in IDREF_ATTRS:
        svg = re.sub(rf'(\s{a}=")([^"]+)(")', lambda m: m.group(1) + " ".join(ref(x) for x in m.group(2).split()) + m.group(3), svg)
    return svg


def namespace(html):
    seen = set(ID.findall(SVG.sub("", html)))         # ids outside figures (headings, stages, the sim) are never renamed
    count = collections.Counter()
    def one(m):
        svg = m.group(0); names = {}
        for i in dict.fromkeys(ID.findall(svg)):
            if i in seen:
                count[i] += 1; n = f"{i}-{count[i] + 1}"
                while n in seen: count[i] += 1; n = f"{i}-{count[i] + 1}"
                names[i] = n
            seen.add(names.get(i, i))
        return _rename(svg, names) if names else svg
    return SVG.sub(one, html)


if __name__ == "__main__":
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "site")
    bad = 0
    for f in sorted(root.rglob("*.html")):
        d = duplicates(f.read_text())
        if d: print(f"ERROR {f}: repeated id(s) {', '.join(d)}"); bad += 1
    print(f"{bad} page(s) with repeated ids"); sys.exit(1 if bad else 0)
