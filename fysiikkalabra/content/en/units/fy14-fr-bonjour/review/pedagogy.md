VERDICT: FAIL
CONTENT-HASH: 61ad9554da6ac05b

Pedagogy review of fy14-fr-bonjour (2026-11-01), against docs/fy14/writing-guide.md §1, §2, §8 and docs/inquiry.md.

## Blocking

1. **Prediction 1 is shown before the student predicts, and it is not a prediction.** The hero figure, just above the Predict box, shows the student saying "Bonjour, madame !" to an adult at the visitor centre. That is word for word the correct option of `pred-greet` ("Bonjour, madame."), in the same situation. The hook adds that the woman says « Bonjour ! » and the Why line names *bonjour*. Also, `pred-greet` has no `reveal`, so its feedback appears as soon as the student clicks Answer (checked in the browser). The student commits to nothing before the evidence (the listening and the dialogue), and the answer is already on the screen.
   *Fix (either way):* (a) make prediction 1 a case the hero and hook do not answer, for example "It is seven in the evening. At the hotel reception a man of about sixty is at the desk. What do you say first?" (Bonsoir, monsieur / Bonjour, monsieur / Salut ! / Au revoir, monsieur), with `reveal: {"after": "theory-tuvous"}` like `pred-name`; or (b) keep the situation, change the student's speech bubble in the hero (`lessons/units/fy14-fr-bonjour/figures.py`) to "… ?" and add the `reveal`. Option (a) is better, because the Why line and hook still point at *bonjour*.

## Polish

2. `inquiry.json` `notice`: the correct option is 98 characters and the distractors 64–75, and it is the only option that sounds balanced. Shorten it to "They are young and the same age; Claire is an adult at work." In all, the correct option is longest in 3 of 6 choices (`pred-name`, `notice`, `check-3`). Also shorten the correct option of `check-3` to about 45 characters ("*vu-ZET*: the *s* becomes a *z*.").
3. `inquiry.json` `check-1` repeats the situation of `pred-greet` (morning, an adult stranger, *Bonjour, monsieur*), so it only tests recall. The unit teaches that *vous* is also the only form for a group, but no task practises it. Make one check a transfer, for example: "You meet two engineers, Claire and Marc. How do you ask where they come from?" (D'où venez-vous ? / Tu viens d'où ? / D'où viens-tu ? / Je viens de Finlande.)
4. The Why question ("Why can one small word, *bonjour*, decide how a whole conversation in France begins?") is never answered by the student. Add a short `reflect` on `pred-greet` and `pred-name` at the end of the Theory summary, asking for that answer in English in one or two sentences. Or add a criterion to `check-write`.
5. French accuracy and consistency:
   - In `gapfill` line 3 the feedback says "You live *{fr}in{/fr}* a town". The English word *in* is tagged as French, and the rule for *à* is not stated. Write: "With a town you use *{fr}à{/fr}*: *{fr}J'habite à Espoo{/fr}* (I live in Espoo)."
   - In `order` the third hint says "A question about the country comes before a question about the town", but nobody asks about the country (Eetu says it himself). Write: "Léa reacts to the country, then asks about the town."
   - In `extension` (say) the tip "*{fr}il{/fr}* (he) is said like Finnish *{fr}il{/fr}*" makes no sense, because Finnish has no word *il*. Write: "*{fr}il{/fr}*: as written, *il*."
   - `unit.md` Summary table and the `listen` list: the *tu* questions use inversion (*Parles-tu anglais ?*, *Où habites-tu ?*), but Léa uses intonation (*Tu parles français ?*). For beginners in the informal register, intonation is more natural and simpler: give *Tu parles anglais ?* and *Tu habites où ?* in the table, and mention inversion as the more careful form.
6. `unit.md` line 3: the Why line has a nested `<span lang="fr"><span lang="fr">bonjour</span></span>`. Remove the inner span. This is also for the visual reviewer.
7. `teacher.md` "Timing": 70–75 minutes for three checks and the written introduction is too short. Either give the check stage 8–10 minutes (take the time from Investigate: listen, which has 23 phrases and can drop the second, slow, listening of each phrase) or say directly that `check-write` is homework.
8. `inquiry.json` `pred-name` prompt: "You will find out in the theory summary" is true for the feedback, but the listening and the dialogue show the answer first. Write: "Commit now; the listening, the dialogue and the theory summary will show you."

## Checked, no finding
- The sequence is adapted well to a language unit: phenomenon → predictions → investigate a phrase list, a dialogue and an ordering task → theory (tu/vous, sounds for Finnish speakers, summary table) → apply (gap fill, match, role-play) → check.
- `pred-name` commits without feedback and opens after the theory section.
- The ordering task is shuffled on load. An empty `explain` keeps its model answer closed. No console errors (Playwright, 390 px).
- The level suits complete beginners: A1 French with English instructions at B1. The French is accurate (dialogue, phrases, liaison and pronunciation tips aimed at Finnish speakers).
- The role-play has a word bank, sentence starters, two registers, a model and criteria. These are the same criteria as in `teacher.md`, with peer assessment.
- The feedback names the misconception (country versus nationality, *et tu*, register, time of day, voiceless *s* in liaison).
- `teacher.md` is practical: timing, organisation, role-play running, formative assessment, common difficulties, follow-up, and the real ITER visit rules kept apart from the scenario.
