VERDICT: DONE

# fy14-fr-cadarache: developer report (2026-11-01)

## Files
- `unit.json`: FY14, chapter 10, order 4, kind french, 75 min, 12 sources, 1 video in `media`.
- `unit.md`: Why line, hero, intro; *Science in France: CEA, CNRS and Cadarache*; *Cadarache, ITER and Provence* (with a to-scale regional map); *Asking for help and finding the way* (four-part polite request, a direction table, French and Finnish floor numbering, the building plan, a `say` of three direction phrases); *Summary* (situation → phrase; de / d' / du / des with countries).
- `inquiry.json`: Think about it (hook at the research building, starters, pair `explain`; optional warm-up video TcBelFXMpOE); Predict (who runs Cadarache → `theory-science`; asking a stranger for help → `theory-help`); Investigate (`say` of 15 phrases, a three-step reception `dialogue` Marc/Aino, an `order` task with a physicist from India, *What did you notice?*); Theory; `reflect`; Apply (directions `match` on the plan, a countries and help `gapfill`, the role-play with four secret role cards in two rounds, word bank, starters, `explain` with model and criteria; optional short cultural investigation); Check (du Japon, premier étage, ITER vs Cadarache, a written message to the researcher).
- `teacher.md`; `lessons/units/fy14-fr-cadarache/figures.py`: hero (a research building in the garrigue, a signpost with blank boards, two faceless figures; no text), `map` (to scale: equirectangular at 43.6° N, 7 px/km, coast, Étang de Berre, Durance, Rhône, five towns, ITER star, 20 km scale bar), `plan` (invented building: ground floor and first floor). Labels are 30 units in an 800-wide figure (about 14.6 px at 390).

## Facts verified (WebFetch, 2026-11-01)
- en.wikipedia CEA: full name, 18 October 1945 under de Gaulle, renamed in March 2010, slightly over 21,000 staff, ten centres.
- en.wikipedia CNRS: 19 October 1939, largest public research body in Europe, about 33,000 staff (2021), fundamental research.
- en.wikipedia *Cadarache*: CEA centre, research since 1959, over 5,000 people, energy research (its ITER schedule is outdated and was not used).
- en.wikipedia *WEST* and EUROfusion (CEA news): Tore Supra 1988–2010, WEST first plasma December 2016, 1,337 s on 12 February 2025, 25 % above the record set in China weeks before. The text says "a world record for a tokamak at the time".
- iter.org node 31973 (7 July 2025): 28 June 2005 in Moscow, Cadarache chosen over Rokkasho. en.wikipedia ITER: Agreement signed in Paris on 21 November 2006; seven members; 2024 baseline (research operation 2034). iter.org *ITER France*: CEA Cadarache is host and neighbour; PACA International School in Manosque from 2007. iter.org *Visiting ITER*: about 35 km north of Aix-en-Provence. fr.wikipedia *Saint-Paul-lez-Durance*: Bouches-du-Rhône, PACA.
- en.wikipedia *Storey*: rez-de-chaussée and premier étage in France; Finland counts the entrance level as the first floor.
- Video TcBelFXMpOE *Saluer - Prendre congé*, Alexandra Siopi, 19 November 2014 (no description or length readable); optional, with a note-taking task only.

## Numbers computed
Map: positions from latitude and longitude (ITER 43.704° N 5.765° E from `facilities.json`; Marseille, Aix, Manosque, Avignon, Toulon, coast and rivers approximate). Great-circle distances: ITER–Aix 32 km (iter.org: about 35 km), ITER–Manosque 15 km, ITER–Marseille 55 km in a straight line.

## Open questions
- The map's coast and rivers are simplified polylines from approximate coordinates; it is labelled as simplified.
- *Bangalore* (the invented physicist's home town) is the established French name; *Bengaluru* is the official English one.

## Checks (2026-11-01)
`python3 scripts/units.py check` (no errors for this unit) · `python3 scripts/build.py fy14-fr-cadarache` → `preview/en/fy14-fr-cadarache.html` · `check_layout.py --width 360` and `--width 1280` OK · `screenshot.py` run and the captures looked at (hero, every stage at 390 and 1280, the components). Playwright (scripts/_browser.launch) at 390 px: both predictions lock on commit with no feedback, stay closed while Investigate is scrolled, and open with the committed option's feedback when their theory section is on screen; every plain choice gives feedback for a wrong and a right option; every model answer stays closed until 15+ characters are written; every match, gap fill and order component answered right and checked; dialogue support steps switch; all components load; no console errors, no raw `$`, no `.katex-error`, no literal `{fr}` or stray `*`.

## Shared issues (not edited)
- `templates/site.css` line 326: below 48 rem `th,td{hyphens:auto}` hyphenates French words inside table cells (e.g. *choco-lat*, *sand-wich* in a first version of the café menu). Worked around in the units: hyphenated French words in `lang="fr"` spans are wrapped in `.nobr`, and wide tables were turned into two columns. Proposed fix: `[lang=fr] td, td[lang=fr], table[lang=fr] td{hyphens:manual}`.
- `templates/inquiry.js` reflection list: the quoted prediction prompts end with "Commit now; the theory summary will show you", which reads oddly after the reveal (already noted in the pilot reviews).

## Fixes after review (2026-11-01)
- WEST: "1,337 seconds (over 22 minutes), which the CEA called a world record for plasma duration: 25 % longer than China's EAST tokamak had managed a few weeks before" (TRIAM-1M held a 5 h plasma in 2003).
- CEA: nine centres (cea.fr, 2026), 21,763 employees (2023) in the source notes; the iter.org 2024 baseline PDF cited; EDF feedback corrected (EDF has its own R&D labs).
- pred-who asks for a reason from the names; role cards are four `fold` activities (*Visitor only*, *Receptionist only*, *Researcher only*); gap distractor *gentils*.
- Visual: plan labels 32 units (about 14.3 px at 390), *le couloir* in ink; map: *le Rhône* beside its line, *la Durance* above the river's middle, the lagoon labelled *l'étang de Berre* and added to the aria-label; *rez-de-chaussée* in the source note tagged.
- Checks rerun: `units.py check` (29 units ok), build, `check_layout` 360/1280 OK, screenshots, Playwright (all tasks, wrong-then-right component answers) OK.
