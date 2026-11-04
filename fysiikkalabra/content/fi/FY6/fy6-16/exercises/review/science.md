VERDICT: PASS
CONTENT-HASH: 81bbe5b3454f7162
Round 2: full review of the exercise set after the round-1 fixes (commit f8abf016e, diff from d0ea57642).

## Blocking
(none)

## Polish
- solutions.md:155 (L2-05 Vastaus) — 10,45 kW is an upper limit, and rounding it up to 10,5 kW gives a power the main fuse no longer allows (10,5 kW → 25,1 A). Write "enintään noin $10{,}4\,\text{kW}$ (tarkasti $10{,}45\,\text{kW}$); ylärajaa ei pyöristetä ylöspäin".
- docs/exercise-bank/FY6.md (fy6-16), carried from round 1 — the price comparison at different times (Taso 2) and the emission comparison (Taso 3; L3-04 has costs only) are not covered. The Taso 1 calculations (charging time; P = 3UI) are also replaced by L1-07 (W = Pt) and L1-08 (RI²). Update the plan, or add the parts.
- exercises.json:74, :82 (L1-07, L1-08) — no `kind` field; the other new tasks have one. Add `"kind": ["reasoning"]` or what applies.

## Checked
- Hash 81bbe5b3454f7162 at start and end.
- Round-1 Blocking resolved: L2-05 now states "Oletetaan, että talon teho pysyy kunkin tunnin ajan taulukon arvossa", and c) says the conclusion holds under that assumption and that peaks within an hour may still need load management.
- Round-1 Polish fixed: L2-07 a) and b) are limited to the measured period 0–3,0 h; L2-05 Kysytty includes c); the L1-06 feedback gives 60 kWh : 11 kW ≈ 5,5 h without losses; the L3-04 rounding reason is the 2-digit electricity cost (390 €).
- One script recomputed every new answer: L1-07 40,7 kWh; L1-08 64 W; L2-05 10,45 kW (limit 6,25 kW for 11 kW, only 19–20 exceeds it); L2-06 5,29 h; L2-07 22,85 kWh, 7,62 kW; L3-04 14 640 km, 390,4 €, 1760,5 €, 1370,1 €, public 1171,2 €; L3-05 7,61 A, 0,408 Ω, 23,6 W and 104 W. All agree.
- L1-06: exactly one correct option, `answer` equals its text.
- Levels 8/7/5, scope, units and tolerances fit.
