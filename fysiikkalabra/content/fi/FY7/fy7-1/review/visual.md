VERDICT: FAIL
CONTENT-HASH: ea82a77916d1dfc0
## Blocking
- Pysähdy ja mieti answer (opened, `details.stop-think-a`) is a formula chain wider than the 360 px column, clipped or scrolling by 26 px at 360 px (`check_layout.py fy7-1 --width 360`, fi, en and fi-easy): `B = \sqrt{(30\,\mu\text{T})^2 + (40\,\mu\text{T})^2} = 50\,\mu\text{T}`. Essential content of the new block is not fully shown. Fix in the shared component (scripts/stopthink.py: pass the answer through the same chain/row layout as lesson text, scripts/mathlayout.py), never by hand-splitting the lesson text.
## Polish

## Checked
batch delta review: opened the stage-Teoria captures at 390 px (pysahdy block label, question, closed answer, spacing, placement after the paragraph it follows) and the figure captures; ran check_layout.py at 360 px for the lesson; read the diff for wording and notation. Answer opened only through check_layout (no capture of an open answer).
