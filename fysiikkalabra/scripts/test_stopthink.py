"""Pysähdy ja mieti (```pysahdy, scripts/stopthink.py): parsing, HTML, and that the translation checks see the block.

  python scripts/test_stopthink.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import stopthink, check_i18n

fails = []
def ok(cond, what):
    if not cond: fails.append(what)
    print(("ok   " if cond else "FAIL ") + what)

F = "Ennen.\n\n```pysahdy\nMikä on $F = 5\\,\\text{N}$?\nToinen rivi.\n---\nViisi newtonia.\n```\n\nJälkeen."
ok(stopthink.parts("Q?\n---\nA.\n") == ("Q?", "A."), "parts: question before ---")
h = stopthink.as_html(F, "Pysähdy ja mieti", "Vastaus")
ok('<aside class="stop-think"><p class="stop-think-label">Pysähdy ja mieti</p>' in h, "HTML: aside with label")
ok('<p class="stop-think-q">Mikä on $F = 5\\,\\text{N}$? Toinen rivi.</p>' in h, "HTML: the question in view, maths kept for the stash")
ok('<details class="stop-think-a"><summary>Vastaus</summary><p>Viisi newtonia.</p></details>' in h, "HTML: answer in details, summary only 'Vastaus'")
ok("```" not in h and h.startswith("Ennen.") and h.rstrip().endswith("Jälkeen."), "HTML: fence gone, text around kept")
ok(stopthink.n_blocks(F) == 1 and stopthink.n_blocks("x") == 0, "n_blocks")
ok(check_i18n.md_shape(F)["stops"] == 1, "check_i18n md_shape counts the block")
fi = "```pysahdy\nVoima $F = 5\\,\\text{N}$?\n---\nKyllä.\n```"
en = "```pysahdy\nForce $F = 5\\,\\text{N}$?\n---\nYes.\n```"
ok(check_i18n.md_shape(fi) == check_i18n.md_shape(en), "a translated block has the same shape (formulas, count)")
sys.exit(1 if fails else 0)
