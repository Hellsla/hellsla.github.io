VERDICT: DONE

# fy14-fr-cafe: developer report (2026-11-01)

## Files
- `unit.json`: FY14, chapter 10, order 3, kind french, 75 min, 6 sources, 2 videos in `media`.
- `unit.md`: Why line, hero, intro; *At a French café: what happens when* (greet, order, ask, bill, pay and thank; coffee words), *Polite ordering* (vous with the waiter, tu with the friend, je voudrais vs je veux; `say` of three key phrases), *Summary* (situation → phrase).
- `inquiry.json`: Think about it (hook at a café terrace, starters, pair `explain` on the steps of a café visit); Predict (first words → `theory-polite`; getting the bill → `theory-steps`); Investigate (the invented menu as an HTML table, `say` of 13 phrases, a three-step `dialogue` Camille/Aino, the `video` R-8NbYM1-ws with four note points, an `order` task with Eetu, Léa and the waiter, *What did you notice?* on tu/vous); Theory; `reflect`; Apply (`gapfill`, a waiter-phrase `match`, the role-play in three rounds: from cues → secret role cards for customer and waiter → swapped cards, word bank, starters, `explain` with model and criteria; optional Easy French video MBK7K1Xw3Lc); Check (asking a price, tu with a friend, *Gardez la monnaie*, a written order with vous/tu).
- `teacher.md`, `lessons/units/fy14-fr-cafe/figures.py` (hero: café terrace, two seated faceless students, a waiter with a tray; no text).

The role-play is the core: a supported dialogue (read → practise → perform) leads to free speaking with role cards that give each partner information the other lacks (no croissants, vegetarian, budget, cash only). There is no long translation worksheet: the gap fill has 8 lines and the match 8 items.

## Facts verified (WebFetch, 2026-11-01)
- fr.wikipedia *Pourboire*: service charge included in café and restaurant prices by law; a tip is neither required nor expected; rounding up is common.
- Larousse FR–EN *café*: café crème = coffee with cream; petit noir = a small cup of strong black coffee; café au lait = coffee with milk. fr.wikipedia *Expresso*: noisette = espresso with a little milk foam; allongé = more water.
- fr.wikipedia *Euro* (centime); *Tutoiement et vouvoiement* (vous with a waiter, tu among young people).
- Videos: R-8NbYM1-ws *Commander au café en français. Dialogue simulé pour la production orale du DELF A1. English subtitles*, La prof Elisabeth, 29 January 2022, 2:44, description warns of a spelling mistake in *eau gazeuse*. MBK7K1Xw3Lc *How to Order Coffee in a French Café | Super Easy French 75*, Easy French (oEmbed only; the page did not load, so no date or length). The spoken content of neither could be played; tasks are open note-taking tasks and teacher.md lists what to check.

## Numbers computed
Dialogue: 3,90 + 5,50 = 9,40 €. Order task: 2 · 3,80 + 8,90 + 1,40 = 17,90 €. Role-play model: 3,80 + 8,90 = 12,70 € (over the 10 € budget), 3,80 + 4,50 = 8,30 €. Check 4 model: 3,50 + 3,00 + 7,50 = 14,00 €. Check 3: 10 − 9,40 = 0,60 €.

## Open questions
- Two cultural statements are common knowledge but have no single checked source: that the waiter usually brings the bill only when asked, and that *Garçon !* now sounds rude. A pedagogy or science reviewer may want a source or softer wording ("usually", "today" are already there).
- The menu prices are invented and said to be invented; no claim is made about real prices.

## Checks (2026-11-01)
`python3 scripts/units.py check` (no errors for this unit) · `python3 scripts/build.py fy14-fr-cafe` → `preview/en/fy14-fr-cafe.html` · `check_layout.py --width 360` and `--width 1280` OK · `screenshot.py` run and the captures looked at (hero, every stage at 390 and 1280, the components). Playwright (scripts/_browser.launch) at 390 px: both predictions lock on commit with no feedback, stay closed while Investigate is scrolled, and open with the committed option's feedback when their theory section is on screen; every plain choice gives feedback for a wrong and a right option; every model answer stays closed until 15+ characters are written; every match, gap fill and order component answered right and checked; dialogue support steps switch; all components load; no console errors, no raw `$`, no `.katex-error`, no literal `{fr}` or stray `*`.

## Shared issues (not edited)
- `templates/site.css` line 326: below 48 rem `th,td{hyphens:auto}` hyphenates French words inside table cells (e.g. *choco-lat*, *sand-wich* in a first version of the café menu). Worked around in the units: hyphenated French words in `lang="fr"` spans are wrapped in `.nobr`, and wide tables were turned into two columns. Proposed fix: `[lang=fr] td, td[lang=fr], table[lang=fr] td{hyphens:manual}`.
- `templates/inquiry.js` reflection list: the quoted prediction prompts end with "Commit now; the theory summary will show you", which reads oddly after the reveal (already noted in the pilot reviews).

## Fixes after review (2026-11-01)
- *Garçon !* softened (old-fashioned, many waiters find it rude) in the theory and in the pred-order feedback; "sit as long as you like" replaced by "the waiter usually does not hurry you, and the bill often comes only when you ask for it".
- The bill no longer appears in the think model, criteria or learn goal 3; pred-bill reframed ("finished ten minutes ago, the waiter has not brought the bill"), with a new distractor (go to the kitchen) and the correct option no longer the longest.
- Role cards are four separate `fold` activities (*Customer only* / *Waiter only*), each closed until opened; the surprise starters (*je ne mange pas de viande*, *il n'y a plus de …*) moved onto the cards.
- Gap fill distractors *à la* and *de rien*; the *prendre* tip; check-1 options balanced; *tu*, *vous* and the source note tagged French.
- Checks rerun: `units.py check` (29 units ok), build, `check_layout` 360/1280 OK, screenshots, Playwright (all tasks, wrong-then-right component answers) OK.
