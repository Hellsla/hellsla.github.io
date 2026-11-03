VERDICT: PASS
CONTENT-HASH: 9e04d532454b24f2

## Blocking

## Polish
- lessons/FY7/fy7-7/sim-spec.md:1 and assets/sims/fy7/fy7-7/sim.js:176,272,278 (comments) — still say "sivujen induktiovirta näkyy pisteenä tai ristinä" / "induced current". Not student-facing, but the spec should match the fixed howto, model box and note ("induktiojännitteen ajama virran suunta").
- lesson.md:316 (figure `derive`) — labels the current I and its caption says "virta kulkee"; fine because the Ydinajatus generator has a lamp (C), but the sim with the same view now has no load. "jos piiri on suljettu" in the caption would keep the two pictures apart.
- lesson.md:352 and 447 — U = U₀ : √2 still without "sinimuotoisella" (C here; the glossary and virhe say it).
- inquiry.json:104 — "Animaation nopeus muuttaa vain esityksen tahtia" while "normaali" already runs at 0,25 × real time (sim.js SLOW); say the motion is slowed.

## Checked
- Round-1 blocker fixed: howto (risti/piste = suunta, johon induktiojännite ajaisi virtaa, jos kytkettäisiin kuorma), model box (ei kuormaa, ei virtaa, ei voimaa; symbolit näyttävät vain jännitteen suunnan) and sim note ("jännite e ja sen suunta") now agree.
- Direction of × / • recomputed from v × B in the canvas frame (θ = 141° in the 1280 px capture: upper side ×, e = +1,58 V = 2,51 V · sin 141°, Φ = −0,311 mWb).
- Φ = BA cos(2πft), e = e₀ sin(2πft), e₀ = NBA·2πf; derivation from e = vBl (v = πfb, two sides, lb = A) consistent with sim (central difference, no peak formula) and figures.
- Worked example 6,786 V → 4,8 V; rounding and order-of-magnitude check real.
- koe-1/koe-2 isolate f and B; model values 1,26 / 2,51 / 5,03 V and 1,26 / 2,51 / 3,77 V; e₀ : f = NBA·2π ≈ 1,26 V·s; simState has e0, T.
- Predictions: exactly one correct each; distractor feedback right.
- siirto 15,99 V and its four mistake values; tarkistus-2 12,30 A, mistakes 8,70 and 6,15 A; virhe 325 V.
- Mains 325 V, 100 reversals/s; wind 19,8 TWh ≈ 24 %, 4,55 MW/turbine, 12 r/min.
- lesson-answers.py output equals my own recomputation.
- Exit ticket and tarkistus-3 model answer match the theory.
