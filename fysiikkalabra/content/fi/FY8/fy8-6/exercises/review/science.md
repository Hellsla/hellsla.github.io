VERDICT: PASS
CONTENT-HASH: 4d9d5477327a2bc7
Round: 2

## Blocking

## Polish
- solutions.md fy8-6-L2-06 Vastaus — "hänen ylimääräinen noin 0,16 V kumoaa osan siitä, että kynnysjännite on … noin 0,1 V pienempi" (my round-1 wording) understates it: 0,16 V cancels the whole 0,09 V deficit (hc/eλ = 1,97 V, Eero 1,88 V) and overshoots by 0,07 V, which is why |+3,65 %| < |−4,5 %|. — Write "kumoaa koko noin 0,09 V:n eron ja ylittää arvon hc/(eλ) noin 0,07 V:lla, joten poikkeama on pienempi kuin Eerolla".
- solutions.md fy8-6-L2-07 Vastaus — 0,0625 eV is the difference of two nearly equal energies; a ±1 nm reading of the half-maximum points changes it by ±0,003 eV, so "kolme merkitsevää numeroa kuten aallonpituuksissa" overstates it. — Give 0,063 eV (or 0,06 eV) with that reason; the key 0.0625 with tolerance 3 % can stay.
- docs/exercise-bank/FY8.md fy8-6 — carried over: Taso 3 says "h tyypillisesti hieman liian suuri", but the set (L3-04, L2-06) shows the single-LED h is usually too small; L1-08 (elektronit sekunnissa) is not in the plan and L1-07 is L2-01 reversed one level lower. — Fix the plan.

## Checked
- Round-1 Blocking L2-06 resolved: the false "lähimpänä hyväksyttyä arvoa" clause is gone; b) is answered in Vastaus (Aino and Salla wrong and why, Salla closer by chance, Eero's −4,5 % is the ~0,1 V gap).
- Round-1 Blocking L2-07 resolved: "intensiteetti on vähintään puolet maksimista … 1,94–2,00 eV" (that band holds about 87 % of the tabulated intensity, "pääosa" is right); E_g is called a material property with thermal spread.
- L2-07 new data: peak 630 nm, half-maximum points 620/640 nm, FWHM 20 nm (typical red LED, round-1 polish applied); ΔE = 2,0000 − 1,9375 = 0,0625 eV; answers.py gives 0,06250, key 0.0625.
- L2-05 now uses the fit's mean point (2,10 V; 14,92 mA): U_k = 1,857 V, recomputed. L3-04 says "yleensä"; c)/d) split matches the solution; h = 6,742·10⁻³⁴ J s.
- L1-06 reordered: one correct option, answer text matches, distractors and feedback right. L1-08 asks for x, key 6,24.
- All 19 answers.py values reproduced; hash identical at start and end.
