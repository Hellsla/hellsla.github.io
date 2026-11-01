VERDICT: FAIL
CONTENT-HASH: a5933b8c1ec948d3

Pedagogy review of fy14-fr-cafe (2026-11-01), against the pilot fy14-fr-bonjour. Built and tested in Playwright at 390 px over HTTP.

## Blocking
1. **Prediction 2 (`pred-bill`) is answered before it is asked.**
   - **Where:** the `think` model answer in Think about it opens before the Predict stage. It says "ask for the bill, pay" and "the waiter usually takes the order at the table and we pay at the end", and its criteria list "bill, pay". Learn goal 3 also says "ask for the bill, pay".
   - **Effect:** together these rule out two distractors and name the right answer before the student commits.
   - **Fix:**
     - Remove the bill and paying steps from the `think` model and criteria. For example: "…eat, and then the end of the visit (Prediction 2 asks how it works)".
     - Reframe `pred-bill` so that the goal does not answer it. For example: "You finished ten minutes ago and the waiter has not brought the bill. Why?" Options:
       - in France the bill comes when you ask (correct);
       - the waiter has forgotten you;
       - you must pay at the counter;
       - the café is too busy.
2. **The information gap in the role-play is on everyone's screen.**
   - **Where:** `roleplay-help` shows all four role cards one after another. The customer reads "no more croissants" and "cash only" right under their own card, and the sentence starters even include *je ne mange pas de viande*.
   - **Effect:** round 2 is "the step from supported to independent speaking that the lesson is built for" (teacher.md), and the **Reacts** criterion cannot be met honestly.
   - **Fix:** put each card in its own closed box headed "Customer only" or "Waiter only", or make each card a separately folded activity (`fold`). Move the surprise-specific starters out of the shared box and onto the cards.

## Polish
3. In `check-1`, the correct option is the longest by 4 characters (26 against 20–22). This is harmless; vary it if you edit.
4. The model answer of `roleplay` has the customer order a croissant and then the tart, but the card says *Ask what is in at least one dish … before you order*. It is fine, but it could show the price question before the order.

## Checked
- **Progression:**
  - The unit uses the prices from *Numbers and prices* and the *tu*/*vous* choice from the pilot.
  - Support fades as the brief asks: dialogue read → practise → perform from cues → role cards.
  - The DELF video gives an authentic voice.
  - It is not a translation worksheet.
- **Predictions:**
  - Both lock on commit with no feedback.
  - Both stay hidden through Investigate and open once `theory-steps` and `theory-polite` have been read.
  - The hook and the hero give nothing away.
- **Model answers:** all three `explain` tasks stay closed until the student has written at least 15 characters.
- **Option lengths:** balanced (all within ±30 %, except the short `check-3` phrases).
- **Feedback:** it explains the misconception (*je veux*, *Garçon*, *s'il te plaît*).
- **Prices:** every total in the dialogue, order, model and checks matches the menu.
- **Timing and support:**
  - The 75-minute timing fits.
  - teacher.md has a fast-pair plan and a plan for running out of time.
  - The theory is about 450 words.
- No console errors, no `.katex-error`.

## Shared issues
- None.
