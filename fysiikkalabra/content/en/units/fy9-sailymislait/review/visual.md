VERDICT: PASS
CONTENT-HASH: ae4685c645f11ec8
SCOPE: delta: s7 and s8 Järkevyys/Reasonableness weight calculations changed from inline to aligned display chains (CI 360 px fix), language en; everything else stands under the previous PASS.

## Blocking
- (none)

## Polish
- Earlier Polish stands (recorded in the previous report, unchanged by this delta).
- Optional: the chain is two rows (G = mg, then m · g with numbers and units) with the result on the second; reads fine.

## Checked
- s7 (G = 2,0 kg · 9,81 m/s² = 19,6 N) and s8 (G = 0,43 kg · 9,81 m/s² = 4,2 N): numbers, symbol G, units and decimal form per language (en) identical in meaning to the old inline text; arithmetic correct (19,62; 4,218).
- Sentences continue after the display block with ", so/joten" as in the existing s3 c) and s5 pattern; no sentence broken awkwardly, rows start with the quantity, units upright with thin space.
- Diff of commit 57e959f176 for this unit touches only these two paragraphs per language; nothing new appears.
- Hash at start and end same (ae4685c645f11ec8).
