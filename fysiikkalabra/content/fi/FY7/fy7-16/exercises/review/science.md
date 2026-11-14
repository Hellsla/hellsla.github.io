VERDICT: PASS
CONTENT-HASH: ac12902ca6fb50a6
SCOPE: delta added-exercise from 17151a3c70a4f503 base 8f23aa7ae3bd

## Blocking

## Polish

## Checked
- Delta round 2: L2-09 and L2-10 (added exercises); hash identical at start and end.
- L2-09: the task now fixes the transmitter current (round-1 polish done), so the line-count ratio equals the flux ratio; 6 lines at 3 mm, 4 at 6 mm (model ratio 0,669), e₀' = 4,2 V · 4/6 = 2,8 V = answers.py (model 2,81 V); e₀ = N·2πf·Φ₀ ∝ Φ₀ at fixed N, f.
- L2-10 (now 70 km): graph-curve is 0,30 dB/km, half power at 10,03 km (read 10 km); a = 10 dB · lg 2 / 10 km = 0,301 dB/km, A = 21,07 dB, P : P₀ = 0,78 % = answers.py; the exact curve gives 0,79 %, inside 5 %.
- Extrapolation past the 40 km graph is justified by the stated uniform fibre (A = aL); checks 0,5⁷ = 0,0078 and 6,3 % at 40 km right.
- Both solutions symbolic first, units and rounding right.
