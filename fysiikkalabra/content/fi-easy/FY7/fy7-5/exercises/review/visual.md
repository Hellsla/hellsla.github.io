VERDICT: FAIL
CONTENT-HASH: fb0f86280d536216

## Blocking
- [Critical] solutions.md:201 (fy7-5-L3-05, Kuvaajan lukeminen) — the row "· (½(−0,02) + 0,09 + 0,63 + 1,77 + 1,77 + 0,60 + ½ · 0,03) V" is one row and is cut off at the card edge on a phone (360 px: content 452 px in a 272 px box; 390 px: 475 in 302; it ends at "+ 1,77 + 1"); at 1280 px the closing "V" touches the edge — the sum the student must check is unreadable — break the bracket at its plus signs: `|A_\text{a}| &= 0{,}004\,\text{s} \\ &\cdot (\tfrac{1}{2}(-0{,}02) + 0{,}09 + 0{,}63 \\ &+ 1{,}77 + 1{,}77 + 0{,}60 \\ &+ \tfrac{1}{2}\cdot 0{,}03)\,\text{V} \\ &= …`.
- [Major] exercises.json:259 (fy7-5-L2-07, core task text) — the chain e = vBl = … is now a centred display block and the sentence's full stop is orphaned: the next line starts ". Hän sanoo, että…" (390 and 1280 px) — a visible typographic error in a task every student reads — restore the inline chain `$e = vBl = 2{,}0\,\text{m/s} \cdot 0{,}50\,\text{T} \cdot 0{,}30\,\text{m} = 0{,}30\,\text{V}$.` (as fy7-7-L2-07 now does).

## Polish
- none

## Checked
- The content changed during the review (packet hash 9bfb830f9422b09a; solutions.md:201 re-broken again): page rebuilt, review redone on the hash above.
- Delta (reflow): solutions.md:39, 70, 132, 179, 201, 254 and the task text of fy7-5-L2-07 from preview/fi-easy/fy7-5.html at 360, 390 and 1280 px (own captures). The other re-broken steps are aligned, punctuation inside, nothing clipped.
- Overflow scan of every display formula at 360/390/1280 px: only L3-05. Hash identical before and after the second pass.

## Scores
illustrations 5 · typography 2 · Finnish 5 · accessibility 3
