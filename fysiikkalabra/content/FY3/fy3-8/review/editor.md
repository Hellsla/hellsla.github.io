VERDICT: PASS
CONTENT-HASH: c897f9d2fa70c9d9

The lesson now delivers its goals. The micro model explains solids in detail. lesson.md:12 gives particle-level reasons for liquids and for gases at constant pressure, and it leaves the gas laws to fy3-9. The lesson tells one story. The worked example answers the bridge-joint question. The sim shows the lattice and the rod with ΔL = αL₀ΔT. The exercises rise from one formula to holes, bimetals and a canister. The exit ticket checks the formula, the hole and the micro model. The length is right: 932 words against 651–1194 in the FY3 siblings. The gold lesson is a stub. Only polish remains. Gases are explained but never practised, and the misconception section repeats earlier text.

## Blocking
(none)

## Polish
- lesson.md:40 — The row "ilma (vakiopaineessa) 3,4" is used nowhere, so gases have no task. — Fix: compare air with water or petrol (γ ratio ≈ 16) in an exit-ticket question or in L3-03, or drop the row.
- lesson.md:12 — In "lähes vapaita, joten … kasvaa paljon enemmän", the "joten" skips a step. — Fix: add that no attraction holds gas particles together, only the surrounding pressure, so faster particles push the boundary outward.
- lesson.md:70 — The three misconceptions are already stated as facts at lines 6, 10 and 12. — Fix: shorten those statements, or let this section give the reason instead.

## Checked
- Lint: 0 errors and 0 warnings. `check_layout.py`: OK at 360 px.
- The goals in meta.json match curriculum.json, and all three states of matter get a micro model.
- lesson.md:21 "Nesteiden (ja vakiopaineessa kaasujen)" matches line 12.
- `answers.py` matches every answer. L1-03 asks for ΔL, and L1-05 gives α = 9,0 · 10⁻⁶.
- The levels have 5/4/3 tasks, and none repeats the bridge example.
- Every level-3 task asks for a reason.
- Exit-ticket q3 tests the micro model, and q2 tests the hole misconception.
- The sim spec matches the lesson table and formula: 20 °C reference, five materials, readouts.
- Each formula is shown in display form once, with its symbols named. γ ≈ 3α is justified and used in L2-02 and L3-03.
- Scope holds: no vectors and no gas-law formula.
