VERDICT: FAIL
CONTENT-HASH: b3f75b21633b9c33

## Blocking
- inquiry.json:137–138 (with sim.js:100–101). Problem: the micro model draws every particle vibrating symmetrically (a pure sine) about an equilibrium point whose spacing is set directly from d₀(1 + EαΔT). So the picture is exactly Cem's account in pred-3 (stronger, symmetric vibration plus larger spacing), which the lesson calls wrong. The sim's text never says this limit. pred-3 is revealed after exp-1, and exp-1 tells the student to watch the micro model, so a student holding Cem's view sees the sim confirm it. Fix: add one sentence to `model` (or `howto`), e.g. "Mikromalli piirtää värähtelyn symmetrisenä ja asettaa hiukkasten keskimääräisen etäisyyden kaavasta; se ei näytä, miksi etäisyys kasvaa (heilahdus poispäin on pidempi kuin heilahdus lähemmäs)." The other option is to make the drawn displacement asymmetric (larger outward than inward).

## Polish
- lesson.md:71 says the formulas are good models for changes of "muutamia kymmeniä kelvinejä". But the sim (ΔT up to 100 K), pred-1 ("tällaisilla lämpötilan muutoksilla α on käytännössä vakio" at 100 K), L1-03 (100 K), L3-01 (100 K) and L3-02 (80 K) go further. For solids, "noin sata kelviniä" or "kymmeniä tai muutamia satoja kelvinejä" would be consistent.
- inquiry.json:115: pred-3 Aino's feedback uses the sim as evidence ("Simulaation mikromallissa hiukkaset ovat samankokoisia…"), but that is an assumption built into the model. Say that the model assumes it, or base the point on the mass and density argument.
- inquiry.json:319: in "Säiliön tilavuus kasvaa vain 1,1 %", the quantity that grows 1.1 % is the ethanol's volume, not the bulb's (the glass grows about 0.03 %). Write "etanolin tilavuus".

## Checked
- All 12 exercise answers were recomputed independently and match answers.py and exercises.json within tolerance (L1-05 0.3375 → 0.34, L2-01 52.08 → 52, L3-03 457 → 460).
- Worked example: 0.0864 m and 0.072 %. The formula is solved symbolically first, and the units are shown.
- Inquiry numbers all check: pred-1/2 (6.00/12.0 mm, 0.0600 %), interpret table (0.36, 2.1, 11, 34 cm³; ideal gas gives 34.1), virhe (28 mm vs 1.8 mm, 0.7 %, ×15), siirto (44 mm; mistakes 0.044 and 110; glass ratio ≈41; 42.9 mm with glass), check-2 (23; mistakes 46 and 15.3), check-3 (air/steel ≈94), exit (21 mm).
- Coefficient tables are realistic at 20 °C (air 3.4·10⁻³ ≈ 1/293 K).
- γ ≈ 3α derivation, the sign convention for cooling, L = L₀ + ΔL, the hole-grows reasoning, and the bimetal bending direction (bends toward the steel) are correct.
- The anharmonic-potential explanation is correct and within FY3 scope (force only as an interaction).
- Water anomaly (density maximum near 4 °C, lakes freeze from the top) is correct in the lesson and check-1. Rail-gap reasoning (ΔL/2 per end, from both neighbours) is correct.
- exp-1 and exp-2 each isolate one parameter. `simState` exposes dT, dL and rel. The initial values reproduce the pred-1/2 numbers.
- Sim: ΔL = αL₀ΔT referred to 20 °C, the "under 0.3 %" statement (max 0.23 %), amplitude ∝ √T, the ×100 exaggeration labelled, chart scaling, 3-significant-figure readouts, and speed affecting the picture only.
- Figures 1 and 2: particles the same size, d > d₀, ΔL marked, exaggeration stated.
