VERDICT: PASS
CONTENT-HASH: f1593e0cfff67369

## Blocking
- none

## Polish
- inquiry.json:106 (punnitus, Reasonableness): "5.00 · 0.041 ≈ 0.21 mol of any gas" uses the molar volume before the lesson has given it, so it assumes the result the activity is building towards. Check backwards only, or say that the number comes from later.
- inquiry.json:326 (laske-r, Principle): "the same for all ideal gases, because the gas laws do not depend on the type of gas" is still close to circular. Name the evidence: "because m/M was the same for every gas at the same p, V and T".
- inquiry.json:393 (virhe, third option feedback): `\text{l}` should be `\textsf{l}`, as everywhere else.
- inquiry.json:168 (kokeile, model box): "A change in volume does not change the speeds … so the temperature stays the same" is true of the model. Consider adding "(as in a slow compression in which the gas keeps the temperature of its surroundings)", so the student does not conclude that a real gas compressed quickly stays at the same temperature.
- lesson.md:230: "the temperature in kelvins is directly proportional to the mean kinetic energy". For point particles this is right (C). "Mean kinetic energy of the motion from place to place" would match the guardrail wording used in the other chapters.

## Checked
- delta review 2026-11-07 round 2 (follow-up consistency edits): inquiry 'Find the error' feedbacks: pressure in Pa with m³ (1 Pa·m³ = 1 J) and litres only with kPa (1 kPa·l = 1 J) are correct and match the lesson's 1 kPa·l = 1 J; kPa with m³ gives a factor 1000 error, right; each feedback still says the error is elsewhere, consistent with the step's correct option; litre as \textsf{l} as in the lesson. Hashes equal at start and end.
- delta review 2026-11-07 (teacher's proofread replacement texts): p = absolute pressure, T kelvin temperature; unit argument Pa·m³ = N·m = J and kPa·l = 1000 Pa·0,001 m³ = 1 J are correct and consistent with R = 8,31 J/(mol·K); inquiry and exit-ticket edits are typesetting only, numbers unchanged (exit ticket n = 0,601 mol rechecked). English text carries the same meaning as fi.
- Both blocking items of round 1 are fixed. Key idea now uses a rigid glass flask pumped empty, which matches punnitus. The check-2 Principle now reads "From pV = nRT the average pressure satisfies p ∝ NT/V", with no k and no "at every moment".
- I recomputed every number in one script and it agrees with the lesson and with lesson-answers.py. The checks were the masses against n = pV/(RT) (scatter ≤ 0.022 g), m/M (spread 0.56 %) and the mean 0.2071 mol giving R 8.32. Also checked were laske-r 8.302 with its mistakes 121.7, 8302 and 0.008302, the worked example (0.2073 mol, 0.83 g, 6.0 g, 24.1 l/mol) and virhe (1.2 and 0.083 mol). Siirto gives 91 200 mol and 2645 kg, with mistakes 9870 and 2.64, and 3360 → 2640 kg. The rest are check-c2 1.068, check-2 3.0 (mistakes 2.25 and 1.69), exp-2 50 (mistakes 200, 71 and 25), the exit ticket 0.601 mol and kertaus 200 kPa.
- The taulukko values pV/(NT) are 1.05, 1.00, 0.98, 0.98 and 0.99, and every row can be set with the sliders' steps.
- sim.js: total impulse divided by the perimeter equals NkT/(LxLy). P_REF is consistent with this, the temperature scales as v ∝ √T, the thermalisation after a change of N is exact, and a change of volume leaves the speeds unchanged.
- exp-1 and exp-2 lock T and V and vary N, and simState gives pMeasured and hitRate.
- Every choice item has exactly one correct option. Each distractor's feedback is right, including the pred-1 argument "more frequent but weaker hits".
- Figures: the speed arrows are 2.67 : 1 against √(29/4) = 2.69. The 2T arrows are 1.39× (√2 is 1.41). The particle counts and the halved volume in paine-ja-tekijat are right, and the mole-mass bars are to scale.
- The model's conditions are stated: point particles, no interaction energy, failure at high p and low T, T in kelvins.
- Scope: the FY3 content "ideaalikaasun tilanyhtälö".
