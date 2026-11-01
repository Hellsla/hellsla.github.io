VERDICT: FAIL
CONTENT-HASH: 50ba844bc762df91

## Blocking

1. **B, the fusion link (causality, consistency).** `unit.md`, *Key idea*, 2nd paragraph: "A charged particle in a magnetic field moves on a circle, just like your electron beam, and a tokamak uses this…". A circle only happens when the velocity is perpendicular to B. The course (`fy14-magnetic-confinement`) teaches a helix that slides *along* field lines, and confinement works because the field lines close inside the torus. Fix: "A charged particle circles around a magnetic field line and slides along it. Your electron beam shows the circling part. A tokamak bends the field lines into closed loops inside the vessel, so the hot plasma stays away from the walls."
2. **B, half range called the uncertainty of the mean (guardrail "Half the range").** `unit.md` *Planning*: "use the mean and take half of the range … as Δx"; `inquiry.json` `vocabulary` ("A simple estimate of Δx") and `check-3` correct feedback. Fix: "…take half of the range as a simple estimate of how much single readings spread, and use it as Δx. It is not the uncertainty of the mean." In `check-3`, keep the option but write "16 is half the range of the single counts. For random counts the spread is typically about √N ≈ 20, which fits."
3. **A, definition of uncertainty.** `unit.md` *Common misconception*: "The uncertainty tells how much the result could change if you repeated the measurement." This covers only random error. It contradicts *Planning* ("how far the true value may be") and the systematic LED-bandwidth error that the worked example and `report-write` list. Fix: "The uncertainty estimates how far the true value may be from the result. Part of it shows as scatter when you repeat the measurement. Systematic errors do not, and repeating does not reduce them."

## Polish

4. `unit.md` *Evidence*, "Spectra and oil drops", and `stations-match`: "always in whole steps of e" is presented as what the qualitative station shows. Write "…has gained or lost charge. Millikan's measurements showed that it changes in whole steps of e."
5. `pred-photons`, last option feedback: "one photon frees one electron" should be "a photon can free one electron" (quantum efficiency < 1).

## Checked

- **Numbers.** I recomputed every number with CODATA constants. LED frequencies 4.797…7.402·10¹⁴ Hz. Fit k = 3.9644·10⁻¹⁵ V·s, b = −1.341 V, h = 6.351·10⁻³⁴ J·s. k_max = 4.192 and k_min = 3.885 (·10⁻¹⁵ V·s), Δh = 0.246·10⁻³⁴, giving (6.4 ± 0.3)·10⁻³⁴ J·s, −4.15 % (shown as −4.2 %).
- **e/m task.** B = 1.1689 mT, e/m = 1.741·10¹¹ C/kg (−1.0 %). The two mistakes give 0.435 and 0.871. r at 1.5 A and 200 V is 4.08 cm, inside Fotoni's range. Helmholtz formula correct.
- **Other numbers.** Δy = 0.758 mm. Wien: 4140 K and 784 nm. Counts: mean 405, half range 16, √N = 20.1. A 1 mm error in r changes r² by ≈ 5 %.
- **Fotoni instructions (WebFetch, 2026-11-01).** LEDs on a vacuum tube, no mercury lamp. The red-LED intensity steps match Prediction 1. The intercept is far from the points. The hot-filament temperature comes from the electrical power, and the sweep reaches 5000 nm, so the infrared peak claim is safe.
- **ITER.** iter.org confirms spectroscopic diagnostics from visible to X-ray, measuring impurity species and ion temperature.
- **Assessment.** Every prediction and check has exactly one correct option, and every distractor's feedback is right. The e/m figure's directions are consistent: for the electron, F = −e v×B points to the centre.
- **Length.** 150 minutes (two 75-minute lessons around the visit) is acceptable for a lab-visit unit. Both lesson plans add up to 75 minutes, and the evidence and key idea come to 438 words.

## Shared issues

None found in the science. The developer's shared issue 4 (pilot `fy14-photoelectric` says "mercury lamp" at Fotoni) is confirmed wrong by Fotoni's instruction.
