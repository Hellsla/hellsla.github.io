VERDICT: FAIL
CONTENT-HASH: 6adb7baad5ee0a31

## Blocking
- [Major] Tutki, experiments 1 and 2 (exp-exp-1-390-1, exp-exp-2-390-1, exp-exp-1-390-2, contact #28/#30) — the Finnish word "tilanne" appears in English text: "Initial state: tilanne: cart and hanging mass", "Kept constant: tilanne, mass of the hanging mass", and in the status line "Initial state set. Kept constant: tilanne, mass m2..." — an English reader meets an untranslated Finnish parameter name in the instructions, three times per experiment — render the parameter's English label ("situation") in every English string that prints the control names (inquiry.json "tapa" values and the sim's status message).
- [Major] Simulation, two-hanging-bodies situation (exp-exp-2-390-1, contact #30) — the two free-body diagram captions in the canvas read "Voimakuvio: m1" and "Voimakuvio: m2" in Finnish, while the cart situation shows "Free-body diagram: cart" — Finnish labels on an English page, and inconsistent with the other situation — use the English caption ("Free-body diagram: m1"); the source is the hard-coded `\text{Voimakuvio: }` string in assets/sims/fy4/fy4-13/sim.js line 179.

## Polish
- [Minor] fig-5-390, fig-6-390, sim-390 — figure and canvas labels (T, G, N, m) fall to roughly 8–9 px at 390 px width; legible but small — enlarge label font in the figures or crop the viewBox.
- [Minor] fig-6-390 — the label m2 sits lower than m1, so the pair reads as unaligned — align both labels on one baseline.
- [Minor] open-exercises-L2-1280-1 (crane figure) — label T1 touches the caption "free-body diagram: upper", and G1/T2 sit on the dashed divider just above the "lower" caption — add vertical space between the two diagrams.
- [Minor] open-exercises-L3-1280-3 — the formula runs "When T = Tmax: Tmax(m1+m2) = m1m2g, so" as one inline string followed by a boxed display fraction — split into display lines at the "so".

## Checked
- Contact sheets 1–6; top-390, sim-390, sim-1280 (via contact), fig-1, fig-5, fig-6, fig-8 at 390; example-390 (contact #7–#9), exp-exp-1 and exp-exp-2 at 390 (full size); theory and open states at 1280 via contact sheets #35–#45; exercise levels 1–3 via contacts #46–#64 plus L1-1, L2-1, L3-3 at full size.
- Rendered page text (site/en/fy4-13.html) searched for Finnish words: only "tilanne" remains; the figure alt texts on the page are English.
- Maths typesetting (KaTeX, units, aligned chains, vectors with overline, LaTeX units in prose) is clean in lesson and example; figure colours follow the convention (force red, velocity blue, acceleration orange).
- Content hash 6adb7baad5ee0a31 at start and end.

## Scores
illustrations 4 · typography 5 · Finnish (English-page leaks) 2 · accessibility 4
