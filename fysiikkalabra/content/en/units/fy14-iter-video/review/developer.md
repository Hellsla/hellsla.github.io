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

## Fixes after review (content hash 14be3bd2753d402e)
- Blocking (pedagogy 1): sort-claims and the sponsor question moved into Investigate, after frame 4 and before the table; the prompt now says "Use your notes, what you know from the chapter's first two units, and iter.org's Facts page". A "35 nations" item added. The table's verdicts now use only the sort's three categories (correct today / outdated / needs context), and the table follows as the evidence.
- Blocking (pedagogy 2): pred-date options are bare years (2025 / 2030 / 2034 / 2039); reasoning only in the feedback.
- Table: middle cells shortened, the longer explanations moved to a paragraph under the table; quantities in LaTeX; 35 nations "ITER's long-used figure; today 34" (verdict: outdated); cost "official estimates about €18–22 billion" (also in unit.json).
- pred-focus: prompt "From the channel and the sponsor alone, predict …"; feedbacks say "the channel's own text spends most of its words on …".
- Frames 1–2: questions as a lettered list. The watch text and teacher.md now say that each student writes all four frames and that pairs can share the listening.
- check-2 correct option: "The 2016 baseline said 2025; the 2024 one says 2034." (feedback names the plan valid in 2022); other options lengthened so it is not the longest.
- Repeated old-date prediction: the media unit's pred-2018 is gone. This unit's pred-date (what a 2022 source said) and the project's pred-schedule (what the new plan says) remain, as the coordinator asked to keep pred-date.
- Checks as for the project unit: all OK.
