VERDICT: PASS
CONTENT-HASH: c780a0d8565071dc

## Blocking

## Polish
- solutions.md:188 (fy8-2-L1-07) with exercises.json L1-07 — the model answer requires the cause "ytimen varaus ja elektronien määrä ovat erilaiset" ("tämä syy vaaditaan"), which the brief's lesson does not teach (it says only that each element has its own states). Physics right — either drop "vaaditaan" and accept "jokaisella alkuaineella on omat energiatilansa", or give the cause in the task text.
- solutions.md:273 (fy8-2-L3-04) Järkevyys — "yli $780\,\text{nm}$, eli infrapunaa" uses another edge of visible light than the lesson and L2-08 ($380$–$750\,\text{nm}$, task band to $720\,\text{nm}$) — write $750\,\text{nm}$.
- solutions.md:283 (fy8-2-L3-05) Vastaus — part d) gives $477\,\text{nm}$ with three figures from $0{,}50\,\text{eV}$ without a reason — add that $3{,}10\,\text{eV} - 0{,}50\,\text{eV} = 2{,}60\,\text{eV}$ is known to hundredths, so three figures stand.
- solutions.md:69 (fy8-2-L2-01) Sijoitus — the shown quotient $1{,}9865 \cdot 10^{-25} : 4{,}0851 \cdot 10^{-19}$ is $4{,}8628 \cdot 10^{-7}\,\text{m}$, the text has $4{,}8627$ (the unrounded value); the answer $486\,\text{nm}$ is unaffected.

## Checked
- One script recomputed all 17 numeric answers from the task texts with my own formulas (h = 6,626e-34 J s, c = 2,998e8 m/s, 1 eV = 1,602e-19 J): every one agrees with exercises.json and answers.py inside the tolerance (largest relative difference 0,35 %, L2-03).
- Intermediate values of every solution recomputed; only the L2-01 last digit above differs.
- L2-07: my least-squares fit gives λ = 12,01 nm/mm · x + 299,65 nm, residuals at most 0,76 nm, 496,6 nm at 16,4 mm (inside the calibrated range).
- L3-04: photon energies 3,90/2,80/2,40/1,50/1,30 eV; levels 1,10/2,40/3,90 eV reproduce all five lines; the mirror solution is excluded by the task's statement about the sixth line.
- L2-08: 496, 413, 282 nm from the ground state, 653 nm only from level 2; exactly one option right; figures to scale, feedback correct.
- L3-05: shares 18,9 / 22,1 / 15,1 %, d) 477 nm; assumptions stated in the task.
- L3-06: mercury 404,7 and 546,1 nm do share the upper level (7³S₁ → 6³P₀, 6³P₂); 0,79 eV matches 5,461 − 4,667 eV; two figures justified.
- L2-05, L2-06: reference lines of H, He, Na, Hg, Ca II, Mg correct and labelled esimerkkiaineisto; line E rightly unidentified; E_y = −0,85 eV is n = 4.
- L1-06, L1-08: one correct option, distractors really wrong, feedback correct.
- Symbols as in the lesson; every solution symbolic first; scope inside FY8.
