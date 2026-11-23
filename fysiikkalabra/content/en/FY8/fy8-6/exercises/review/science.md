VERDICT: PASS
CONTENT-HASH: e4dcc85503760ad7
SCOPE: delta md-paragraphs,numbers,reflow,typography,wording from ceed05861c35b96a base 64d4935

## Blocking
(none)

## Polish
- exercises/solutions.md:375 fy8-6-L2-06 — "overshoots it a little" is right but vague: the overshoot ($\approx 0.07\,\text{V}$) is close to the gap itself ($\approx 0.09\,\text{V}$) — optionally write "and overshoots it by about $0.07\,\text{V}$", which also explains why $+3.65\,\%$ is smaller in size than Eero's $-4.5\,\%$.
- exercises/solutions.md fy8-6-L3-04 Formula — the last sentence still says "For a single LED $eU_\text{k} = hf$"; $\approx$ would match the first sentence and the glossary ($eU \approx hf$).
- exercises/solutions.md fy8-6-L3-02 Formula — say that $\Delta h = \tfrac{h_\text{max} - h_\text{min}}{2}$ is half the range of the steepest and shallowest lines (an estimate; guardrails "Showing uncertainty"). Carried over from earlier rounds.

## Checked
- Hash e4dcc85503760ad7 (with `--lang en`) at the start and at the end, the same as the packet's.
- Diff: only one L2-06 sentence and one symbol in the L3-04 Formula row changed. No numbers, answers, answers.py or tolerances changed.
- L2-06 recomputed: $\tfrac{hc}{e\lambda} = 1.968\,\text{V}$ at $630\,\text{nm}$. The gap to Eero's $1.88\,\text{V}$ is $0.088\,\text{V}$ ("about $0.1\,\text{V}$", correct). Salla's extra $2.04 - 1.88 = 0.16\,\text{V}$ is larger than the gap, so it cancels the gap and overshoots it by $0.072\,\text{V}$. The new wording is correct and the old "cancels part of" was wrong.
- L2-06 values: $h$ = $5.858$, $6.329$, $6.868 \cdot 10^{-34}\,\text{J}\,\text{s}$; deviations $-11.6\,\%$, $-4.5\,\%$, $+3.65\,\%$. All match the solution.
- L3-04: $eU_\text{k} \approx hf$ with the fitted line $U_\text{k} \approx \tfrac{h}{e} f + b$ now agrees with L1-05 and the glossary. This settles my earlier Polish item, except for the single-LED sentence above.
