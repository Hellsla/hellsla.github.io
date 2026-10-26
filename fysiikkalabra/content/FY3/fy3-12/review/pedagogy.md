VERDICT: PASS
CONTENT-HASH: 3c40c07fd4da8095

## Blocking
(none)

## Polish
- Round-1 polish still open (not re-judged, not blocking): pred-1/pred-2 both have Bea right and the correct option longest; figure "energy-balance" arrow does not split at the atmosphere and lacks "avaruus"; figure "heat-transfer" rod and vacuum unlabelled.
- Lesson has no simulation, so the NOTES.md §1 point (canvas and DOM readout as plain interface text) does not apply here.

## Checked
- Diff only touches symbols and numbers as maths: ΔT in the "Kun tasapaino rikkoutuu" text and table header, P = UAΔT and units in the exit-ticket answer, powers of ten and J/(kg·K) in L3-02. Values unchanged (5,1·10^14 m², 2,6·10^20 kg, 4,0·10^3 J/(kg·K); answer 0,139 K).
- LaTeX syntax is sound (`5{,}1`, `\tfrac{\text{J}}{\text{kg}\cdot\text{K}}`); decimal commas kept; checks (lint, latex, build, inquiry 41/41, layout 360) pass.
- No plain-text ΔT or unicode powers of ten remain in the lesson's JSON or lesson.md.
- Learning path, staging, worked example, exercise levels and exit ticket are unchanged since the round-1 PASS.
- Not seen: 768 and 1280 px captures of the figures and the maths table header (only the 1280 top capture exists).
