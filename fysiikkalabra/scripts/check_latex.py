"""Find LaTeX fragments that KaTeX cannot parse. Usage: python scripts/check_latex.py content/FY3/fy3-2
Uses the vendored templates/vendor/katex/katex.min.js, so no npm install is needed."""
import re, sys, pathlib, subprocess, json
ROOT = pathlib.Path(__file__).resolve().parents[1]
folder = pathlib.Path(sys.argv[1])
frags = []
for f in sorted(folder.glob("*.md")):
    t = f.read_text()
    t = re.sub(r"```latex\n(.*?)```", lambda m: "$$" + m.group(1) + "$$", t, flags=re.S)
    frags += [m.strip() for m in re.findall(r"\$\$(.*?)\$\$", t, re.S)]
    frags += re.findall(r"(?<!\$)\$([^$\n]+?)\$(?!\$)", re.sub(r"\$\$.*?\$\$", "", t, flags=re.S))
katex = (ROOT / "templates/vendor/katex/katex.min.js").resolve()
js = "const k=require(%s);let bad=0;for(const s of %s){try{k.renderToString(s,{throwOnError:true})}catch(e){bad++;console.log('BAD:',s,'->',e.message)}}console.log(bad?bad+' bad':'all LaTeX ok ('+%d+' fragments)')" % (json.dumps(str(katex)), json.dumps(frags), len(frags))
r = subprocess.run(["node", "-e", js], capture_output=True, text=True)
print(r.stdout.strip() or r.stderr.strip())
sys.exit(1 if "BAD:" in r.stdout else 0)
