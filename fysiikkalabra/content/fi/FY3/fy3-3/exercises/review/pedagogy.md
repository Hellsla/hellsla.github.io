VERDICT: FAIL
CONTENT-HASH: 74b0725cf058af36

Delta review over the audit's PASS (d88a831999bf6f9a): L2-03 replaced by an extrapolation from a point graph (figure fy3-3/extrapolation-points).

## Blocking
- exercises.json:62-69 / solutions.md (L2-03) — tolerance 0,05 (45,1-49,9 kPa) does not accept every reasonable line, which NOTES §11 requires of a by-eye fit. The last point is at $102{,}5\,\text{kPa}$, not on a grid line (100 is the nearest); a student reading it as 100 and using it with (0; 75) gets $50\,\text{kPa}$ and is marked wrong, and the solution itself accepts 45-50 (50 is outside, 45 is outside by 0,1). The four middle points are off-grid too. Fix: widen to 0,08 (43,7-51,3), or put the last point on a crossing ((100 °C; 100 kPa), answer 50 kPa) and say the range.
## Polish
- Level 2 fits (read, slope, extrapolate); text says 'Oleta lineaarisesti' once, good. Figure at 360 px readable, but only 0 °C and 100 °C labelled on x beyond -100/-50; the faint grid makes 102,5 hard to read.
- The description lists 82, 89, 96 which no one can read exactly; harmless (only extremes needed) but the points are not exactly collinear (0,28 vs 0,26 kPa/°C), so which pair is used changes the answer by about 2 kPa.
## Checked
- Figure needed: no values in the text; data (0; 75) ... (100; 102,5) only in figure/description; the old task had the points in the text.
- $k=27{,}5/100=0{,}275$, $p=75-27{,}5=47{,}5$ kPa verified; solution has Kuvaajan lukeminen and all 7 stages.
- Not a repeat of check-2 (table, zero-pressure temperature), a different quantity.
