VERDICT: FAIL
CONTENT-HASH: 974cbb7890e9f925

## Blocking
1. [Major] `inquiry.json`, the box "Sentence starters for every speech" (`selita-390-3`, `contact-4` #44 at 1280). All six labels show raw Markdown: "\*\*Opening:\*\* Madam / Mr Chair …", "\*\*Evidence:\*\* …" and so on. Inside raw HTML, Markdown is not converted (writing guide §1). This is the main language support for every speech, and the asterisks make it look broken. Fix: write `<strong>Opening:</strong>` and the same for Evidence, Rebuttal, Conceding, Question and Closing.

## Polish
1. [Minor] Roles table at 390 (`selita-390-1`). Automatic hyphenation gives "proposi-tion", "opposi-tion" and "fact-check-ers", and the Task column wraps into narrow 3–4-line cells. Fix: shorten the "Who" cells ("1 student / teacher", "3", "2", "the rest"), or see the shared table note in fy14-fusion-society.
2. [Minor] Judging paragraph (`selita-390-2`). "The judges score each team … The team that changes more votes … wins" leaves open what the scores decide. Fix: "The scores give each team feedback; the team that changes more votes wins."
3. [Minor] For science/editorial: the model answer of "Discuss: the strongest card for each side" calls ITER's cost growth "also a result, not a guess". Cost estimates are reported figures, not measured results. Fix: "a reported fact, not a forecast".
4. [Minor] French tip for *Je suis d'accord*: "žö svi". The unit's own rule is "u = Finnish y", so *suis* is closer to "syi". Use "žö SYI da-KOR" in both *je suis* tips. In the sentence starters at 390, a lone "…" wraps to its own line ("That is a fair point, but / …"). Join it with a no-break space.
5. [Minor] Predictions (`stage-ennusta`). After an answer, the page says "Feedback appears when you have read the theory section", but the reveal comes from the evidence cards in *Investigate*. This is a shared template string (Shared issues). Until it is fixed, the lead could say "after the evidence cards".

## Checked
- Fresh captures for this hash: contact-1, 2 and 4, top/intro at 390 and 1280 (the hero has no text and faceless figures), selita-390-2 and 3, the say component in fx-4 (via contact-2).
- I also looked at the video card at 390 and 1280 and at every stage at 1280 through the contact sheets.
- Opened myself in Playwright at 390 and 1280: all 5 model answers after writing (both opening-speech models and the video-source answer), and all 7 choices with their feedback (prediction locks saved).
- The unit has no worked example, numeric task or second figure. No `.katex-error`, no raw `$`, no overflow and no console errors.
- I scanned the rendered text for raw markup and found only the box above. French text has `lang="fr"` (13 spans).
- The hash was unchanged at the end.

## Scores
illustrations 4 · typography 4 · English/French 4 · accessibility 4

## Shared issues
- `templates/inquiry.js` §1: the pending text of a prediction always names "the theory section", even when the reveal is a `theory` activity in *Investigate* (the evidence cards). It should name the linked activity or say "when you have read the evidence".
- The table hyphenation at 390, as noted in fy14-fusion-society.
