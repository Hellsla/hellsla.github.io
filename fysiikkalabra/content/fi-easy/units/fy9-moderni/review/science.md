VERDICT: PASS
CONTENT-HASH: 65899c5d542677f7
SCOPE: full (asked); changes since the passed version 43cb3edae017c63d: three new ```pysahdy boxes in unit.md, hero and pallo figures as WebP with H-dot labels, one inquiry solution split into paragraphs; Sovella task set untouched

## Blocking
None.

## Polish
- Ydinajatus box "Yksi fotoni antaa energiansa yhdelle elektronille" holds for absorption (photoelectric effect, ionisation), not for Compton scattering, where the photon gives only part of its energy. The unit has no Compton content and the fi text says the same thing, so this is a level-appropriate simplification (C), not a finding. Say it here only if the fi text is ever changed.

## Checked
- The three Pysähdy boxes, against fi `content/fi/units/fy9-moderni/unit.md`. Physics is identical in each, with only the wording made simpler: (1) one photon gives its energy to one electron ("antaa" for fi "luovuttaa"); (2) no electrons come off when $hf < W$, because they only come off when $hf \geq W$ (fi's "koska" sentence is split in two, and the reason is kept); (3) after $2T_{1/2}$, $N = N_0(\tfrac12)^2 = \tfrac14 N_0$, a quarter (fi "hajoamatta" becomes "ei ole vielä hajonnut"). The answer to each box follows from the paragraph just before it, and each agrees with the Yleisiä virheitä list ("Kaksi puoliintumisaikaa…") and with the puolitus figure ($n = 2 \to \tfrac14$).
- Pallo figure: the new $\dot{H}_1$ and $\dot{H}_2$ labels sit on the nearer and the farther sphere, the same as in fi and the same as the aria-label and the derivation. The derivation $\dot{H}_2 = \dot{H}_1 (r_1/r_2)^2$ states its conditions (a point source, radiation even in every direction, no absorption in air).
- Inquiry solution (lead shielding): only the paragraph breaks changed, and the text is word for word the same. Recomputed: $I_0 = 583$, $I = 176$, $d_{1/2} = 5{,}79\,\text{mm} \to 5{,}8\,\text{mm}$. Correcting for the about 6 % absorbed in the aluminium gives $5{,}50\,\text{mm}$, which matches the table's $5{,}5\,\text{mm}$.
- Unit text recomputed: a 660 nm photon has $1{,}88\,\text{eV}$, below water's $12{,}6\,\text{eV}$; $60\,\text{keV}/1{,}9\,\text{eV} \approx 3{,}2 \cdot 10^4$, which fits "yli $30\,000$"; doubling the distance gives $\tfrac14$. The formula sets, symbols and conditions are unchanged from the passed version.
- The Sovella task set is unchanged since the round-2 PASS, in which every value was recomputed. `practice.py check --lang fi-easy` OK (9 tasks, 136 points, the same as fi and en).
- The hash was 65899c5d542677f7 at both the start and the end.
