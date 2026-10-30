"""Tests of scripts/fbdspec.py: specs draw with their physics checked, wrong specs are refused, a text-only
"Voimakuvio" step is found, and the build's markdown keeps the drawn diagram inside its step."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fbdspec, i18n
import markdown


def render_md(text):                                   # build.py's render_md around markdown (importing build.py builds the site)
    text, figs = fbdspec.render(text)
    return fbdspec.restore(markdown.markdown(text, extensions=["fenced_code", "tables", "nl2br"]), figs)

fails = 0
def ok(cond, what):
    global fails
    print(("ok   " if cond else "FAIL ") + what); fails += not cond

def refused(spec, why):
    try: fbdspec.draw(spec, "t"); ok(False, f"refused: {why}")
    except ValueError: ok(True, f"refused: {why}")

GOOD = {
    "a hanging lamp": "G 14,7\nT 14,7 ylös\na 0\n",
    "a book pressed against a wall": "pinta 0\nG 4,9\nF 20 0 työntö\nN 20 @oikea\nF_mu 4,9 ylös @oikea\na 0\n",
    "a sledge pulled at 30°, components": "pinta 0\nG 392\nN 332\nT 120 30\nF_mu 104 vasen\na 0\nakselit 0\nkomponentit T\n",
    "a block sliding down a 30° slope": "pinta 30\nG 98\nN 84,9\nF_mu 20 ylös\na alas\nakselit 30\nkomponentit G\n",
    "a curling stone slowing down": "pinta 0\nG 186\nN 186\nF_mu 1,9 vasen\na vasen\n",
    "a balloon against the ceiling, and a mass on a rope": "pinta 0\nF_noste 0,10 ylös\nG 0,039\nN 0,061 @ylä\na 0\n---\nG 0,10\nT 0,10 ylös\na 0\n",
    "a slope rising to the left": "pinta -20\nG 50\nN 47\nF_mu 17,1 ylös\na 0\n",
}
for name, spec in GOOD.items():
    try: svg = fbdspec.draw(spec, "t"); ok(svg.startswith("<svg") and "aria-label=" in svg and "#c92a2a" in svg, f"draws: {name}")
    except ValueError as e: ok(False, f"draws: {name}: {e}")

refused("G 10\nN 10\na 0\n", "a normal force without a contact surface")
refused("pinta 0\nG 10\nN 8\na 0\n", "forces that do not cancel when a = 0")
refused("pinta 0\nG 10\nN 10\nF_mu 3 vasen\na oikea\n", "a net force against the acceleration")
refused("pinta 0\nG 10\nN 10\nF_mu 3 ylös\na vasen\n", "friction up a level surface")
refused("pinta 0\nG 10\nG 10\n", "two forces with one symbol")

i18n.set_lang("fi")
svg = fbdspec.draw(GOOD["a block sliding down a 30° slope"], "t")
ok("30 asteen kaltevalla" in svg and "kitka" in svg and "kiihtyvyys" in svg, "the text alternative names the slope, the forces and a (fi)")
i18n.set_lang("en"); svg = fbdspec.draw(GOOD["a block sliding down a 30° slope"], "t"); i18n.set_lang("fi")
ok("30-degree slope" in svg and "friction" in svg, "the text alternative is in the page language (en)")
ok("pitemmiksi" in fbdspec.draw("pinta 30\nG 98\nN 84,9\nF_mu 5 ylös\na alas\n", "t"), "a tiny force drawn longer than to scale is said so")
L = fbdspec.LENGTHS; svg = fbdspec.draw(GOOD["a curling stone slowing down"], "t")
ok("eri mittakaavassa" in svg and "pitemmiksi" not in svg and abs(L["F_mu"] - fbdspec.SPLIT * L["G"]) < 1e-6,
   "a level surface with a weak horizontal axis gets its own scale by itself")

L = fbdspec.LENGTHS
fbdspec.draw("pinta 30\nG 81,6\nN 70,7\nF_mu 25,8 ylös\na alas\nakselit 30\nkomponentit G\n", "t")
ok(L["F_mu"] < L["G_x"] and abs(L["N"] - L["G_y"]) < 0.1, "one scale for forces and components: friction shorter than G_x, N equal to G_y")
fbdspec.draw("pinta 0\nG 900\nN 900\nF 620 oikea\nF_i 380 vasen\nF_r 240 vasen\na 0\n", "t")
ok(abs(L["F"] - L["F_i"] - L["F_r"]) < 1e-6, "a sum of forces is drawn as a sum")
svg = fbdspec.draw("pinta 0\nerikseen\nG 12000\nN 12000\nF 620 oikea\nF_i 380 vasen\nF_r 240 vasen\na 0\n", "t")
ok(abs(L["F"] - L["F_i"] - L["F_r"]) < 1e-6 and abs(L["F"] / L["G"] - fbdspec.SPLIT) < 1e-6 and "eri mittakaavassa" in svg,
   "`erikseen`: the horizontal forces on their own scale, still a sum, and the text alternative says so")
svg = fbdspec.draw("pinta 0\nG 784,8\nN 784,8\nF 24 oikea kitka\nF_v 18 vasen\nF_r 6,0 vasen\na 0\n", "t")
ok("kitka" in svg and abs(L["F"] - L["F_v"] - L["F_r"]) < 1e-6, "`kitka` makes another symbol a friction force (from the surface), the sum still drawn")
refused("pinta 20\nerikseen\nG 10\nN 9,4\nF_mu 3,4 ylös\na 0\n", "`erikseen` on a slope")
ok(fbdspec.missing("**Voimakuvio:** Paino alas ja tukivoima ylös.\n**Kaava:** $N = mg$") != [], "a text-only Voimakuvio step is found")
ok(fbdspec.missing("**Voimakuvio:** Kappale suorakulmiona.\n```voimakuvio\nG 1\nT 1 ylös\na 0\n```\n**Kaava:** $T = mg$") == [], "a step with its diagram passes")

md = "**Voimakuvio:** Lamppu suorakulmiona.\n```voimakuvio\nG 14,7\nT 14,7 ylös\na 0\n```\n**Kaava:** $T - mg = 0$"
html = render_md(md)
ok('<div class="fig fbd"><svg' in html and "FBDTOKEN" not in html and "```" not in html, "the build draws the spec in place of its block")
ok(html.index("Voimakuvio") < html.index("<svg") < html.index("Kaava"), "the diagram stays inside its step")
a, b = fbdspec.render(md)[1].values(), fbdspec.render(md.replace("Lamppu", "Lamp"))[1].values()
ok(list(a) == list(b), "the same spec draws the same figure whatever the text around it (every language)")

print("ok every force-diagram spec test passed" if not fails else f"{fails} failed")
sys.exit(1 if fails else 0)
