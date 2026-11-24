VERDICT: PASS
CONTENT-HASH: 93390456432de3c2

## Blocking

## Polish
- inquiry.json koe-3 question, third option — this distractor reaches the right conclusion ("Ei sovi") for a wrong reason. That is fine because the prompt asks "Mistä päättelet?", but the feedback never says the conclusion itself is right. A student who chose it may think a line fits. Fix: open the feedback with "Johtopäätös on oikea, mutta perustelu ei:".

## Checked
- Delta: only the text of koe-3's third option changed ("vaikka mittaukset olisivat tarkkoja" was removed). The physics is unchanged. The option is still a wrong reason, and the feedback still names the right criterion: random residuals versus a pattern. It also says "yleensä", as the guardrail asks.
- Exactly one option is correct. The correct option's pattern (above the line at the ends, below it in the middle) is the one I recomputed in round 1: residuals $+10, -0{,}9, -5{,}7, -6{,}2, -3{,}7, +0{,}9, +7$ with $b = 80$. The two "Sopii" options stay wrong, and their feedback is right.
- The prompt's numbers ($5{,}8\,{}^\circ\text{C}$ minimum, $60\,{}^\circ\text{C}$ change) were not touched and match the round-1 recomputation (minimum $d = 5{,}80\,{}^\circ\text{C}$ at $k = -1{,}90$).
- The content hash was the same at the start and the end of the review.
- My round-1 polish items still apply where that text is unchanged. None of them blocks.
