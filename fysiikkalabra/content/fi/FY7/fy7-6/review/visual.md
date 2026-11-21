VERDICT: FAIL
CONTENT-HASH: 9fe1c3d74e83aec1
## Blocking
- lesson.md line 172: the edit turned `<figure class="unit-photo">` into `<figurefigure class="unit-photo">` (the eddy-current-brake photo). The element is unknown, so the photo renders unstyled at full width (366x1270 px at 390 px, page overflow 1256 px at 360 px in check_layout), without the expand button and credit line, and its caption is cut from it. See review/shots/fy7-6-stage-selita-390-3.png. Restore `<figure`.
- Pysähdy ja mieti answer chains `F = mg = 0{,}020\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 \approx 0{,}196\,\text{N}` (69 px) and `P = Fv \approx ...\approx 0{,}059\,\text{W}` (59 px) are clipped at 360 px in the opened answer (check_layout, fi, en, fi-easy). Fix in the shared component (scripts/stopthink.py through mathlayout), not by hand.
## Polish

## Checked
batch delta review: opened the stage-Teoria captures at 390 px (pysahdy block label, question, closed answer, spacing, placement after the paragraph it follows) and the figure captures; ran check_layout.py at 360 px for the lesson; read the diff for wording and notation. Answer opened only through check_layout (no capture of an open answer).
