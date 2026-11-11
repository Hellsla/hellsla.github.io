"""Kuvitusauditoinnin luettelot ja kuvakatalogi (docs/illustration-audit/).

  python docs/illustration-audit/build.py            kaikki kurssit, joilla on data/<KURSSI>.tsv
  python docs/illustration-audit/build.py FY3        yksi kurssi

Lähde on data/<KURSSI>.tsv, rivi per kuva, erottimena |:
  tunniste | fysiikka | pedagogiikka | visuaalinen | tyyli | suositus | perustelu | korvausehdotus | opettajan päätös
Suositus: PIDA, KEVYT, UUSI (piirrä uudelleen), KORVAA, VIRHE (fysiikan virhe), KESKEN (ei arvioitu).
Opettajan päätös on tyhjänä ODOTTAA. Skripti ei muuta mitään tämän hakemiston ulkopuolella: se lukee kuvaluettelon
(docs/figures/catalog.json) ja piirtää kuvat samalla koodilla kuin sivusto (scripts/figcat.py render).
"""
import html, json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REC = {"PIDA": "PIDÄ", "KEVYT": "KEVYT KORJAUS", "UUSI": "PIIRRÄ UUDELLEEN", "KORVAA": "KORVAA UUDELLA KUVALLA",
       "VIRHE": "FYSIIKAN VIRHE", "KESKEN": "ARVIOIMATTA"}
ORDER = ["VIRHE", "KORVAA", "UUSI", "KEVYT", "PIDA", "KESKEN"]
CAT = json.loads((ROOT / "docs/figures/catalog.json").read_text())
FIGS = {f["id"]: f for f in CAT["figures"]}


def rows(course):
    out = []
    for line in (HERE / "data" / f"{course}.tsv").read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        p = [x.strip() for x in line.split("|")] + [""] * 9
        out.append(dict(id=p[0], f=p[1], p=p[2], v=p[3], t=p[4], rec=p[5], why=p[6], idea=p[7], decision=p[8] or "ODOTTAA"))
    return out


def chapter(fid):
    owner = fid.split("/")[1] if fid.startswith("pics/") else fid.split("/")[0]
    return owner, (CAT["lessons"].get(owner) or {}).get("title", "")


def use(fid):
    f = FIGS.get(fid, {})
    if fid.endswith("/hero"):
        return "avauskuva"
    used = " ".join(f.get("used_in", []))
    where = [w for k, w in (("lesson.md", "teoria"), ("inquiry.json", "tutkimusvaihe"), ("exercises.json", "tehtävä"),
                            ("solutions.md", "ratkaisu"), ("tasks.json", "soveltava tehtävä tai koe")) if k in used]
    kind = {"graph": "kuvaaja", "diagram": "kaavio", "illustration": "kuvitus"}.get(f.get("kind"), "")
    return (kind + ": " + ", ".join(where)) if where else (kind + ": ei käytössä")


def anchor(fid):
    return re.sub(r"[^a-z0-9]+", "-", fid.lower()).strip("-")


def fig_svg(fid):
    """The SVG of one figure as the page shows it: drawn by figcat, or cut out of the text for a hand-pasted one
    (id "<owner>/~<file>-<n>": the n-th <svg> of the source file the catalog names)."""
    name = fid.split("/")[-1]
    if name.startswith("~"):
        path = ROOT / FIGS[fid]["source"].split(" (")[0]
        src = path.read_text().replace('\\"', '"')
        if path.suffix == ".json":
            src = src.replace("\\n", "\n").replace("\\\\", "\\")
        ms = list(re.finditer(r"<svg\b.*?</svg>", src, re.S))
        n = int(name.rsplit("-", 1)[1])
        tags = list(re.finditer(r"<svg\b[^>]*>", src))
        return next((m.group(0) for m in ms if m.start() == tags[n - 1].start()), "") if n <= len(tags) else ""
    out = subprocess.run([sys.executable, "scripts/figcat.py", "render", fid], capture_output=True, text=True, cwd=ROOT).stdout
    return out[out.find("<svg"):] if "<svg" in out else ""


def md(course, rs):
    L = [f"# {course}: kuvituksen arviointiluettelo", "",
         f"Kuvia {len(rs)}. Asteikko 1–5: F fysiikka, P pedagogiikka, V visuaalinen laatu, T tyylin yhtenäisyys. "
         f"Esikatselu: [catalog/{course}.html](catalog/{course}.html) (avaa paikallisesti repositorion kopiosta).", "",
         "| Tunniste | Luku ja käyttö | F | P | V | T | Suositus | Perustelu | Ehdotus korvaavaksi kuvaksi | Opettajan päätös |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for r in rs:
        owner, title = chapter(r["id"])
        L.append(f"| [`{r['id']}`](catalog/{course}.html#{anchor(r['id'])}) | {title or owner}; {use(r['id'])} | {r['f']} | {r['p']} | "
                 f"{r['v']} | {r['t']} | {REC[r['rec']]} | {r['why']} | {r['idea']} | {r['decision']} |")
    (HERE / f"{course}.md").write_text("\n".join(L) + "\n")


def catalog(course, rs):
    site = "../../../site"
    h = [f'<!doctype html><html lang="fi"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
         f'<title>{course}: kuvakatalogi</title><link rel="stylesheet" href="{site}/site.css">'
         f'<link rel="stylesheet" href="{site}/vendor/katex/katex.min.css"><script src="{site}/vendor/katex/katex.min.js"></script>'
         f'<script src="{site}/vendor/katex/contrib/auto-render.min.js"></script><style>'
         'body{margin:0;padding:16px;background:#f6f1e6;font:16px/1.45 system-ui,sans-serif;color:#1f2933}'
         'h1{font-size:24px;margin:0 0 8px}nav{position:sticky;top:0;background:#f6f1e6;padding:8px 0;z-index:5;display:flex;flex-wrap:wrap;gap:8px}'
         'nav button{font:inherit;padding:8px 12px;border:1px solid #1f2933;border-radius:6px;background:#fff;cursor:pointer}'
         'nav button[aria-pressed=true]{background:#1f2933;color:#fff}'
         '.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,420px),1fr));gap:16px;align-items:start}'
         'body.phone .grid{grid-template-columns:360px}'
         '.card{background:#fff;border:1px solid #c9c2b2;border-radius:8px;overflow:hidden}.card header{padding:8px 12px;border-bottom:1px solid #e3dccb}'
         '.card code{font-size:15px;font-weight:700}.card .ch{font-size:14px;color:#6b7480}.card .fig{padding:8px}.card .fig svg{display:block;width:100%;height:auto}'
         '.card footer{padding:8px 12px;border-top:1px solid #e3dccb;font-size:15px}.b{display:inline-block;padding:2px 8px;border-radius:4px;font-size:13px;font-weight:700;color:#fff}'
         '.PIDA{background:#2b8a3e}.KEVYT{background:#b8622d}.UUSI{background:#c92a2a}.KORVAA{background:#7048e8}.VIRHE{background:#1f2933}.KESKEN{background:#6b7480}'
         '.sc{font-size:13px;color:#6b7480;margin-left:8px}.idea{margin-top:6px;padding:6px 8px;background:#f6f1e6;border-radius:4px}'
         f'</style><body><h1>{course}: kuvakatalogi</h1><p>Kuvia {len(rs)}. Päätökset kirjataan tiedostoon <code>data/{course}.tsv</code> kuvatunnisteella.</p>'
         '<nav><button data-f="all" aria-pressed="true">Kaikki</button><button data-f="act">Uudelleen piirrettävät ja korvattavat ensin</button>'
         '<button data-f="fix">Vain muutosehdotukset</button><button id="ph" aria-pressed="false">Puhelinleveys 360 px</button></nav><div class="grid">']
    for r in rs:
        owner, title = chapter(r["id"])
        svg = fig_svg(r["id"]) or "<p>Kuvaa ei voitu renderöidä.</p>"
        sc = f"F {r['f']} · P {r['p']} · V {r['v']} · T {r['t']}" if r["f"] else ""
        idea = f'<div class="idea"><b>Ehdotus:</b> {html.escape(r["idea"])}</div>' if r["idea"] else ""
        h.append(f'<article class="card" id="{anchor(r["id"])}" data-rec="{r["rec"]}" data-rank="{ORDER.index(r["rec"])}"><header><code>{html.escape(r["id"])}</code>'
                 f'<div class="ch">{html.escape(title or owner)} · {html.escape(use(r["id"]))}</div></header><div class="fig">{svg}</div>'
                 f'<footer><span class="b {r["rec"]}">{REC[r["rec"]]}</span><span class="sc">{sc}</span><div>{html.escape(r["why"])}</div>{idea}'
                 f'<div class="ch">Opettajan päätös: {html.escape(r["decision"])}</div></footer></article>')
    h.append('</div><script>renderMathInElement(document.body,{delimiters:[{left:"$",right:"$",display:false}]});'
             'const g=document.querySelector(".grid"),cs=[...g.children],o=cs.slice();'
             'document.querySelectorAll("nav button[data-f]").forEach(b=>b.onclick=()=>{document.querySelectorAll("nav button[data-f]").forEach(x=>x.setAttribute("aria-pressed",x===b));'
             'const f=b.dataset.f;(f==="act"?cs.slice().sort((a,b)=>a.dataset.rank-b.dataset.rank):o).forEach(c=>{g.appendChild(c);'
             'c.hidden=f==="fix"&&(c.dataset.rec==="PIDA"||c.dataset.rec==="KESKEN")})});'
             'document.getElementById("ph").onclick=e=>{const on=document.body.classList.toggle("phone");e.target.setAttribute("aria-pressed",on)}</script></body></html>')
    (HERE / "catalog").mkdir(exist_ok=True)
    (HERE / "catalog" / f"{course}.html").write_text("\n".join(h))


def counts():
    L = ["| Kurssi | Kuvia | Arvioitu | Pidä | Kevyt korjaus | Piirrä uudelleen | Korvaa | Fysiikan virhe | Arvioimatta |", "|---|---|---|---|---|---|---|---|---|"]
    tot = [0] * 8
    for p in sorted((HERE / "data").glob("*.tsv"), key=lambda p: int(re.sub(r"\D", "", p.stem))):
        rs = rows(p.stem)
        c = [len(rs), sum(r["rec"] != "KESKEN" for r in rs)] + [sum(r["rec"] == k for r in rs) for k in ("PIDA", "KEVYT", "UUSI", "KORVAA", "VIRHE", "KESKEN")]
        tot = [a + b for a, b in zip(tot, c)]
        L.append(f"| [{p.stem}]({p.stem}.md) | " + " | ".join(map(str, c)) + " |")
    L.append("| **Yhteensä** | " + " | ".join(f"**{x}**" for x in tot) + " |")
    (HERE / "COUNTS.md").write_text("# Arvioidut kuvat kursseittain\n\nTuotettu skriptillä `build.py`; älä muokkaa käsin.\n\n" + "\n".join(L) + "\n")


if __name__ == "__main__":
    for c in (sys.argv[1:] or [p.stem for p in (HERE / "data").glob("*.tsv")]):
        rs = rows(c)
        bad = [r["id"] for r in rs if r["rec"] not in REC]
        assert not bad, bad
        md(c, rs); catalog(c, rs); print(c, len(rs))
    counts()
