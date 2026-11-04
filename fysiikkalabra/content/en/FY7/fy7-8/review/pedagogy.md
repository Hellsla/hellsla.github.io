VERDICT: PASS
CONTENT-HASH: 5da4632bb8b3a2c1

## Blocking

## Polish
- inquiry.json (prior) — lists only induction and the generator; prediction 2 needs P = UI and P = RI² (FY6) — add them (open since round 1).
- exit-ticket.json Q1 — 500:25 turns, 230 V gives 11.5 V, same answer as exercise L1-01 — change the numbers (open since round 1).
- inquiry.json (siirto, mistake 2.4) — "voltage drop in volts divided by a thousand" is hard to read — say "R·I = 2.4 kV; you gave the voltage drop, not the power".
- lesson.md grid figure (capture #9, 390 px) — "local substation" label touches the house roof and "20 kV" sits on the line; move labels.

## Checked
- Round-1 blocker fixed: sim bar label now reads P_arriving (capture fy7-8-sim-390), matching the readout; sim.js:134 uses a lang key.
- No Finnish words visible to students in the sim, lesson, inquiry or figures (P_h is defined in the formula text as the power loss; decimal comma in the sim allowed).
- Learning path, predictions refutable by koe-1, seven-step worked example, find-the-error, transfer task and checks as passed in round 1; no content changed beyond the fix.
- Sim readout and sliders usable at 390 px.
