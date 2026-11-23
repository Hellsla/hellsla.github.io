VERDICT: PASS
CONTENT-HASH: 66cbf9bb521d16b8
SCOPE: delta md-paragraphs,numbers,reflow,teacher-figure,typography from f2d06e99ef2be864 base e238aa9

## Blocking

## Polish
- exercises/solutions.md:185 (L3-05 Kaava) — $t$ stands for two different times in one aligned block: the time in $I = \dfrac{Ne}{t}$ (one second) and the travel time $t = \dfrac{s}{v}$ — name the travel time differently, e.g. $t_\text{matka} = \dfrac{s}{v}$.
- exercises/solutions.md:147 (L2-05 Kaava) — the old version said what $I_\text{väli}$ is in the Kaava line; now only the Periaate says it. Fine as it is; the earlier Polish items (L1-01 $P = UI$ comparison, L2-06 b) wording, L3-05 $14{,}5\,\text{h}$ rounding) still stand.

## Checked
- Delta only: every Kaava step now an aligned block that starts from the definition ($I = \dfrac{Q}{t}$, $U = \dfrac{E}{Q}$, $Q = Ne$) and then solves for the unknown; each rearrangement is algebraically right and ends in the form the Sijoitus row uses.
- L3-04 Kaava now starts from $U = \dfrac{E}{Q}$ and $Q = It$ before $E_k = U_k I_k t$: consistent with its Periaate. L2-08 starts from $U = \dfrac{E}{Q}$, then $Q = I_0 t_1 + \tfrac{1}{2} I_0 t_2$ (rectangle plus triangle): right.
- Recomputed in one script all 16 answers (20 C, 1800 J, 30 s, 108 C, 9,99·10¹⁷, 39,96 kJ, 11 C, 8,0 h, 1,2, 9,36·10¹⁹, 22,8 C, 140 J, 12,5 Wh, 1,92·10⁻² mm/s …): all agree with answers.py; no number in the diff changed.
- Model answers L1-05, L1-06, L1-07, L2-06, L2-07 only split into paragraphs; wording and physics identical.
- kaavio-malli picture: teacher-approved figure, generator unchanged; still matches the model answer (cells plus up, current from + along the top).
- Hash identical at start and end.
