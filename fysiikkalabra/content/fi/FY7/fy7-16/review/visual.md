VERDICT: FAIL
CONTENT-HASH: a04cee3f0da6f997
## Blocking
- First block question reads "Puhelin nostetaan langattoman laturin päältä $3\,\text{mm}$:n korkeudelle $20\,\text{mm}$:n korkeudelle.": two target heights, garbled, the starting height unclear (the figure shows z = 3 mm and z = 20 mm). Write e.g. "Puhelin nostetaan $3\,\text{mm}$:n korkeudelta $20\,\text{mm}$:n korkeudelle laturin yläpuolella." (see review/shots/fy7-16-stage-selita-390-2.png).
- Pysähdy ja mieti answer (opened, `details.stop-think-a`) is a formula chain wider than the 360 px column, clipped or scrolling by 56 px at 360 px (`check_layout.py fy7-16 --width 360`, fi, en and fi-easy): `A = aL = 0{,}18\,\text{dB/km}\cdot 50\,\text{km} = 9{,}0\,\text{dB}`. Essential content of the new block is not fully shown. Fix in the shared component (scripts/stopthink.py: pass the answer through the same chain/row layout as lesson text, scripts/mathlayout.py), never by hand-splitting the lesson text.
## Polish

## Checked
batch delta review: opened the stage-Teoria captures at 390 px (pysahdy block label, question, closed answer, spacing, placement after the paragraph it follows) and the figure captures; ran check_layout.py at 360 px for the lesson; read the diff for wording and notation. Answer opened only through check_layout (no capture of an open answer).
