VERDICT: FAIL
CONTENT-HASH: 1841d4aa72592c3b

## Blocking
- [Major] solutions card, every multi-step chain (`.eq-chain` rows: Kaava, Muunnokset, Sijoitus, Järkevyys) in the NEW tasks (L2-05, L3-04, L3-05: Sijoitus rows in L3-05 are empty in the capture) — the chain renders as an empty white box about 36 px wide, so the model solution shows words ("joten", "Kohta a):") with no calculation. Seen in the 1280 captures (open-exercises-L3-1280-8, L2-1280-8) and reproduced in a fresh render of preview/fy5-12.html with all details open (grid columns collapse to `0px 0px`, chains carry `kx-wide data-glued`; flaky: sometimes they render at about 250 px). The same boxes appear in untouched old tasks, so it is the site-wide "inline formulas never wrap" change (kx-wide/glued script with `.eq-chain` in templates/site.css line 343), not the content — but it hides the required solution steps of every new task that has a chain. Fix (template, not content): make `.eq-chain` keep its content width inside opened solution cards (e.g. `min-width:min-content` on the grid columns / skip kx-wide gluing inside `.eq-chain`), rebuild, retake the shots, re-review.

## Polish
- [Minor] fy5-12-L2-05 text — the table header cell "Hiljainen kohta" with row labels "1." … "6." is plain text; fine, but "Mikä on äänen taajuus?" could say "Määritä äänen taajuus kaikkien kuuden kohdan avulla" so the solution use of x1 and x6 is not a surprise.
- [Minor] fy5-12-L3-05 — "kaksi merkitsevää numeroa" with answer 850 Hz: write 8,5 · 10^2 Hz in Vastaus to make the two figures visible.

## Checked
- Hash 1841d4aa72592c3b (matches the packet). Opened open-exercises-L3-1280-8 (L3-05 Sijoitus/Vastaus/Mallivastaus) and L2-1280-8 (L2-06 solution, L2-07 task and 9-row table).
- New tasks read in full; recomputed: L1-08 200 Hz, L2-05 680 Hz (minima at path differences 0,25 m steps), L2-07 lambda 2,0 cm and A 4,0 mm, L3-04 N at 4,00 m and 340 Hz, L3-05 y1 gives 853 Hz and y2 851 Hz with n=0 and n=1: all consistent.

## Scores
illustrations 5 · typography 2 (blank chains) · Finnish 5 · accessibility 3
