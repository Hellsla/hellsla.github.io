VERDICT: PASS
CONTENT-HASH: c8939c0291044cc2

Round 2: L1-03 tolerance 0,02 → 0,15 and the Vastaus line reworded; the round-1 blocking item is fixed.

## Blocking
(none)
## Polish
- exercises.json:26 — tolerance 0,15 accepts 0,2975…0,4025 s, so 0,30 s (a one-figure round-down, or a misread minimum 12,3 s) also passes; harmless, but 0,12 (0,308…0,392) would not.
## Checked
- (12,9 − 12,2)/2 = 0,35 s; 0,35 · 0,85 = 0,2975 and 0,35 · 1,15 = 0,4025, so both 0,35 and 0,4 pass; the full range 0,7 s is rejected.
- New Vastaus: 0,35 s is the exact half-range, reported uncertainty one figure → 0,4 s, both accepted; agrees with the tolerance and NOTES §2.
- Rest of the solution (figure reading, midpoint 12,55 ± 0,35) unchanged and still right.
