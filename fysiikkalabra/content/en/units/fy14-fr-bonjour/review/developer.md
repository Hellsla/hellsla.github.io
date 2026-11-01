VERDICT: DONE

# fy14-fr-bonjour: developer report (2026-11-01)

## Files
- `content/en/units/fy14-fr-bonjour/unit.json`: FY14, chapter 10, order 1, kind french, subjects french + english, 75 min, no sim, 9 sources
- `content/en/units/fy14-fr-bonjour/unit.md`: the Why question, the hero, a short scenario intro, the sections *Tu or vous?*, *Sounds for Finnish speakers* (with a `say` table of the four sound points) and *Summary* (a tu/vous table)
- `content/en/units/fy14-fr-bonjour/inquiry.json`: the activities by stage:
  - Think about it: a hook and a pair `explain`.
  - Predict: two `choice` tasks. The second waits for *Tu or vous?* before it shows feedback.
  - Investigate: a `say` table of 23 phrases, a `dialogue` at the ITER visitor centre (A Aino, B Claire, three support levels), an `order` task for an evening conversation, and a `choice` on what the student noticed.
  - Theory summary: three theory sections.
  - Apply: a `gapfill` with 8 lines, a `match` with 10 items, the role-play (a word bank and sentence starters, then an `explain` with a model dialogue and the three speaking criteria), and an optional extension on *il / elle* (`say` + `gapfill`).
  - Check: three `choice` checks (Salut to a professor, finlandais/finlandaise, the liaison in *vous êtes*) and a written self-introduction (`explain`).
- `content/en/units/fy14-fr-bonjour/teacher.md`: timing, pairs, running the role-play, the speaking criteria, common difficulties and the follow-up
- `lessons/units/fy14-fr-bonjour/figures.py`: the hero. It shows a sunny Provence scene with a generic visitor centre (no sign or logo), cypresses and lavender. Two faceless `herolib.person` figures stand under speech bubbles with `\text{}` labels.

French spans carry `lang="fr"`, including the French in italics inside the English text and, in component data, `{fr}…{/fr}`. French text uses a no-break space before ? ! : ; and inside « ».

## Facts verified (WebFetch, 2026-11-01)
- **ITER (Wikipedia):** ITER is built near the Cadarache research centre. Its headquarters are in Saint-Paul-lez-Durance. It has seven members.
- **iter.org:** the home page lists the seven members. The *Visiting ITER* page names a Visitor Centre with a belvedere. It places the site about 35 km north of Aix-en-Provence. Visitors must be at least 16, and 16–17-year-olds need a parent or guardian (stated in teacher.md).
- **fr.wikipedia, Saint-Paul-lez-Durance:** the commune is in Bouches-du-Rhône (Provence-Alpes-Côte d'Azur) and hosts both Cadarache and ITER.
- **fr.wikipedia, Tutoiement et vouvoiement en français:** *vous* is used with strangers and *tu* among young people. People move from *vous* to *tu* easily but rarely back. *Tu* is common in scientific and technical work.
- **Wiktionnaire:** *salut* is familiar and means both hello and goodbye. *Bonsoir* is used in the evening, both when meeting and when leaving.
- **en.wikipedia, Liaison (French):** liaison between a pronoun and its verb is compulsory. **French phonology:** the r is uvular; French has nasal vowels.

## Doubts and open questions
- The guide says people are never shown in generated images, but the brief asked for two people meeting. I drew the faceless `herolib.person` figures that other heroes already use. A reviewer may want something else.
- The pronunciation hints are rough Finnish-based spellings (e.g. *mösjöö*, *bõ-jour*, *vu-ZET*), not IPA. They are approximations on purpose.
- The browser voice may read « » or the ‿ sign oddly. The phrases a student can play contain neither.
- Shared problems I did not fix (outside my folders):
  - At 1280 px, `check_layout` FAILs only because the shared tail is too wide: the *Sources* lead line, and the teacher notes when they are open, exceed 44 rem.
  - At widths over 48 rem, the `say` tables keep site.css `td{white-space:nowrap}` and `table{display:block}` with separate thead/tbody tables. The header and the columns no longer line up, and the long meanings run past the box and need sideways scrolling.
  - Plus Jakarta Sans has no italic face, so italics are slanted by the browser and the space after an italic word looks lost ("*Bon* is" reads as "Bonis").

## Fixes after review (2026-11-01)

Content hash after the fixes: edd56ca7362d855c. Files: `unit.md`, `inquiry.json`, `teacher.md`, `lessons/units/fy14-fr-bonjour/figures.py` (hero rewritten).

### Pedagogy
1. (Blocking) `pred-greet` is now the evening case: seven in the evening, hotel reception, a man of about sixty (Bonsoir, monsieur ✓ / Bonjour, monsieur / Salut ! Ça va ? / Au revoir, monsieur; 15–20 characters), with `reveal: {"after": "theory-tuvous"}`. The hero has no words (empty bubbles with three dots, aria-label updated), so neither the hero, the hook nor the Why line answers it. Checked in the browser: it locks on commit and its feedback opens only when *Tu or vous?* is on screen.
2. `notice` correct option: "They are young and the same age; Claire is an adult at work." (60 vs 60–73). `check-3` options 31–39 characters, correct "*vu-ZÈT*: the *s* of *vous* becomes a *z*.". `pred-name` options balanced (22–28: *Comment je m'appelle ?* and *Comment allez-vous, madame ?* replace the shorter distractors).
3. `check-1` is now a transfer to *vous* for a group: two engineers, "D'où venez-vous ?" vs *Tu viens d'où ?* / *D'où viens-tu ?* / *Je viens de Finlande.*
4. New `back-to-predictions` reflect after the summary on `pred-greet` and `pred-name`, asking for the answer to the Why question in one or two English sentences.
5. Gapfill de/à feedback states both rules; order hint 3 "Eetu says where he comes from; then Léa reacts and asks about his town."; *il* tip "said as it is written in Finnish: *il*"; *tu* questions with intonation (*Tu parles anglais ?*, *Tu habites où ?*) in the table, the listen list, the order task, the match and the role-play model, and the summary text names inversion as the more careful form.
6. Nested span in the Why line removed.
7. teacher.md timing: listening 12–21 min without the second slow listening; Check 65–75 min (three checks about 5 min, check 4 finished as homework); a *Running out of time* plan added.
8. `pred-name` prompt: "Commit now; the listening, the dialogue and the theory summary will show you."
Also: sentence starters (`think-help`) for the Think about it pair task.

### Science
1. Intro: "under construction (as of November 2026)". 2. Hook: "a staff badge". 3. Summary *vous* column: *Je vais bien, merci.* 4. Order hint rewritten (above). 5. Gapfill *toi*: "*Tu* is only the subject of a verb …; after *et* use *toi*." 6. `{fr}` removed from English *in*. 7. Classmate gapfill: "For verbs like *parler* and *habiter* …". 8. "rarely a mistake".

### Visual
1. Hero: no text (empty bubbles with three dots).
2. Not touched (fixed in units.css by the coordinator).
3. One respelling convention in unit.md and every `say` tip (and in fy14-photoelectric): italic, stressed syllable in capitals, nasal *õ/ã/ẽ*, Finnish letters (*y*, *ö*, *ž*, *š*), never `lang="fr"`; explained once in *Sounds for Finnish speakers* and in the listen lead. Browser check: no element with `lang="fr"` contains a respelling.
4. *in* untagged; nested span removed; *il* tip; check-2 "lower-case letter".
5. Shared (see below).
6. Worked around in the unit: the gap is now `[[appelez-vous|appelle-vous|appelles-vous]]`, so no hyphen follows the select (checked at 390).
7. "Je m'appelle …" uses a no-break space before the ellipsis in the summary table.

### Checks
`units.py check` (no errors for this unit), `build.py fy14-fr-bonjour`, `check_layout` 360 OK (the summary table scrolls) and 1280 OK, `screenshot.py` re-run and looked at (hero, sounds, summary table, gapfill). Playwright at 390 and 1280: both predictions lock with no feedback, stay closed through Investigate and open when *Tu or vous?* scrolls into view; every check shows feedback after a wrong answer; check 4's model stays closed before writing; no console errors, no raw `$`, no `.katex-error`, no literal `*` or `{fr}`.

### Shared issues (not edited)
- `templates/site.css` line 397 `.intro-media>p{margin:0}`: the opening paragraph touches the hero; use `margin-top:.8rem` (visual 5).
- `assets/units/fy14/fx/gapfill.js`: keep a select and the text that follows it up to the next space in one `white-space:nowrap` span (visual 6; worked around here).
- `templates/inquiry.js` reflection list: `.scenario` and `.ask` are joined without a space ("…never met.What do you say first?").
