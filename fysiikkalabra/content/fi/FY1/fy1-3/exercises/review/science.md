VERDICT: PASS
CONTENT-HASH: 1a41d04fd9a53a26

Full review, round 2. Only L2-08 changed since round 1; I recomputed every answer again.

## Blocking

## Polish
- solutions.md:140 (L1-08) — Carried over: "joten työntömitta on tarkempi väline" infers accuracy from resolution alone. — Limit the claim to reading uncertainty.
- solutions.md:163 (L2-06) — Carried over: "eli siinä on systemaattinen virhe" should say *todennäköisesti*, as line 164 does.

## Checked
- Round-1 Blocking is fixed (exercises.json:307, solutions.md:201). Option 4 now says "kymmenen heilahduksen aika 14,300 s". The Mallivastaus gives 14,3 s ± 0,2 s for ten swings and the period as about 1,43 s ± 0,02 s; 0,2/10 = 0,02 s is right.
- The round-1 Polish items in L2-08 are done. The uncertainty is now "käsin otetun ajan epävarmuus Δt = 0,2 s", the stem marks 14,30 s and 14,36 s as calculator means of ten swings, the text says "kuulan massan", and the typo is fixed.
- The added remark in option 4's feedback (unrounded means are kept for the comparison, the result is rounded for reporting) is right and removes the inconsistency.
- L2-08 still has exactly one correct option. The difference 0,06 s and the half-ranges 0,20 s and 0,15 s are right, and "cannot be shown, not proof of equality" follows the guardrail.
- All 19 numeric answers were recomputed with my own formulas and agree with exercises.json and answers.py within tolerance.
- The hash was the same at the start and the end.
