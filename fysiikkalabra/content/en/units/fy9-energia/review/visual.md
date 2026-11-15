VERDICT: PASS
CONTENT-HASH: 99322ddd2a419363
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- B `sovella/solutions.md` s7 b, Formula: the layout lifts "$s_\text{c} = (1 - 0.38)\,s$ and $E_{100,\text{c}} = \ldots$" into one box and drops the "and" and the full stop, so the text reads "In frost the distance is" followed by two rows of which only the first is a distance. Writing "In frost the distance is $s_\text{c} = (1 - 0.38)\,s$, so $E_{100,\text{c}} = \ldots$" as two sentences would read cleaner.
- C `sovella/tasks.json` s7 a and solutions: "tell what the comparison shows", "A relative difference tells how large a part" read as translated Finnish; "say what the comparison shows", "shows how large a part" are more natural.
- C s7 solutions c, thermal physics: "Keeping the temperature takes heating power" → "Keeping the cabin warm takes heating power".

## Checked
- Hash at start and end: 99322ddd2a419363 (captures re-made for this hash).
- Every hunk of the diff read: P1 wording (internal energy, transferred to the surroundings as heat) is carried out correctly and reads well in unit.md, inquiry.json, s1, s4, s6 and the `ketju` aria-label.
- Derive it yourself box: `stage-selita-390-3`, `stage-selita-390-4`: the three rows $P_1$, $P_2$, $P_3$ are aligned on `=`, nothing clipped.
- ADDED TASK s7 at 390 px: contact-7 (#73–#84) and `stage-exercises-390-49`, `-50`, `-54`, `-55`: title, visible source link, results-page link, table (three columns fit), parts a–e, all opened solutions, common mistakes, also accepted, rubric. Aligned rows keep `=` in one column; no clipped or scrolled formula; no orphaned punctuation.
- s7 at 1280 px: contact-13 (#145–#156) and `stage-exercises-1280-36`, `-39`: card, table and solution rows intact.
- Every number with a unit in the added text is LaTeX; decimal point throughout.

## Scores
illustrations 4 · typography 4 · language 4 · accessibility 4
