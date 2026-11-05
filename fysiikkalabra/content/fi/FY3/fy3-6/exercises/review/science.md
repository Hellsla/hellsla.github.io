VERDICT: PASS
CONTENT-HASH: 3dd71e954a48a7f8
Round: 1 (YO-skill task)

Scope: the new task L2-08 (find the error, added 2026-11-05). The rest of the set and answers.py are unchanged since the round-2 PASS.

## Blocking
- none

## Polish
- solutions.md L2-08 "Oikein: levy luovuttaa ympäristöön $243\,\text{kJ}$" and the option-4 feedback. $m = 3{,}0\,\text{kg}$ has two significant figures, so the stated result should be about $2{,}4 \cdot 10^2\,\text{kJ}$. Fix: "noin $240\,\text{kJ}$ ($2{,}4 \cdot 10^2\,\text{kJ}$)". Row 3's intermediate value can stay.
- exercises.json L2-08 row 3 substitutes without units. The feedback calls this acceptable ("Perusyksiköillä…"), but a strict reader might pick row 3 for it. Optionally add the units, so that row 4 stays the only defensible choice.

## Checked
- My own script gives Q = 450 · 3,0 · (−180) J = −243 000 J. Rows 1–3 are correct, and row 4 is the only wrong line: a negative Q is allowed, and the plate gives energy away. "Laskussa ei ole virhettä" is last, as the schema requires.
- Every option's feedback is correct. Row 1 catches the lesson's "+273 for ΔT" mistake. Row 3 and row 4 catch the "Q is always positive" mistake. The sign convention matches the brief ("jäähtyessä negatiivisia").
- The conditions are stated: there is no phase change, so Q = cmΔT holds. The value c = 450 is given and matches the lesson's table.
- The correct option is not identifiable by form. The four "Rivi n: …" labels have the same pattern and similar length.
- Inline chains: "ΔT = 40 °C − 220 °C = −180 K" and "Q = 450 · 3,0 · (−180), eli Q = −243 000 J" are each under about 300 px, and the second breaks at "eli".
- Renders: I viewed review/shots/fy3-6-open-exercises-L2-1280-11.png and -12.png (after the commit). The options are shuffled and the wrong-option feedback shows. I checked the phone width from the text only.
- The hash was the same at the start and at the end.
