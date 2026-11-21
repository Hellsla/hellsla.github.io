VERDICT: FAIL
CONTENT-HASH: 039c8cf75efde315
## Blocking
- Pysähdy ja mieti answer (opened, `details.stop-think-a`) is a formula chain wider than the 360 px column, clipped or scrolling by 198 px at 360 px (`check_layout.py fy7-4 --width 360`, fi, en and fi-easy): `F = I l B \sin\alpha = 4{,}0\,\text{A} \cdot 0{,}50\,\text{m} \cdot ... \approx 0{,}25\,\text{N}`. Essential content of the new block is not fully shown. Fix in the shared component (scripts/stopthink.py: pass the answer through the same chain/row layout as lesson text, scripts/mathlayout.py), never by hand-splitting the lesson text.
## Polish
- Answer: the chain ends with `\approx 0{,}25\,\text{N}`, but 4,0 * 0,50 * 0,25 * 0,5 is exactly 0,25; `=` is cleaner.
## Checked
batch delta review: read the diff (3 new pysahdy blocks: placement, question wording, answer notation), ran check_layout.py at 360 px with the answer open; spot-checked sibling lessons' captures for block rendering (label, closed answer, spacing). Own 390 px capture of this lesson not opened.
