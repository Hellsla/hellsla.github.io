VERDICT: PASS
CONTENT-HASH: b771002b9af91a64

## Blocking

## Polish
- sim.js:102 — `fi` is no longer called since the readout moved to TeX (`tx`), and `lastT` (sim.js:20) is still unused; remove both.
- sim.js:57, 71–74 — the readout shows the measured pressure from the first frame, when the window holds one step (the 390 px capture shows "p ≈ 0", the 1280 px one 89 against theory 100). Show "–" until the 90-step window is full, or start the window full by running 90 steps in setup.
- inquiry.json:141, 179 (exp-1, exp-2 intro) — still "pari sekuntia": at "hidas" the 1,5 s window takes 3 s of real time to refresh; "muutama sekunti" would be safer (carried over from the previous review).

## Checked
- LaTeX conversion of sim.js: only the strings changed (`tx` gives a TeX decimal comma `{,}`; the minus is TeX math minus). The physics lines (speed ∝ √T, wall momentum per time per effective length, pRef, pTheory = 100·(T/300)/V, θ = T − 273,15) are unchanged; renaming the thermometer x from `tx` to `thx` avoids a name clash and moves nothing.
- Readout values: 300 K → 27 °C (26,85 rounds to 27); 100 K, 0,5 dm³ → −173 °C, theory 66,7 → 67; v = 1,00·v₃₀₀ K at 300 K. The screenshots show these values rendered by KaTeX, with units right.
- tests/sims/fy3-3.json: the two rewritten assertions check the same numbers (27 °C at 300 K; −173 °C and theory 67 at 100 K, 0,5 dm³) in the TeX string via `simText`; the only thing dropped is the check of the Unicode minus sign, which is typography, not physics. The slider-unit check (/K/, /dm/) still holds on the rendered text. No physics check was lost or loosened.
- All 12 exercise answers recomputed independently = answers.py = exercises.json (L1-05 −270,45 → −270; L2-04 3,996 → 4,0; L3-03 −126,6 → −127); solutions symbolic first.
- Worked example: k = 0,37 kPa/°C, θ₀ = −270 °C (least squares −271 °C); the liquefaction caveat is stated. Extrapolation and kelvin figures to scale.
- Inquiry: pred-1 600/300 = 2.00, vRel 1,41; pred-2 50 → 100 at vRel 1,00; virhe 128,2 kPa; siirto 121,7 → 122 kPa, mistakes 404 and 83,8; check-2 −273 °C; misconception 293/283 = 1,035.
- exp-1 locks V and varies T; exp-2 locks T and varies V; simState gives theta, vRel, pRel and pTheory.
- The scope stays inside FY3, and p ∝ T is stated with its conditions (constant V and n).
