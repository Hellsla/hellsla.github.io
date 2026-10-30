VERDICT: PASS
CONTENT-HASH: de5a6232952666b9

## Blocking

## Polish
- inquiry.json:497 (check-3 model), :492, lesson.md:386 — "putoaa samalta korkeudelta, joten osuu … samalla nopeudella": a high-jump mattress top is ~0,5–0,7 m above the ground, so the jumper actually lands on it more slowly (which only helps). The hook states equal speed as a premise, so not an error — fix: "oletetaan, että hyppääjä osuu kumpaankin alustaan samalla nopeudella" in the model answer, or "(patjan paksuus jätetään huomiotta)".
- lesson.md:489 vs :550 — F_ka is defined as |Δp|/Δt (a magnitude), but the worked example uses the signed m(v − v0)/Δt and says "Voima on positiivinen" — fix: say in the example that the sign comes from Δp, or define F_ka = Δp/Δt and its magnitude separately.
- lesson.md:559, :566 — "Muutos on 2mv" while Kaava (:514) gives Δp = −2mv — fix: "muutoksen suuruus on 2mv".

## Checked
- Every lesson/inquiry number recomputed in one script with my own formulas (SHM model: Δt = π/2·√(m/k), F_max = v√(mk), bounce Δt = π√(m/k)): exp-1/2/3, predictions, conclusion model, retrieval, Etsi virhe, siirto (+ all 3 mistakes, 400 N, ≈8 kg), check-2 (12 m/s, 24, 5,4, 12 000, 450 N), check-1, worked example (3,48; 870 N; 0,57 N; ×1500; 145 N): all agree.
- Figures to scale: liikemaara (v and p arrow ratios 20:1,5 and 1:1:½), pysaytys (0,0393 s/80 N, 0,157 s/20 N, quarter-sine with drop), kimpoaminen (Δp = 2p0), keskivoima (rectangle = 2/π of half-sine peak), tarkistus-kolmio (900 N, 6/12 ms).
- sim.js: RK4 of F = kc, impulse from trapezoids of every step independent of Δp from velocities; crushable bumper stops at v = 0 (force ends), spring bumper releases at c = 0; graph range 0,5 s/120 N holds the extremes (0,444 s, 113 N; max compression 0,28 m < 0,32 m). Model box states limits (no friction, weight cancels, lossless spring).
- Experiments isolate their varied parameter (locked m, v1, tormays / puskuri); simState gives dt, Fmax, I, v2, dp, p1.
- Each choice item has exactly one correct option; every distractor feedback explains the error correctly.
- Impulse principle derived from N2 for constant net force; variable force via area; conditions (net force, weight neglected in the example with numeric justification) stated.
- Exit ticket: unit identity and braking-impulse direction/magnitude correct.
- Scope: momentum, impulse, impulse principle within FY4 central contents; no conservation/collisions pre-empted wrongly.
