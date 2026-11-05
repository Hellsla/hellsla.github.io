VERDICT: PASS
CONTENT-HASH: b76bee1182410114

## Blocking

## Polish
- L2-07 b) does the same calculation as the existing L3-03 (two points on the E_k,max(f) line → f0, then W), one level lower. This is not a duplicate, because part a) is the error analysis. Still, L3-03 now reads as easier than a level-3 task.
- L1-07 is tagged `kind: data`, but it has no data table. It is a one-formula calculation plus a comparison, so `reasoning` (or no kind) fits.
- L3-04 caption: "kahdella valotehoilla" → "kahdella valoteholla". The Annettu line lists e = 1,602·10⁻¹⁹ C, but the task text gives only 1 eV = 1,602·10⁻¹⁹ J. Add e to the task text, or say in the solution that the two are the same number.
- L2-07 Vastaus: "kolme merkitsevää numeroa kuten datan energioissa": 0,55 eV has two significant figures. Say "sadasosan tarkkuudella" instead.

## Checked
- Recomputed every new answer in one script with my own formulas: L1-07 f0 = 5,561·10¹⁴ Hz (λ0 = 539 nm, red 650 nm gives 1,91 eV < 2,30 eV) ✓; L2-05 least-squares slope 4,195·10⁻¹⁵ V/Hz → h = 6,72·10⁻³⁴ J s, f0 = 5,57·10¹⁴ Hz, W = 2,34 eV. Residuals ≤ 0,018 V; the tolerance includes 6,626·10⁻³⁴ ✓. L2-06: differences 0,89/0,91/0,90/0,91 → 0,90 eV with W_B > W_A (W_A ≈ 2,30, W_B ≈ 3,20 eV), and both thresholds lie below 8,0·10¹⁴ Hz ✓. L2-07: the three points are collinear; k = 4,133·10⁻¹⁵ eV/Hz, f0 = 5,17·10¹⁴ Hz, W = 2,137 eV ✓. L3-04: photon 3,100 eV, U_s = 0,80 V (zero current from −0,80 V down), W = 2,30 eV, η = 0,0930 % at both powers ✓. L3-05: A 2,64 eV and C 3,40 eV release electrons, B 2,00 eV does not; I = 1,516 + 0,294 = 1,810 µA; U_s = 1,10 V ✓.
- MC L1-06: exactly one correct option, and each distractor is a real wave-model error with correct feedback ✓. L1-08: the model answer's numbers agree with E = hc/λ ✓.
- Data tasks give the stated uncertainty and are labelled esimerkkiaineisto. The level-3 tasks are multi-step YO modelling tasks. Every new task has a complete Annettu–Järkevyys solution and is within FY8 scope.
- Spot-checked the render at 1280 px (L3-04 table and solution): clean, no overflow.
- Content hash b76bee1182410114 is the same at the start and the end.
