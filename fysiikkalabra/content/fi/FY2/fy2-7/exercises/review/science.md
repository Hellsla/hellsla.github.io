VERDICT: PASS
CONTENT-HASH: 72f39e958439a660

Round 2 (round 1: FAIL, 2 Blocking).

## Blocking

## Polish
- solutions.md L3-05 Sijoitus (aligned block) — the losses are named $H_1 … H_4$, a symbol the lesson does not use. Write $E_{\text{häviö},1}$ … or say once "$H_i$ = jakson häviöenergia".
- solutions.md L3-05 Vastaus — "häviö kasvaa virtaa nopeammin, joten osuus kasvaa" holds at a roughly constant line voltage. Add "kun jännite pysyy samana" (C as it stands, so not blocking).
- exercises.json L2-07 — the distractor "Sähkö kulkee johdossa hitaasti…" is half true, because electrons drift slowly (it is the energy that travels fast). The feedback rightly rejects the reasoning. Optional: say "energia siirtyy nopeasti" in the correct option and the model answer.

## Checked
- Round-1 Blocking 1 (L3-05 c, causality): resolved. The model answer now says that the loss grows faster than the current, so it grows faster than the input. The task text gives the hint "kaksinkertainen virta → nelinkertainen häviöteho", so c) is fair.
- Round-1 Blocking 2 (L2-05 b): resolved. The explanation now quotes the data, 75 → 49 MWh against 820 → 430 MWh, which is true (the shares are 9,15/8,95/9,84/11,4 %).
- Round-1 Polish, all done: L2-05 now has 9,62 % with three significant figures, properly justified; L2-06 states the same line and the same 100 MW, and its added "virta puolittuu" is right at constant power; the L3-05 data now follow loss ∝ I² (share/P = 0,00083 for every period); the plan records why the omitted items were left out.
- Recomputed L3-05 independently: E = 1016 MWh, loss 42,09 MWh, p = 4,14 % → 4,1 %; the evening share is 43 %; the plain mean is 3,7 %; the answer key is 4,1 (within tolerance).
- Recomputed all new answers in one script (L1-07 4,8; L1-08 72; L2-05 9,62; L2-06 0,0625; L3-04 6,59; L3-05 4,14). All agree with answers.py and exercises.json.
- L1-06: reordering the choices left exactly one correct option, and every feedback is unchanged and right. L2-07: exactly one correct option after the rewording, and every distractor is wrong.
- Scope: still no P = RI² law, only the data-derived factor 4 given as a hint (C). Nothing from FY3.
- The hash was unchanged at the start and at the end.
