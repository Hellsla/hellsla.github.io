VERDICT: PASS
CONTENT-HASH: 47fff9ff6ab0e619

Visual & editorial review of the English translation of fy9-liike, round 2.

## Checked
- Rebuilt with `python3 scripts/build.py fy9-liike` (preview/en/fy9-liike.html) and checked in Playwright at 390 and 1280 px with every box open: no horizontal scroll (scrollWidth = viewport), no element wider than the viewport, 0 KaTeX errors, no unrendered $…$, no page errors.
- Round-1 Blocking 1 (s3 figure label "braking distance" crossing the braking line and the circled reading point (40 s, 20 km/h)): FIXED. figures.json now has "braking dist." (13 characters, no longer than "jarrutusmatka") and the figure was redrawn (foreignObject x 87, width 158). Own captures of svg[data-fig=fy9-liike-s3-graph] at 390 and 1280: the label lies inside the green area, clear of the braking line and of the circled point; only its first letter reaches a few pixels left of the dashed 10 s line, which is less than the Finnish label does (x 81, width 170) in the passed source.
- Text-only changes since round 1 (cart, neutral pronouns, average speed, Exercises) read naturally; decimal point and LaTeX rules kept.

## Blocking
(none)

## Polish
1. [Minor] exit-ticket item 2 answer at 390 px: the chained `\dfrac` wraps tightly onto the next line (same as the Finnish page, shared layout).
2. [Minor] Coordinates keep the Finnish semicolon "(12 s; 85 km/h)"; a comma is usual in English.
3. [Minor] review/shots/ captures are from round 1 (stamp e13d8db6ead3da45); regenerate with screenshot.py if a current set is wanted.
