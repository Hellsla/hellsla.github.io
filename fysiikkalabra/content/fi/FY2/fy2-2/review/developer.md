VERDICT: DONE

Fix, round 1. `check_lesson.py fy2-2`: every line ok.

- `lesson.md`: Kaava is now "Energian yksikkö ja kerrannaisyksiköt" (prefix display, substitution, magnitude ladder); conservation only recalled in Ydinajatus with a reference to the previous chapter; "1 J = 1 N·m" dropped; misconception sum changed to 1,5 MJ + 300 kJ; numbers with units in LaTeX.
- `figures.py`: Sankey uses porridge 800 = 200 + 600 kJ (not the example's numbers) and sits in Ydinajatus; ketju gets a "kasvi" label.
- `inquiry.json`: ennuste-2 gets a premise and correct "tuhat vuotta" feedback (about 1000 h ≈ 40 days of sunlight); koe-2 records $E$ in EJ, no $k$; johtopäätös model 620 EJ; siirto: tuulivoimapuisto, 0,300 TJ, 50.7 removed, 51000 feedback = answer in MJ, rounding by the gigajoule; tarkistus-2 0.1 feedback about the missing conversion, colon division; virhe "kilo tarkoittaa tuhatta"; howto without slider; numbers with units in LaTeX.
- `sim.js` / `lang/fi.json`: slider removed (Kohde + ▲▼ remain), 17 px canvas text, window of about 2,4 powers, rungs named by prefix, value under the selected name; readout "Lähde: …" with LaTeX numbers; s_sydan, s_bensiini (Tilastokeskus 43 MJ/kg, 0,75 kg/l) fixed; `E_EJ` in simState.
- `tests/sims/fy2-2.json`: slider checks replaced by button and clamp checks; E_EJ, readout and label-size assertions added.
- `lesson-answers.py`, `sim-spec.md`, `exit-ticket.json` (joulea, LaTeX) updated.

Not fixable here: glossary "joule" still says 1 J = 1 N·m (shared with FY3).
