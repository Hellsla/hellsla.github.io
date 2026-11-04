VERDICT: PASS
CONTENT-HASH: 3f119d54f341f3cc

## Blocking

## Polish
- lesson.md (Common misconception) — carried over: "used in sterilisation and medicine ... not enough to change nuclei" holds for sterilisation and diagnostics; 15–18 MV radiotherapy makes some photoneutrons. C at this level.

## Checked
- Only change since the last PASS: lessons/FY8/fy8-12/figures.py:208 `tuntematon` d-axis labels every 6 mm instead of every 4 mm; grid (2 mm × 50 /min) and curve (800 /min, d½ = 12 mm) unchanged.
- Rendered SVG: d labels 6, 12, …, 48 at their grid lines; y labels 200–800. The curve meets 400 /min exactly at the labelled 12 mm line, so reading d½ = 12 mm still works; 24 mm → 200 and 48 mm → 50 (the solution's check) are also labelled.
- Tick labels are plain integers, so the English figure shows the same numbers; review/shots/fy8-12-fig-14-390.png shows them without overlap.
- figures.json alt text "thickness from zero to 48 millimetres, grid spacing 2 millimetres and 50 pulses per minute ... 800 pulses per minute" is still true; it does not mention label spacing.
- inquiry.json:390–411 (check 2): answer 12, tolerance 0.06, mistakes 24 and 400, hints and solution ("grid spacing 2 mm and 50 pulses per minute") still correct; no text refers to 4 mm labels.
- Content hash 3f119d54f341f3cc at start and end, equal to the packet.
- Round-1/2 recomputations unaffected (1.61·10⁵ ion pairs, 24 mm lead, Al 0.60, apron 5.6 %).
