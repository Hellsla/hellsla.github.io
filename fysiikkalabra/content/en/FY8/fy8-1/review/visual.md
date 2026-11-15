VERDICT: FAIL
CONTENT-HASH: e96f36a65e8ac7e1

## Blocking
- [Major] solutions, inquiry feedback, lesson text (about 25 display blocks cut out of running sentences) — a lifted formula is set as `$$...$$` in the middle of a sentence, so the punctuation or connective that followed it ("$$, so", "$$. The…", "and $$") lands as an orphan fragment (", so", "so", "and") on a line of its own in a separate box; seen in fy8-1 open-exercises-L2-1280-5 (", so" / "so" between the Substitution blocks). Many are also one-row `aligned` blocks of a short formula (e.g. a single `1240 eV nm : 2.30 eV ≈ 539 nm`) that never needed lifting. — the sentence reads as broken fragments and the Substitution/Reasonableness blocks lose their flow — keep short and single-row formulas inline; lift only chains that really clip at 360 px and make the whole step one display (the connective text inside `\text{}` or in a following line with no leading punctuation), or move the trailing words ("so …", ". The …") into the same display or the next sentence.

## Polish
- [Minor] Row wrapping: "hc = 6.626·10^-34 J s / · 2.998·10^8 m/s = 1.9865…" is merged by the build into two rows, fine, but the manual three-row source is redundant; leave the chain to mathlayout.

## Checked
- Source diff of commit 27b591e3f5 for this lesson; open-exercises captures of fy8-1 (1280) for the rendering of the lifted blocks; the pattern is the same source construct in all lessons of this batch. Figures unchanged by the diff, not re-judged.

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 4
