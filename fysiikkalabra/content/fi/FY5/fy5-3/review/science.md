VERDICT: PASS
CONTENT-HASH: b8e74f9726d4330d

## Blocking

## Polish
- assets/sims/fy5/fy5-3/sim.js:863 — after the release, `before = state(t - dtStep)` still lies on the circle for the first T/12, so the readout and the panel show a nonzero |Δv̄| for that interval. inquiry.json:238 says "katkeamisen jälkeen Δv̄ oli nolla". That is true once T/12 has passed, and the run always lasts longer than T/12 (τ > T/12 for every r and T the sliders allow) — fix: clamp `before` to the release state (`max(t - dtStep, rel.t)` gives Δv̄ = 0 straight away), or add "hetken kuluttua" to the model answer.
- inquiry.json:401 — the 4th criterion of tarkistus-3 asks students to mention gravity curving the path, but the prompt asks only about direction and timing. A criterion should ask only what the task asks — fix: drop it, or add "miltä lento näyttää sivulta" to the prompt.
- lesson.md:260 — the aria-label says "kaksi kohtaa A ja B ovat samalla säteellä". This clashes with A at r and B at 2r, because *säde* also means the distance — fix: write "samalla keskipisteestä lähtevällä suoralla".

## Checked
- One script recomputed every number in the lesson, inquiry, exit ticket and sim: Esimerkki 29 m/s, siirto 29,9 km/s with its mistakes, tarkistus-2 72,0 m/s with its mistakes, Etsi virhe 13 / 6,6 / 26, sim 1,57 / 3,14 m/s, |Δv̄| 1,63 m/s, exit 0,25 1/s, 4,0 s, ×3. All agree, and so does lesson-answers.py.
- Definitions match the glossary. There are no angular quantities, so the lesson is in scope.
- Causality: no horizontal force after the break, so by N1 the puck goes along the tangent. Nothing says a force pushes outward.
- The figures are to scale. Tangent: 4 equal tangent arrows, CCW. Release: equal spacing. Δv̄: v̄ ⟂ r, Δv̄ points inward. Two-radii: 1:2 radii and arrows. Hero: arrow ratio 2,0.
- The ennuste-1 option figures match their texts, and exactly one is correct.
- sim.js: exact circle, straight-line release, board time τ = √(R²−r²)/v, α from the actual displacement. simState gives every measured key.
- Experiments: each locks the right parameter and isolates the varied one.
- Every choice item has exactly one correct option, and each distractor's feedback is right.
- Hash checked at the start and the end.
