# Fysiikkalabra agent office

A standalone pixel office inspired by Fysiklabbet's agent office. Open `agent-office/index.html` through a static web server. No npm install, build step, CDN or API key is needed; the font is already in this repository.

```sh
cd /workspace/hellsla.github.io
python3 agent-office/export_history.py
python3 -m http.server 8000 --bind 127.0.0.1
```

The exporter only reads Git metadata and atomically replaces `agent-office/history.js`. It exports the last 200 first-parent commits reachable from the current checkout, including merge diffs against their first parent. It never stages, commits, switches branches, reads private Claude sessions, runs agents, or reads or writes lesson working files. Refresh the browser after exporting to see the new snapshot. Export manually when you want an update; there are no hooks, watchers, scheduled jobs or changes to Claude configuration. Concurrent uncommitted work is intentionally absent from the replay.

Commit times are shown in Europe/Helsinki, with daylight saving handled by Python's timezone database. Desk highlights come from changed file paths, not authenticated agent identities or session logs. A review-file change is not a passing review. A merge is not a deployment. Counts describe the full selected day within the exported history, not events before the replay clock. The scene and brief activity windows are illustrative.

The page includes day selection, pause/play, playback speed, next event, a keyboard-accessible time slider and role buttons, clickable desks and commit entries, fullscreen, and a still-scene control. It respects reduced-motion preferences and starts paused. All commit titles are rendered as text. The reference upload's external scripts and data were missing; this implementation has its own canvas art, styles and scripts, and includes no third-party analytics.

All implementation and generated metadata live in this directory. No changes are needed in lesson sources, simulations, shared templates, CI, or `.claude/` files. There is deliberately no link added to the public homepage. Publishing or merging remains a separate decision.
