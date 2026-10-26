# Fysiikkalabra agent office

A standalone pixel office inspired by Fysiklabbet's agent office. Open `agent-office/index.html` through a static web server. No npm install, build step, CDN or API key is needed; the font is already in this repository.

```sh
cd /workspace/hellsla.github.io
python3 agent-office/export_history.py
python3 -m http.server 8000 --bind 127.0.0.1
```

The exporter only reads committed Git objects and atomically replaces `agent-office/history.js`. It exports the last 200 reachable commits, including branch commits for individual review rounds and merge diffs against their first parent. It reads committed lesson content and review reports to compute historical gate evidence. It never stages, commits, switches branches, reads private Claude sessions, executes historical code, runs agents, or reads or writes lesson working files. Refresh the browser after exporting to see the new snapshot. Export manually when you want an update; there are no hooks, watchers, scheduled jobs or changes to Claude configuration. Concurrent uncommitted work is intentionally absent from the replay.

Commit times are shown in Europe/Helsinki, with daylight saving handled by Python's timezone database. Desk highlights come from changed file paths, not authenticated agent identities or session logs. Counts describe the full selected day within the exported history, not events before the replay clock. Each snapshot belongs to its particular commit; time order across branches does not establish that one version supersedes another.

Follow a lesson through development, saved automatic checks, parallel science/pedagogy reviews, the two-approval gate, and the teacher/publication desk. Paper packets and arrows illustrate the route; they do not assert actual timed file transfers. Review badges use the same normalized content hash rule as `fysiikkalabra/scripts/reviews.py`, including simulation test specifications: both reports must say PASS and match the selected commit's lesson hash. Missing, invalid, failed or stale reports keep this gate closed. Content changes can invalidate earlier PASS reports. A matching legacy marker is a separate prototype exception, explicitly labelled, not a two-review approval.

A standing review gatekeeper holds a clipboard with the two review results. Its open/closed sign, welcoming hand or stop paddle, and barrier follow the selected snapshot's review gate. Click the character or its keyboard-accessible role button for an explanation. It personifies the automatic rule in `reviews.py`; it is not an extra running agent or the teacher's publication decision.

Saved `review/checks.txt` reports have no content hash, so check freshness and CI success stay unknown; a matching review pair alone never claims all publication requirements passed. Presence in committed `site/` means only that an HTML page exists in that snapshot, not that it matches a fresh render or is deployed. A merge does not identify its human approver or prove deployment. The office visualizes these rules but does not enforce or change branch protection, CI, builds or publishing settings.

The page includes day and lesson selection, pause/play, playback speed, next event, a keyboard-accessible time slider and role buttons, clickable desks and commit entries, fullscreen, and a still-scene control. It respects reduced-motion preferences and starts paused; playback and file-packet animation pause together. All commit titles and lesson metadata are rendered as text. The reference upload's external scripts and data were missing; this implementation has its own canvas art, styles and scripts, and includes no third-party analytics.

All implementation and generated metadata live in this directory. No changes are needed in lesson sources, simulations, shared templates, CI, or `.claude/` files. There is deliberately no link added to the public homepage. Publishing or merging remains a separate decision.
