VERDICT: PASS
CONTENT-HASH: d7eef146fb89c633
Round 2: delta against the version round 1 reviewed (whitespace-only fixes in s7).

## Blocking
- (none)

## Polish
- B `sovella/solutions.md` s7 b, Formula: the layout lifts "$s_\text{c} = (1 - 0.38)\,s$ and $E_{100,\text{c}} = \ldots$" into one box and drops the "and", so "In frost the distance is" is followed by two rows of which only the first is a distance. Two sentences would read cleaner.
- C `sovella/tasks.json` s7 a and solutions: "tell what the comparison shows", "A relative difference tells how large a part" → "say what the comparison shows", "shows how large a part".
- C s7 solutions c, thermal physics: "Keeping the temperature takes heating power" → "Keeping the cabin warm takes heating power".
- C s7 c, the first bullet (Thermal physics) is about 100 words and runs 21 lines at 390 px; acceptable, could be split at "In a combustion-engine car".

## Checked
- Hash at start and end: d7eef146fb89c633 (captures re-made for this hash). `git diff -w c502cb9e26`: only the two blank lines in solutions.md and the s7 d sentence round 1 already saw.
- s7 c Model answer at 390 px: `stage-exercises-390-56`, `-57`: a lead paragraph, three real bullets (Thermal physics, Electricity, Mechanics) with hanging indent and a gap between items, then the closing paragraph; no raw "- " marker; inline formulas ($P = R_\text{s}I^2$, $\tfrac{n}{V} = \tfrac{p}{RT}$) whole, nothing clipped.
- s7 e Model answer at 390 px: `stage-exercises-390-59`: three bullets and the closing paragraph, Common mistakes list below intact.
- s7 at 1280 px: `stage-exercises-1280-40`, `-41`, `-42` (c, d, e solutions, Common mistakes, Also accepted), `-43`, `-44` (rubric): lists rendered as lists, cards and spacing unchanged, reading column kept.
- Contact sheet `contact-7` (#73–#84): the task card, table, parts a–e and the rest of the solution as in round 1; nothing else moved.
