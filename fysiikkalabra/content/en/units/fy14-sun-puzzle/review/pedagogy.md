VERDICT: PASS
CONTENT-HASH: 48a48bf08ce39cb6

Pedagogy re-review of fy14-sun-puzzle (2026-11-01), after the "Fixes after review" in review/developer.md (commit 7843fefa). I rebuilt the page and tested it in Playwright at 390 px. `check_layout.py --width 360` is all OK. There are no console errors, no raw `$` and no `.katex-error`.

## Earlier findings: all resolved
- Old Blocking 1 is resolved:
  - The `review` feedback now ends "Keep this in mind for later in the lesson." and no longer links the mass defect to the Sun's puzzle.
  - `pred-models` is open again: nothing before it states that nuclear energy is the answer.
  - In the browser it locks on commit and opens only when `theory-key` is on screen.
- Polish 2: in `find-error`, the correct option (43 characters) is no longer the longest (44 and 52).
- Polish 3: `check-explain` uses $E = \Delta m \cdot c^2$.
- Polish 4: `check-3` now tests an assumption. With only $70\ \%$ hydrogen the estimate is shorter, longer or unchanged, and the feedback for each option repairs the reasoning.
- `check-1` is also rebalanced (52 against 51 and 51).

## Polish (not blocking)
1. `inquiry.json` `check-3`: the correct option ("It becomes about $30\ \%$ shorter.") gives $7 \cdot 10^{9}$ years in its feedback. That is still longer than the Sun's present age, $4.6 \cdot 10^{9}$ years. One clause in the feedback would close the loop with the lesson's question: "… still longer than the Sun's present age, so the conclusion holds."

## Checked again
- Predictions:
  - `pred-coal` and `pred-models` lock on commit with no feedback.
  - They open with `theory-candidates` and `theory-key`.
  - The hero, the hook and the Why line give nothing away.
- The model answers of `kelvin-debate` and `check-explain` stay closed until the student writes something.
- The theory is about 530 words.
- The historical investigation (data, source, ordering, pair discussion) is unchanged and good.

## Re-check 2026-11-01: photographs
Aston portrait follows the completed Eddington argument in Key idea (not inside the calculation) and shows who made the decisive measurement; `eddington-source` comes earlier, and later checks are answered by the text anyway. Eddington portrait in People is fine. No lesson ids, no ×, British spelling.
