VERDICT: PASS
CONTENT-HASH: 1c5432d0afe46711

## Blocking

## Polish
- inquiry.json koe-1 question.solution "Vastaus" — the new prompt asks for the exact initial temperature, and the answer key is $26{,}6\,{}^\circ\text{C}$, but the solution's answer line leads with $27\,{}^\circ\text{C}$ and gives $26{,}57$ only in brackets. A student who enters 27 is marked wrong (tolerance 0,05). Lead with $26{,}6\,{}^\circ\text{C}$ and explain that the slider bracket justifies three figures here, or say that the key asks for one decimal. (This predates the diff, but the new prompt makes it more visible.)

## Checked
- Delta only: the hook text and the lesson's Miksi question now say "lasissa" instead of "lasin pohjalla/pohjalle". This is a physics improvement: ice is less dense than water, so it floats and does not sit on the bottom. It now matches "kellua" in the same sentence.
- koe-1 prompt: the old wording ("no ice left but the final temperature not yet above 0 °C") described a single point that a slider with $0{,}5\,{}^\circ\text{C}$ steps cannot bracket. The new wording (two successive slider values, then the exact threshold where all the ice just melts and the end state is exactly $0\,{}^\circ\text{C}$) states the boundary case correctly (≥, guardrail).
- Recomputed: $s m_\text{j}/(c_\text{v} m_\text{v}) = 33\,400/1257 = 26{,}57\,\text{K}$, so the threshold is $26{,}57\,{}^\circ\text{C}$. It lies in the bracket $26{,}5\ldots27{,}0\,{}^\circ\text{C}$ that the solution names, and the key 26,6 (tolerance 0,05) accepts it. The initial state (ice at $0\,{}^\circ\text{C}$, $T_\text{j}$ locked) is the same as the solution's assumption.
- The new prompt agrees with the johtopäätös model answer ($T_\text{v} \ge 26{,}6\,{}^\circ\text{C}$) and with hint 2.
- Content hash at the start and at the end: 1c5432d0afe46711.
