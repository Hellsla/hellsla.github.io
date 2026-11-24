VERDICT: PASS
CONTENT-HASH: db20b0cd98688b14

## Blocking

## Polish
- lessons/FY7/fy7-7/sim-spec.md:1 and assets/sims/fy7/fy7-7/sim.js:861,957 — call the dot/cross "induktiovirta"/"induced current", while the sim's `model` box says no load is connected and no current flows, and `howto` says the symbols show which way the voltage *would* drive a current — say "induktiojännitteen suunta" in the spec and the comments too (internal docs only; the student-facing texts agree).
- exit-ticket.json:7 — "ilman liukurenkaita ja harjoja": a power-station rotor's electromagnet still gets its (much smaller) field current through slip rings or a brushless exciter; the theory's "suuri virta saadaan käämeistä ilman liukukoskettimia" is the precise form — consider "suuri virta … ilman liukurenkaita" so no student reads that the whole machine has none (C as written).
- assets/sims/fy7/fy7-7/sim.js:972 — the e(t) graph has a fixed ±20 V scale; at N = 250, B = 0,05 T, f = 1,0 Hz, e₀ = 0,16 V and the curve is nearly flat. Not wrong (the readout gives the value), but an auto-scaled or two-step scale would let the shape show at every setting.

## Checked
- All numbers recomputed in one script with my own formulas (worked example 6,786 V → 4,8 V; koe-1 1,26/2,51/5,03 V, T = 1,0/0,50/0,25 s; koe-2 1,26/2,51/3,77 V; siirto 15,99 V and its four mistakes; kettle 8,70 A → 12,3 A and its mistake; 325 V; 0,20 Hz; e₀/f = NBA·2π = 1,26 V·s): all agree with lesson-answers.py and the texts; sig figs justified.
- Sim physics: Φ = BA cos θ, e = −N ΔΦ/Δt by central difference (d = 10⁻⁵ s); peak over 720 samples with arbitrary θ₀ = 2,51326 V vs analytic 2,51327 V; formula not used, so the e₀ ∝ f result emerges from the induction law.
- Sim geometry: θ = normal–field angle, side velocity along the normal, × / • follow v × B (checked at θ = 107° in the 1280 px capture: Φ = −0,117 mWb, e = 2,40 V, right side moving up = into page); graph scales hold the largest values (0,6 mWb, 18,85 V).
- Experiments: koe-1 locks N, B and varies f; koe-2 locks N, f and varies B; slider steps reach 1/2/4 Hz and 0,10/0,20/0,30 T; simState gives e0 and T.
- Derivation e₀ = NBA·2πf from e = vBl with v sin θ, two sides, A = lb; derive figure: θ between v and B, v sin θ ⟂ B, current directions agree with v × B.
- Φ(t)/e(t) figure: cos/sin with correct phase and coil end-views; power figure: sin², mean P₀/2.
- Effective value defined by mean power in a resistor; P = UI stated for a resistive load, phase difference/power factor named.
- Predictions: exactly one correct each; distractor feedback names the right mechanism (rate of change, not size of flux; same ΔΦ in half the time).
- Check-1, Etsi virhe, kertaus, explain model answer and exit ticket agree with the theory.
- Scope inside FY7 (generator, AC, effective values); wind and grid-frequency facts plausible (2024 statistics not verifiable offline).
