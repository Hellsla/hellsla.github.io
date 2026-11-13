VERDICT: PASS
CONTENT-HASH: 61f5aabd12ab2d28
SCOPE: delta added-exercise from d7be126d63bbf8b3 base 81db4a6fd727

## Blocking
- none

## Polish
- exercises/solutions.md fy1-2-L1-10 — the MAFY mean distance 384 400 km is centre to centre, while the signal goes from the Moon's surface to the Earth's; surface to surface gives 1.255 s (2 % less, inside the tolerance), so four significant figures overstate the precision — add "(centre-to-centre distance; the radii are small beside it)" or give 1.28 s.

## Checked
- Added task fy1-2-L1-10 only; hash recomputed at start and end.
- Table value 384 400 km correct; c = 2.998·10^8 m/s given in the task.
- t = s/c for a signal at constant speed c; km → m conversion right.
- Independent recompute 1.28219 s = answers.py 1.282188; tolerance 4 % fits a table lookup.
- Reasonableness check (4·10^8 m over 3·10^8 m/s, a little over 1 s) is real.
- Inside FY1 scope (s = vt with c); en numbers identical to the Finnish original.
