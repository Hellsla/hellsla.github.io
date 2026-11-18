VERDICT: FAIL
CONTENT-HASH: 19c370b7c9fc0c25

## Blocking
- [Major] visual verification incomplete — the packet's capture folder `content/en/FY4/fy4-1/exercises/review/shots/` does not exist (no contact sheets, no `sol-fy4-1-*` captures), so the changed Kaava lines in solutions.md (cart A/B meeting, correction factor k, police car and truck) could not be judged as rendered — a delta review of math typography needs the captures — fix: regenerate the captures (`python scripts/screenshot.py fy4-1`, packet rebuilt with `scripts/review_packet.py`) and re-run the visual review.

## Polish
None (diff read as text only: the three new Kaava lines are inline chains with correct `\text{}` subscripts and `\,` spacing, the display formula stays its own `$$` line; layout of the longer inline Kaava lines at 390 px is unverified).

## Checked
- No captures could be opened (folder missing). Read the diff and packet only.
- Hash at start and end: 19c370b7c9fc0c25 (unchanged).

## Scores
illustrations n/a · typography n/a · Finnish n/a · accessibility n/a
