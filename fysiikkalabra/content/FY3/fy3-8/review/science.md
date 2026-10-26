VERDICT: PASS
CONTENT-HASH: 430952439731068d

## Blocking

## Polish
- lesson.md:173 — "enintään noin sata kelviniä" is right for metals (α near-constant over 100 K, as L1-03 and L3-01 use), but water's γ changes sign at 4 °C and grows strongly with temperature; "kiinteillä aineilla enintään noin sata kelviniä, nesteillä vähemmän" would match the L1-04 remark in solutions.md.
- inquiry.json olomuodot — the correct option still credits the gas's large expansion to weak bonds only; at constant pressure the cause is V ∝ T (next chapter); the lesson's pointer to *Kaasujen tilanmuutokset ja Boylen laki* could be repeated in the feedback.
- lesson.md:102 (figure particles) — amplitude arrows are symmetric; outward-longer arrows would match "heilahtaa kauemmas naapuristaan kuin lähemmäs" (the sim's symmetric swing is now disclosed in inquiry.json simulaatio.model and Bea's feedback, which settles the round-1 sim item).

## Checked
- Conversion check: word-diff of exercises.json, exit-ticket.json, inquiry.json and lesson.md against the pre-figure-pass version — only symbols wrapped in maths, `·`→`\cdot`, `1/K`→`\tfrac{1}{\text{K}}`; every number, coefficient and sign unchanged; numerals of solutions.md identical apart from the LaTeX exponents.
- All 12 answers recomputed from task text: answers.py = my values; exercises.json within tolerance (2,88→2,9; −51,75→−52; 52,08→52; 3,024→3,0; 457→460).
- Worked example 0,0864 m ≈ 86 mm, 0,07 %; symbolic first; units.
- Predictions: 6,00 / 12,0 mm, 0,0600 %; correct options right, wrong-option feedback sound.
- olomuodot 0,36 / 2,1 / 11 / 34 cm³; virhe 27,9 mm vs 1,84 mm, ×15; siirto 44 mm, mistakes 0,044 and 110, glass-corrected 42,9 mm, ratio 41.
- check-2 23·10⁻⁶ 1/K, mistakes 46 and 15,3; check-3 ratio ≈ 94 ("noin sata"); exit ticket 21 mm.
- Volume figure: V₀ bracket from cold surface to bulb bottom in both flasks, ΔV is the rise above the dashed cold level; labelled exaggerated.
- sim.js speed control scales only the vibration clock tAnim; dT, dL, L, rel, spacing independent of time and speed; simState keys for exp-1/exp-2 unchanged; max change 0,23 % < 0,3 % as stated.
- Experiments isolate T (exp-1, material and L₀ locked) and L₀ (exp-2, material and T locked).
- Moved sim note (L₀ at 20 °C, particles keep size, thin lines, dashed 20 °C) now in howto and readout; nothing lost.
