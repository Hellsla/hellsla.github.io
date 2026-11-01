VERDICT: PASS
CONTENT-HASH: fe3577a0c0da4706

Pedagogy re-review of fy14-secret-fusion (2026-11-01), after the "Fixes after review" in commit 3ed55db3. I rebuilt the page and tested it in Playwright at 390 px. Both predictions lock when the student commits and show no feedback. `pred-secret` opens at `theory-war` and `pred-zeta` at `theory-zeta`. Model answers stay closed until the student writes. No console errors, raw `$` or katex errors.

## Earlier findings: all resolved
1. `zeta-data` (70/30, then 30/70 after the current is reversed) comes before `theory-zeta`. The student now reads the evidence before the prediction opens. The distractors (equal shares, stopping, heating) each get feedback that repairs the misconception, and the note marks the numbers as simplified.
2. `pred-secret` now names both reasons: "too close to hydrogen-bomb physics and fuel".
3. The sorting item is now a real motive: governments feared.
4. `teacher.md` makes `check-write` homework and gives the ZETA data its own time.
5. The option lengths are re-balanced.

## Blocking
None.

## Polish
1. `teacher.md`, Investigate. With `zeta-data` added, 12–40 min is full. Name the order task as the first thing to skip if time is short.

## Shared issues
- `scripts/inquiry.py` still renders the `pair` note after the textarea, inside a `<p class="task">` (invalid nesting).
- There are no photographs yet (the photo pass).
