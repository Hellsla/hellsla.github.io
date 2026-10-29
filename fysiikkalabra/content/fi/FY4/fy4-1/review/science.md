VERDICT: PASS
CONTENT-HASH: 37d95c045210014f

## Blocking

## Polish
- inquiry.json:448 (siirto, mistake 50) — "alkupaikka on noin $-11\,\text{m}$": it is exactly −11 m from the given data (4,0 m − 5,0 m/s · 3,0 s); drop "noin". (carried from round 2)
- assets/sims/fy4/fy4-1/sim.js:1248 — the control "Nopeus (toisto)" (hidas/normaali/nopea) in a lesson about velocity can be read as the carts' velocity; consider "Toistotahti" (tests/sims/fy4-1.json follows the label). (carried)
- inquiry.json (data, mistake 1,3) — only the first neighbouring pair gives 1,3; the others give 1,7 / 1,55 / 1,25 / 1,65, so the neighbour-pair feedback fires for one pair only (correct where it fires). (carried)

## Checked
- Unit-as-LaTeX commit 212c48d: a script compared every changed hunk (47, all in lesson.md, inquiry.json, exit-ticket.json, exercises.json, solutions.md) old vs new, normalising `{,}`, `\,` and the Unicode minus — the multiset of numbers and of number–unit pairs is identical in every hunk; a word diff confirms each change only wraps the same value and unit (e.g. −5,0 m → $-5{,}0\,\text{m}$, 0–10 s → 0–$10\,\text{s}$). No value, sign or unit changed.
- Round-2 polish on the endpoint mistake (1,9) is fixed: Δx now 19 m − 4,1 m, consistent with "lue piste suoralta".
- One script recomputed every inquiry and lesson number: exp-1 4,0; exp-3 −3,0; data LS slope 1,494 ± 0,029 (intercept 4,10, so x₀ = 4,1 m and "1,49 ± 0,03" hold), line 4,1→19,1 m ⇒ 1,5; siirto 39 (x₀ −11); check-2 13 (origin at 4,8 s); example 2,5 m/s, 170 m = 1,7·10² m; E path 16 m, v_ka 0; pr-nopeus 7,5 / 3000 / 0,13 / 130; pred-3 meeting at 6 s, 12 m — all match lesson-answers.py and the text.
- Ruler label change (39e7459): only the x-position/alignment of "x (m)" moved (598, right-aligned); no physics touched. At 390 px it sits right of the "40" tick without overlap (sim and exp-3 captures); readouts show model values 0,0 / 30,0 m correctly.
- sim.js model unchanged: pos/vel/path give A 0→20 m, B 0→40, C 20→40, D 30→0, E 0→8→8→0 with s = 16 m; simState exposes t, xA, x2 for every experiment; tapaus locked, t varied.
- `model`/`calc` boxes state model values, constant velocity, no friction/acceleration, case 4 exception and Δx = 0 with s ≠ 0 — consistent with the theory and sim-spec.
- Figures to scale where claimed (displacement 40 px/m; jogger; robot data on 11,1 px/m, points and line match the table; E graph).
- Formulas and conditions (uniform motion, x₀ at t = 0), sign conventions (signed Δx, v; non-negative s, |v|) consistent across theory, summary, checks, exit ticket.
- Hash identical at start and end.
