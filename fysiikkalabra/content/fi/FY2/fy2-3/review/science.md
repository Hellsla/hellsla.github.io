VERDICT: PASS
CONTENT-HASH: a521877d291249c4

## Blocking

## Polish
- content/fi/FY2/fy2-3/inquiry.json:81 — the sim's Mallin oletukset says the powers are "luvun taulukon tyypillisiä pyöristettyjä arvoja", but the table has an LED lamp at 8 W and no toaster, while the sim uses a 10 W lamp and a 1000 W toaster — say "tyypillisiä pyöristettyjä arvoja" without "luvun taulukon", or add the 10 W lamp and the toaster to the table (internal consistency only; the values are plausible).
- content/fi/FY2/fy2-3/lesson.md:108 — the 2025 price figure (Tilastokeskus, about 18 snt/kWh in total) carries no table or period; name the statistic (for example the household total price, a given quarter) so it can be checked.
- glossary.json "teho" (shown with this lesson) — adds "P = W/t" and "P = Fv", which FY2's scope and this slot exclude ("työn käsitettä ei tässä moduulissa vielä käytetä"); the shared entry is not in this lesson's hash, but the page's term box contradicts the slot.

## Checked
- P = ΔE/Δt defined as the rate of conversion or transfer, the mean-power condition for uneven use stated, E = P t and t = E/P only "tasaisella teholla"; no work or force in the lesson (scope).
- 1 kWh = 1000 W · 3600 s = 3,6 MJ; kW·h = kWh shown; "teho on 2 kWh" misconception correct.
- Figures to scale: bars 400 : 200 : 16 px = 2000 : 1000 : 80 J; graph lines end at 120, 60 and 4,8 kJ at 60 s (1,83 px/kJ, 6,43 px/s), and the slope triangle 40 kJ / 20 s = 2000 W.
- Worked example recomputed: 0,080 kW · 120 h = 9,6 kWh, 192 snt = 1,92 € → 1,9 €; symbolic first, rounding and check right.
- Every number in inquiry.json and the exit ticket recomputed independently (15 h, 540 kJ, 864 kJ, 30 min, 21,9 → 22 kWh, 800 W, 0,90 €, 43,8 vs 36,5 kWh, 0,15 vs 0,24 kWh, 800 000 kettles); agrees with lesson-answers.py.
- Each choice item has exactly one correct option; every distractor's feedback names the actual error with correct numbers (the 150 h and 1 h options included).
- Experiments: koe-1 locks A, tA, B and varies tB; the slider (1–1440 min, 1 min steps) reaches 900 min where EB_kJ = EA_kJ = 540; koe-2 reaches EA_kWh = 1 at 30 min; measured keys are in simState.
- sim.js implements E = P t with t in seconds, the disc turning in proportion to P (fixed turns per kWh), solid line to the device's time and dashed beyond; the constant-power assumption and the duty-cycling of fridge, sauna heater and kettle are stated in the model box.
