# Fysiikkalabra — Claude Code scaffold

A Fysiklabbet-style teaching site (theory + simulations + exercises) built with Claude Code and a team of 15 agents.
It lives in the `fysiikkalabra/` folder of the `hellsla.github.io` repository.

## Quick start
```bash
cd fysiikkalabra
pip install markdown playwright && playwright install chromium
python scripts/build.py              # builds site/ from reviewed lessons only
python scripts/build.py fy3-2        # preview one lesson regardless of status
python scripts/build.py --all        # every lesson, drafts included (what CI runs)
python scripts/test_sims.py          # Playwright over every built simulation
python scripts/check_latex.py content/FY3/fy3-2   # KaTeX parse check (uses vendored katex, no npm)
python scripts/screenshot.py fy3-2   # review/fy3-2-390.png and -1280.png
claude                               # open Claude Code in this folder
```
If the pip `playwright` version does not match an already installed browser, point the scripts at it:
`PW_CHROMIUM=/path/to/chrome python scripts/test_sims.py`.

Inside Claude Code:
```
/build-lesson fy3-2        # draft one lesson with you, then run producers + reviewers
/review-lesson fy3-2       # reviewers only, on an existing lesson
/daily-news                # one news item (also wired as a scheduled task)
/weekly-newsletter         # draft this week's newsletter
```
Agents live in `.claude/agents/`, commands in `.claude/commands/`, house rules in `CLAUDE.md`.
Nothing is published unless `meta.json` says `"status": "reviewed"`.

## Libraries and CI
p5.js 1.9.4 and KaTeX 0.16.11 are vendored in `templates/vendor/` and copied to `site/vendor/` on build,
so pages and headless tests work without a CDN. `.github/workflows/fysiikkalabra-ci.yml` (at the repository
root) builds all lessons and runs the sim and LaTeX checks on every push that touches this folder.

## Publishing
`hellsla.github.io` serves GitHub Pages straight from the repository root, and `site/` is git-ignored,
so built lessons are not live yet. Two options, to be decided: commit `site/` (served at
`/fysiikkalabra/site/`), or add a workflow that builds and pushes `site/` on merges to `main`.

## Curriculum and sources
`curriculum.json` covers FY1–FY8 with module goals, central contents, transversal competences and a proposed
lesson-slot list per module, generated from the LOPS 2019 texts in `docs/lops2019/` (PDF + extracted text).
The slot list is a proposal: reorder or rename before drafting. The reference lesson in `content/_gold/` is
`fy4-4` Newtonin toinen laki; the first draft is `content/FY3/fy3-2/` Työ ja energia.

## Exercise schema
```json
{ "id": "fy3-2-L2-03", "level": 2, "text": "...", "answer": 2.0, "unit": "m/s²", "tolerance": 0.05 }
```
