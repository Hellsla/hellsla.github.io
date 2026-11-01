VERDICT: DONE

Unit fy14-fusion-debate, "Debate: should governments invest more in fusion?" (FY14 chapter 8, order 2). Developer report 2026-11-01.
Content hash at hand-over: 974cbb7890e9f925.

## Files
- `unit.json` (14 sources, 1 media credit for the video, checked 2026-11-01), `unit.md` (Why, hero, nine evidence cards A–I, Key idea: claim–evidence–reasoning, Format: motion, roles table, order and time limits, judging criteria; Common misconception; Summary), `inquiry.json` (26 activities), `teacher.md`; `lessons/units/fy14-fusion-debate/figures.py` (hero: classroom debate, two lecterns, chair with a timer, screen with a bar chart and a torus, audience from behind; faceless figures, no text).
- Core path: review (institutional plan); first opinion; predictions (ITER cost growth ×3–4; FIA USD 4.48 billion) revealed by the evidence cards; sort the cards (for / against / either) with feedback; group task on the strongest card for each side; theory; debate-phrase match and sentence starters for every speech; preparation of the opening speech (two model speeches); best-rebuttal choice; run sheet for chair, fact-checkers and judges; three checks (weakest argument, fact-checking NIF, evidence vs reasoning); individual position paragraph after the debate; French corner (`say`: à mon avis, je suis / ne suis pas d'accord, l'argent public, la recherche).
- Supplementary video EhAemz1v7dQ: YouTube oEmbed and page read 2026-11-01: "Do we Need Nuclear Energy to Stop Climate Change?", Kurzgesagt – In a Nutshell, 13 April 2021, 9:03; about fission. Used as an optional source-evaluation task (questions only on creator, date, topic and limits); teacher.md says its spoken content was not checked.

## Numbers
ITER 18/5.9 = 3.05, 22/5.9 = 3.73; NIF 3.15/2.05 = 1.54, 8.6/2.08 = 4.13; deuterium 0.0348 g per litre.

## Facts verified (2026-11-01; sources in unit.json)
JET 69.26 MJ (EUROfusion); NIF (Wikipedia); deuterium abundance; ITER *Advantages* and *Safety*; Ember 2025 (renewables 33.8 %, coal 33.0 %, wind + solar 17.3 %); FIA 2026 survey (WNN 14 Jul 2026; public share USD 980.7 million in SolarQuarter 15 Jul 2026); ITER costs and 2024 baseline (Wikipedia); IPCC SR1.5; STEP 2040 (GOV.UK); Commonwealth Fusion Systems spin-off 2018, DOE milestone funding May 2023; Alcator C-Mod 1991–2016, 2.05 atm 2016, proposed to DOE 1985.

## Checks
units.py check OK; check_layout 360/1280 OK; screenshots looked at (hero redrawn: speakers behind the lecterns; "1.5 minutes" replaced by "90 seconds"); Playwright: predictions lock until the cards are on screen, 7 choices answered, model answers only after writing, no console errors, no raw `$`, no katex errors.

## Open questions
- Card F's "about 5 billion euros" for the 2024 baseline follows Wikipedia's summary; ITER's own baseline documents were not read.

## Shared issues
None in the components used (match, video, say).
