VERDICT: PASS
CONTENT-HASH: 325b5ecdcdaccc5e

## Blocking

## Polish
- exercises/solutions.md:19 — The answer is "$1{,}08 \cdot 10^{4}\,\text{C}$ eli noin $11\,000\,\text{C}$, kaksi merkitsevää numeroa": the first form has three significant figures. Give only $1{,}1 \cdot 10^{4}\,\text{C}$, which has two like 3,0 Ah.
- exercises/solutions.md:70 — "$0{,}20\,\Omega$, sadasosaohmin tarkkuudella" contradicts its own reason. $(1{,}2\,\text{V} : 1{,}2\,\text{A}) = 1{,}0\,\Omega$ is known only to tenths, so the difference is $0{,}2\,\Omega$. Answer $0{,}2\,\Omega$ and name 1,2 V and 1,2 A as the limiting data.
- exercises/solutions.md:121 — "häviö on muutamia prosentteja": 3,24 kJ : 43 kJ ≈ 7,5 %. Write "noin 7 %".

## Checked
- I recomputed all twelve answers in one script with my own formulas, and all of them agree: 2,0 Ah; 10 800 C; 468 Wh; 16 h; 4,0 Ah; 5,0 A; 0,20 Ω; 97,5 min; 84 %; 1,28; 33,3 %; 3,24 kJ.
- answers.py computes the right physics from the task text, including the 40 mΩ conversion, the 15→80 % share, the half-usable lead-acid capacity, and $R_\text{s} I^2 t$ with 5400 s.
- The rounded answers 470 Wh, 98 min, 1,3, 33 % and 3,2 kJ all fall within the 2 % tolerance. 11 000 C is at 1,9 %.
- Figure ex-current: 2,0 A for 0–1,5 h and 1,0 A for 1,5–2,5 h on a 0,5 grid. The description gives the same values, and the answer is not shown.
- Charging-circuit tasks use the lesson's voltage law, with current + → − in the battery. Each check of the terminal voltage from both sides is a real check (12,6 V; 1,2 V).
- Notation matches the lesson: $E$, $R_\text{s}$, $U_\text{lat}$, $W$ for energy and $\eta = W_\text{akku} : W_\text{lat}$.
- The energy wording "sisäenergiaksi, joka siirtyy lämpönä" is used, and "muuttuu lämmöksi" does not appear. Efficiency stays under 100 %, and the task states its storage assumption (L2-04).
- Every solution is complete: data, principle, the formula solved symbolically, conversions, substitution, rounding and a reasonableness check.
- The data are realistic: lead-acid 12,0–12,6 V charged at 13,8–14,4 V, Li-ion around 3,8 V, and e-bike 36 V.
- Within FY6 scope; Level 3 combines capacity, energy and the voltage law.
