VERDICT: DONE

# fy14-fr-lire: developer report (2026-11-01)

## Files
- `unit.json`: FY14, chapter 10, order 5, kind french, 75 min, 9 sources.
- `unit.md`: Why line, hero, intro; *Why you understand more than you think* (international vocabulary, Swedish and Finnish loans, five strategies), *False friends* (table), *Summary* (strategy → example).
- `inquiry.json`: Think about it (hook in a café in Manosque, starters, pair `explain` with five look-alike words); Predict (how much you will understand → `theory-why`; *actuel* → `theory-false`); Investigate (step 1 skim the **original** news text, *What is the text about?*; step 2 look-alike `match` with English/Swedish/Finnish relatives in the feedback; step 3 true / false / not in the text `match`); Theory; `reflect`; Apply (sorting `match`: look-alike, false friend, context; word bank and starters; English summary `explain`; a second original text about the Manosque school with a transfer `explain`; optional real French news); Check (*actuellement*, *milliard*, an unknown word; a written explanation of three strategies).
- `teacher.md`; `lessons/units/fy14-fr-lire/figures.py`: hero (an open newspaper on a café table, lines without words, highlighted look-alikes, a magnifying glass; no text).

## The texts
Both texts were written for the unit (A2–B1, about 190 and 70 words); no sentence is copied from the CEA, AFP, EUROfusion or ITER. The page says they were written for the course and when the facts were checked.

## Facts verified (WebFetch, 2026-11-01)
- EUROfusion (CEA news) and Connaissance des énergies (AFP, 18 February 2025): WEST, CEA Cadarache, 1,337 s on 12 February 2025, over 22 minutes, 25 % above the record set in China weeks before, a plasma of several tens of millions of degrees.
- iter.org *What will ITER do?*: 500 MW of fusion power from 50 MW of input heating. en.wikipedia ITER: seven members; research operation 2034 (2024 baseline). ITER press release 29 July 2026: sixth of nine sector modules installed on 28 July 2026, almost six months ahead of schedule.
- iter.org *ITER France*: PACA International School in Manosque from 2007, 130 pupils aged 3–18, six language sections and a European section, France's commitment to bilingual education.
- fr.wikipedia *Nombres en français*: long scale (milliard 10^9, billion 10^12).
- Check 1 uses "about 5,000 people on site" (iter.org *Facts and figures*, 2026, cited in fy14-iter-project).
- Manosque–ITER: 15 km in a straight line (computed from coordinates), written "à une quinzaine de kilomètres".

## Open questions
- The record may be beaten after November 2026; the text dates it (12 February 2025) and teacher.md asks the teacher to check.
- The etymologies used (Swedish *trottoar*, *paraply*, *byrå* from French; Finnish *insinööri* via Swedish *ingenjör* from *ingénieur*; English *battle*/*battery* related to *battre*) are standard dictionary etymologies, not cited individually.

## Checks (2026-11-01)
`python3 scripts/units.py check` (no errors for this unit) · `python3 scripts/build.py fy14-fr-lire` → `preview/en/fy14-fr-lire.html` · `check_layout.py --width 360` and `--width 1280` OK · `screenshot.py` run and the captures looked at (hero, every stage at 390 and 1280, the components). Playwright (scripts/_browser.launch) at 390 px: both predictions lock on commit with no feedback, stay closed while Investigate is scrolled, and open with the committed option's feedback when their theory section is on screen; every plain choice gives feedback for a wrong and a right option; every model answer stays closed until 15+ characters are written; every match, gap fill and order component answered right and checked; dialogue support steps switch; all components load; no console errors, no raw `$`, no `.katex-error`, no literal `{fr}` or stray `*`.

## Shared issues (not edited)
- `templates/site.css` line 326: below 48 rem `th,td{hyphens:auto}` hyphenates French words inside table cells (e.g. *choco-lat*, *sand-wich* in a first version of the café menu). Worked around in the units: hyphenated French words in `lang="fr"` spans are wrapped in `.nobr`, and wide tables were turned into two columns. Proposed fix: `[lang=fr] td, td[lang=fr], table[lang=fr] td{hyphens:manual}`.
- `templates/inquiry.js` reflection list: the quoted prediction prompts end with "Commit now; the theory summary will show you", which reads oddly after the reveal (already noted in the pilot reviews).

## Fixes after review (2026-11-01)
- Article: the record is attributed to the CEA ("Selon le CEA, ils ont battu un record mondial de durée : c'est 25 % de plus que le record du tokamak chinois EAST, établi quelques semaines plus tôt"); the summary model and the true/false feedback follow.
- Opening question is open ("How much of a French news text about fusion can you understand after a few weeks of French?"); learn goal 1 and the back-to-predictions prompt reworded; "about 200 words".
- *battre* feedback ("are related to"); second text: "s'était engagée à offrir une scolarité bilingue à ces enfants"; a new read-aloud `say` task with four sentences from the article.
- Visual: word endings use non-breaking hyphens (U+2011) in theory, table and feedback; no-break spaces between numbers and units; `.nobr` on *États-Unis*, *Saint-Paul-lez-Durance*, *Bouches-du-Rhône*; *vrai / faux / pas dans le texte* tagged French.
- Checks rerun: `units.py check` (29 units ok), build, `check_layout` 360/1280 OK, screenshots, Playwright (all tasks, wrong-then-right component answers) OK.
