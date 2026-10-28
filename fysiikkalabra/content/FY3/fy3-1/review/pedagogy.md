VERDICT: PASS
CONTENT-HASH: d5016cfcfdfdcdd5

## Blocking
(none)

## Polish
1. Koe 2 table at 390 px (exp-exp-2-390.png): the table scrolls sideways (scrollWidth 383 > 332) and the G (N) column, the quantity the prediction is about, starts out of view. Shorten the column labels (e.g. "kappale", "g", "G") or let the table wrap so all three columns show.
2. Canvas at 390 px (sim-390.png): the meter scale runs 0–2500 N, so at 10 kg the pointer sits at "0" and the spring barely stretches; the first experiment's "katso jousen venymä" shows little at 10→30 kg. The readout and the bar chart carry the quantity, so this is not blocking. Consider a meter scale that follows the chosen mass, or a one-line intro hint to read G from the bars.
3. Canvas at 390 px: the bar-chart axis labels (150, 100, 50), "asteikko 0–248 N" and the "G (N)" title sit close together and are small (about 9 px), though not overlapping; the Kuu/Mars/Maa/Jupiter labels are legible. At 1280 px the text is small relative to the canvas but clear. Raise the tick and caption font a step on narrow canvases.
4. inquiry.json:pred-1 and pred-2 feedback say "Mallin arvot tukevat…" but the student reads this before Tutki when the box is reopened; "mallin arvot" is clear after the experiment, so no fix is needed. Check only that the wording still reads well when the box is reopened later.
5. exercises.json fy3-1-L3-03: "mittari näyttää 26 kg" (a force meter scaled in kg) is a hard reading for a first-time student. The idea is good and matches the misconception section, but a sentence saying "asteikko on vain nimeltään kilogrammoina" would help.

## Checked
- All LaTeX canvas labels and readouts ($m$, $g$, $G = mg$, units) render in KaTeX at 390 and 1280 px; no overlaps between spring, arrow, meter and bar chart; the legend is one line.
- Sim moved by hand (m=30, 100 kg, Earth): spring, arrow, pointer and bars follow G proportionally; the bar scale changes with mass and is stated.
- The sims check now passes (the packet's FAIL was stale); inquiry 62/62.
- Learning path: FY1 retrieval, then the hook, two predictions with justifications, two controlled experiments (one variable locked each), calibration table, theory, reflection; only G = mg and force as a measure, no Newton's laws (in scope).
- The opening question about the astronaut is answered in theory, reflection and check 3.
- Predictions can be refuted: the experiments record G at min 2 values; the wrong options' feedback repairs the misconception.
- Worked example has six single-step stages, symbolic first; it is not repeated in the exercises.
- Exercises: 5/4/3 levels, original, with unit and tolerance; the exit ticket tests mass versus weight and proportionality.
- Finnish and terms are correct (case after number+unit, glossary terms); the howto/model text sits behind Käyttöohje and Mallin oletukset, and the visible lead is short.
- Workload is on the heavy side (12 exercises and 3 checks after a long inquiry) but still one lesson.
