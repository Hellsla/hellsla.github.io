VERDICT: FAIL
CONTENT-HASH: d363d2c649b787b2

## Blocking
- [Major] open-exercises-1280-1 (L1-01 Sijoitus), L2-1280-3 (L2-02), L2-1280-5 (L2-04 Kuvaajan lukeminen, Kaava, Sijoitus), L3-1280-3 (L3-02) — every rowed chain that starts `t = \dfrac` or `v_\text{A} = \dfrac` puts the left side at numerator height and the first `=` below the fraction bar, so the first row reads as three different levels. The set's solutions are mostly such chains, so the defect appears in nearly every solution — set the first row's left side and relation on the fraction's math axis in the row layout (`scripts/mathlayout.py` / its CSS; the source is correct) and recapture.

## Polish
- [Minor] solutions.md L3-01, L3-02 — the runner's subscript is $\text{R}$ (English "runner"), and in L3-02 $x_\text{B}$ is the bus, while the lesson uses B for the second body — use $x_\text{J}$ (juoksija) and $x_\text{bussi}$, or $x_\text{A}$/$x_\text{B}$ as the lesson does.
- [Minor] solutions.md L3-02 Sijoitus — "$= 16 - 20 = -4\,\text{m}^2/\text{s}^2$" drops the units mid-chain and gives $-4$ with one figure — "$= 16\,\text{m}^2/\text{s}^2 - 20\,\text{m}^2/\text{s}^2 = -4{,}0\,\text{m}^2/\text{s}^2$".
- [Minor] open-exercises-1280-1 (L1-01 task) — the inline position function breaks across lines ("$x_\text{B} = 24\,\text{m} -$ / $3{,}0\,\text{m/s} \cdot t$"). Inline maths should stay on one line — keep it unbroken (or give it its own line).
- [Minor] exercises.json L1-04 / L2-04 (kaksi-karrya) — the crossing at $t = 5\,\text{s}$ falls between gridlines (every $2\,\text{s}$) — gridlines every $1\,\text{s}$ would make the reading match the $0{,}04$ tolerance more comfortably (optional).

## Checked
- open-exercises-1280-1, -4 (L1-01…L1-04 with the kaksi-karrya figure, all solutions open)
- open-exercises-L2-1280-3, -5 (L2-02, L2-03, L2-04)
- open-exercises-L3-1280-3 (L3-02, L3-03)
- contact-3 (#29 exercise stage at 390 px)
- The figure gives every value L1-04 and L2-04 need, and the description does not give the answer away. Plain number+unit in prose: none found.

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 4
