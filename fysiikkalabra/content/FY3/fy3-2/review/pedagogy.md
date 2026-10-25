VERDICT: PASS
CONTENT-HASH: 0e6f5c36e1389db3

## Blocking

## Polish
- inquiry.json:hook — "Fysiikassa vain toinen tekee" lets the student guess the answer to the opening question before committing (hissi vs. kantaminen); the question itself (what should "työ" mean?) stays open, but end the text at "Arkikielessä molemmat tekevät työtä." and let pred-3 do the sorting.
- inquiry.json:pred-3 — the only prediction with no experiment and no reveal gate; the sim pulls only along the motion, so nothing in Tutki can test it, and the right option's feedback names no evidence. Fix: add a one-line note that the sim covers only motion-parallel force, or gate pred-3 on the reflect step.
- inquiry.json:joule — at 390 px the third column header "Lämpömäärä Q (J)" is clipped (table scrolls sideways). Fix: shorten headers to "W (J)" and "Q (J)".
- lesson.md:156 — heading is "## Kaavat"; house form says "## Kaava". Check the lint expectation and align.
- Workload: 3 predictions, 2 experiments, interpret, example, error item, transfer, 12 exercises, 3 checks and exit ticket is near the upper limit of one lesson; consider trimming if students report fatigue.

## Checked
- Prerequisite: pr-paino retrieves G = mg from fy3-1; matches prior.
- Opening question is answered in Selitä/reflect, not before commitment; feedback gated by reveal (pred-1, pred-2).
- Variable control: exp-1 varies s only (F, t locked); exp-2 varies t only; each can refute its prediction (W doubles; W same, P falls).
- Wrong-option feedback repairs the misconception (work vs. time, work vs. power, force vs. effort).
- Worked example: 5 stages, symbolic first, then substitution, sanity check; figure present; not repeated by exercises (virhe item deliberately reuses it).
- Exercise levels 5/4/3 fit the rubric; L3 items need reasoning; exit ticket tests the core ideas.
- Finnish: case after number+unit correct (80 N:n, 36 kJ:n); glossary terms consistent; model vs. measurement wording kept.
- Phone: 390 px page and sim readable, sliders and Vedä usable, readout under canvas; figures legible.
- Playwright 390 px on preview: wrong pred-1 committed, feedback hidden; still hidden after 1 recorded measurement; shown after the 2nd (s=20); reflection section present.
