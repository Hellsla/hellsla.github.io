VERDICT: PASS
CONTENT-HASH: d1b7eae9124ab56b

## Blocking

## Polish
- content/fi/FY2/fy2-4/inquiry.json:375 — the feedback "Hyötysuhde on laitteen ominaisuus, joka pysyy suunnilleen samana käyntiajasta riippumatta" is broader than the lesson, which ties this to steady operation (a cold engine or a just-switched-on lamp differs); add "kun laite käy tasaisesti" as in the Tiivistelmä. The option stays clearly wrong either way.
- content/fi/FY2/fy2-4/lesson.md (Ydinajatus, tarkistus-3 model) — the filament lamp's "lämpö" is largely infrared radiation; "lämmöksi ja lämpösäteilyksi" once would avoid the picture that all loss is conduction (C, not a finding).

## Checked
- η = E_a/E_o = P_a/P_o with "tasaisella teholla" stated where the power form and the time cancellation are used; E_o = E_a + E_h; guardrail efficiency-limit wording, the resistance heater at about 100 %, and "what counts as useful decides η" (kettle vs lamp) all present and consistent in theory, summary, goals and checks.
- Sankey figures to scale: 120 px = 100 J split 6 + 114 px (5 J + 95 J); lamp pair at 1,6 px/W: 96 → 4,8 + 91,2 px (60 → 3 + 57 W) and 16 → 4,8 + 11,2 px (10 → 3 + 7 W).
- Worked example 2000 W · 180 s = 360 kJ, 0,90 · 360 kJ = 324 kJ, losses 36 kJ; symbolic first, rounding and check right.
- Every inquiry number recomputed (1200 J, 15/45 kW, 75 %, 600/150/450 kJ, 1200/300 kJ, 2,0 W of 40 W, 250 W with mistakes 1250 and 15 000 W, 80 % with mistakes 20 and 125 %, 30 % vs 333 %, 4,0 : 5,0 = 80 %, exit ticket 70 %, 50/150 W).
- Each choice item has exactly one correct option; the 60 % option's "häviöitä vain 24 kW" and the virhe item's "(2,4 + 5,6) : 8,0 = 100 %" are right.
- Experiments: koe-1 locks laite = auto and P_o = 60 kW (inside the auto range 10–100 kW, step 5 kW), varies t; koe-2 locks lamppu at 40 W (range 10–100 W, step 5); Eo, Ea, Eh are in simState.
- sim.js implements P_a = ηP_o, E = P t, arrows 100 px · η and 100 px · (1 − η); the model box states constant η, steady power, load dependence (strong for petrol, weak for electric motors) and reflected light in the panel's losses; ennuste-2 feedback says the sim only repeats its assumption.
- Typical values (5 %, 30 %, 90 %, 90 %, 25 %, 20 %) realistic and labelled as rounded typical values; low-load petrol engine caveat stated.
