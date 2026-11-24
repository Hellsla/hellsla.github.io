VERDICT: PASS
CONTENT-HASH: d458f829079223e4

## Blocking

## Polish
- inquiry.json simulaatio `howto` — even at "normal" the display runs at 0.25 × real time (sim.js `SLOW`; slow/fast 0.125/0.5), so a $2.0\,\text{Hz}$ coil is seen turning once every $2\,\text{s}$. That can blur what "rotation frequency" means. Fix: add one clause, e.g. "even at normal speed the rotation is shown slowed down; the readings and the time axis are model time".
- inquiry.json simulaatio `calc` — "at the moment $t = 0$ it [θ] is zero" holds only after a reset. When a control changes, sim.js starts the new sweep from the angle already reached (`th0`), so that sweep's Φ graph does not start at $BA$. Fix: "θ = 0 at the start (and after Aseta alkutila); a change of control continues from the angle reached".
- lesson.md:232 — the phrase "a frequency converter changes the voltage of the generator to the grid frequency" describes full-converter turbines. A doubly-fed machine converts only the rotor's part. This is a fair simplification (C) and is noted only for accuracy.

## Checked
- Sim physics: Φ = BA cos θ, with e taken from a central difference of Φ (factor 1 − 10⁻⁷). The peak search finds the exact T/4 sample. Velocity arrows lie along the normal. The cross/dot from q v × B agrees with the sign of e (checked at θ = 90°; screenshot at θ = 78°: e = 2.46 V = 2.513 sin 78°). simState has the keys e0 and T. The f slider (step 0.5) and the B slider (step 0.05) reach every value the experiments ask for.
- Experiments: koe-1 locks N and B and varies f; koe-2 locks N and f and varies B. Both isolate the varied parameter. reset gives θ₀ = 0.
- I recomputed every number in one script with my own formulas: worked example 6.786 V / 4.798 V; koe values 1.26, 2.51, 5.03, 1.257, 3.770 V; e₀/f = 1.26 V·s; siirto 15.99 V; the four siirto mistakes (22.62, 959.7, 31.99, 2.546); kettle 8.696 / 12.30 / 6.149 A; 325 V and 163 V; 0.20 Hz; 0.0020 Wb; 0.050 s; 1.4 A; the sim's largest value 18.85 V against its ±20 V axis. All agree. The statistics are consistent with each other (19.8 TWh / 24 % ≈ 82 TWh).
- Phi–e figure: Φ is a cosine from BA and e is a sine with its peak at T/4, matching e = −N dΦ/dt. The small coil pictures show the right orientations.
- Derivation figure: θ is the angle between v and B, v sin θ is the perpendicular component, and the current symbols (lower right into, upper left out) agree with v × B.
- Derivation: v = πfb, two sides, lb = A gives e₀ = NBA·2πf, with θ the same as the normal–field angle used in the formula.
- Power figure: P₀ sin², mean ½P₀. The resistive / in-phase condition for P = UI is stated, with the power factor mentioned.
- Predictions: exactly one option is correct in each. Every distractor's feedback names the right mechanism (rate of change, not size; same ΔΦ in half the time).
- virhe, check-1, tarkistus-2 and the exit ticket are consistent with the theory. The sig-fig reasons are correct (230 V has three figures).
- Scope: generator, alternating current, rms values and wind power are inside the FY7 contents. There is no self-induction or impedance beyond a mention of the power factor.
