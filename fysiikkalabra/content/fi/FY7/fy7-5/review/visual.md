VERDICT: FAIL
CONTENT-HASH: 5bf3eff7e60f102c
## Blocking
- Pysähdy ja mieti answer (opened, `details.stop-think-a`) is a formula chain wider than the 360 px column, clipped or scrolling by 22 px at 360 px (`check_layout.py fy7-5 --width 360`, fi, en and fi-easy): `|e| = 200 \cdot 0{,}020\,\text{Wb} : 0{,}50\,\text{s} = 8{,}0\,\text{V}`. Essential content of the new block is not fully shown. Fix in the shared component (scripts/stopthink.py: pass the answer through the same chain/row layout as lesson text, scripts/mathlayout.py), never by hand-splitting the lesson text.
## Polish

## Checked
batch delta review: read the diff (3 new pysahdy blocks: placement, question wording, answer notation), ran check_layout.py at 360 px with the answer open; spot-checked sibling lessons' captures for block rendering (label, closed answer, spacing). Own 390 px capture of this lesson not opened.
