VERDICT: PASS
CONTENT-HASH: 338baa44a2d54eaa

## Blocking

## Polish
- [Minor] fig-4 ("tyypit") at 390 px: the "jälkeen" carts are drawn paler than the "ennen" carts. Check that this is the intended ghost style and not an animation frame caught mid-way. If it is intended, no change is needed.
- [Minor] I did not run the animation or click the play button. The static frame is clean, but the motion itself is unjudged.

## Checked
- Captures opened: fy4-10-fig-2-390 (vuorovaikutus), fy4-10-fig-3-390 (kimmoton törmäys) and fy4-10-fig-4-390 (tyypit), all at readable size.
- The diff adds animation groups to "vuorovaikutus" and "tyypit". Labels, colours (force red, momentum violet, velocity blue) and layout are unchanged in the static frame, with nothing clipped or overlapping.
- site.css: animation runs only under `.is-playing`, so the default state is still. It is off under `prefers-reduced-motion` and in print, and has a 40 px play button with a focus ring.
- Stamp matches the hash. The other captures were not opened, because the diff does not touch them.

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 5
