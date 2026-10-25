VERDICT: PASS
CONTENT-HASH: 96b0f0b71d02cb96

## Blocking

## Polish
- inquiry.json:95 (taulukko) — rows 2–4 share W = 20 J at different speeds; for the same stroke a slower (cooler) compression needs less work, so equal W silently means different strokes. ΔT also relies on an unstated c_V ≈ 718 J/(kg·K) — add "puristusmatka valitaan niin, että W = 20 J" and, optionally, name the model's c_V.
- lesson.md:51 — "ΔU = Q + W" in the Kaava SVG is plain text, not LaTeX in a foreignObject as the convention requires — move it to a fig-tex foreignObject.
- exercises.json fy3-5-L3-03 / solutions.md (L3-01, L3-03) — "sisäenergia riippuu käytännössä vain lämpötilasta ja määrästä" holds for an ideal gas; say "ideaalikaasun" (as inquiry does) so the condition is stated.

## Checked
- All 12 answers recomputed independently; match answers.py and exercises.json (L3-02 1,699 → 1,7 m inside 2 %).
- Sign convention ΔU = Q + W (W on the system) consistent in lesson, glossary, solutions, inquiry, exit ticket.
- Worked example: W = +150 J, Q = −40 J, ΔU = 110 J; symbolic before substitution; staged.
- Table ΔT: 27,9 / 55,7 / 22,3 / 0,0 °C reproduced with m = 0,50 g, c_V = 718 J/(kg·K); kaavio 20 → 76 °C consistent.
- kaavio numeric −20 J, mistakes +20 and 0 correct; siirto 5,4 J, mistakes 6,6 and 599,4 correct.
- Fire-piston magnitude plausible (adiabatic r ≈ 20 on ~8 cm³ needs ~5 J, ~1000 K).
- check-2 30 J, mistakes 230 and 10 reproduce the stated errors; check-1 adiabatic expansion cools.
- Predictions' correct options and feedback physics sound (isothermal row 4 refutes "pressure alone").
- All solutions solve symbolically first; units and magnitudes realistic.
- Scope: first law only, no second law; no sim.
