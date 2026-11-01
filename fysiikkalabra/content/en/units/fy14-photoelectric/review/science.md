VERDICT: PASS
CONTENT-HASH: b0acda37ffbeec0d

Update 2026-11-01 for two later commits:
- **4ec672e4:** only the y position of the current label changed in sim.js (its baseline is capped inside the canvas). The physics and the readout values are unchanged.
- **ba143d0c:** unit.md and teacher.md now say that the Fotoni photocell station uses LEDs of different colours, which agrees with the fy14-fotoni unit. The planck-data task still uses mercury lines as an invented example, without claiming that Fotoni uses them. Its numbers are unchanged.

Both changes are correct, and the verdict stays PASS.

Science re-review of fy14-photoelectric, 2026-11-01 (updated for the Planck sentence: the law was presented on 19 Oct 1900 and its derivation with energy elements on 14 Dec 1900, both to the German Physical Society; correct). It covers the fixes after review, the new `pred-stop`, `hook-discuss`, the rewritten options and the sim changes.

## Previous findings
All eight are resolved:
1. The misconception now says "most loosely bound electrons at the surface".
2. The worked example shows $4.9049 \cdot 10^{-19}$ J.
3. The seven stage labels follow the guide §3, including "Unit conversions" in planck-data.
4. The fitted-line sentence is in planck-data. My own fit gives $h = 6.60 \cdot 10^{-34}$ J·s and $W = 1.89$ eV.
5. The readout says "$hf \le W$: no electrons leave".
6. The measure labels and the numeric unit are in LaTeX.
7. The electroscope is negatively charged, and the text adds UV-C protection.
8. The calc box notes the rounding of h.

## New content
I recomputed every number with exact constants:
- **pred-stop:** $U_\text{s}$ = 0.120, 0.395 and 1.773 V give the readings 0.12, 0.40 and 1.78 V on the 0.02 V grid. Exactly one option is correct, and each distractor's feedback names the right reason.
- **find-error:** the feedback numbers are 2.48 eV and 0.34 eV.
- **pred-bright, check-1, check-3 and review:** after the options were rewritten, each still has exactly one correct option.
- **Sim model box:** "no time axis; real experiments show no measurable delay" is accurate at this level. Attosecond emission times are not measurable delays in a classroom sense.

## Simulation
I rebuilt the page and checked the sim in Playwright:
- The physics in sim.js is unchanged: same constants, same $I = I_0(1 - eU/E_{\text{k,max}})$, same uniform $E_\text{k}$ spread, same retarding polarity (cathode +, collector −).
- The beam now lands on the cathode's inner face.
- At 300 nm with $U = 1.00$ V the current is 5.2 nA, which matches the model's 5.23 nA.
- At 650 nm the sim shows $I = 0.0$ nA and "no electrons leave the metal".

## Figures
The energy-diagram and $U_\text{s}$–$f$ figures keep the same numbers: 1.91 eV and 3.10 eV, $W$ = 2.36 eV, 0.74 eV, $f_0$ = 5.71 and 10.4 ·10¹⁴ Hz, and a slope of 1.65 V per 4·10¹⁴ Hz.

## French corner
The respellings are sound: *ly-MJÈR*, *ẽ-ne-lek-TRÕ*, *le-ner-ŽI*, *fre-KÃS*. The sentence is grammatical.

## Blocking
None.

## Polish
None.

## Checked
Physics, maths, LaTeX, the 7-step solutions, the sim model and readouts, the figures, history and sources (as in the first review), misconceptions, and assessment correctness.
