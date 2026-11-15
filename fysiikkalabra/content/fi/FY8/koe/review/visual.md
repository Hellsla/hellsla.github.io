VERDICT: FAIL
CONTENT-HASH: bf86b739daceb22b

## Blocking
- [Major] solutions.md fy8-k4 b and c, Järkevyys (page-390-29, page-390-30) — two formulas are clipped at the callout's right edge at 390 px: "= 28,30 MeV − 2,22 MeV − 8," (8,48 MeV lost) and "17,59 MeV : 5,03 u = 3,5 MeV" ("/u" cut, so the unit reads MeV) — a value and a unit cannot be read on a phone (the 2026-11-15 rule) — make every row fit 360 px (shared callout/mathlayout, or one `=` step per formula) and run `check_layout.py FY8-koe --width 360`.
- [Major] solutions.md, Sijoitus/Muunnokset of k2 b, k2 c, k4 a, k4 c, k5 a–c, k6 d, k7 c, k7 d (page-1280-10, -20, -41; page-390-13, -15, -28, -36, -46, -55) — chains are hand-split into separate `$…$` pieces: binary operators lose their spacing ("Hz −5,0 · 10¹⁴ Hz= 1,8", "u+2 · 1,008665 u−4,002603 u= 0,030377 u"), the first step sits in a white box in small type while its result ("= 5,32 mSv", "≈ 511 keV", "≈ 31 mm") hangs outside in larger type, and at 1280 px the equals signs are not aligned — clearly poor mathematical readability in the model solutions, against "never split by hand" — write each quantity's calculation as one inline chain that starts with the quantity and let mathlayout break it.
- [Major] solutions.md fy8-k6 c Järkevyys (page-390-45) — `$2^{4}$ = $16$`: a plain-text equals sign between two formulas — write `$2^{4} = 16$`.

## Polish
- [Minor] fy8-k1 a Perustelu — "Valosähköisessa" → "Valosähköisessä".
- [Minor] fy8-k6 a Vastaus, Yleisiä virheitä (page-390-43, -48) — "$\ln R$ -kuvaaja" breaks at the hyphen — write "$(d, \ln R)$-kuvaaja", as "$(t, N)$-kuvaaja".
- [Minor] fy8-k1 e Perustelu, k7 e rubric (page-390-8, -60) — "(" alone at a line end before its formula — put the parentheses inside the maths.
- [Minor] fy8-k1 b Perustelu — "Kynnystaajuus $5{,}6 \cdot 10^{14}$" lacks $\text{Hz}$.
- [Minor] fy8-k1 d Perustelu (page-390-8) — the stacked inline fraction (1 − 1/2)/(1/2 − 1/3) is very small on a phone — write it with a colon.

## Checked
- The hash changed during the review (5416b79b… → bf86b739…: tasks.json, k4 d task text); captures retaken with `screenshot.py FY8-koe`, stamp bf86b739.
- New captures opened: page-390-28, -29, -30, -46, page-1280-20 (k4 d's new sentence reads well; findings confirmed).
- Before the change (all other text identical): top-390, top-1280, fig-1, fig-3, fig-6, fig-18, page-390-1…61, page-1280-2, -9, -10, -21, -41, contact-14.
- Graphs: quantity and unit on the axes, points distinct from fits, error bars in k2, dashed extrapolation labelled; legible at 390 px. Tables fit (k3, k6 vertical on a phone).

## Scores
illustrations 4 · typography 2 · Finnish 4 · accessibility 3
