VERDICT: PASS
CONTENT-HASH: 2953f276a281a98f

Pedagogy re-review of fy14-fusion-debate (2026-11-01) after commit 04ac2449. The page was rebuilt, served on port 8775 and tested in Playwright at 390 px.

## Earlier findings
Old Blocking 1 is resolved.
- `pred-public` asks for the public share of the USD 14.24 billion; the answer is on card E, about USD 0.98 billion or 7 %.
- `pred-origin` asks where Commonwealth Fusion Systems came from; the answer is on card I, a spin-off of an MIT laboratory.
- Neither answer appears in fy14-fusion-society or in any earlier unit. *Confinement concepts* mentions only an HTS magnet built by MIT and CFS together, which is a fair hint and not the answer.
- Both questions can be argued before the evidence, and both feed the motion.
- In the browser, both lock with no feedback, stay closed until the cards are on screen, and then open with the committed option's own feedback.

Polish 2–9 are resolved:
- the phrase bank uses `<strong>` and no raw `**` is left;
- the steps add up to 21 minutes (1 + 4 + 4 + 5 + 2 + 3 + 2), which fits the 42–63 slot;
- the chair's phrases are on the page and the chair's script is in `teacher.md`;
- the rebuttal and closing speakers have preparation lines;
- the votes decide the winner and the scores are for feedback and assessment;
- `rebuttal` is shortened;
- the feedback on card C accepts *either*;
- the opposition model has 123 words;
- the video task has sentence starters.

Delta check after commit f3c5f463:
- the chair's script now reads the motion word for word;
- the `check-1` distractor now says "cost estimates grew", and its feedback notes the different scope;
- Polish 2 below is done.

The page was rebuilt and tested again in Playwright: the predictions lock and reveal, and the model answers stay closed until the student writes.

## Blocking
None.

## Polish
1. `check-2` (64 against 63) and `check-3` (61 against 60): the correct option is still the longest, by one character. This is harmless. Elsewhere there is no length pattern.
2. ~~`check-1` distractor scope~~: done in f3c5f463.

## Checked
- 75 minutes, roles, timing, the phrase bank with a match and starters for every speech and for the chair, the fact-checkers' script, and four 0–3 criteria shown on the page; the opinion is not graded.
- CLIL and B1–B2 English, the group work, and the French corner.
- All five model answers stay closed with an empty answer and with 5 characters.
- There are no console errors, no KaTeX errors and no horizontal scroll at 390 px.
