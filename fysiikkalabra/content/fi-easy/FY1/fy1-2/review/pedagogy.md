VERDICT: PASS
CONTENT-HASH: b84e90cd29627708

## Blocking

## Polish
- inquiry.json (koe-1, koe-2) — both experiments show the same fact (t ∝ s). The investigation never makes the student convert a unit or round, which are the slot's goals. Make one recorded step a conversion (km to AU by hand, then compare with the readout) and keep the other as the check — fix: change koe-1's `intro`.
- inquiry.json `ennuste-2` — the title "kauempana oleva luotain" does not match its question about light and distance. The prompt already gives the 33 s base, so the answer follows from one multiplication. Rename it "Valon kulkuaika kymmenkertaisella matkalla" and ask for the reasoning in `justify`.
- inquiry.json `voyager-malli` — the correct option is much longer than the other two, so it can be picked without reading. It also asks about "malli vs mittaus" before the student has seen a measurement. Shorten it to one sentence and move the 142,5 vs 143,05 AU comparison into the feedback only.
- lesson.md "Merkitsevät numerot" — the first paragraph is about 140 words and holds four rules. Split it at "Kuun keskietäisyydestä". The exit ticket has no sig-fig or AU item either, so swap one of its two items for `0,0250 m`.
- Source mismatch to pass to the science reviewer, not a pedagogy blocker: the scope brief gives 119,7 AU at the heliopause but the sim and the text use 119,0 AU. Also, in fi-easy "suoraan verrannollinen" is used in feedback without being explained, and femto appears in the table but not in the prefix list or the figure.

## Checked
- Opening Miksi question: committed predictions come first, and it is answered in the explain item and in the reflect item.
- Prerequisites: the retrieval item (kertaus) uses powers of ten from fy1-1 and has misconception-based distractors, each with repairing feedback.
- Predictions: each wrong option's feedback names its misconception, and the experiments can refute them (the model gives 19,7 h and 3340 s).
- Variable control: koe-1 locks the date and varies n; koe-2 varies only the date. The 0,01 slider precision is tolerable on a phone.
- Worked example: seven stages, one step each, symbolic first, with a check. The numbers (4,50·10⁹ km, 4,17 h) are correct and it differs from the transfer task.
- Transfer task `siirto`: hints are progressive, the mistake values (484000000 and 3236) are real, and the solution is complete. tarkistus-2 is also complete.
- The three checks cover concept, application and explanation; the explain criteria are observable, and the correct options are not always first.
- Figures: hero, conversion and quantity read clearly at 390 px; the conversion figure's description gives the same data.
- Simulation at 390 and 1280 px: the visible lead is short, the controls fit, and usage, model and calc sit behind their boxes. At 1280 px it sits beside the experiments.
- Workload: heavy but within one lesson because the retrieval, reflect, Etsi virhe and sig-fig items are optional.
