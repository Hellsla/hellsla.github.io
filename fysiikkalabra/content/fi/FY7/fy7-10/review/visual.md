VERDICT: FAIL
CONTENT-HASH: 98bc56f76f95a9e3
## Blocking
- Pysähdy ja mieti answer (opened, `details.stop-think-a`) is a formula chain wider than the 360 px column, clipped or scrolling by 130 px at 360 px (`check_layout.py fy7-10 --width 360`, fi, en and fi-easy): `v = c : n = 3{,}00 \cdot 10^{8}\,\text{m/s} : 2{,}42 \approx 1{,}24 \cdot 10^{8}\,\text{m/s}`. Essential content of the new block is not fully shown. Fix in the shared component (scripts/stopthink.py: pass the answer through the same chain/row layout as lesson text, scripts/mathlayout.py), never by hand-splitting the lesson text.
## Polish

## Checked
batch delta review: read the diff (3 new pysahdy blocks: placement, question wording, answer notation), ran check_layout.py at 360 px with the answer open; spot-checked sibling lessons' captures for block rendering (label, closed answer, spacing). Own 390 px capture of this lesson not opened.
