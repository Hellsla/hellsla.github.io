VERDICT: PASS
CONTENT-HASH: 1b08d793dcc1fb99

## Blocking

## Polish
- content/fi/FY1/fy1-8/exercises/exercises.json:153 — feedback of statement 2 says "Jos kulma muuttuu massan mukana", but the statement only says the angle varies between runs — "Jos kulma vaihtelee, ei tiedetä, johtuuko ajan muutos massasta vai kulmasta."

## Checked
- New task L1-09 (Väitteet tosi/epätosi): truth values 1 T, 2 F, 3 F, 4 T, 5 F correct; at least one true and one false; `answer` string matches the statements.
- Statement 3 feedback keeps resolution (0,01 s) apart from hand-timing uncertainty (about 0,2 s), as the guardrails require.
- Statement 4 and its feedback say a difference below the uncertainty cannot be shown and that this does not prove no effect (guardrail wording on overlapping intervals).
- Statement 5 matches the lesson's "Yleinen virhekäsitys" (a refuted hypothesis is a result).
- Solution L1-09 complete (Kysytty, Periaate, Mallivastaus) and agrees with every feedback.
- All 17 numeric answers recomputed in one script; all within tolerance (L2-07 least squares 0,2995 m/s; L3-04 3,75; L3-05 10 min).
- Half-range called a simple estimate of scatter, never the uncertainty of the mean; terms consistent with the lesson.
- Scope: FY1 (s = vt, ε = Δt/t, planning a fair experiment); no later-course physics.
- Content hash identical at start and end.
