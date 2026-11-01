VERDICT: PASS
CONTENT-HASH: 7535d2d9b9420b7a

Pedagogy re-review of fy14-iter-project (2026-11-01) after the "Fixes after review" in review/developer.md (commit c6532e4f; the hash also covers the shared timeline data and component as changed in 525827b2 and b3bbc371, which is the version tested). Rebuilt, served over HTTP and tested in Playwright at 390 and 1280 px.

## Earlier findings
- **Old Blocking 1 is resolved.** The timeline now shows the eight ITER events (`ids`), and every card is closed until the student opens it. The activity is 2,256 px tall at 390 px (before: 20,865 px), and the page is 23,800 px (before: 42,300 px). The task ("open and read at least five", about 10 min) matches the component. Opening a card works, and the 2024 card gives its evidence only after the predictions are committed.
- **Polish 2–3 are done.**
  - 1987 agreement and 1988 conceptual design are now consistent in the text, the summary and `order-story`.
  - `pred-schedule` asks for a justification from known delays.
  - `find-error` is rebalanced.
- Both predictions lock with no feedback. `pred-why` opens at `theory-why` and `pred-schedule` at `theory-schedule`.
- All 5 model answers stay closed until the student writes.
- No console errors and no `.katex-error`.

## Polish (not blocking)
1. `pred-schedule` and the video unit's `pred-date` both turn on the 2025 → 2034 change. The coordinator's reasoning is accepted: one prediction is about the official plan, the other about what a 2022 source says. No change is needed.
2. Apply is still full: the order task, the error-finding task and the 60–80-word paragraph, plus the optional role-play. The plan for running short of time in `teacher.md` covers this.
