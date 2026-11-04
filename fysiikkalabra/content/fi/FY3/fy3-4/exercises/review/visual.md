VERDICT: PASS
CONTENT-HASH: 931d64b231b7ad76
ROUND: 2

## Blocking
(none) Round 1 Blocking resolved: L3-04 Järkevyys now reads "vesipatsaan ylintä 15 m:ä ... välikerroksessa vain 0,03 % ... laskettu ero noin 0,06 %", which matches the layer table (5,0 + 10,0 m of 20,0 m; 118 Pa / 196 200 Pa = 0,06 %).

## Polish
- [Minor] Data tables (L2-05, L2-06, L2-07, L3-05) — header centred/left, numbers right-aligned or offset; align them the same (site-wide table style, not task content).
- [Minor] L3-04 Vastaus — the "Kaksi merkitsevää numeroa kuten tiheyserossa 1000 − 998,2 = 1,8 kg/m^3" chain breaks after the minus at the line end; harmless at 1280 px.
- [Minor] L3-05 Sijoitus c) — the chain 122,6 + 367,9 + 613,1 + 858,4 = 1962 kN has no units on the terms; add kN.
- [Minor] Answer-field wording: "Vastauskenttään" (fy3-4) vs "Vastauslaatikkoon" in fy3-5..7; pick one site-wide.

## Checked
- 1280 px: open-exercises-1280-6 (L1-06, correct option now second, reworded), -8 (L1-08, Finnish quotes ”…” now used), L2-1280-5..10 (L2-05 table, label "Taulukon lukeminen"), L3-1280-5, -6 (L3-04 solution, new Järkevyys), L3-05 start. Captures are newer than the fixed content. No red KaTeX, no overflow, cards contain open solutions.
- Diff HEAD~1 read: only wording, option order, kind tag (L2-05 "graph" removed: a table) and labels changed. No 360/390 open-state capture of the exercises; relied on the passed layout 360 px check.
- No plain-text quantity in the changed text.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
