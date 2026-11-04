VERDICT: FAIL
CONTENT-HASH: 76206f426c2e0dce

## Blocking
- solutions.md L3-04 Sijoitus and Vastaus — component C is worked only at 1,5, 2,0 and 3,0 V; the row U = 1,0 V, I = 0,1 mA (nonzero, R = 10 kΩ) is skipped, and the answer says C's resistance falls "600 Ω:sta 31 Ω:iin" although the task asks for all voltages where the current is not zero — add "1,0 V : 0,1 mA = 10 kΩ" to C's list and write "pienenee 10 kΩ:sta 31 Ω:iin" (the 600 Ω stays the c) answer).

## Polish
- exercises.json L2-06 (also L2-02, L3-03, L3-04 B) — four tasks revolve around the filament lamp's rising R; L2-06 repeats L2-02 (read R of the bulb from the characteristic) with a table — keep, but vary the lamp's context (a car bulb, a bike light) so the set does not read as one task four times.
- exercises.json L2-05 a) — "piirrä ... sovitussuora" has no figure or drawing answer, and the solution reads the line at 50,0 mA from a graph the student never sees — add one sentence to the solution saying the line is drawn on paper/with a tool and the check value (U = 7,5 V at I = 50 mA) is what the student compares with.
- exercises.json L1-08 — second wire-length task after L1-07 (same idea, now numbers); fine as level 1, but the solution could end with "R ∝ l" as the rule so it is not just a one-off result.
- exercises.json L3-04 a) — "diodi (LED)" is in the text although diodes are met only in a later chapter; the resistance-by-elimination route (A constant, B rising like the lamp, C the rest) works, but add one hint line to the solution: "diodin resistanssi pienenee, kun virta lähtee kasvamaan".
- exercises.json L2-07 b) — averaging four R values is a weaker method than L2-05's slope; fine for an error-analysis task, state in the solution that the slope gives the same 4,9 Ω.

## Checked
- Counts 8/7/5 and kinds match docs/exercise-bank/FY6.md (characteristic MC, rho vs R MC, wire length, 8-point table, lamp table, "0 V → 0 Ω" error, three components, temperature experiment).
- Recomputed: L1-08 0,30 A; L2-05 R ≈ 150 Ω, ΔR 1,7 Ω; L2-06 ratio 1,98; L2-07 4,93 Ω; L3-04 600 Ω and 23×; L3-05 38,1 %. All match answer fields.
- L1-06 and L1-07: one correct choice, distractors are real misconceptions, feedback repairs them.
- L2-07 correctly names 0 : 0 as undefined, not zero, and tests that R is constant.
- L3-05 asks for variables, set-up and two error sources with fixes (YO-style experiment design); model answer is complete.
- No new task repeats the lesson's worked example; level 3 combines data, model and reasoning.
- Finnish and case after number+unit correct; the "kulmakerroin = R" convention matches I on the x axis.
- 1280 px captures readable; no 360 px exercise captures listed (the 4-column table of L3-04 should be confirmed on a phone).
