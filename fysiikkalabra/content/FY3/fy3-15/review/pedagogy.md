VERDICT: PASS
CONTENT-HASH: 7e12e856a6b7b3cc
## Blocking
None.
## Polish
- inquiry.json ketju — the numeric asks only for the steam-cycle loss (248 MW), but pred-1 is about which stage loses most; the other two losses (40 and 12 MW) appear only in the solution after answering. Ask for all three (or "how many times the boiler's loss") so the student tests the prediction with own numbers.
- inquiry.json kaukolampo — the table is not marked as example data ("Yhteistuotantolaitoksen ... 400 MW", no "esimerkki"/model); only the model answer says so. Write "esimerkkilaitoksen (mallin) kaksi ääritilaa" and note the straight line is an assumption. No `source` field is set on ketju/kaukolampo/tyypit.
- inquiry.json hook and pred-1 ask almost the same question ("missä vaiheessa menee eniten"), so the prediction feels like a repeat; let the hook ask why the cooling water is warm and keep "which stage" for the prediction.
- exercises.json fy3-15-L3-03 — uses a heat pump's "lämpökerroin 3,00" with no pointer to where it was taught; add one line defining it or confirm it is in the prerequisite lesson.
- lesson.md Kaava — the condenser formula P_L = c q_m ΔT adds a third idea (with figure) beyond the slot's chains and cogeneration; only L2-04 uses it, so keep it short.
## Checked
Core path clear: hook, 2 predictions, 3 table tasks, conclusion (explain; no experiments so no `after`; model answer opens only after own text and says the figures are example/type values), 2 checks, exit; kertaus, kaukolampo-tarve, reflect, Etsi virhe, siirto, check 3 are in Valinnainen boxes. Sim-less design justified (a sim would only multiply). Both predictions have wrong options that the tables can refute; Aino/Bea/Cem/Daniel are right once in four. Example differs from the investigation numbers and is staged. Exit ticket tests the product rule, cogeneration and the hydro/heat engine contrast. Finnish good. No captures; judged from text.
