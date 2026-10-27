"""Find LaTeX fragments that KaTeX cannot parse. Usage: python scripts/check_latex.py content/fi/FY3/fy3-2
Checks the .md files (```latex fences, $$...$$, $...$) and every string in the .json files of the folder
(exercise texts, exit-ticket questions and answers), because the page renders $...$ in those too, and the .md files
of the lesson's language-neutral half (lessons/FY3/fy3-2/sim-spec.md).
Uses the vendored templates/vendor/katex/katex.min.js, so no npm install is needed. Exit code 1 if anything is bad."""
import re, sys, pathlib, subprocess, json
ROOT = pathlib.Path(__file__).resolve().parents[1]
folder = pathlib.Path(sys.argv[1])

def fragments(text):
    text = re.sub(r"```latex\n(.*?)```", lambda m: "$$" + m.group(1) + "$$", text, flags=re.S)
    display = [m.strip() for m in re.findall(r"\$\$(.*?)\$\$", text, re.S)]
    rest = re.sub(r"\$\$.*?\$\$", "", text, flags=re.S)
    return display + re.findall(r"(?<!\$)\$([^$\n]+?)\$(?!\$)", rest)

def strings(node):
    if isinstance(node, str): yield node
    elif isinstance(node, dict):
        for v in node.values(): yield from strings(v)
    elif isinstance(node, list):
        for v in node: yield from strings(v)

code = ROOT / "lessons" / folder.resolve().parent.name / folder.resolve().name
frags = []
for f in sorted(folder.glob("*.md")) + (sorted(code.glob("*.md")) if code.is_dir() else []):
    frags += fragments(f.read_text())
for f in sorted(folder.glob("*.json")):
    for s in strings(json.loads(f.read_text())): frags += fragments(s)
katex = (ROOT / "templates/vendor/katex/katex.min.js").resolve()
js = "const k=require(%s);let bad=0;for(const s of %s){try{k.renderToString(s,{throwOnError:true})}catch(e){bad++;console.log('BAD:',s,'->',e.message.split('\\n')[0])}}console.log(bad?bad+' bad':'all LaTeX ok ('+%d+' fragments)')" % (json.dumps(str(katex)), json.dumps(frags), len(frags))
r = subprocess.run(["node", "-e", js], capture_output=True, text=True)
print(r.stdout.strip() or r.stderr.strip())
sys.exit(1 if "BAD:" in r.stdout else 0)
