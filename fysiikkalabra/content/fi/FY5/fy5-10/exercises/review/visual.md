VERDICT: FAIL
CONTENT-HASH: f7eb8d3fceb84386

## Blocking
- [Major] solutions card, every multi-step chain (`.eq-chain` rows: Kaava, Muunnokset, Sijoitus, Järkevyys) in the NEW tasks (L2-07, L3-04, L3-05 and the aligned blocks of L2-06) — the chain renders as an empty white box about 36 px wide, so the model solution shows words ("joten", "Kohta a):") with no calculation. Seen in the 1280 captures (open-exercises-L3-1280-7) and reproduced in a fresh render of preview/fy5-10.html with all details open (grid columns collapse to `0px 0px`, chains carry `kx-wide data-glued`; flaky: sometimes they render at about 250 px). The same boxes appear in untouched old tasks, so it is the site-wide "inline formulas never wrap" change (kx-wide/glued script with `.eq-chain` in templates/site.css line 343), not the content — but it hides the required solution steps of every new task that has a chain. Fix (template, not content): make `.eq-chain` keep its content width inside opened solution cards (e.g. `min-width:min-content` on the grid columns / skip kx-wide gluing inside `.eq-chain`), rebuild, retake the shots, re-review.

## Polish
- [Minor] fy5-10-L2-07 text — "kulkeakseen mikrofonien väli." is ungrammatical — "kulkeakseen mikrofonien välin."
- [Minor] fy5-10 solutions L3-04 Vastaus — "Paksumpaan narun vaihtaminen muuttaa väliainetta" — "Narun vaihtaminen paksumpaan muuttaa väliainetta".
- [Minor] fy5-10-L2-07 and fy5-11-L2-05 — both measure the speed of sound from the slope of a distance-time table with an unknown constant offset, in neighbouring chapters (341 and 343 m/s); the idea is the same, only the set-up differs — consider varying one (e.g. fy5-11 asks the echo factor 2 as the point).

## Checked
- Hash f7eb8d3fceb84386 (matches the packet). Opened open-exercises-L3-1280-7 (L3-04 Järkevyys, L3-05 task, table, Annettu/Periaate; Kaava row blank).
- New tasks read in full; recomputed: L1-08 1,4 km, L2-05 2,6 m/s, L2-06 3,0 m/s (swap gives 0,33), L2-07 341 m/s, L3-04 v²/F about 22, 5,1 m, L3-05 4,9 s: all consistent. Tables and a/b text clean. Graph kind only where a graph is asked.

## Scores
illustrations 5 · typography 2 (blank chains) · Finnish 4 · accessibility 3
