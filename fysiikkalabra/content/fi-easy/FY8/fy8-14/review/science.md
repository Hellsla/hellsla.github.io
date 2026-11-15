VERDICT: PASS
CONTENT-HASH: 979782283a530c66
Mode: full, round 1 (fi-easy)

## Blocking
- none

## Polish
- lesson.md, Kaava "Annihilaatiofotonin energia" — "noin $150\,000$-kertainen näkyvän valon fotoniin verrattuna" holds only for the most energetic violet photon ($3{,}3\,\text{eV}$, as lesson-answers.py computes it); Tarkista 2's Järkevyys uses a $2\,\text{eV}$ photon and gets $2{,}6 \cdot 10^{5}$ — say "suurienergisimpään näkyvän valon fotoniin verrattuna" or "satojatuhansia kertoja".
- inquiry.json `rontgen` table — the last column ($0{,}05$; $1{,}6$; $3{,}3\,\%$) is computed from unrounded $d_{1/2}$; from the table's own rounded values a student gets $0{,}045$; $1{,}7$; $3{,}4\,\%$ — either show $1{,}7$ and $3{,}4$ or say in the text that the column was computed before rounding.
- inquiry.json `ennuste-2`, feedback of the correct option and of "Yksi riittää" — "kasvaimen kautta kulki vain noin neljäsosa janoista" is true for large $N$ only (model: $10\,\%$ at $N = 10$, $5\,\%$ at $20$, $26\,\%$ at $50$ and $200$); add "suurilla $N$:n arvoilla", as the johtopäätös model answer already does.
- inquiry.json `tarkistus-3` model and criterion 2 — "annosnopeus pienenee etäisyyden neliön mukaan" holds when the patient is far enough to act as a point source; "likimain" would cover it.

## Checked
- Every choice has exactly one correct option and right feedback; X-ray production, contrast, PET, radiotherapy, safety principles, dose table, summary and exit ticket are correct and in FY8 scope.
- Recomputed in one script with own formulas: $m_e c^2 = 8{,}187 \cdot 10^{-14}\,\text{J} = 511\,\text{keV}$; $f = 1{,}2355 \cdot 10^{20}\,\text{Hz}$ and both mistake values; worked example $n_\text{A} = 2{,}353$, $n_\text{B} = 4{,}198$, ratio $3{,}59$; siirto $772{,}0 \to 770\,\text{MBq}$ and its three mistakes; Etsi virhe $0{,}36 \cdot 0{,}15$.
- Text numbers: Tc-99m $6{,}3\,\%$ after a day, Am-241 $-1{,}6\,\%$ in ten years, $25\,\text{kGy} \to 6{,}0\,\text{K}$, time-of-flight $c\Delta t/2 = 4{,}5\,\text{cm}$, FDG $5{,}7\,\text{mSv}$, lead $d_{1/2}$ $0{,}26$ and $3{,}9\,\text{mm}$ (ratio 15), tissue and bone $d_{1/2}$ at 30, 60, 100 keV from the XCOM coefficients.
- Simulation: re-implemented the seeded model independently; koe-1 values agree ($N = 10$: $18{,}4\,\text{cm}$; 20: $4{,}0$; 50: $1{,}4$; 200 and 1000: $0\,\text{cm}$; share $25{,}5$–$28\,\%$); over seeds 1–100 the scatter at small $N$ is as the feedback says.
- sim.js implements the stated model (isotropic in-plane direction, exact back-to-back, chord to ring, back-projection); limits stated in Mallin oletukset; `simState` gives `virhe` and `osuus` at the experiment's values; koe-1 locks potilas and ilmaisu and varies only $N$.
- Figure `kontrasti` is to scale (half-value markers at $1{,}1$, $2{,}2$, $3{,}4\,\text{cm}$; curve ends); sädehoito figure $5 \cdot 0{,}40 = 2{,}0\,\text{Gy}$.
