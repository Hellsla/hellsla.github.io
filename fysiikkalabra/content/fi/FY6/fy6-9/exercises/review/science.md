VERDICT: PASS
CONTENT-HASH: 0fcb8d2cc4f7c3c6

## Blocking

## Polish
- exercises.json:276 (L3-04) — "Kennon lataaminen täyteen vei kummallakin kerralla 11,0 Wh" holds only if each charge started from the same empty state before the discharge; a recharge after the 2,0 A discharge (0,2 Ah left in the cell) would need less. (B, minor) — add "ennen kumpaakin purkausta samasta tyhjästä tilasta".
- solutions.md:191 (L3-05) — "kaksi merkitsevää numeroa kuten jännitteissä": the voltages and their differences (1,90 V, 1,70 V, 1,50 V) have three figures; the limiting datum is R_kok = 0,40 Ω — "kuten resistanssissa 0,40 Ω".
- solutions.md:160 (L2-06) — 1,5 Wh "kuten virrassa ja ajassa", but the difference 4,2 V − 3,7 V = 0,5 V has one decimal (one figure); name the difference as the limit.
- solutions.md:179 / exercises.json (L3-04) — the solution gives 0,7745 = 77,45 %, the answer field 77.5; write 77.45 or round the same way in both (within tolerance).
- docs/exercise-bank/FY6.md:55 — the plan says "virta kulkee akun sisällä −→+" during charging; that is the discharging direction. L1-07 (+ → −) is right; fix the plan line. The plan's CC–CV graph and its error claim were replaced by L2-07 and L2-06: update the plan. L2-06 and L3-03 share 2,0 A / 1,5 h.

## Checked
- All 20 answers recomputed in one script with my own formulas, and answers.py re-run: every pair agrees (< 0,2 %).
- L2-05 trapezoid 9,32 Wh (mean 3,73 V, realistic); L2-06 1,5 Wh, also RI²t with R = 0,25 Ω.
- L2-07: least-squares slope 2,50 A/V → 0,40 Ω; intercept E = 12,39 V, fitting a 12 V lead cell; slope from the fitted line; 5 % tolerance fits.
- L3-04: Q 2,6 / 2,4 Ah, W 9,62 / 8,52 Wh, η 77 % (87 % at 0,50 A), R_s = 0,10 Ω, E = 3,75 V at both currents; condition stated.
- L3-05: stage currents 4,75 / 4,25 / 3,75 A, 7,12 h; exact integral of R dQ/(U_lat − E) gives 7,13 h, so the stage model is good; bounds 6,0 h and 8,6 h right.
- L1-06, L1-07: exactly one correct option, every distractor wrong and its feedback right; L1-07 matches the lesson's + → − charging direction.
- Levels fit (L1 one formula, L2 data/error/graph, L3 multi-step YO style); no duplicate of an existing task; notation as in the brief.
- "FAIL layout 360 px": check_layout.py shows it is preview/en/fy6-9 (inline 0{.}4\,\Omega), not this Finnish exercise set; fi passes.
