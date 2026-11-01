VERDICT: FAIL
CONTENT-HASH: 974cbb7890e9f925

Pedagogy review of fy14-fusion-debate (2026-11-01). The page was built with `python3 scripts/build.py fy14-fusion-debate`, served on port 8775 and tested in Playwright at 390 px.

## Blocking
1. `inquiry.json` `pred-cost` and `pred-private` are answered in the previous lesson. *Fusion in the energy system* (chapter 8, unit 1), which this unit's `review` question builds on, says in its section *Uncertainties*:
   - "ITER's estimated cost grew from 5.9 billion euros in 2006 to 18–22 billion euros";
   - "USD 4.48 billion of it in the year to July 2026".

   Students therefore recall two numbers they read one lesson earlier. They do not argue a prediction from what they know, so the commit-then-evidence step is lost.

   Fix: replace both with predictions the cards answer for the first time. For example:
   - (a) the public share of the private industry's money: "Of the USD 14.24 billion raised by fusion companies, about how much came from public sources?" (card E: about USD 0.98 billion, about 7 %);
   - (b) where Commonwealth Fusion Systems came from: a spin-off of a publicly funded MIT laboratory (card I).

   Both feed the motion directly. Or move the two current questions to Think about it as a labelled recall ("Remember from the last lesson …") with immediate feedback, and add one new prediction.

## Polish
2. `inquiry.json` `language`: the sentence starters "for every speech" show raw `**Opening:**`, `**Evidence:**` and so on. Markdown is not rendered inside raw HTML, as can be seen at 390 px. Write `<strong>Opening:</strong>`. This is the core phrase bank, so fix it before publishing.
3. `unit.md` Format and `teacher.md` timing: the seven steps add up to 22 minutes (1 + 4 + 4 + 6 + 2 + 3 + 2), but the slot 42–63 is 21 minutes, with no time for changing speakers. Shorten the open floor to 5 minutes, or say "about 22 minutes".
4. Roles: the chair has no script. Add chair phrases to the phrase bank: "I now give the floor to …", "You have 30 seconds left.", "Thank you; time is up." The rebuttal and closing speakers have no preparation task: `prepare` asks only for the opening speech. Add one line to `prepare-help`: "Rebuttal speakers: write two 'Our opponents will say … but …' lines. Closing speakers: choose the one card you will repeat."
5. Winner rule: the format says that the vote decides, while judges also score 0–3 on four criteria. Say what the scores are for: feedback and the grade, not the winner.
6. Option lengths: the correct option is the longest or tied in `pred-cost` (43 against 33–39), `rebuttal` (68 against 57–65), `check-2` (64 against 63) and `check-3` (61 against 60). Shorten `pred-cost` to "About three to four times as high." and `rebuttal` to "We accept the cost grew; however, records keep improving."
7. `sort`: card B and card C are marked only "for", while the prompt says some cards suit both sides. A student who answers "either" for C (activation) is marked wrong. Accept both answers, or make the feedback for "either" acknowledge it.
8. `prepare`: the opposition model is 72 words, below the 100–150 words asked. Lengthen it to match.
9. The optional `video-task` has no sentence starters. Add "The video was made by … in …", "One argument we could use is …" and "A limit of this source is …".

## Checked
- The 75 minutes are workable: roles, order and time limits, a judge's sheet, a plan for a class of 24, fast groups and running out of time are all given. The four criteria (evidence, accuracy, reasoning, language; 0–3) are shown on the page and in `teacher.md`, and the opinion is not graded. There is a phrase bank of six functions with a match and starters for every speech. There is a script for fact-checkers. The debate is evidence-based on both sides, as the brief asks.
- CLIL: there are starters for the opinion, strongest-card, speech and final tasks, group work in fours, a speaking-centred lesson, and a French corner (*à mon avis*, *je (ne) suis (pas) d'accord*). The English is B1–B2.
- In the browser, both predictions lock with no feedback and stay closed until the evidence cards are on screen. Then each opens with the committed option's own feedback.
- All five model answers stay closed with an empty answer and with 5 characters, and open only after an answer of the student's own. There are no console errors, no KaTeX errors and no horizontal scroll at 390 px.

## Shared issues
- `templates/inquiry.js`: a theory reveal opens on the first visible pixel of the section. See the fy14-fusion-society review.
