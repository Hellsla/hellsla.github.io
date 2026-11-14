VERDICT: PASS
CONTENT-HASH: a26ea5aec23e5d8e
SCOPE: delta added-exercise from 17151a3c70a4f503 base 8f23aa7ae3bd

## Blocking

## Polish
- exercises.json:258 (L2-09) — the line-count ratio equals the flux ratio only at the same transmitter current; the task fixes the frequency but not the current — add "lähetinkäämin virta pysyy samana".

## Checked
- Delta: L2-09 and L2-10 added; hash identical at start and end.
- charger-points: lines at flux steps ref/6,5 with the coaxial-loop flux; 6 lines cross the receiver at 3 mm and 4 at 6 mm (model ratio 0,669), so e₀' = 4,2 V · 4/6 = 2,8 V = answers.py (model 2,81 V). e₀ = N·2πf·Φ₀ ∝ Φ₀ at fixed N, f right.
- graph-curve is 0,30 dB/km: half power at 10,03 km (read 10 km); a = 10 dB · lg 2 / 10 km = 0,301 dB/km, 35 km → 10,5 dB → 8,84 % = answers.py (exact curve 8,91 %, inside 5 %); check 0,5^3,5 = 0,088 right.
- Uniform fibre stated, so A = aL holds; solutions symbolic first.
