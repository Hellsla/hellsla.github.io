VERDICT: PASS
CONTENT-HASH: cd77831d711f3f85

## Blocking

## Polish
- [Minor] solutions.md L2-01 Muunnokset (open-exercises-L2-1280-1) — "$54\,\text{km/h} = \dfrac{54\,\text{m}}{3{,}6\,\text{s}}$" reads as if the car covered 54 m in 3,6 s — write "$v_0 = 54\,\text{km/h} = \dfrac{54}{3{,}6}\,\text{m/s} = 15\,\text{m/s}$" (or "$54 : 3{,}6$").
- [Minor] solutions.md L2-01 Järkevyys — "Voiman etumerkki on negatiivinen", yet Kaava and Vastaus give $F_\text{ka}$ as a positive magnitude ($6000\,\text{N}$) — say "Voima $F = -6{,}0\,\text{kN}$ osoittaa liikettä vastaan…" so the sign refers to a quantity that was shown.
- [Minor] solutions.md L1-03 Järkevyys — "joten tulos $4{,}9$ on sopiva" drops the unit; L3-03 Järkevyys writes $\tfrac{0{,}20 \cdot 8{,}0}{0{,}020}\,\text{N}$ with bare numbers inside — "$4{,}9\,\text{N}\cdot\text{s}$", and units in the substitution as elsewhere in the set.
- [Minor] solved chains with a fraction (L3-01 Kaava/Sijoitus, L3-02, L3-03, L2-02 Sijoitus; open-exercises-L3-1280-2…4, L2-1280-3) — the left side ($I$, $v$, $v_0$, $\Delta F$) sits higher than its "=", and L3-01's short "$I$" is pushed onto a row of its own; this comes from the page's chain layout (`mathlayout.py`), so it shows in every lesson — for the developer: align the left side to the baseline of the first "= …" row.
- [Minor] ex-potku graph (open-exercises-L3-1280-1) — the tick reads $1$ between $0{,}8$ and $1{,}2$, while the solution says $1{,}00\,\text{s}$ — label it $1{,}0$ for a uniform scale.

## Checked
- contact-5, contact-6 for triage
- open-exercises-1280-1 (L1 header, L1-01 task, answer, full solution, "Kirjoita ratkaisu" button)
- contact views of open-exercises-1280-2…5 (L1-02…L1-05)
- open-exercises-L2-1280-1 (L2-01), -3 (L2-02/L2-03); contact views of -2, -4, -5
- open-exercises-L3-1280-1 (L3-01 with ex-potku graph), -2, -3, -4 (L3-01…L3-03 solutions); contact view of -5
- fig-6-390 (tarkistus-kolmio, shared figure style for comparison)
- Text: exercises.json and solutions.md in full from the packet. No plain number+unit found in student text; the answer-box unit labels (kg·m/s, N·s) are page UI.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 5
