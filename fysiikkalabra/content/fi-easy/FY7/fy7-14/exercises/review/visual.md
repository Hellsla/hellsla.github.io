VERDICT: PASS
CONTENT-HASH: d546c7be180b582b

## Blocking

## Polish
- [Minor] solutions.md:64 — at 390 px the line breaks after the opening parenthesis before the inline formula; harmless, could be avoided with "eli" instead of brackets.

## Checked
- Packet captures have no phone-width opened solutions, so own Playwright captures of the current preview build (preview/fi-easy) at 390 px and 1280 px, every solution open; plus a scripted scan of every formula of the exercise set at 360 and 390 px: none wider than its box, none scrolling, no page overflow.
- The hash changed during the review (f139c7b268916dd7 → current: commit 7e4ba8466f put the bracketed formula of 14-7 back inline); preview rebuilt, 14-7 Järkevyys re-captured at 390 and 1280: the formula sits inside its parentheses in the sentence, nothing clipped.
- Delta: the other 4 re-broken blocks (607,2 nm, 94,2 nm, 540 nm, 221 nm) at 390 and 1280 px, full size (unchanged by the later commit). Rest not re-reviewed.

## Scores
illustrations 4 · typography 5 · Finnish 5 · accessibility 4
