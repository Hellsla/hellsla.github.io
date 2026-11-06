VERDICT: PASS
CONTENT-HASH: 7285f36aa764b4e1
Mode: delta, round 2 (supersedes round 1)

## Blocking
(none)
Round 1 reported the L2-07 and (en) L2-05 chains as clipped Major, measured before the page's flFitMath step had run. Re-measured with it running: page scrollWidth 390 in both languages, no element outside the viewport except inside the designed sideways-scrolling `.kx-wide` / `.eq-chain` lines. These are old, untouched tasks with formulas identical to the passed Finnish, so they are Polish, not blocking for the new-task review.

## Polish
- [Minor] fy4-10-L2-07 task — the student's chain (330 px, `.kx-wide`) scrolls sideways inside its own line, so its tail `= 0.70 m/s` is only seen by scrolling; the same in the passed Finnish. Follow-up for a shared fit/mathlayout rule (wrap a fraction chain), not this PR.
- [Minor] fy4-10-L2-02 solution — chain about 364 px scrolls in `.eq-chain`; CI KaTeX about 20 px wider.

## Checked
- Re-rendered at 390 px with every hint, feedback and solution open, flFitMath present: scrollWidth 390; opened fy4-10-L2-07 and L2-05 (en) captures.
- fy4-10-L2-08 (new): task, five options with feedback and solution open in both languages; no overflow, units upright, `\cdot` used, clear order principle, formula, substitution, result, check.

## Scores
illustrations 4 · typography 4 · Finnish 5 · accessibility 4
