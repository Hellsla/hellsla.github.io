VERDICT: FAIL
CONTENT-HASH: 60ac1e5410bf6b4f

## Blocking
- inquiry.json:394 (karkea, option "Lisätä virhe-arvioon …") — "paisuttaisi virhe-arvion noin kymmenkertaiseksi" is wrong: without 4,31 s the half-range is (3,25 − 3,07) s : 2 = 0,09 s, with it (4,31 − 3,07) s : 2 = 0,62 s, about 7 times (5 times against the worked example's 0,12 s) — write "noin seitsenkertaiseksi" or "moninkertaiseksi".
- inquiry.json:499 (check-2) — the lesson's own rule (Esimerkki, Tulos: ε has the significant figures of Δx) gives Δt = 0,05 s (one figure) and ε = 2 %, which the relative tolerance 0.03 against 2.1 rejects (4,8 % off) — raise tolerance to 0.05 and say in the solution that 2 % (one figure, as Δt) is the strict rounding, 2,1 % the unrounded value.

## Polish
- inquiry.json:234 (exp-2 solution) — calls t̄ − T "Δt" while the sim's readout beside it shows "vaihteluvälin puolikas Δt = 0,250 s"; use Δt_sys (as L3-01 and the sim slider do).
- inquiry.json:3 contribution — names only random and systematic error; add karkea virhe, now one of the three learn goals.
- lesson.md:11 — "kello käynnistyy vasta, kun kuula on jo liikkeellä" is a gross error only once; add "kerran" so it is not confused with the constant start delay of L3-01 (systematic).
- exit-ticket.json item 3 — 2,0 % has two figures while Δt = 0,09 s has one; same rule as check-2.
- lessons/FY1/fy1-3/lesson-answers.py:38 — inq-ice-corrected (62,3 °C) is used nowhere; remove.

## Checked
- Teacher's rules 2026-10-28: no × or ÷ anywhere; \cdot in all products; the one division written as an operation (siirto Järkevyys) uses ':'; \frac elsewhere; Δx = x − x_oikea, Δt_sat, Δt_sys used; karkea virhe in theory, activity, summary, misconception and glossary.
- Every lesson-answers.py number recomputed independently and in the live sim (simState at exp-1/2/3 settings): 2,6995 s, 0,085/0,525 s, ratio 6,18, −0,22 s, < 0,01 s, 0,25–0,26 s.
- Worked example 3,18 s ± 0,12 s, 3,8 %; siirto 5,44 g and its four mistakes; check-2 2,08 %; ice data 1,5 °C, 0,1 °C, ×15.
- Figures: error-types dots give means 2,41 s and 2,59 s (Δt_sys ≈ 0,19 s) as labelled; example-plot dots, mean and band to scale.
- Formulas for mean, half-range, d/2, ε, Δx_sys and correction: correct with conditions; inside FY1 central contents.
- Sim implements t_i = T + Δt_sys + Δt_sat g_i, rounded to 0,01 s; limits stated in Mallin oletukset.
