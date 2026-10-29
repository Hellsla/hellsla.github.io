VERDICT: PASS
CONTENT-HASH: 79ffdbfbc7529212

## Blocking

## Polish
- inquiry.json:178, 229, 282, 290 — measure labels still write units as plain "(N)", "(kg)", "(m/s)" after a LaTeX symbol; `$\Sigma F_x$ ($\text{N}$)` would follow the all-LaTeX rule fully (unchanged from round 2).
- lesson.md (Miksi-vastaus, "Lastin paino ei sinänsä vedä autoa taaksepäin") — true on level ground; the hook and figure show a level road (C), "tasaisella tiellä" would make it explicit (unchanged).

## Checked
- Full review; since round 2 only sim.js (phone layout), tests/sims/fy4-4.json and one solution label changed; lesson.md, inquiry.json, figures, exit ticket and lesson-answers.py identical.
- Sim phone layout: model(), pos(), vel(), findEnd(), fit() and simState unchanged; only pixel scales (PX 270 px/m, S 10 px/N) and panel offsets differ, so the motion, the force-diagram proportions (one scale, F short beside G) and the fitted a_x are the same physics at both widths. Largest |v| in any run 4,7 m/s stays on the ±5 m/s axis; G up to 14,7 N fits the 320 px diagram panel.
- Test change: canvas-size assertion now 600×400 wide, 600×(taller) under 500 px; it tests layout, not physics; every physics assertion (a = ΣF/m, sign of a with leftward pull, simState keys) kept.
- 390 px captures: track 0–2,0 m, N up from the bottom face apart from G, F from the side, v blue/a orange beside the cart only, graph axes labelled in LaTeX.
- Recomputed in one script: worked example a = 1,02 m/s² up (10,8 without G); siirto 7000 N, mistakes 25 200 / 5,0 / 13 734; check-2 1,0 (1,67, 2,33); check-3 a = 1,67 m/s², N = 11,8 N; experiment model values 1,0/2,0 and 2,0/1,0 m/s², exp-3 stop at 0,75 s; lesson-answers.py agrees.
- Experiments isolate the varied parameter (locked alku/suunta/m; alku/suunta/F; alku/F/m); simState gives sumFx, a, v, m.
- Valitse: exactly one correct (T > G while slowing on the way down); each distractor one error, feedback right.
- Predictions, check-1, exp-3 question and exit ticket: correct options and feedback consistent with ΣF ∥ a.
- Hash identical at start and end.
