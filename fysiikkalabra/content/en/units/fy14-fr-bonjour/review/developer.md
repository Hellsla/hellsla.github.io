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
