VERDICT: DONE

# fy14-fr-nombres: developer report (2026-11-01)

## Files
- `content/en/units/fy14-fr-nombres/unit.json`: FY14, chapter 10, order 2, kind french, 75 min, 8 sources, 2 videos in `media`.
- `unit.md`: Why line (97), hero, intro; sections *Counting to 100* (table 70–100, Belgian/Swiss forms), *Prices in euros* (decimal comma, € after the number, centimes, a `say` table of five price questions), *Sounds of the numbers* (final consonants, vingt/cent, liaison with euros, final stress, `say`), *Summary* (two-column table).
- `inquiry.json`: Think about it (hook at the market in Aix, sentence starters, pair `explain` on how numbers are built); Predict (70 in France → `theory-count`; reading 2,50 € → `theory-prices`); Investigate (`say` 0–100, the `video` AvHO3T7cyNI from 2:31, a `match` of number words to digits, *What did you notice?*); Theory; `reflect`; Apply (listening in pairs: two `say` tables + two `match` lists, a receipt `gapfill`, a phrase `match`, the market role-play with word bank, starters and an `explain` with model and criteria; optional extensions: phone numbers in pairs, vowel combinations video O68Ql8Ux4iE); Check (three choices: 97 € by ear, writing 2,80 €, *six euros* liaison; a written text message with model and criteria).
- `teacher.md`: what to check in the videos, 75-minute timing, fast pairs, running out of time, organisation, assessment, difficulties, follow-up.
- `lessons/units/fy14-fr-nombres/figures.py`: hero (a Provençal market stall with blank price tags, faceless seller and student; no text).

## Facts verified (WebFetch, 2026-11-01)
- fr.wikipedia *Nombres en français*: soixante-dix / quatre-vingts / quatre-vingt-dix in France; septante, nonante in Belgium and Switzerland; huitante in Vaud, Valais, Fribourg; *et* in 21…71 but not in 81, 91; quatre-vingts with *s* only when nothing follows.
- fr.wikipedia *Euro*: in France *centime*, not *cent*. fr.wikipedia *Séparateur décimal*: decimal comma (NF X 02-003).
- en.wikipedia *Telephone numbers in France*: ten digits, stated as five pairs; 06 and 07 mobile.
- iter.org *Visiting ITER*: about 35 km north of Aix-en-Provence.
- Videos (oEmbed + page metadata): AvHO3T7cyNI *French NUMBERS 1-100*, Juancker´s Languages, 21 August 2023, chapters 1–10 … 91–100 (61–70 at 2:31, 91–100 at 3:55); O68Ql8Ux4iE *French Pronunciation: French vowel combinations*, Learn French, 19 October 2022 (description: six vowels; combinations change the sound). The spoken content could not be played; tasks use only the chapters and the description, and teacher.md lists what to check.

## Numbers computed
Receipt: 1,80 + 1,20 + 3,70 + 4,95 + 9,90 = 21,55 €. Market model: 4,90 + 1,20 = 6,10 €. Check 4 model: 3,70 + 4,95 = 8,65 €. Every price in words was checked against its digits.

## Open questions
- Respellings follow the pilot convention (Finnish letters, capitals for stress, õ/ã/ẽ). *un* is written *ẽ*, as most speakers in France merge it with *in*.
- The browser voice may read *quatre-vingts* in prices slightly differently in different browsers; the teacher's voice is named as the main model.
- The video length "about 4.5 min" is inferred from the last chapter starting at 3:55; YouTube did not give the duration.

## Checks (2026-11-01)
`python3 scripts/units.py check` (no errors for this unit) · `python3 scripts/build.py fy14-fr-nombres` → `preview/en/fy14-fr-nombres.html` · `check_layout.py --width 360` and `--width 1280` OK · `screenshot.py` run and the captures looked at (hero, every stage at 390 and 1280, the components). Playwright (scripts/_browser.launch) at 390 px: both predictions lock on commit with no feedback, stay closed while Investigate is scrolled, and open with the committed option's feedback when their theory section is on screen; every plain choice gives feedback for a wrong and a right option; every model answer stays closed until 15+ characters are written; every match, gap fill and order component answered right and checked; dialogue support steps switch; all components load; no console errors, no raw `$`, no `.katex-error`, no literal `{fr}` or stray `*`.

## Shared issues (not edited)
- `templates/site.css` line 326: below 48 rem `th,td{hyphens:auto}` hyphenates French words inside table cells (e.g. *choco-lat*, *sand-wich* in a first version of the café menu). Worked around in the units: hyphenated French words in `lang="fr"` spans are wrapped in `.nobr`, and wide tables were turned into two columns. Proposed fix: `[lang=fr] td, td[lang=fr], table[lang=fr] td{hyphens:manual}`.
- `assets/units/fy14/fx/say.js`: no listening mode that hides the French text. A dictation (hear a price, write it) is therefore done in pairs: one partner plays the line, the other does not look. Proposed: an optional `"hide": true` that shows only *Listen* buttons and reveals the text on demand.
- `templates/inquiry.js` reflection list: the quoted prediction prompts end with "Commit now; the theory summary will show you", which reads oddly after the reveal (already noted in the pilot reviews).
