VERDICT: FAIL
CONTENT-HASH: 4228b47aaf494d40

## Blocking
- [Major] inquiry.json, Examples-stage 'find the error' task (rendered at 390 px) — the calculation is written as an inline `$\begin{aligned}…$` inside a sentence, which KaTeX sets as a block centred vertically in the line: 'Opiskelija laskee:' / 'Missä on' sit beside the middle rows of the block and 'virhe?' falls below it, the closing full stop floats on the wrong row; the same happens inside the clickable answer option ('…so W = −90 J and [block] .') — the sentence is hard to read and the option looks broken — put the chain in display maths on its own lines (as fy2-2's 'Find the error' does), the sentence before it ending in a colon and the question after it; in the option put the chain after the sentence, or keep it as one inline chain.

## Polish
- none

## Checked
- batch delta review: rendered the changed prompt and option at 390 px in the page; figures untouched by the diff and not re-opened.
