VERDICT: PASS
CONTENT-HASH: 5a7036e668845eab

Round 2 (exercise bank): round-1 Blocking item and the fix diff (HEAD~2..HEAD~1) re-checked; new tasks re-read in full.

## Blocking

## Polish
- exercises.json:188 (fy3-3-L2-06) — carried from round 1: 80,0 → 48,6 °C in 4 h (≈10 K/h at first) is a very poor thermos; values like 90 → 75 °C over 4 h would be more realistic (the ≈0,17 per-hour fraction would then be ≈0,05). Physics and answer correct as they stand.
- solutions.md:235 (L3-05) — "kolme merkitsevää numeroa kuten ilmanpaineessa 101 kPa": the limiting datum is really the overpressures 600/900 kPa (taken as three numbers); naming them would be more honest. Result 145 °C unaffected.

## Checked
- Round-1 Blocking resolved: solutions.md:212 (L3-04) now "Toistaminen pienentää keskiarvon satunnaista virhettä mutta ei poista systemaattista virhettä" (guardrail "Measurement and data").
- Round-1 Polish resolved: L3-05 shows T3 = 418,61 K, θ3 = 145,46 °C before rounding to 145 °C; "ylipaine" defined in the task (kokonaispaine − ilmanpaine) and the task now says total pressure ∝ T; plan in docs/exercise-bank/FY3.md updated (L3 "lämpötila ei ole lämmön määrä" moved to fy3-5, varoventtiili listed).
- One script recomputed the changed numbers: L3-05 p2 796,65 kPa, ylipaine 695,65 kPa, θ3 145,46 °C, ΔEk/Ek 13,64 %; L2-06 ratio 1,741, per-hour fractions 0,168/0,172/0,167/0,169 (solution's "≈0,17", with last-hour ΔT 34,4 K, right); L2-07 gaps 12,0/3,6/0,9/0,3 K; L3-04 sums and half ranges unchanged and right.
- answers.py output matches exercises.json for every new task (255, 1,5, 1,7, 40, 0,6, 145).
- L1-06 and L1-08: options only reordered; still exactly one correct option, feedback unchanged and right.
- Added definitions in L2-05 b) and L3-04 c) (systematic = same direction every time, random = both directions) are correct and consistent with the solutions.
- L2-06 hint (drop divided by the hour's starting temperature difference) matches the solution's reasoning.
- Aligned Sijoitus blocks: every line recomputed, no change of value.
- No Newton's laws or other FY4 content; notation T = θ + 273,15 as in the brief.
