VERDICT: FAIL
CONTENT-HASH: 2c00c7827a1d53fa

## Blocking
- [Major] solutions card, every multi-step chain (`.eq-chain` rows: Kaava, Muunnokset, Sijoitus, Järkevyys) in the NEW tasks (L2-05, L2-06, L3-04, L3-05: Kaava, Muunnokset, Järkevyys rows; the aligned display blocks render) — the chain renders as an empty white box about 36 px wide, so the model solution shows words ("joten", "Kohta a):") with no calculation. Seen in the 1280 captures (open-exercises-L3-1280-7) and reproduced in a fresh render of preview/fy5-11.html with all details open (grid columns collapse to `0px 0px`, chains carry `kx-wide data-glued`; flaky: sometimes they render at about 250 px). The same boxes appear in untouched old tasks, so it is the site-wide "inline formulas never wrap" change (kx-wide/glued script with `.eq-chain` in templates/site.css line 343), not the content — but it hides the required solution steps of every new task that has a chain. Fix (template, not content): make `.eq-chain` keep its content width inside opened solution cards (e.g. `min-width:min-content` on the grid columns / skip kx-wide gluing inside `.eq-chain`), rebuild, retake the shots, re-review.

## Polish
- [Minor] fy5-11-L3-04 — the steepest slope is 35 degrees, but part c) and the solution call it a "jyrkänne"; say "jyrkin kohta" or "jyrkempi rinne".
- [Minor] fy5-11-L1-08 — same situation as fy5-17-L1-03 (sonar depth from echo, 1480–1500 m/s) in the order delay from depth; near-duplicate in a later chapter, consider a different context (e.g. echo from a cliff in air).
- [Minor] fy5-11-L2-05 Kysytty — "Anna vastaus yksikössä m/s" is a plain unit in prose; set it as `$\text{m/s}$` (also fy5-11-L2-06, fy5-12 "hertseinä" is a word and fine).

## Checked
- Hash 2c00c7827a1d53fa (matches the packet). Opened open-exercises-L3-1280-7 (L3-05 solution with aligned blocks fine, blank chains in Muunnokset and Järkevyys).
- New tasks read in full; recomputed: L1-08 48 ms, L2-05 343 m/s (round trip 2d), L2-06 8,0, L2-07 32 degrees, L3-04 depths 40,0..71,8 m and 35 degrees, L3-05 200: all match. Scope (reflection, diffraction, echo) fits the chapter; simplifying assumptions consistent with the explanations.

## Scores
illustrations 5 · typography 3 (blank chains) · Finnish 5 · accessibility 3
