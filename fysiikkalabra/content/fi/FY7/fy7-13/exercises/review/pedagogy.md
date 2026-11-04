VERDICT: FAIL
CONTENT-HASH: 061654f593114adf

## Blocking
- exercises.json fy7-13-L3-04 b) and solutions.md fy7-13-L3-04 — b) asks "Tarkista, sopiiko tulos taulukon lukemiin", but the table ends at x = 7,0 mm and the second-order maximum is at 10,0 mm, so the check cannot be done, and the solution never does it. Fix: add rows x = 7,5 … 10,0 mm (I = cos²(πx/5 mm), e.g. 0,00 at 7,5, 0,91 at 9,5, 1,00 at 10,0) and add one sentence to the b) solution reading the table, or reword b) to "Mikä on toisen kertaluvun maksimin paikka?" and drop the check.
- solutions.md fy7-13-L3-05 b) and Vastaus — the solution says three light spots on the cardboard ("reikä ja maksimit k = ±1"). The zeroth-order beam is reflected straight back through the hole, so no spot appears there; the visible spots are the two k = ±1 maxima. Fix: answer "kaksi valopistettä (k = ±1); keskimaksimi palaa reiän kautta takaisin" in both the b) step and the Vastaus text (and Checked line in Järkevyys if it counts three).
- exercises.json fy7-13-L3-05 text, lead over ~45 words (about 52) in one paragraph. Split points: "...osuu kohtisuoraan levyn pintaan." / "Levystä heijastuneet ensimmäisen kertaluvun maksimit k = ±1 ... molemmin puolin. Opiskelija mittaa ... tulokset ovat taulukossa." (three paragraphs if the second is cut after "molemmin puolin.").

## Polish
- fy7-13-L2-05 lead is about 42 words: still within the limit, but a break before "Hän mittaa mittanauhalla ..." reads better; "Hila on kohtisuorassa ... ja varjostin on kohtisuorassa sädettä vastaan" repeats itself.
- fy7-13-L2-06 a) "määritä kulma ensin tangentista" gives away the error; better ask first "Mikä opiskelijan päättelyssä on virheellistä?" and then a) and b).
- Data tables use decimal points ("6.3", "0.09"); the text uses commas. Use "6,3" etc. if the renderer does not convert them.
- fy7-13-L3-05 is close to the existing L3-02 (reflection grating, hole in cardboard, ±1 maxima); its added value is averaging and the k = 2 check, which is fine, but L3-04 tagged "graph" asks for no graph: ask for a sketch of I(x) or drop the tag. Plan figures (pattern, setup, white) are not used by any new task.
- solutions.md L3-05 b): "b)Toiselle" missing a space.

## Checked
- Counts 8/7/5 reached; ids and levels fit the plan; no duplicate of the worked example.
- L2-05 sin values and slope 0,0634 (633,7 nm) recomputed; L2-06 error 5,53 % correct; L3-04 data fit cos² pattern, 625 nm correct; L3-05 d values and mean 0,7374 µm correct.
- L1-06, L2-07 distractors target real misconceptions, each with its own feedback.
- 1280 px captures of L3-04/05 render cleanly, tables and solutions readable; no 360 px captures listed.
