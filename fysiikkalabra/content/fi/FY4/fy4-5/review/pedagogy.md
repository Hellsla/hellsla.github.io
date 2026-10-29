VERDICT: FAIL
CONTENT-HASH: 47e70a6d03eb853b

## Blocking
- lesson.md:72 (`suunnat`, lessons/FY4/fy4-5/figures.py) — this figure illustrates the new rules but breaks them. In three of its four "voimakuviot" (lattia, rinne, lamppu), the floor, slope or ceiling is drawn inside the force diagram. The lamp's T arrow runs up to the ceiling as if it were the cord. Only the helium panel separates a pictorial tilannekuva from the rectangle. Line 172 ("voimakuvioon piirretään vain suorakulmio ja voimat"), line 8 and the summary say otherwise, and students copy figures. — Draw each panel like the helium one: a small pictorial tilannekuva next to a rectangle-only diagram with no surface. Update the aria-label to match.

## Polish
- lesson.md:63 — "alkaa kappaleen reunasta" is vague. → "Kitkan nuoli alkaa kosketuspinnan kulmasta kappaleen ulkopuolelle tai päättyy siihen. Sitä ei piirretä kappaleen sivua pitkin sivun keskeltä."
- lesson.md:60 — step 3 says every arrow *starts* at its point. The push exception, which the check-3 model uses, first appears at line 172. → "Piirrä kullekin voimalle yksi nuoli, joka lähtee voiman vaikutuskohdasta. Työntävän voiman nuoli voi myös päättyä vaikutuskohtaan."
- lesson.md:172 — "kappale saa näyttää siltä kuin se oikeasti näyttää" sounds optional. → "Tilannekuvassa kappaleet piirretään sellaisina kuin ne näyttävät, mutta voimakuvioon piirretään vain suorakulmio ja voimat."
- inquiry.json:504 — "kahvan voima kahvan kiinnityskohdasta" does not match malli-tyonto, where F *ends* at the corner. → "kahvan voiman nuoli alkaa tai päättyy kahvan kiinnityskohtaan". fbd_magnitudes asks for dashed components that the model figure does not show: draw F_x or drop the phrase.
- inquiry.json:105 — "*Komponentit*-ruutu" does not match the checkbox label. → "Ruutu *Näytä voiman F komponentit*". The sim's force diagram is about 7 px text at 390 px (this predates the change). Enlarge it on phones.

## Checked
- No point model is left in the lesson, inquiry, solutions or sim (the select and its tests are gone). The only "piste" is the exam-score sense.
- Colours are taught (step 6, summary). They are applied in tilanne, the sim legend and malli-hissi.
- tilanne: pictorial tilannekuva beside the rectangle. Friction starts at the outline, N<G, and the labels are clear.
- hissi a–d: a pictorial cabin plus a rectangle, one error per distractor, and feedback that names it. The red v in c is the intended error, and the prompt matches.
- virhe: the description does not reveal the error. The μ subscript touches the arrowhead (cosmetic).
- Worked example: staged, with the diagram before the equations. No labels collide.
- check-3 is a real draw task. The fbd plan is fully covered.
- The Finnish in the changed text is natural. Case after number+unit is correct.
- review/shots is stale. I judged from /tmp/claude-0/figshots and a fresh 390 px sim capture. The hash changed mid-review because of a sim F_y label offset only; I checked it and it does not affect these findings.
