VERDICT: PASS
CONTENT-HASH: 3f48bc8fead4207e

## Blocking

## Polish
- solutions.md:125 (L1-06 model answer) — "Diodin yli on vain pieni jännite …, koska vastus ottaa suurimman osan" reverses the cause: the diode's voltage is small because of its characteristic (about 0,7 V once it conducts), and the resistor gets the rest — write "Diodin jännite on päästösuunnassa pieni, joten suurin osa jännitteestä jää vastukselle."
- solutions.md:215 (L2-09 Järkevyys) — "pienempi kuin luvun paneelin suurin teho (0,92 W), kuten pitääkin" holds only if this is the lesson's panel at the same irradiance, which the task does not say — compare with the figure's own short-circuit current times open-circuit voltage only, or say that it is the same panel.
- lessons/FY6/fy6-14/figures.py:218 (ex-led description, L1-05) — the description does not give the point the task reads (2,2 V at 10 mA), so a reader who cannot see the figure cannot answer the task — add "virta on 10 mA jännitteellä 2,2 V".

## Checked
- All 20 numeric answers recomputed in one script (R = (U − U_D)/I, P = UI, η = P/(GA), E = Pt, the table maxima in L2-06 and L3-02, the yearly sums 1027 kWh/m² and 5340 kWh in L3-04, the load-line intersection 13,78 mA at 2,02 V in L3-05); all agree with answers.py and exercises.json.
- L3-04 c: six deficit months (Jan–Mar, Oct–Dec), production 853 kWh, deficit 2517 kWh; "vähintään" is correct because hourly mismatches within a month only add to the purchase.
- L3-05 a: threshold from the steep part extrapolated, 2,00 V, as the glossary defines; c: 0,10 V over a four-fold current, right.
- L2-06 table: U/I matches each load resistor within rounding; the powers in the solution are right.
- L2-08: exactly one correct option and one correct reason; each distractor's feedback names its error correctly (parallel branches are independent; a diode in series blocks the lamp).
- L1-06, L1-07: each has exactly one correct option; the forward/reverse rule matches the glossary.
- Rounding: shown answers (e.g. 2,1·10² Ω, 3,9·10² Ω, 17 %, 20 %) fall inside the page check; the limiting data are named correctly under P7(b).
- L2-01 reverse voltage 9,0 V and the 5 V reverse rating remark: correct and safety-relevant.
- Figures ex-led (2,2 V at 10 mA from the model m = 0,050 V) and ex-kenno (198,7 mA at 4,0 V) give the read values, and neither writes the answer.
- Scope: components only, with no p–n microphysics; Level 3 combines Kirchhoff, Ohm and power.
