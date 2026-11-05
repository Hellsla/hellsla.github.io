VERDICT: PASS
CONTENT-HASH: 4a08579575d5056c

## Blocking
None. Round-1 item fixed: fy1-k3 c now asks the student to compare relative uncertainties. The criterion and the model answer give the right mechanism: a larger v_E both lengthens the lead (≈ 6 %) and lowers the closing speed v_A − v_E (≈ 7 %), and the two add to ≈ 13–14 % (±0,3 km of 2,1 km). The false "lähes samoista nopeuksista" sentence is gone.

## Polish
- fy1-k3 c: the solution says "≈ 15 %"; 0,3/2,1 ≈ 14 %. The closing clause "lisäksi Aaron kulkema matka kasvaa saman ajan mukana" reads like a third effect. It is not one: s = v_A(t − t₀) only carries over the time's relative change. Consider dropping "lisäksi".
- fy1-k4 a criterion 1: "todennäköiseksi karkeaksi virheeksi" would follow the outlier guardrail more closely.
- fy1-k4 b: half the range is a scatter estimate chosen for the task, not the uncertainty of the mean.

## Checked
Delta from round 1. Hash 4a08579575d5056c at start and end.
- Osa 1 reordering: c (sähkövirta, index 0), g (overlap, index 0) and the unchanged items each still have exactly one correct option at the stored index. Each Perustelu argues by content, not position.
- fy1-k7 b/c: the task now gives the reading uncertainty of 1 mm and asks whether the line goes through the origin. The physical reason (0 sheets → 0 mm) and the residuals (≤ 0,6 mm, inside 1 mm) were recomputed with an origin fit: 0,1020 mm/sheet, 102 µm, ±1 mm/500 = 2 µm, 784 kg/m³. The criteria ask only for what is given.
- fy1-k5 b ("selvästi") and fy1-k6 c (pinta-ala alternative accepted, no force language required) were polished as suggested.
- Recomputed: k3 642,9 s, 2057 m, extremes 1800 m and 2354 m, 6,25 % + 7,14 % = 13,4 %.
- Rubric sums: k3 4 + 6 + 5, k7 4 + 6 + 5 + 5. Total 20 + 4 × 15 + 2 × 20 = 120 offered, maximum 70. `answers.py` output is unchanged and agrees.
