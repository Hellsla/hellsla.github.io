VERDICT: FAIL
CONTENT-HASH: 98de5c06868345fc
SCOPE: delta (Stop and think boxes only, git diff origin/main)

1. Blocking:
- B (internal consistency/order): the edit moved the `usf` figure (graph of U_s against f, slope = h/e, threshold frequencies of Na and Zn), not just the box. The figure now sits on lines 52-117, right after the `energy` figure in Key idea. That is before eV, Einstein's equation, the retarding voltage and U_s are defined (lines 125-159). On origin/main it came after "The work function only moves the line sideways." The reader meets a graph of a quantity that has not been introduced yet. The third box ("same slope") is now no longer next to the graph it relies on. Fix: keep `usf` after line 159, followed by the "same slope" box. Put the hf < W box straight after the `energy` figure (line 50).
2. Checked: box 1 (hf < W: the energy is lost as heat) restates line 32, which comes before it; at this level it is C under the guardrails, and the wording was already there before the edit. Box 2: 2.0 V gives 2.0 eV, correct and follows from the eV definition. Box 3: the slope is h/e, a constant, and W only shifts the line; correct. Fences and LaTeX are well formed. Hash is the same at start and end.
