VERDICT: PASS
CONTENT-HASH: 1381e6fc2a8531a8

## Blocking

## Polish
- solutions.md:189 (L3-05 Sijoitus/Järkevyys) — the table has no 4→1 line (97,3 nm), though atoms at n = 4 emit it; a careful pupil will ask why. — Add one sentence: "Suora siirtymä 4 → 1 lähettää lähteen aallonpituuden 97,3 nm, joka suodatettiin pois, joten sitä ei ole taulukossa."
- solutions.md:147 (L2-05 Kuvaajan lukeminen) — the slope is read from the line's two axis intercepts (1/n² = 0 and 0,250), both outside the measured range 0,028–0,111; correct for a straight line, but the guardrail asks that extrapolation be named. — Read two points of the fitted line inside the data range, or say the intercepts are extrapolated and why that is allowed (the model is linear).
- solutions.md:169 (L2-07) — part b) is the same computation as L1-08 (E₃ − E₁ = 12,1 eV), and the pupil's claim "radalla n = 3 elektroni on 9 kertaa kauempana" (Bohr r ∝ n²) is neither confirmed nor corrected, while the lesson does not teach radii. — Say in a) that the radius claim may hold in Bohr's model but the photon energy is the level difference; optionally use 5 → 1 (13,06 eV, new).
- exercises.json:242 (L3-04 a) — "Perustele, miksi päätetaso ei voi olla n = 1, n = 2 eikä n ≥ 4" names the answer m = 3 before the pupil reasons; at level 3 "Päättele, mille tasolle siirtymät päättyvät, ja perustele, miksi muut tasot eivät käy" keeps the task.
- exercises.json L2-06 — "jotakin tasoparin erotusta": write "perustilasta ylemmän tason erotusta" to match the solution (answer stays 3).

## Checked
- One script recomputed all 20 answers with my own formulas; all agree with exercises.json and answers.py within tolerance (L2-05 slope −3289 THz → 13,60 eV; L3-04 365,3 THz; L3-05 97,25 nm).
- L1-06: one correct option; distractor feedback numbers right.
- L2-05 data within ±0,5 nm of the model (656,5; 486,3; 434,2; 410,2 nm).
- L2-06: photon energies 4,13 / 3,00 / 2,48 / 5,99 / 5,00 eV; three match 3,0 / 5,0 / 6,0 eV.
- L3-04: only m = 3 gives integers (4,00; 5,00; 6,00); m = 1 and 2 values in the solution right.
- L3-05: five lines identified correctly; n = 5 lines (95,0; 434; 1282; 4052 nm) absent; cascade sum 12,75 eV.
- Notation, constants, conversions as in the brief; levels 8/7/5; render at 1280 px clean.
- Hash identical at start and end.
