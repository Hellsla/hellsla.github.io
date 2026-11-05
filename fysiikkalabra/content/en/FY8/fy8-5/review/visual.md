VERDICT: PASS
CONTENT-HASH: e43ea85aaa4a9edf

## Blocking
(none; the item below is resolved, see Follow-up)

## Earlier blocking (resolved)
- [Major] inquiry.json learn[1] — the new goal "interpret an orbital as a quantum state of the electron and its picture as a region inside which the electron is detected with a chosen probability." is 26 words; inquiry.validate rejects it (a goal is one short line, at most about 20 words), so `build.py fy8-5` exits 1 and `screenshot.py fy8-5` fails in every language; the en page cannot be built and the preview still shows the old goal, so visual verification is incomplete — fix: `"interpret an orbital as a quantum state of the electron and its picture as a region of chosen detection probability."` (20 words; built in a scratch copy: validation passes, fi and fi-easy render), then capture again.

## Polish
(none)

## Checked
- delta review of 2c31ff041: learning goal 2 (orbital as a quantum state, its picture as a region); diff read. `screenshot.py fy8-5 --lang en` FAILS (build.py exits on the en inquiry.json, see Blocking); preview/en/fy8-5.html is stale (old goal).
- Earlier: batch delta review: opened the captures of the changed passages (theory-1280 / example-390), source diff read; no figure changed; text-only edits render cleanly, no clipping, no horizontal overflow, no inline formula wrapped.

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 3

## Follow-up (uncommitted edit, hash e43ea85aaa4a9edf)
- The earlier Blocking item is resolved: learn[1] now uses the suggested 20-word goal. `screenshot.py fy8-5 --lang en --if-stale` built the page and wrote 67 captures and 6 contact sheets; preview/en/fy8-5.html holds the new goal.
- Own 390 px element capture of the goals box (scratchpad fy8-5-goals-390.png): goal 2 wraps to four lines, as goals 1 and 3 do (each takes three or four lines); bullets and hanging indent align; no clipping; page scrollWidth 390 (no horizontal scroll). top-390 opened too: the opening is unchanged.
- Blocking: none. Polish: none new.
