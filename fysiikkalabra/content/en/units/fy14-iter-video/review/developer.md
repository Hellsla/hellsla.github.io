VERDICT: DONE

Unit fy14-iter-video, "Inside the largest fusion reactor: a video investigation" (FY14 chapter 7, order 3). Developer report 2026-11-01. Content hash at hand-over: dc30a3e24eb0b99d.

## Files
- `unit.md`: Why line, hero (laptop with an original drawing of an assembly hall, notebook, magnifier; no text, no frame of the video), Checked (claim-by-claim table: video 2022 vs verified Nov 2026), Key idea (evaluating a video), misconception, summary. Selita about 151 words.
- `inquiry.json` (26 activities): hook, retrieval (plan or result); predictions (the date the video gives → reveal theory-checked; what it focuses on → reveal theory-checked); before watching: vocabulary match (placed after the predictions so it cannot hint at them); while watching: `video` component and four note frames (main ideas, technical concepts, collaboration, construction challenges) as teacher-checkable explain tasks; the checked table; after watching: key idea, word bank + pair discussion on reliability, reflect, claim sorting (source evaluation), sponsor question, 80–100-word written explanation, optional Kurzgesagt comparison (second `video` component), misconception, comprehension checks (numbers, dates, precise wording), recommendation paragraph, summary, French corner.
- `unit.json` (8 sources; `media` credits for both embedded videos), `teacher.md` (what to check against the video before the lesson, timing, supplementary-video evaluation), `figures.py`.

## Video verification (2026-11-01)
- 4BkOUOK0XzM: oEmbed title "We Went Inside the Largest Nuclear Fusion Reactor", The B1M. The B1M page gives 13 April 2022, narrator Fred Mills, paid promotion for Thinkproject and the narration as an article: 35 nations, $22BN, 23,000 t, ~1 million components, 104 km ITER Itinerary, 10× Sun core, 2× shuttle launch force, first power-on 2025, "net energy", grid decades away, private companies, US infrastructure bill. Questions use only these claims.
- An auto-transcript on a third-party mirror (howtoclicks-ytsuben.pages.dev) adds 1985 Reagan–Gorbachev, 150 million °C, energy comparisons, an ITER staff member, schedule reasons, 45 languages; not used for questions; listed in teacher.md for the teacher to verify. Length "about 10 min" from the transcript timestamps (~9:30); teacher to confirm.
- Supplementary: mZsaaturR6E Kurzgesagt "Fusion Power Explained – Future or Failure", 10 Nov 2016, 6:15 (rosetta.to) — included, optional. EhAemz1v7dQ Kurzgesagt "Do we Need Nuclear Energy to Stop Climate Change?", 13 Apr 2021, 9:03, no fusion/ITER — not used (suggested for chapter 8). R-8NbYM1-ws La prof Elisabeth, DELF A1 café dialogue — not used (French café unit).
- Verified facts in the table: iter.org facts (23,000 t, ~1 million components, 104 km, 150 vs 15 million °C), Members page, 2024 baseline PDF, What will ITER do, Wikipedia (costs; NIF Dec 2022).

## Open questions
- The teacher must watch the video once before the lesson and confirm the items listed at the top of teacher.md.

## Shared issues (not edited)
1. `scripts/screenshot.py` opens the pages as `file://`, so components that fetch a data file (`timeline`, `iter`, `map`) show "could not be loaded (TypeError: Failed to fetch)" in the captures. Over HTTP (python3 -m http.server -d preview) they load and work; I checked this. Proposed fix: serve `preview/` with a local HTTP server in screenshot.py (and check_layout.py), as the components need it.
2. The course brief links Yle "https://yle.fi/a/20-153568" for the ITER media task, but that page is an Yle Oppiminen French lesson, *Osa 4: Ravintolat, kahvilat, baarit* (2012, updated 2016), about restaurants and cafés. It is not about ITER. The media unit uses two verified Yle ITER articles instead (2020 and 2005) and says so in teacher.md. Proposal: offer the café page to the developer of `fy14-fr-cafe`.
3. `scripts/test_inquiry.py` / `check_choices.py` do not cover units (known); I tested predictions, reveals, model answers, choices, numeric and components with my own Playwright script over HTTP.
4. `docs/FY14_PLAN.md` says the B1M video's spoken content could not be read. The channel's own page (theb1m.com/video/inside-iter-worlds-largest-nuclear-fusion-reactor) publishes the narration as an article; the plan could mention it as the verification source.
