VERDICT: PASS
CONTENT-HASH: 2474e1ec80a119e6

## Blocking
- None.

## Polish
- None.

## Checked
- Delta review, round 4: `johtopaatos` criterion 3 now reads "hehkulampun hyötysuhde on noin $5\,\%$. Siis vain pieni osa otetusta energiasta on hyötyä." It is about the lamp of koe-2, which the conclusion comes `after`. The core-path task gives the data for it, and criterion 1 already asks for the calculation that produces it (7).
- The model answer meets all three criteria: the definition with numbers, the time cancelling, and $5\,\%$ with the remaining $95\,\%$ as losses (6).
- Recomputed: $P_\text{o} = 40\,\text{W}$, $\eta = 0{,}05$. $t = 10\,\text{s}$ gives $400\,\text{J}$ / $20\,\text{J}$ and $t = 20\,\text{s}$ gives $800\,\text{J}$ / $40\,\text{J}$, both $5\,\%$. $P_\text{a} = 2{,}0\,\text{W}$, losses $95\,\%$. All agree (4).
- Nothing in the criterion refers to the optional koe-1 or to the engine. It matches the koe-2 feedback (line 229, 235) and the lamp value used elsewhere in the lesson (line 75, 442).
- The rest of the diff (ennuste-1 and koe-1 `optional`, koe-1 hint 3 in kJ) is unchanged since round 3 and was judged there.
- Hash `--lang fi-easy` identical at start and end.
