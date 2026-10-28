VERDICT: PASS
CONTENT-HASH: eddc57610d8a36e9

## Blocking

## Polish
- exercises.json L3-03 vs solutions.md L3-03 — the task still says "lukemavirhe on enintään $0{,}1$" and asks for the worst case where the errors add. The revised solution says "epävarmuus on noin $0{,}1$ … varovaisesti arvioiden noin $0{,}2$". The arithmetic is the same either way. Say it the same way in both, preferably as the guardrail does: "lukeman epävarmuus noin $0{,}1$; pahimmassa tapauksessa erotuksen epävarmuus $0{,}2$". An uncertainty is not a guaranteed limit.
- solutions.md L3-03 — $\Delta$ stands for differences ($\Delta y$, $\Delta x$) and also for uncertainties ($\Delta y_\text{luku}$, $\Delta k$). Name $\Delta k$ once in words ("kulmakertoimen epävarmuus").
- solutions.md L3-02 Vastaus — "väliltä 10–$20\,\text{min}$" puts only the second number in LaTeX. L3-01 Järkevyys still has "0,47 sekunnissa" in plain text.

## Checked
- The diff since the last pass only converts numbers with units to LaTeX (L1-01, L1-05, L2-02, L2-03, L2-04, L3-01, L3-02) and rewords L3-03 from "virhe enintään" to "epävarmuus … varovaisesti". No answer, unit or tolerance changed.
- One script recomputed every answer from the task text: 1,3 m/s; 27 cm; 10 vrk; −1,5 cm/h; 4,8 g; 2,5 m/s; 23 cm; 0,9 kg; 1,757 → 1,8 (2,4 % off, tolerance 3 %); −0,47 s; 2,0 (the middle slope is −1,2 °C/min); 16 (relative errors 20 % and 1,25 %). All equal answers.py.
- The guardrails for fits are met:
  - extrapolation is named with its assumption (L2-02 beyond 6 min, L3-01 at t < 0);
  - the line through the origin has a stated physical reason (L1-05, direct proportionality);
  - the slopes are taken from points on the fitted line;
  - L3-02 shows that the non-constant slope rules out one line, and the cooling explanation (the temperature difference to the room shrinks) is the right mechanism.
- Physical plausibility: 1,0 kg/l is water's density; an A4 sheet is about 5 g; 9 km/h cycling; 13 h for the candle.
- Every solution has the seven parts, is symbolic first, has correct conversions (kg → g, km → m, min → s) and real reasonableness checks. The signs are explained (L1-04, L3-01).
- Hash identical at start and end.
