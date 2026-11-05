VERDICT: PASS
CONTENT-HASH: 6a5961577f7f1398
Round 2: full review of the exercise set after the round-1 fixes (commit f8abf016e, diff from d0ea57642). Round 1 had no Blocking items; four of its five Polish items are fixed.

## Blocking
(none)

## Polish
- docs/exercise-bank/FY6.md (fy6-15 Taso 1), carried from round 1 — the plan's third L1 item (largest power on a fuse) is existing L1-02, so L1-08 (U = E_max d) was added instead, and it is the mirror image of L2-03. Update the plan line, or give L1-08 a context other than an air gap.
- solutions.md:54 (L1-06 Mallivastaus) — it still quotes the old option wording "ohjaa vikavirran johdinta pitkin maahan"; the option now reads "ohjaa vikavirran maahan". Make the quote match the option.
- exercises.json:104 (L1-08) — the task has no `kind` field; every other new task has one. Add `"kind": ["reasoning"]` or the kind that applies.

## Checked
- Hash 6a5961577f7f1398 at start and end.
- Round-1 Polish fixed: L2-07 Vastaus now uses the lesson's wording (the fuse protects people only with protective earthing; the RCD cuts the current through the body); L3-05 b) lists weeks 3, 5 and 7; L2-05 Järkevyys says "yli kuusikymmenkertaiseksi" (ratio 61); L3-04 gives the physical reason for the origin line and explains the first point's deviation.
- L1-06 and L1-07 after the reorder: exactly one correct option each, `answer` equals its text, distractor feedback unchanged and right.
- One script recomputed every new answer: L1-08 6,0 kV; L2-05 61,1; L2-06 9,57 A (1400 + 800 W; the five pairs above 2300 W); L2-07 115 mA; L3-04 k = 0,297 K/W, 20,5 A, ΔT 30 K at 16 A and 74 K at 25 A; L3-05 6,17 kΩ, currents 0,26/1,9/5,5/17,0/41,8 mA. All agree.
- Thresholds of IEC 60479-1 type, RCD 30 mA, series model R_e + R_k: correct and inside FY6 safety content.
- Levels 8/7/5, units and tolerances fit.
