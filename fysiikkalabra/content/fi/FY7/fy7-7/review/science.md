VERDICT: FAIL
CONTENT-HASH: f736e8dbc2f04541

## Blocking
- inquiry.json:104–105 (sim `howto` and `model`), assets/sims/fy7/fy7-7/sim.js:9,105 and its note "Violetti: jännite e ja virta" — **A, internal contradiction**: the model box says no load is connected ("käämiin ei ole kytketty kuormaa, joten pyörittämiseen ei tarvita voimaa"), so no current flows in the coil, yet the howto and the sim show "sivut, joiden induktiovirta kulkee paperiin päin (risti) tai paperista ulos (piste)". A student is told current flows in an open coil. — Say what the symbols really show, e.g. howto: "…ympyrät ovat käämin sivut; risti ja piste näyttävät, mihin suuntaan induktiojännite kuljettaisi virtaa, jos käämiin kytketään kuorma"; sim note "Violetti: jännite $e$ ja sen ajama virran suunta". (The direction itself is right, v × B.)

## Polish
- lesson.md:351–356 and 447 — U = U₀ : √2 is given without "sinimuotoisella"; the glossary and the virhe item say it. Add the word once in Tehollinen arvo and in the summary (C in this lesson, where every voltage is sinusoidal).
- inquiry.json:104 — the howto says the animation speed only changes the pace, but even "normaali" runs at 0,25 × real time (sim.js SLOW); say the motion is slowed so the student does not read 2 Hz as the true pace.

## Checked
- Φ = BA cos(2πft), e = e₀ sin(2πft), e₀ = NBA·2πf; derivation from e = vBl (v = πfb, two sides, lb = A) and θ consistent between Kaava, sim (normal–field angle) and figure.
- Figures 8, 10: phase of Φ and e, coil icons, v ⟂ coil plane, × / • directions agree with v × B.
- Worked example 6,786 V → 4,8 V; rounding and order-of-magnitude check real.
- Sim: e from central difference of Φ (no peak formula), peak by 720 samples (error < 10⁻⁵); simState has e0, T; koe-1/koe-2 isolate f and B; model values 1,26 / 2,51 / 5,03 V and 1,26 / 2,51 / 3,77 V recomputed.
- Predictions: exactly one correct each; distractor feedback right (flux change BA → −BA unchanged per turn).
- siirto 15,99 V and all four mistake values; tarkistus-2 12,30 A, mistakes 8,70 and 6,15 A.
- Mains 325 V, 100 reversals/s, Fingrid 49,9–50,1 Hz; wind 2024 figures self-consistent (19,8 TWh ≈ 24 % of ≈ 82 TWh; rotor 12 r/min = once per 5 s).
- Exit ticket and tarkistus-3 model answer match the theory.
- Exercises: see exercises/review/science.md (no blocking).
