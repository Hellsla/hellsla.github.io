VERDICT: PASS
CONTENT-HASH: 40bfc5cc82bd45c1

## Blocking

## Polish
- content/en/FY7/fy7-3/inquiry.json:136,137,191,192 — the experiments' `names` for I and N are still Finnish ("virta", "kierroksia"); the page shows "Kept constant: virta, kierroksia" (shot exp-koe-1-390-2) — translate to "current", "number of turns" (language, not physics).

## Checked
- Every number in lesson.md, inquiry.json, exit-ticket.json, exercises.json and solutions.md compared with the passed Finnish version: the multiset of numbers is identical in all five files (decimal comma → point only).
- Recomputed in one script: theory figure 200/100/50 µT; worked example 12.57 mT, ratio 251; error item 5.0e-5 T vs 5.03 mT; transfer 0.265 A and its mistakes 26.5 A, 3.33 A; check 2 1.5 mT, mistakes 0.015 and 9.42 mT; exit ticket unchanged.
- Sim model (finite coil on axis, R = 2.0 cm): load 1.232 vs long 1.257 mT; koe 1 4.67/2.46/1.66/1.25 mT; koe 2 2.46, 2.41 (5 cm), 1.25 (end), 0.363 (2 cm outside) mT — all as stated in predictions, feedback and model answer.
- Interpret: least-squares slope 2.465 mT/A, B0 0.035 mT, ΔA 0.0121; μ0 = 1.233·10⁻⁶; relative uncertainty 0.49 % + 1.25 % = 1.74 %; finite-coil factor 0.983 → 1.254·10⁻⁶; table value outside 1.21–1.25 correctly attributed to the systematic short-coil effect.
- Directions: right-hand rule (current up → anticlockwise from above), coil figure (upper row ⊙, lower ⊗ → field right, N right), sim "front strands down" → N right, exit ticket 2 (anticlockwise → north pole facing) all correct.
- Conditions stated where used: wire much longer than r, other wires far; long coil, centre, air inside; ends ≈ half; iron core strengthens.
- Electromagnet mechanism (domains aligned by the coil field, soft iron returns almost to disorder) faithful and correct; no para-/diamagnetism or self-induction.
- Assessment: one correct option in each choice item; every distractor's feedback names the actual error.
- Measurement data marked as example (`source: example`), sim numbers called model values.
