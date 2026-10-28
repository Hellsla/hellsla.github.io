VERDICT: FAIL
CONTENT-HASH: d175129d0f7ac9c5

## Blocking
- inquiry.json:96 (ennuste-2, "Noin tuhat vuotta") — $6 \cdot 10^{23}\,\text{J}$ is not "koko Auringon energia yhden sekunnin aikana" ($3{,}8 \cdot 10^{26}\,\text{J}$, about 600 times more) — say it equals about a thousand hours (about 40 days) of sunlight on the Earth.
- inquiry.json:328 (tarkistus-2, mistake 0.1) — 0,1 is $1{,}0 : 10$ without converting, not the inverted ratio (0,01) — make the feedback about the missing conversion.
- inquiry.json:274 (siirto, mistake 51000) — 51 000 is the right answer in MJ, not "0,30 TJ = 300 000 GJ" (that gives a negative number) — the feedback should say $51\,000\,\text{MJ} = 51\,\text{GJ}$.
- lang/fi.json:194 and sims.fy2-2 `s_*` (readout) — the teacher's rule requires LaTeX for readout values, but the source lines show numbers and units as plain text ("32 MJ", "1361 W/m²", "46 MJ/kg", "3600:lla", "1600 MW") — write each as `$…$`, as `s_uraani` already does.

## Polish
- lesson.md:69 — $1\,\text{J} = 1\,\text{N}\cdot\text{m}$ brings in force and work (FY3); drop it.
- inquiry.json:270 — mistake 50.7 is unreachable and inside the tolerance; delete it. The rounding cites significant figures for a subtraction where 300 GJ is known only to 10 GJ.
- inquiry.json:259 — 360 GJ a day is an average 4,2 MW, high for one turbine; say "tuulivoimapuisto".
- inquiry.json:241 — "kilo on tuhat joulea" → "kilo tarkoittaa tuhatta".
- lang/fi.json:201 `s_sydan` — 1 J is the beat's mechanical output, not what the heart "needs". `s_bensiini` names no source (Tilastokeskus: 43 MJ/kg at 0,75 kg/l).

## Checked
- lesson-answers.py recomputed: 340 kJ, 3,2, $6{,}25 \cdot 10^{20}\,\text{J}$, 66 MJ, 51 GJ, 100, 2500 J.
- All 28 sim values recomputed, with sensible source/estimate labels.
- Web-verified: Tilastokeskus 2023 79,8 TWh and 1,32 million TJ; OL3 1600 MW; Energy Institute 620 EJ.
- Figures to scale (log ladder, Sankey 450 = 110 + 340).
- Experiments: names match, simState gives E_MJ and k (20,79).
- Worked example: symbolic first, substitution, real check.
- Scope and form: no FY3/FY4 content, no ×, LaTeX canvas.
