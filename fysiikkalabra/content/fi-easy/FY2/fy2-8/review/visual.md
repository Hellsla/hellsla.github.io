VERDICT: PASS
CONTENT-HASH: 0820bc39ae57687e

## Blocking
(none)

## Polish
- [Minor] whole page (pre-existing, outside this delta) — other inline formulas still break at 390 px, e.g. `\text{C} + \text{O}_2 \rightarrow \text{CO}_2`; templates/lesson.html glues only pieces of at most 14 characters, so a longer formula can break (teacher's rule: never) — brace each as one group `${...}$`, as done in fy7-2 L1-02, or show it as a display row.
- [Minor] inquiry.json Tutki, Mallin oletukset (uncommitted edit) — the parenthesis after $-18\,{}^\circ\text{C}$ now holds a whole definition with a semicolon ("… eli lämpötila, jonka malli antaa, kun Maa lähettää … Auringolta; ei tarkka ennuste"), long for fi-easy — make it sentences: "… noin $-18\,{}^\circ\text{C}$. Se on yksinkertaisen säteilytasapainomallin efektiivinen säteilylämpötila. Malli olettaa, että Maa lähettää avaruuteen yhtä paljon energiaa kuin se saa Auringolta. Luku ei ole tarkka ennuste."

## Checked
- delta review of 2c31ff041: Ennusta feedback, the self-assessment criterion and the lesson paragraph (new bold terms **säteilytasapainomalli**, **efektiivinen säteilylämpötila**); diff read. The hash changed during the review (uncommitted inquiry.json edit: Ennusta feedback and Mallin oletukset now define the radiation-balance model), so the review was redone on it: `screenshot.py fy2-8 --lang fi-easy --if-stale` retaken after the edit.
- Own 390 px element captures of each changed block opened (scratchpad caps/fi-easy-fy2-8-*-390.png, incl. the edited feedback and Mallin oletukset box): text wraps cleanly, KaTeX renders, no clipping, no horizontal scroll. Measured every inline .katex (getClientRects().length) at 360, 390 and 1280 px, all boxes open and all feedback shown, after `build.py fy2-8`: no formula in a changed passage breaks onto two lines.
- Earlier: batch delta review: opened the captures of the changed passages (theory-1280 / example-390), source diff read; no figure changed; text-only edits render cleanly, no clipping, no horizontal overflow, no inline formula wrapped.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
