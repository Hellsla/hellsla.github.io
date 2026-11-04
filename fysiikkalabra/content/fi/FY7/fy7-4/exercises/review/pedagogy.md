VERDICT: FAIL
CONTENT-HASH: e1d566ce1d59da9e

## Blocking
- solutions.md fy7-4-L3-05, Sijoitus (a) — the display chain `I = \sqrt{\dfrac{2\pi \cdot 0{,}010\,\text{m} \cdot 0{,}0030\,\text{kg} \cdot 9{,}81\,\text{m/s}^2}{4\pi \cdot 10^{-7}\,\tfrac{\text{Vs}}{\text{Am}} \cdot 0{,}50\,\text{m}}} = \sqrt{2943\,\text{A}^2} = 54{,}25\,\text{A}` overflows a 360 px phone by 6 px (`check_layout.py` FAIL, "cannot wrap"; the only deterministic failure, also reported by the visual reviewer) — split it: first the denominator `\mu_0 l = 6{,}28 \cdot 10^{-7}\,\text{Vs/A}`, then `I = \sqrt{\dfrac{2\pi \cdot 0{,}010 \cdot 0{,}0030 \cdot 9{,}81}{6{,}28 \cdot 10^{-7}}}\,\text{A}`, and put `= \sqrt{2943}\,\text{A} = 54{,}25\,\text{A}` on its own row.

## Polish
- solutions.md fy7-4-L2-07 Järkevyys — uses a coil radius of 1,2 cm (about 70 turns, "lähellä 60"); the lesson example has 1,3 cm and 60 turns (l = 4,9 m). Use 1,3 cm: 5,3 m is then about 65 turns, and the students' check against the lesson example works.
- exercises.json fy7-4-L2-05, L2-07, L3-04 captions — "(esimerkkiaineisto)" plus maths in the caption makes the tables scroll at 360 px; shorten the caption and keep "esimerkkiaineisto" in the task text.
- solutions.md fy7-4-L1-08 Periaate — "verrannollinen sini $\sin\alpha$ eikä kulmaan" is ungrammatical: "verrannollinen kulman siniin $\sin\alpha$ eikä itse kulmaan $\alpha$".
- exercises.json fy7-4-L2-06 — the pupil's quoted solution uses straight quotes and a rounded F (3,04·10^-3 N); use ”…” and mark what is wrong in a), not only in the solution, by saying "Etsi virhe" with the numbers 6,0 cm and 2,5 cm left visible (already so); consider letting b) ask for the percentage error of the pupil's result.
- exercises.json fy7-4-L3-05 b) — only the vertical stability is asked; add one sentence to the solution that sideways the arrangement is unstable (the wires would flip), so the word "vakaa" is not taken as a general result.

## Checked
- New tasks L1-06..08, L2-05..07, L3-04..05 recomputed: 0,30 N; 0,094 N; B values 0,0858/0,0834/0,0871/0,0844/0,0850 T, mean 0,085 T; 0,0405 T (pupil's 0,017 T explained by 2,5 : 6,0); 5,3 m; 0,351 T and μ = 0,20; 54,25 A. All match answers and tolerances.
- L1-06 direction: current east, field north gives force up (I × B), correct; distractors are real misconceptions with repairing feedback.
- Levels fit: L2 error analysis (the plan's "koko johtimen pituus" error), data with mean and spread, graph of the speaker coil; L3 friction rail model and levitating wire in YO style; counts 8/7/5.
- No duplicate of the speaker-coil worked example; L3-04 builds on L2-04 without repeating it.
- Solutions have all steps and sanity checks; Finnish otherwise correct.
- Screenshots not opened; phone fit judged from the 360 px layout check output.
