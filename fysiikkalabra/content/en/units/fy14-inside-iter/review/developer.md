VERDICT: DONE

Unit fy14-inside-iter, "Inside ITER: the machine and fusion gain" (FY14 chapter 7, order 2). Developer report 2026-11-01. Content hash at hand-over: 1bec3935b27c6132.

## Files
- `unit.md`: Why line, hero, Machine (parts, read in Investigate), Key idea (Q, breakeven, JET 0.67, Q = 10, burning plasma), Formula: Fusion gain (+ power bar figure; gain vs electricity; scientific gain vs commercial viability), Fuel (tritium cycle, breeding, test blanket modules, radiation protection), Worked example (7 staged steps: Q and alpha power), misconception, summary. Selita about 337 words.
- `inquiry.json` (23 activities): hook, retrieval (neutron has no charge); predictions (highest heat flux → reveal theory-machine; electricity to grid → reveal theory-gain); `iter` explorer (about: false so the Q/schedule panel cannot give prediction 2 away) with explain; vocabulary match; theory; word bank + pair discussion; reflect; worked example; Fuel reading; numeric tritium per pulse (0.355 g, 3 mistake feedbacks, full 7-step solution); error-spotting (JET Q is not electricity); optional `iter` quiz; 3 checks; explain; summary; French corner.
- `unit.json` (11 sources), `teacher.md`, `figures.py` (hero tokamak cut-away, no text; power bars to scale).

## Numbers (Python, NIST atomic masses, c² = 931.494 MeV/u)
- D–T Q-value 17.589 MeV; helium 3.540, neutron 14.049 MeV. Li-6 + n → He-4 + T: 4.78 MeV.
- Q = 500/50 = 10; P_alpha = 3.5/17.6 · 500 = 99.4 MW; neutrons 400.6 MW; fusion share of heating 99.4/(99.4+50) = 0.665.
- Tritium per 400 s pulse: N = 5e8·400/(17.6·1.602e-13 J) = 7.093e22; m = N·3.016·1.661e-27 kg = 3.554e-4 kg = 0.355 g (exact constants 0.3552 g). Per second 0.888 mg; deuterium per pulse 0.237 g; 200 GJ per pulse; 1 kg T ≈ 2,800 pulses.
- 500 MW heat · 1/3 = 167 MW (≈170 MW) < 300 MW plant draw. JET 16/24 = 0.667.

## Facts verified (2026-11-01)
- Q = 10, 500 MW from 50 MW, burning plasma, TBMs (Li-6), no electricity, nuclear licence 2012 — iter.org What will ITER do. 830 m³, 400–600 s, 150 million °C ≈ 10 × Sun core, JET 0.67 — iter.org facts. Over 300 MW drawn, 15 MA, Q_DT > 5 long pulses — Wikipedia ITER, ITER PDF. Component numbers — iter.json (its own sources). Burn fraction about 1 %, closed loop, detritiation — iter.org/node/15779. Bioshield — iter.org/node/20365. Tritium half-life 12.32 a, CANDU production, Li-6 breeding — Wikipedia Tritium.

## Open questions
- "about one third" thermal-to-electric conversion is a typical steam-cycle value stated as a rough assumption, not an ITER figure.
- Plasma density statement ("hundreds of thousands of times less dense than air") rests on n ≈ 1e20 m⁻³ vs air 2.5e25 m⁻³ (common textbook values, not an ITER page).

## Shared issues (not edited)
1. `scripts/screenshot.py` opens the pages as `file://`, so components that fetch a data file (`timeline`, `iter`, `map`) show "could not be loaded (TypeError: Failed to fetch)" in the captures. Over HTTP (python3 -m http.server -d preview) they load and work; I checked this. Proposed fix: serve `preview/` with a local HTTP server in screenshot.py (and check_layout.py), as the components need it.
2. The course brief links Yle "https://yle.fi/a/20-153568" for the ITER media task, but that page is an Yle Oppiminen French lesson, *Osa 4: Ravintolat, kahvilat, baarit* (2012, updated 2016), about restaurants and cafés. It is not about ITER. The media unit uses two verified Yle ITER articles instead (2020 and 2005) and says so in teacher.md. Proposal: offer the café page to the developer of `fy14-fr-cafe`.
3. `scripts/test_inquiry.py` / `check_choices.py` do not cover units (known); I tested predictions, reveals, model answers, choices, numeric and components with my own Playwright script over HTTP.
4. `docs/FY14_PLAN.md` says the B1M video's spoken content could not be read. The channel's own page (theb1m.com/video/inside-iter-worlds-largest-nuclear-fusion-reactor) publishes the narration as an article; the plan could mention it as the verification source.

## Fixes after review (content hash 46ad737ab67de926)
- Blocking (science 1): "over 300 MW" removed everywhere. Theory now cites iter.org Power supply (node/2751, fetched 1 Nov 2026): 110 MW at the least, up to 620 MW in 30-second peaks, cooling water and cryogenics about 80 %. Comparison: "about 170 MW … far less than ITER's peak demand of 620 MW". Feedbacks, models and criteria updated. unit.json: new iter.org source; Wikipedia source no longer claims 300 MW; teacher.md attribution fixed.
- Blocking (pedagogy 1): learning goal 3 reworded ("compare the fusion gain $Q$ with the electricity a power plant would produce, and explain what else commercial viability needs"). pred-gain replaced: "Suppose ITER had turbines that turn one third of its 500 MW of fusion heat into electricity. Would it send net electricity to the grid?" (yes ~450 / yes ~170 / break-even / no); revealed by theory-gain and the chart.
- Blocking (visual 1): power chart rebuilt (560 wide, all labels 26 units, about 16.6 px at 390; captions in ink, no subscripts); third bar drawn as the range 110–620 MW (solid to 110, pale dashed range to 620, "peaks"). aria-label matches the drawing.
- Polish: "about 400 MW" in Reasonableness; pred-heat options give a short function for each part (balanced lengths, correct not longest); pair-gain criterion "needs a $Q$ far above 1"; given-line equalities braced; tritium Answer reworded ("This is the tritium burned in one 400-second pulse; …"; the `N &=` lines were already aligned); `$\text{D–T}$` in running text; criteria numbers in LaTeX; teacher.md makes the Fuel reading and the tritium task default homework.
- Coordinator note: explorer task wording now says "in the drawing or in the list of parts below the panel" to match the new layout.
- Checks as for the project unit: all OK.
