VERDICT: PASS
CONTENT-HASH: daa6fc4f95361ced
Mode: delta
Round: 2

## Blocking
- none

## Polish
- (none)

## Checked
- delta review 2026-11-07 round 2 (follow-up consistency edits): L1-08: shortened correct option (extending the line beyond the measured range, assuming the linear dependence holds there) is correct; option lengths now 95–105 characters (fi), comparable, all four of the same 'X, because Y' form, so no length giveaway; answer equals the option text; the teacher's full definition opens the feedback and agrees with the rest of it. Exactly one correct option. Hashes equal at start and end.
- delta review 2026-11-07 (teacher's proofread replacement texts): L1-08 correct option, answer key, feedback and model answer now define extrapolation as extending the fitted line beyond the measurement range assuming the linear p(θ) dependence holds there, result a model-based estimate, not measured: correct, exactly one correct option, distractors unchanged and still wrong. English text carries the same meaning as fi.
- Scripted comparison of fy3-13-L2-08 against fi: text, table cells, answer, kind, four choices, correct flag and order identical; every number (13.5, 0.8, 1.0 kPa, intervals 101.0-103.0, 101.8-103.8, 114.5-116.5, 62 kPa, -100 degC, 120 degC) equals fi; English decimal point throughout.
- Recomputed: 115.5-102.0 = 13.5 kPa (>10 x 1.0); 0.8 < 1.0 so intervals overlap; fitted slope ~0.34 kPa/degC gives ~62 kPa at -100 degC. Correct choice is the only valid conclusion.
- Physics: "cannot show" is not "no difference"; extrapolation is an estimate under a linearity assumption; sealed rigid bottle justifies rising p. Same as fi.
- check_i18n.py: nothing for fy3-13; build.py fy3-13 succeeds (see report).
- Caption shortened to fit 390 px: still describes the data (air pressure, sealed bottle); no physics change.
