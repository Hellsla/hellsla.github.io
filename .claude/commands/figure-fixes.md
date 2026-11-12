---
description: Make the figure corrections the teacher approved in the illustration audit for one course, show each before and after, and stop for the teacher's approval
argument-hint: <COURSE, e.g. FY3 | FY10 | FY14 | TVT> [<lesson-id> …]
model: opus
effort: medium
---
Make the approved figure corrections of $ARGUMENTS. Work in `fysiikkalabra/` (`cd fysiikkalabra` first): every path below is relative to it. Report to the teacher in Finnish.

**What this is.** The illustration audit (`docs/illustration-audit/`, teacher 2026-11-11) judged every drawn figure, and the teacher decided figure by figure. The redraws and the shared corrections (axis title beside the arrow, the Sun as a plain disc) are done. What is left is the per-figure light corrections: a label on a line or on the frame, a colour, a sparse composition, a unit written as a vertical fraction. This command does those for one course. It adds no figure, writes no exercise and changes no physics.

**Read first:** `docs/illustration-audit/INDEX.md` (the teacher's rulings at its end), `docs/illustration-audit/data/<COURSE>.tsv`, NOTES.md §3 (figures, palette, every label LaTeX, text at 24 px or more), `scripts/figstyle.py` (the house style) and one corrected figure as the model: `fy7-11/observer` in `lessons/FY7/fy7-11/figures.py`.

**Which figures.** A row of `data/<COURSE>.tsv` is `id|F|P|V|T|recommendation|why|proposal|decision`. Work on a figure only when its decision column holds an approval (`KEVYT KORJAUS hyväksytty…`) and does not yet say `TEHTY`. A row with an empty decision, or one that says `PIDÄ`, is left exactly as it is, whatever the recommendation column says (teacher: "älä muuta jos en sanonut niin"). If lesson ids follow the course in the arguments, work on those lessons only. List the figures you will touch before you change anything.

**For each figure:**
1. Render it as it is and keep that picture: the SVG its `figures.py` draws, on a page with `site/site.css` and KaTeX, captured at 600 px and at 360 px. Look at the capture.
2. Make the correction the row's `why` names, in the figure's own function. Nothing else in the file changes: a helper another figure uses is copied, never edited. The content, the numbers and the scale stay; if the figure is to scale, check the lengths from the code.
3. Render again and look at both widths. A figure is done when you have seen it, not when the code looks right: no label on a line, another label or the frame; every text 24 px or more; the corrected thing really is better than before, for a student, not only tidier. If the original turns out to be better than the correction, leave it and say so in the report.
4. Write the figure into the texts of every language (`scripts/figures.py <id>` and `--lang en`, `--lang fi-easy`; `practice.py figures`, `investigations.py figures`, `units.py figures`, `guides.py figures` for the other page types). A changed description or word needs its translation in that language's `figures.json`.

**Rulings that hold for every figure** (INDEX.md): a force is red and starts on the body; air resistance is drawn as a push against the motion, its tip on the face the air presses on (as in `fy4-14`); the Sun is a disc without rays; an energy flow diagram follows `fy2-4/lamp` (grey in, green useful, orange heat, widths to scale); a unit on an axis is written on one line (`\text{m/s}`), except where the fraction is the point (`fy6-6/energia` stays).

**Never:** change `scripts/figlib.py`, `scripts/figstyle.py`, `scripts/herolib.py`, `scripts/fbd.py`, a template or another course's figures (a need for a shared change goes into the report as a proposal); record an approval (`docs/teacher-figures.tsv`, `reviews.py approve-figures`, `carry`, `carry-item`); start a science, pedagogy or visual review; touch a figure without an approved decision; fix a physics error quietly (report it at the top instead).

**Checks before you stop:** `python scripts/lint_lesson.py <id>` for each changed lesson (no new error), `python scripts/practice.py check`, `investigations.py check`, `units.py check`, `guides.py check` as the page types need, and `python scripts/figcat.py build`. A lesson edited here is linted as an edited lesson until its figures are approved: errors about text you did not touch are expected then and go away with the approval; report them, do not fix them.

**Then stop and hand over.** Commit on your own branch, push, open a draft pull request whose title begins `[odottaa hyväksyntää]` and whose description begins with the line **Älä merge ennen kuin hyväksyntä on kirjattu: muuten sivut putoavat sivustolta ja mainin CI menee punaiseksi.** (2026-11-12: #502 was merged before its approval was recorded; the next build would have dropped six lessons and main's CI was red). Report:
- first, any physics error found and any figure you left because the original was better;
- one row per figure: its id, what changed, and the before and after captures (both widths);
- the checks' results as they came out;
- what is left undone and why.

The pages whose figures changed are drafts until the teacher has looked. After the teacher names the approved figures, and only then, record a row in `docs/teacher-figures.tsv` for exactly those figures (`reviews.figure_hash(<id>)`, the date, the id, the hash; `approve-figures <id>` would approve every figure of the lesson at once), run `python scripts/reviews.py carry <id>` (and `--exercises`, and each `--lang`) for a lesson or `carry-item investigation|sovella|koe|unit|guide <id>` for the other page types, check that `python scripts/reviews.py verify` exits 0 (it needs the full git history: `git fetch --unshallow` in a shallow clone), and mark the rows `TEHTY ja hyväksytty <date>` in `data/<COURSE>.tsv`. Then:
- Compute each hash in a fresh process with `PYTHONDONTWRITEBYTECODE=1`, after deleting `__pycache__`, and check it equals the hash of the drawing the teacher saw. A stale `__pycache__` (a figures.py switched back and forth within the same second, e.g. for the before capture) gave the old drawing's hash on 2026-11-12, and CI (Python 3.12) failed `verify`.
- Rebuild `site/` (`python scripts/build.py`): no page may be removed, and `git status site/` shows only the pages you meant to change.
- Run `python scripts/check_layout.py <page> en/<page> fi-easy/<page> --site --width <w>` for every changed page at all eight widths CI uses (360 390 640 768 1024 1280 1440 1920; `PW_CHROMIUM=/opt/pw-browsers/chromium` in a cloud container). A moved label must also fit in English, which is often longer ("säätö" → "control"). CI measures text a few pixels wider than a local Chromium, so leave a margin.
- Only then take `[odottaa hyväksyntää]` off the title, remove the warning line and mark the pull request ready.
