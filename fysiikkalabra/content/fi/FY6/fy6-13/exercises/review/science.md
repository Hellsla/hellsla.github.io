VERDICT: PASS
CONTENT-HASH: 6f38db9cc5bb5b1e
Round: 2, science, mode full. Scope: the round-1 fixes to fy6-13-L1-09 (commit 57a66480d). The rest of the set is unchanged. Checked from text only, no renders.

## Blocking

## Polish

## Checked
- Statement 2 now reads "virta kulkee … eristeen läpi samalla tavalla kuin johtimissa". It is false by the lesson's model and is no longer contradicted by electrolytic leakage, so the round-1 polish item is resolved. Its feedback adds "Eriste ei johda sähköä", which matches the lesson.
- Statements 1 and 4: only the feedback chains were split. I recomputed Q = 1,2 mC, QU = 14,4 mJ, ½QU = 7,2 mJ and 28,8 mJ at 24 V.
- The truth values T, F, F, F, T are unchanged, and the answer string, statements and solution agree.
- Solution: Q = CU and W = ½CU² each stand on their own row before substitution, and the verdicts are five paragraphs. The physics is unchanged, including the "half to the resistor" point within the lesson's resistive charging model.
- All numeric answers of the set were recomputed from answers.py in one call: no mismatch.
- Inline width (text estimate): the longest row, `W = ½ · 100 · 10⁻⁶ F · (12 V)²`, is about 220 px.
