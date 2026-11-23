VERDICT: FAIL
CONTENT-HASH: bdc5964bdde3ce76

## Blocking
- inquiry.json:308 (siirto, solution, Järkevyys) — **A (causality, consistency).** "Suuremmassa pullossa paine ja kulmakerroin ovat suuremmat" makes the bottle's size the cause of the higher pressure. At constant V and n the pressure depends on n/V, not on V alone. The same solution's Periaate also says "Pullon koolla ei ole väliä". With the prompt (line 289, "isompaa pulloa") and p0 = 120,0 kPa, the student is left thinking that a bigger bottle gives a higher pressure. — Fix: make the reasonableness check say that the second group's gas was at a higher pressure (more gas for its volume), so p0 and k are both larger in the same ratio and θ0 stays the same. Or drop "isompaa pulloa" from the prompt and say only that the pressure was higher.

## Polish
- lesson.md:126, 139 and inquiry.json epavarmuus text — the steep line as printed (100,1 kPa + 0,387 kPa/°C·θ) gives 103,97 kPa at 10 °C, which is 0,03 kPa below that error bar. Only the exact line (100,13; 0,3867) touches the bar end. This is a rounding artefact and the answer does not change. You could print 100,13 and 0,3867, or say that the values are rounded.
- lesson.md:41 (Kaava) and Ydinajatus — guardrail: p linear in θ at constant V holds for a thin gas far from condensing. Only Tiivistelmä (line 203) says "harvan kaasun". Add "harvan" where the law is first used.
- lesson.md:136 — "paine olisi nolla siinä lämpötilassa, jossa hiukkasten keskimääräinen liike-energia on pienimmillään" is acceptable (C). "Ideaalikaasun mallissa" covers it. Leave it unless the developer touches the paragraph.

## Checked
- Recomputed everything in one script, and it matches lesson-answers.py: the worked example θ0 = −276,02 °C, the extreme lines −258,66 and −294,81 °C, Δθ0 = 18,08 °C (exact lines 18,11), suora −275,8 °C, siirto −276,9 °C, tarkistus-2 −282,9 °C, virhe −276,1 °C (wrong −316), kertaus 1,068, exit k = 0,36 kPa/°C and the interval −282…−258 °C. Every mistake value (−296, −307, −298, 36,1, ±sign) matches the error it names.
- The least-squares line of the data is k = 0,3667, p0 = 101,26 kPa, θ0 = −276,2 °C. The best line in the example (101,3; 0,367) and points A and B lie on it.
- The exact steep and shallow lines pass every ±1 kPa bar and touch the bar ends at 10/85 and 25/100 °C, as the text says. s2 misses the bars at exactly 10, 70, 85 and 100 °C, matching its feedback.
- Figure coordinates checked against the data. Formula figure (to scale): best line zero at −276,1 °C, extreme lines at −259,0 and −295,2 °C, all seven points correct. Zoomed figures: points, ±5 px bars, best line, A and B, s1, s2 and both extreme lines all agree with their equations. The pointers to the line labels land on the right lines.
- Thermometer and hero pictures: a closed rigid bottle, the bath thermometer and the pressure gauge. Labels θ, p, V = vakio and Q are consistent with the model.
- Every choice item has exactly one correct option, and each distractor's feedback is correct (kertaus, ennuste-1/2, aineisto, aariviiva, virhe, tarkistus-1, check-c2).
- The measurement terms follow the guardrails: epävarmuus vs virheraja, "yleensä" for fits, outliers wording, "todennäköisesti" for the interval, example data marked as model-based.
- Scope: within FY3 (temperature, gas at constant volume, the experiment by extrapolation). Liquefaction and the limits of extrapolation are stated.
- The worked example has its seven stages, is solved symbolically first, and justifies its significant figures (Δθ0 to two figures, result to whole degrees).
- The explain model answers and their criteria agree with the theory.
