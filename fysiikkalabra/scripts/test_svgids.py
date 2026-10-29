"""svgids.py: a figure shown twice on a page gets its own definition ids and its references follow them.

  python scripts/test_svgids.py"""
import pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import svgids

fails = 0
def check(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f": {detail}")); fails += not ok

FIG = ('<svg role="img" aria-labelledby="t1 d1"><title id="t1">T</title><desc id="d1">D</desc><defs>'
       '<linearGradient id="g"><stop/></linearGradient><clipPath id="c"><rect/></clipPath><mask id="m"><rect/></mask>'
       '<marker id="arr"><path/></marker><path id="p"/></defs>'
       '<rect fill="url(#g)" clip-path="url(#c)" mask="url(#m)"/><line marker-end="url(#arr)"/><use href="#p"/><use xlink:href="#p"/></svg>')
page = f'<h2 id="teoria">x</h2>{FIG}<p>between</p>{FIG}<div id="g2"></div>{FIG}'
out = svgids.namespace(page)
svgs = re.findall(r"<svg\b.*?</svg>", out, re.S)
check("no repeated ids after namespacing", svgids.duplicates(out) == [], svgids.duplicates(out))
check("the first copy keeps its ids", svgs[0] == FIG)
check("the second copy refers to its own gradient, clip path, mask, marker and use target",
      all(s in svgs[1] for s in ('id="g-2"', 'url(#g-2)', 'id="c-2"', 'url(#c-2)', 'id="m-2"', 'url(#m-2)', 'url(#arr-2)', 'href="#p-2"', 'xlink:href="#p-2"')), svgs[1])
check("accessibility references follow (aria-labelledby with two ids)", 'aria-labelledby="t1-2 d1-2"' in svgs[1] and 'id="t1-2"' in svgs[1])
check("a third copy gets the next suffix", 'id="g-3"' in svgs[2] and 'url(#g-3)' in svgs[2])
check("ids outside figures are never renamed", 'id="teoria"' in out and 'id="g2"' in out)
check("no copy points at another copy's definitions", "url(#g)" not in svgs[1] + svgs[2])
check("a page without repeats is unchanged", svgids.namespace(f"<p id='a'></p>{FIG}") == f"<p id='a'></p>{FIG}")
check("duplicates() reports a repeated id", svgids.duplicates('<a id="x"></a><b id="x"></b>') == ["x"])
print(f"{fails} failure(s)"); sys.exit(1 if fails else 0)
