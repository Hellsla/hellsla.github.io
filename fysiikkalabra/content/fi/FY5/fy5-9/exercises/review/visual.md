VERDICT: FAIL
CONTENT-HASH: 1908baceb1a28e91

## Blocking
- [Major] solutions card, every multi-step chain (`.eq-chain` rows: Kaava, Muunnokset, Sijoitus, Järkevyys) in the NEW tasks (L2-05, L2-06, L2-07, L3-04, L3-05) — the chain renders as an empty white box about 36 px wide, so the model solution shows words ("joten", "Kohta a):") with no calculation. Seen in the 1280 captures (open-exercises-L2-1280-7/8/9, L3-1280-8) and reproduced in a fresh render of preview/fy5-9.html with all details open (grid columns collapse to `0px 0px`, chains carry `kx-wide data-glued`; flaky: sometimes they render at about 250 px). The same boxes appear in untouched old tasks, so it is the site-wide "inline formulas never wrap" change (kx-wide/glued script with `.eq-chain` in templates/site.css line 343), not the content — but it hides the required solution steps of every new task that has a chain. Fix (template, not content): make `.eq-chain` keep its content width inside opened solution cards (e.g. `min-width:min-content` on the grid columns / skip kx-wide gluing inside `.eq-chain`), rebuild, retake the shots, re-review.

## Polish
- [Minor] fy5-9-L1-07 — the correct option "lyhenee, koska jousivakio on neliöjuuren sisällä" gives a formula position as the reason, not a physical one — e.g. "koska jäykempi jousi kiihdyttää kappaletta nopeammin"; the formula goes in the feedback only.
- [Minor] fy5-9-L2-05 solution — the line is said to pass through the last data point (1,00 m; 4,04 s²) although it is a fit; fine for the answer, but "suora kulkee origon ja pisteen" reads like a two-point read; add "likimain".
- [Minor] the Kaava row of L2-05/06 `a = T²/m = 4π²/k, joten k = 4π²/a` is a chain mixed with a following clause; once chains render, check that it breaks at the clause.

## Checked
- Hash 1908baceb1a28e91 (same at start and end). Opened open-exercises-1280-8 (L1-07, L1-08), L2-1280-2 (old L2-02, shows the same blank chains), -7, -8, -9 (L2-06, L2-07, tables, a/b text), L3-1280-8 (L3-05 solution).
- New tasks read in full (text, data, choices, solutions); answers recomputed: L2-05 g 9,78, L2-06 k 20,1, L2-07 7,2 %, L3-04 k 25,1 N/m, m0 21 g, 30 % too low, L3-05 0,598 m/s, 0,13 %: all match their solutions. Graph kind only where a graph is asked; data error direction (large angle gives longer T) correct. No duplicate in fy5-7/8.

## Scores
illustrations 5 · typography 2 (blank chains) · Finnish 5 · accessibility 3
