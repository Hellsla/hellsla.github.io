VERDICT: FAIL
CONTENT-HASH: 2787a77cd4887df2

## Blocking
- inquiry.json:396 (check-patteri, option "Alle $100\,\%$, koska minkään laitteen hyötysuhde ei voi olla $100\,\%$.") — **A, Major (assessment correctness).** The option's conclusion "alle 100 %" also covers the keyed answer "Lähes $100\,\%$": a heater at "lähes 100 %" *is* below 100 %. The lesson itself says (lesson.md:91) that only an "ihanteellinen, häviötön laite" would reach $100\,\%$, so a student can defend this option from the theory. The option's feedback, "Hyötysuhde on enintään $100\,\%$, ei aina sen alle", then implies the heater may reach 100 %, which goes against the keyed "lähes". The task has two defensible options. — Give the distractor a conclusion that is clearly separate from the keyed answer, e.g. "Noin $50\,\%$, koska puolet sähköstä kuluu johtojen lämmittämiseen", with feedback saying the wire's heat also ends up in the room. Or change the reason in the current option so that its claim is plainly false. Keep exactly one correct option.

## Polish
- inquiry.json:62/66/71/75 (ennuste-1 feedback) — calling $25\,\%$ "(simulaation mallin arvo)" presents a real-world typical value as if the sim produced it. The prediction is then "tested" against a number the sim takes as input, which koe-1's intro admits. Say "tyypillinen arvo" and let koe-1 show the energy split. (Minor)
- lesson.md:93–100 (efficiency table) — the FY2 scope note asks for real values with a named source. "Tyypillisiä pyöristettyjä arvoja" is honest but names no source. Add one line naming a source (e.g. Motiva) or mark the values as approximate. (Minor)
- sim.js:48 (`nuolet` note "Nuolten paksuudet ovat suhteessa tehoihin") — the input arrow is always 100 px. Changing $P_\text{o}$ does not thicken it, so "in proportion to the powers" holds only inside one picture. Add "saman laitteen". (Minor, B)
- lesson.md:64 / tarkistus-3 model — most of a filament's loss leaves as infrared radiation. "Lämpö, joka lämmittää lamppua" is a fair FY2 simplification (C), but one clause such as "näkymättömänä lämpösäteilynä" would name the mechanism. (Minor)
- lesson.md Esimerkki, Tulos — the $10\,\%$ loss share comes from $1 - 0{,}90$, so the 2-figure precision of $36\,\text{kJ}$ is generous. Acceptable at this level; no change needed. (Minor)

## Checked
- All 31 lesson-answers.py numbers recomputed independently in one script; all agree (worked example 360/324/36 kJ, koe-1 600/150/450 kJ, siirto 250 W and its mistakes 1250 W and 15 000 W, tarkistus-2 80 % and its mistakes 20 % and 125 %, virhe 30 %/333 %).
- Sankey figures to scale: lamp 120/6/114 px (5 %); pair 1,6 px/W in both lamps (60 W: 96 px, 10 W: 16 px, 3 W: 4,8 px). "Kuusi kertaa paksumpi" is correct.
- Formula section named after its law; $\eta = P_\text{a}/P_\text{o}$ carries its constant-power condition; derivation with $t$ cancelling is correct.
- Efficiency limit uses the guardrail wording; heater "lähes 100 %"; FY2 "lämpö" usage allowed; scope stays inside FY2 (no chains, no Carnot limit).
- Typical values (5/30/90/90/25/20 %) plausible, with load dependence stated for petrol and electric motors.
- ennuste-1, ennuste-2, koe-2 question, virhe, tarkistus-1: exactly one correct option; distractor feedback correct.
- koe-1/koe-2: the adapter sets `laite` before `Po` (Object.entries order), so setRange does not overwrite 40 W or 60 kW; only `t` varies; simState gives Eo, Ea, Eh.
- sim.js `split()` implements $P_\text{a} = \eta P_\text{o}$, $E = Pt$; the model box states constant η and constant power.
- Exit ticket answers 70 %/150 J, 50 W/150 W correct.
- Hash identical at start and end.

## Scores
- 1 Physics and mathematical correctness: **2** — theory, figures and every number correct, but one task (check-patteri) has two defensible options, an A error in a task per the standard's level 2.
- 6 Experimental reasoning (physics of models): **4** — controlled variables are right and the model's assumptions are honestly stated, but the engine prediction is "tested" against an input value.
