VERDICT: FAIL
CONTENT-HASH: 666d88a4cc20c442
## Blocking
- Pysähdy ja mieti answer (opened, `details.stop-think-a`) is a formula chain wider than the 360 px column, clipped or scrolling by 344 px at 360 px (`check_layout.py fy7-15 --width 360`, fi, en and fi-easy): `I = I_0 \cos^2\theta = 200\,\text{W/m}^2 \cdot \cos^2 60^\circ = ... = 50\,\text{W/m}^2`. Essential content of the new block is not fully shown. Fix in the shared component (scripts/stopthink.py: pass the answer through the same chain/row layout as lesson text, scripts/mathlayout.py), never by hand-splitting the lesson text.
## Polish

## Checked
batch delta review: read the diff (3 new pysahdy blocks: placement, question wording, answer notation), ran check_layout.py at 360 px with the answer open; spot-checked sibling lessons' captures for block rendering (label, closed answer, spacing). Own 390 px capture of this lesson not opened.
