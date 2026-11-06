VERDICT: FAIL
CONTENT-HASH: e2a4b4fa15ee78b7
ROUND: 1

## Blocking
- [Major] fy6-2-L2-08 task text vs. option order — the task says "Jos suunnitelmassa ei ole virhettä, valitse viimeinen vaihtoehto", but on the page "Suunnitelmassa ei ole virhettä" stands third (Rivi 2, Rivi 3, Suunnitelmassa …, Rivi 1, Rivi 4); the page keeps an option last only when its text matches the no_error strings ("Laskussa ei ole virhettä" or "Päättelyssä ei ole virhettä", lang/fi.json) — the instruction points to the wrong option, so the student is misled — reword the option to "Päättelyssä ei ole virhettä" (or the task to "valitse vaihtoehto, jonka mukaan virhettä ei ole") and confirm in the render that it is last.
- [Major] fy6-2-L2-08 Mallivastaus, the line ΔI = 0,010 · 140,0 mA + 2 · 0,1 mA — at 390 px the chain is 312 px wide in a 304 px box (kx-wide, scrolls without a cue), so the final "mA" is cut ("0,1 m/") — shorten the chain (for instance write the 140,0 mA as the reading in the sentence) or put it in two lines, so that it fits about 300 px.

## Polish
- [Minor] fy6-2-L2-08 feedback of "Suunnitelmassa ei ole virhettä" — it says "Suunnitelmassa on virhe", which gives the answer away to anyone who picks it as a guess — fine as a hint, but say "Tarkista virherajat" without the claim.

## Checked
- Renders at 390 px of fy6-2-L2-08 with a wrong choice (feedback open) and the correct one, Vastaus and Näytä ratkaisu open: the order of options and the clipped chain were read from these. Overflow measured (page 390 = viewport, no element outside); the clip measured from the formula's own box (312 vs 304 px).
- Text only: the distractors catch the chapter's warned mistake ("suurin alue aina paras"); the correct row is not identifiable by form; scope (range choice, fuse, OL, virheraja) is taught in the lesson; the paragraph splits in L3-01..03 read well (not rendered).
- Not seen: 360 px and 1280 px captures.

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 3
