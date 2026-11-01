VERDICT: PASS
CONTENT-HASH: f5bc3f119dc791ac

Science, fact and French-accuracy re-review of fy14-fr-lire, 2026-11-01 (HEAD 63a494f6).

## Previous findings
1. Resolved. The article now says "*Selon le CEA, ils ont battu un record mondial de durée : c'est 25 % de plus que le record du tokamak chinois EAST, établi quelques semaines plus tôt.*" The summary model says "The CEA called it a world record: 25 % longer than China's EAST". The true/false feedback quotes the new wording. The French is correct (*le record … établi*). The facts agree with EUROfusion/CEA and AFP: 1,337/1,066 = 1.25, and 22.3 min.
2. Resolved. The text says "about 200 words".
3. Resolved. The *battre* feedback now says "are related to".
4. Resolved. The second text now says "*s'était engagée à offrir une scolarité bilingue à ces enfants*", which matches iter.org *ITER France*. The model follows it.

## Blocking
None.

## Polish
1. New `fx-say-article`, line 4: *C'est une expérience* is respelled *se-ty-neks-…*. Everywhere else in the chapter *c'est* is *sè* (*sè kõ-BJẼ*, *sè-ta GOŠ*), so write *sè-ty-nèks-pe-RJÃS sjã-ti-FIK* for consistency with the pilot. The other three respellings in this task are correct: *fy-ZJÕ ny-kle-ÈR, rö-KOR dö dy-RE a ka-da-RAŠ*, *fi-zi-SJẼ dy se-ö-A õ mẽt-NY*, and *pro-dyi-RA pa de-lek-tri-si-TE*.

## Checked
The whole diff since the last review: the reworded learn goal and opening question, the non-breaking hyphens and spaces (no text changed), and the French tagging. All eight true/false/not-in-text answers still follow from the revised article. Every choice has exactly one correct option. The facts are unchanged and still current (ITER press release of 29 July 2026; Baseline 2024, research operation 2034; 500 MW from 50 MW).
