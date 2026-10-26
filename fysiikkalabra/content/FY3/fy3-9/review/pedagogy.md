VERDICT: FAIL
CONTENT-HASH: 2bf5975e86980e7d

## Blocking
- inquiry.json:3,66,103,127,216,236,239-243; exercises.json:64,90; exit-ticket.json:4-8 — the rule "symbols in prose as maths" is not met: "(V, p)-koordinaatistossa", "(1/V, p)-pisteet", "(T, V)-kuvaajasta", "1/V:n funktiona", "tai 1/V", "p₁V₁", "p₂", "V₂", "θ" stand as plain text, while the same symbols are in $...$ elsewhere (lesson.md uses $1/V$, $(V, p)$). The student sees two typefaces for one symbol. Fix: wrap every symbol, pair and formula in prose in $...$ ($(V, p)$, $1/V$, $p_1V_1$, $\theta$), also in exp-1/exp-2 intros and exit-ticket answers.
- sim.js:110-114 and the table headers — the simulation's readout and table (T = 293 K, "Vakio pV = ...", V/T, 1/V, tilavuus V, θ) are monospace/plain text, not maths. The same rule applies to the page text behind the named boxes. Fix: render the readout symbols as italic/KaTeX (or at least italic with proper subscripts) and the table headers likewise.

## Polish
- fy3-9-fig-5 (absolute-zero): the "−273 °C" label under the origin sits on the figure's bottom edge in both plots and is nearly clipped at 390 px; add bottom margin to the viewBox.
- sim: the gauge scale numbers "100" and "200" are overlapped by the needle and cramped at 390 px; enlarge the dial or leave out the 100 label. The "Nopeus" control is clear and its note correctly says it changes only pace.
- solutions.md L2-01: the closing remark on real-gas deviation (≈1,8 m³) contradicts the answer 2,0 m³ asked under "oleta että Boylen laki pätee"; move it to a separate "Huomio" line or drop it.
- lesson.md:111 — "Kireässä pussissa ilman paine pysyy hieman matkustamon painetta suurempana" → "Kireässä pussissa ilman paine on hieman suurempi kuin matkustamon paine".
- ruisku (inquiry.json:127): "Laske taulukkoon uusi sarake pV (tai 1/V)" — give the student a space to enter the computed column, or state that the row 30 ml is what to find by calculation; now it is a pure mental check.

## Checked
- Figures 2-5 (micro-boyle, iso-processes, boyle-graphs, absolute-zero) in the captures: all labels in LaTeX type, uncluttered, colour paired with labels (T₁/T₂, "kaari"/"suora", "jatke"), print quality; each sits beside the paragraph it explains; they teach the mechanism, the curve-versus-line step and the extrapolation.
- Layout: phone captures at 390 px have nothing clipped, the lab at 1280 px puts the simulation beside the experiments; worked example is five stages, one step each, solved symbolically first.
- No lesson ids in prose; prerequisites cited by chapter names (*Paine ja hydrostaattinen paine*, *Lämpölaajeneminen*).
- Predictions are refutable by exp-1 and exp-2 (reveal after min 2/3 recordings), wrong options' feedback repairs the misconception; no answer disclosed before commitment.
- ruisku item gives noisy data and a real reason (heating on fast compression); check-3 has model answer and criteria; exit ticket tests the core idea.
- Exercises: three levels, none repeats the sipsipussi example; Finnish reads well; workload is one lesson.
- Solutions in LaTeX with symbolic step first; numbers verified (L1-04 2,6 l, L2-02 90 °C, L3-02 202 kPa).
