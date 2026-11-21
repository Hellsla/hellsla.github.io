VERDICT: FAIL
CONTENT-HASH: 7a13db15ea11f6eb
## Blocking
- Pysähdy ja mieti answer (opened, `details.stop-think-a`) is a formula chain wider than the 360 px column, clipped or scrolling by 117 px at 360 px (`check_layout.py fy7-3 --width 360`, fi, en and fi-easy): `B = \mu_0 \tfrac{N I}{l} = 4\pi \cdot 10^{-7}\,\tfrac{\text{Vs}}{\text{Am}} \cdot ... \approx 2{,}51\,\text{mT}`. Essential content of the new block is not fully shown. Fix in the shared component (scripts/stopthink.py: pass the answer through the same chain/row layout as lesson text, scripts/mathlayout.py), never by hand-splitting the lesson text.
## Polish
- The long chain with nested `\tfrac` units will need row-breaking at an `=` or `\cdot` boundary once the component is fixed.
## Checked
batch delta review: opened the stage-Teoria captures at 390 px (pysahdy block label, question, closed answer, spacing, placement after the paragraph it follows) and the figure captures; ran check_layout.py at 360 px for the lesson; read the diff for wording and notation. Answer opened only through check_layout (no capture of an open answer).
