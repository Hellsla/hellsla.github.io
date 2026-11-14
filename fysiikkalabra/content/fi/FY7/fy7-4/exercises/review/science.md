VERDICT: PASS
CONTENT-HASH: f44c17044fad7b3b
SCOPE: delta added-exercise from eb78314c0c339d07 base 8f23aa7ae3bd

## Blocking

## Polish
- figures.py force_angle description "tasaisesti nouseva käyrä" — the curve is 0,45 N · sin α, rising ever more slowly; "nouseva ja loiveneva käyrä" would not suggest a straight line to a reader who cannot see it.

## Checked
- Delta: L2-09 added; hash identical at start and end.
- Points 0,12/0,22/0,32/0,39/0,44/0,45 N agree with 0,45 sin α within ±0,01 N; reading F_max on the fitted curve at 90° (a grid point) is right practice.
- B = F_max/(I l) = 0,45/(6,0 · 0,25) = 0,30 T = answers.py; check at 30° gives 0,30 T; magnitude realistic for a magnet gap.
- α defined as the angle between wire and field, consistent with F = I l B sin α.
