VERDICT: PASS
CONTENT-HASH: f73c1faf99b28bab

Round 2 (delta review of round 1 fixes; round 1 hash 5d2b5d87bf295a65). Science review of fy9-tasavirta, 2026-11-04.

## Round 1 Blocking, verified
1. **B1 s5 a Vastaus** (`sovella/solutions.md`): now "eli mittarien virherajojen mukaan todellinen arvo on todennäköisesti
   välillä noin 88–106 Ω". Fixed in the source and in the built preview (390 and 1280).

## Round 1 Polish, verified
- P1 Tutki Järkevyys: "noin 22 %". Recomputed: R/l·A at 0,20 m = 0,611 µΩ·m against the fit slope 0,500 µΩ·m
  (fit k = 7,07 Ω/m, b = 0,302 Ω), ratio 1,22. Correct.
- P2 s3 d: "hieman mittausalueen yläpuolella …" in solutions.md and the tasks.json criterion. Recomputed I = 4,625/(3,6+0,733)
  = 1,07 A (largest measured 1,00 A), P = 4,10 W, internal 0,84 W, share 83 %. Correct.
- P3 unit.md: "missä U on nimellisjännite" present.
- P4 s2 d Periaate: the clause on the average source voltage 36 V is present and consistent with the alternative η = 36 V : 42 V.
- P5 keitin: "kodin suuritehoisimpia laitteita mutta ei suurimpia energian kuluttajia". Correct.
- P6 s5 b: "Metallin ja hiilikalvon resistanssi muuttuu lähinnä lämpötilan mukana". Correct.

## New problems introduced by the fixes
None. The rewritten source notes (Tutki, s3) contain no physics claims that conflict with the data. No other numbers
changed; the s3 answers, tolerances and practice.py check (6 tasks, 95 p) are unchanged.

## Edits made by this reviewer (round 2)
- `inquiry.json` Tutki source_note: "Arvot on keksitty, ja niihin on lisätty mittausten kaltaista vaihtelua." (the
  previous wording named the lead resistance, which is the answer to the intercept question).
- `lessons/units/fy9-tasavirta/sovella/figures.py` ik_graph: the I_k label moved above-right of the point, because its
  background box hid the last part of the dashed extrapolation line; figures regenerated with practice.py figures.
- `sovella/tasks.json` source notes: "ovat keksitty esimerkki" → "on keksitty" (grammar).

## Remaining Polish
None from the science side.
