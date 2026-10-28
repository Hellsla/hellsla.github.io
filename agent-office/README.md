# Fysiikkalabra agent office

A standalone pixel office inspired by Fysiklabbet's agent office. Open `agent-office/index.html` through a static web server. No npm install, build step, CDN or API key is needed; the font is already in this repository. The drawing lives in `office-scene.js`, separately from the history and evidence controller in `office.js`.

The **FI / EN** button switches the controls, canvas labels, status messages, role/about dialogs and speech bubbles between Finnish and English. Finnish is the initial default; the choice is remembered locally and can be overridden with `?lang=fi` or `?lang=en`. Commit messages, file names and authored material titles remain unchanged. Translations are bundled locally in `office-i18n.js`; no translation service or network request is used.

**Office only / Vain toimisto** fills the viewport with just the office and hides the header, panels, timeline and surrounding controls. Open `agent-office/?view=office&lang=fi` (or `lang=en`) directly for presentation. Playback starts automatically unless reduced motion is selected. Move the pointer or touch the screen to reveal small language, pause and return controls, which fade away when idle. Escape restores the full interface; Space pauses/resumes when the office canvas has focus. Presentation also works within the existing fullscreen mode.

Funny speech bubbles follow the illustrated task: checking units, waiting for a second report, revising stale work, or waiting for publication approval. They never invent a successful review or approval. The **Speech bubbles / Puhekuplat** checkbox hides them. The coffee lounge has a sofa, coffee machine and mugs. At most one idle colleague takes an occasional break, returns before their next handoff, and does not interrupt an active delivery or delay the other reviewer. Breaks rotate across loops and remain illustrations; they never pause real agents, change logs or write material files. Both features respect pause and reduced motion.

```sh
cd /workspace/hellsla.github.io
python3 agent-office/export_history.py
python3 agent-office/export_lineage.py
python3 -m http.server 8000 --bind 127.0.0.1
```

The exporter only reads committed Git objects and atomically replaces `agent-office/history.js`. It exports the last 200 reachable commits, including branch commits for individual review rounds and merge diffs against their first parent. It reads committed material content and review reports to compute historical gate evidence. It never stages, commits, switches branches, reads private Claude sessions, executes historical code, runs agents, or reads or writes material working files. Refresh the browser after exporting to see the new snapshot. Export manually when you want an update; there are no hooks, watchers, scheduled jobs or changes to Claude configuration. Concurrent uncommitted work is intentionally absent from the replay.

Commit times are shown in Europe/Helsinki, with daylight saving handled by Python's timezone database. Desk highlights come from changed file paths, not authenticated agent identities or session logs. Counts describe the full selected day within the exported history, not events before the replay clock. Each snapshot belongs to its particular commit; time order across branches does not establish that one version supersedes another.

Follow a material through development, saved automatic checks, parallel science/pedagogy reviews, the two-approval gate, and the Lauri/publication desk. People carrying material packets illustrate the handoffs; they do not assert actual timed file transfers. Historical review badges use the supported committed review schema and trusted current read-only hashing helpers, including simulation dependencies: both reports must say PASS for the selected content version, directly or through a recorded carry row. Missing, invalid, failed or stale reports keep this gate closed. Content changes can invalidate earlier PASS reports. A matching legacy marker is a separate prototype exception, explicitly labelled, not a two-review approval.

The connected office has a shared developer/support workshop, quiet science and pedagogy review rooms, a central coordination island, an external-review meeting room, a testing station, coffee corner, Lauri’s planning nook and a publishing area. Doorways connect them to shared circulation. Role-specific equipment, windows and varied furniture distinguish the spaces. Packets illustrate work moving between people; report colours follow the selected evidence. No extra agents are launched.

The nine human roles have distinct sprites: developer headphones and gold clothing, science reviewer grey curls and blue, pedagogy reviewer braid and pink, amber test operator, brown-jacketed orchestrator, blue support colleague, green-jacketed publisher with a tie, mint-clad external reviewer with a scarf, and Lauri’s black hair, stubble and red plaid shirt. Every person has an inspectable portrait. The review inbox and website display are fixtures with details but no human portrait. Motion uses elapsed time, eased starts/stops, directional poses and rounded corners; pause and reduced motion stop animation.

The publisher prepares material for the website preview only after Lauri’s visit and matching recorded approval. The renderer accepts `publicationDecision: {status: "approved", contentHash: "<current material hash>"}`; both current review requirements must also be met. Existing exported history has no human approval evidence, so a merge or HTML page never triggers publication preparation. An older approval does not apply, and the illustration never claims successful deployment.

Science and pedagogy work independently in parallel, with staggered copy collection, different review durations and separate report deliveries. Which role finishes first varies deterministically by material version; these timings are illustrative, not measured session durations. Room labels distinguish recorded verdicts from the current walkthrough activity. The review desk counts delivered reports and visibly waits at 1/2; it becomes READY only after both illustrated deliveries and two current recorded PASS verdicts. Report packets carry PASS, FAIL, STALE or INVALID labels. A failed, stale or invalid report leads to a REVISE handoff; a missing report keeps the desk waiting without inventing a report or publication handoff. Fixing a version requires new checks and reviews, not reuse of its previous approvals.

Playback has two explicit modes. **Lesson journey** (the default) loops the illustrated handoffs while keeping the recorded commit and clock fixed. **Day history** advances through the recorded commits and their evidence. Both start paused. **Next handoff** steps through the illustrated work periods and each reviewer's separate pickup, completion and report arrival, including with reduced motion; **Next commit** changes the historical snapshot. **Office zoom** enlarges the drawing inside its scrollable viewport, including on phones. Every room or station can be inspected by clicking it or using its role button.

Two report trays beside the orchestrator represent the automated review gate. The rule is not an employee. The orchestrator handles reviewed packets and visits the publisher; Lauri then discusses the proposal with the publisher, with the characters facing each other. The website preview is a wall display beside publishing, not a courier character. Technical verdicts, counts, hashes and publication evidence remain in the inspection panel.

Saved `review/checks.txt` reports have no content hash, so check freshness and CI success stay unknown; a matching review pair alone never claims all publication requirements passed. Presence in committed `site/` means only that an HTML page exists in that snapshot, not that it matches a fresh render or is deployed. A merge does not identify its human approver or prove deployment. The office visualizes these rules but does not enforce or change branch protection, CI, builds or publishing settings.

The page includes day and material selection, pause/play, playback speed, next event, a keyboard-accessible time slider and role buttons, clickable desks and commit entries, fullscreen, and a still-scene control. It respects reduced-motion preferences and starts paused; playback and file-packet animation pause together. All commit titles and material metadata are rendered as text. The reference upload's external scripts and data were missing; this implementation has its own canvas art, styles and scripts, and includes no third-party analytics.

All implementation and generated metadata live in this directory. No changes are needed in material sources, simulations, shared templates, CI, or `.claude/` files. There is deliberately no link added to the public homepage. Publishing or merging remains a separate decision.


Material journeys follow verified ancestry from the selected commit, using `history-lineage.js` and `office-journey.js`. `export_lineage.py` reads Git ancestry and the existing snapshot export without recomputing or altering review evidence. Run it after refreshing `history.js`. Unrelated branches are never joined merely because of their timestamps. Missing ancestry stops the chain. Repeated identical states are skipped; changed content hashes increment the version number. Stages can represent successive reports on the same version, so stage numbers are not claimed counts of real review sessions. The evidence panel follows the displayed stage, while the day timeline remains the selected endpoint. Playback stops at the last recorded stage; Play replays the chain. Use **Next recorded stage** to skip ahead or **Next handoff** to inspect individual transfers.

A reviewer with a failed, stale or invalid report carries it directly to development on their independent schedule. The developer remains available to receive feedback, revises the material and returns to the test runner before the next recorded stage. Missing reports do not fabricate feedback. Motion and speech illustrate the recorded status; no specific reviewer findings, actual transfer times or missing PASS results are invented. Lauri has black hair and a red plaid collared shirt, with light stubble and no glasses. Characters working at computers face their screens. Movement and typing respect pause and reduced motion.

Run the dependency-free ancestry and review-stage checks with `node agent-office/test-journey.cjs`.

Speech chooses randomly among three context-specific lines per task, avoiding an immediate repeat within the same situation. Each visible bubble remains stable while paused or switching language. The office canvas omits the extra corridor stage counters, numbered review headings, coffee captions and crossed-out status footnotes; recorded evidence remains available in the details panel. The publication desk states: “JULKAISIJA EHDOTTAA, LAURI PÄÄTTÄÄ”.


### Whole webpage review with an external reviewer

Select **Whole webpage review / Koko verkkosivun arviointi** in the playback menu to explore an optional workflow described by Lauri: request an external review, share the webpage, consider its overall structure and usability, return suggestions to Lauri, brief Claude on selected changes, then check and revisit. The external review room can also be inspected in the office. All six steps work with Next handoff, pause, reduced motion, office-only presentation and FI/EN.

This mode is an illustrative scenario, not exported review evidence. It does not contact external reviewers, read conversations, invent specific findings, or change material hashes, review verdicts or publication eligibility. Recorded history and evidence panels are hidden during the scenario and restored when returning to material or day playback. The lesson science/pedagogy review gate stays separate; whole-webpage feedback may lead to changes that require fresh checks and affected lesson reviews.

Run `node agent-office/test-web-review.cjs` for external-review handoffs and isolation from recorded approval evidence.

The publisher proposes; Lauri decides. Lauri walks over after the review handoff, stays for the discussion, then returns. The publisher may prepare the website preview only with recorded approval matching the content hash; the illustrated visit alone grants neither approval nor deployment. External review takes place at a meeting table, with Lauri and the visitor facing each other.


### Updating static assets

After changing any office JavaScript, stylesheet or exported history, run `python3 agent-office/version_assets.py` and include the updated `index.html` in the same commit. The page uses content hashes in asset URLs so cached scripts from an older character renderer are not combined with a newer controller. No build or server-side code is required at runtime.

Run `node agent-office/test-assets.cjs` to verify the asset versions before pushing.


Commit timestamps are shown with seconds in Europe/Helsinki. In Material journey mode the main clock follows the displayed stage's commit, rather than staying on the selected day timeline endpoint. A handoff within the same stage keeps that timestamp; Next recorded stage advances to another saved version. Day history mode labels its clock as replay time. Full dated timestamps with UTC offsets are available on hover and in snapshot evidence, including the repeated hour when daylight saving ends. Run `node agent-office/test-time.cjs` to check formatting and both Helsinki clock changes.


### Recorded work and current layouts

The refreshed snapshot includes 27–28 October 2026. `history_evidence.py` reads both the old `content/<course>/<lesson>/` layout and Finnish `content/fi/<course>/<lesson>/`, shared code under `lessons/`, simulation assets and language strings. It imports only the trusted current review helpers, never historical Python. Each commit's saved review schema selects combined or separately hashed lesson/exercise content. Recorded carry rows are labelled explicitly; CI verification of those rows is not inferred.

The material evidence panel shows cumulative committed usage entries for development, correction, science/pedagogy reviews, full versus partial reviews, coordination and general-purpose support. Repeated log references copied during moves are counted once. These figures do not establish live sessions or their exact chronology. Separate exercise hashes and verdicts explain why exercise work can continue independently of lesson approval.

There are still three dedicated active agent definitions. Two additional offices represent coordination and general-purpose work actually named in committed usage logs. The four parked agents remain inactive and are not portrayed as working. The walkthrough's movement is still an illustration: private prompts, uncommitted work, off-repository external reviews and human approval cannot be recovered from these files. The history freshness label states the latest included commit. Refresh manually with export_history.py, export_lineage.py and version_assets.py when publishing new work; this remains a static snapshot, not live monitoring.

Run `python3 agent-office/test_history_evidence.py` to compare all current exported lesson/exercise hashes and verdicts with the actual application review state and verify the requested dates and recorded extra roles.

At a merge, the journey follows the actual parent carrying the displayed material evidence when exactly one parent matches it. This retains the source branch's review/correction rounds instead of silently skipping them along main's first parent. Ambiguous merges keep the existing first-parent route; unrelated branches are never spliced together by timestamp.


### Connected office layout

The drawing now uses one connected floor in `office-floor.js`: a shared developer/support workshop, two quiet reviewer rooms, a central coordination island with project board and report trays, a glazed meeting room for external review, a testing station, coffee corner, Lauri's planning nook and a publishing desk beside a website preview display. Windows, open doorways, varied furniture and shared circulation replace the equal-sized room cards. The furniture and walking routes use the same geometry.

Only human roles have people and portraits. The review gate is an automated inbox fixture; the orchestrator handles reviewed packets. The website is an output display, with the publisher preparing approved work. Lauri faces the publisher during the proposal discussion and faces the external reviewer at the meeting table. Support has a flexible desk in the workshop. Technical counts, hashes, report verdicts and publication evidence remain in the inspection panel; the floor shows understandable tasks instead. These visual changes do not alter the evidence or approval rules.

Run `node agent-office/test-floor.cjs` for doorway/board clearance, face-to-face handoffs and the distinction between human roles and inspectable fixtures.


### Testing and web publishing work periods

`office-processing.js` defines illustrative work periods, separate from commit timestamps. Material delivery reaches the test operator, pauses for calculation/simulation/exercise/mobile-layout tasks, then allows collection by the reviewers. The developer waits beside the bench while the operator types. Re-tests and the external-review example also pause at the bench. Next handoff includes each work task, including with reduced motion.

The material journey now lasts 56 illustrative seconds per recorded stage; the external-review example stays at 42. After Lauri's discussion, a matching recorded `publicationDecision` permits the publisher to deliver the approved bundle to the automated Web publishing station. It then prepares the HTML/CSS bundle. Earlier preview building still belongs to development/testing. The station is a fixture, not a new AI agent. Preparation never establishes deployment success.

An optional snapshot `deploymentDecision: {status: "published", contentHash: "<current material hash>"}` permits the final illustrated transfer and published website label after preparation. A matching `status: "failed"` shows attention needed. Missing or stale evidence keeps the website as a preview. These fields are explicit input contracts; existing committed exports supply no such deployment record. The animation never executes tests, builds, uploads or publishes anything.

Run `node agent-office/test-processing.cjs` for the waiting period, each test task, re-tests, approval-gated transfer, processing delay and current versus stale/failed deployment evidence.
