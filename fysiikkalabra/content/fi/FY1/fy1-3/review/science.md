VERDICT: FAIL
CONTENT-HASH: 19b5ecc68b950a1c

## Blocking
- inquiry.json:519 (check-2 solution, Vastaus) and exit-ticket.json:12 (item 3) — the rounding contradicts the lesson's own rule. A virhe-arvio has one figure (two if the first is 1), and ε has as many figures as Δx (Esimerkki, Tulos). So Δt = 0,05 s and 0,09 s both give ε = 2 %, but the page says "2,1 %, kaksi merkitsevää numeroa; erotus 0,10 s jaetaan tarkalla luvulla 2" and "2,0 %". The exercise set (L2-01) follows the rule, so the page teaches it both ways. Fix: in check-2's Vastaus write "$2\,\%$, yksi merkitsevä numero kuten virhe-arviossa $0{,}05\,\text{s}$ (laskimen arvo $2{,}08\,\%$)", and in the exit ticket write "$\approx 2\,\%$". Keep answer 2.1 with tolerance 0.05.

## Polish
- lesson.md:11 — "kello käynnistyy vasta, kun kuula on jo liikkeellä" reads like L3-01's constant (systematic) delay. Add "kerran".
- inquiry.json:3 contribution — names only random and systematic error. Add karkea virhe.
- lessons/FY1/fy1-3/lesson-answers.py:38 — inq-ice-corrected is unused. Remove it.
- lesson.md — Δx stands for both the signed error and the half-range estimate. Add one sentence that says so.
- inquiry.json exp-3 solution — writes 0,0850 s, but the readout shows 0,085 s.

## Checked
- Round-1 blockers: karkea now says seitsenkertaiseksi (0,09 → 0,62 s) ✓. The check-2 tolerance accepts 2 %, but its solution is still wrong (see Blocking).
- Teacher's rules: no × or ÷; \cdot for products; ':' in the one division written as an operation; Δx = x − x_oikea; karkea virhe has its own section and appears in the activity, misconception, summary and goals.
- One script recomputed all 12 lesson-answers.py values and the sim series: exp-1 −0,22 s and −0,0005 s with half-range 0,25–0,26 s; exp-2 2,6995 s; exp-3 0,085 / 0,525 s (ratio 6,18).
- Worked example 3,18 s ± 0,12 s, 3,8 %. siirto 5,44 g with mistakes 5,6 / 27,2 / 4,8 / 28 g. Ice 1,5 / 0,1 °C. Exit ticket item 1: 19,9 g. karkea mean shift 0,19 s.
- Figures: error-types means 2,41 s and 2,59 s; range-half band from the dots; example-plot to scale; zero-scale 47,5 g.
- Formulas: correct, conditions stated, inside FY1 central contents.
- Sim: implements t_i = T + Δt_sys + Δt_sat g_i, rounded to 0,01 s; readings stay on the axis; limits stated; each experiment locks the parameters it does not vary, and the measured keys exist in simState.
