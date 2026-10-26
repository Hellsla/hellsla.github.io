VERDICT: PASS
CONTENT-HASH: e56ebee5dbb1da71

## Blocking
(none)

## Polish
- sim canvas and DOM readout (sim.js; captures exp-1-390-1, lab-1280-1) — "p/p_ref", "V = 100 %", "N = 100", "Mitattu paine p/p_ref = 1,43" are plain interface text beside the maths-typeset experiment lines and table headers; the mismatch is visible side by side. Per NOTES.md §1 this stays until the teacher decides; list only.
- inquiry.json "pred-n" — the 4th option's feedback ("Mittauksissa paine kaksinkertaistui") is fine, but options 1 and 3 say "Mittauksissa ... kasvoi" before the student has tested anything if the box is opened early; the reveal gating keeps this safe, so only reword to "Koe 1 näytti" for clarity.
- inquiry.json "punnitus" — the "esimerkkiarvoja, hajonta ±0,02 g" is clear, but helium 0,83 g gives 0,2075 mol against the lesson.md 0,207 mol average: say "noin 0,207 mol" in the question prompt too so rounding does not look like an error.
- inquiry.json "exp-2" — 600 K and N = 100 gives p about 2,0; students may need ~4 s per reading at 0,5x speed twice; consider naming the speed option "nopea" in the intro to keep the hour realistic.
- lesson.md "Esimerkki" Järkevyys — one stage carries two ideas (24 l check and the air balloon comparison); the second could go to the Yleinen virhekäsitys section.

## Checked
- Round-1 blocking items fixed: exit-ticket and inquiry symbols render as maths; experiment Alkutila/Vakiona lines and table headers are maths in the captures.
- Learning path: hook, Boyle retrieval, prediction (reveal after exp-1, min 2), weighing, sim, experiments, theory, reflection, example, error-spotting, transfer, exercises, three checks, exit ticket; opening question answered only after commitment.
- Experiments can refute their predictions (exp-1 measures hit rate and pressure; exp-2 lets the student find N = 50 from data, not a displayed formula).
- Weighing data are consistent (0,83/4,00 ... 9,10/44,0 all 0,206-0,208 mol); R about 8,3 follows; balloon problem 2640 kg checks out.
- Worked example staged in five steps; transfer task has three hints and mistake feedback; check-3 has model answer and criteria.
- Exercises: three levels, none repeats the example; solutions in LaTeX with sensible checks.
- Figures legible at 390 px; wide layout at 1280 px puts the sim beside the experiments with no clipping.
- Finnish and glossary terms (ainemäärä, moolimassa, moolinen kaasuvakio) correct; case after number+unit fine.
- Workload fits one lesson.
