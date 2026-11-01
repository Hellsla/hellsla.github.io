VERDICT: PASS
CONTENT-HASH: c017b09db5bac17d

## Blocking
(none)

## Polish
1. [Minor] Year strip (shared `timeline.js`) at 390 with *All eras*: 104 marks in 340 px. Marks are stacked by 10-px buckets but are 12–14 px wide, so 50 pairs of marks overlap (the 1950s and the 2020s become blocks). Each mark is a 12-px tap target. The cards below carry every event, so nothing is lost. Fix: stack by `Math.round(X/14)` (the mark width plus a gap) so that neighbours never overlap. Optionally, on narrow strips, hint "choose an era to see the marks apart".
2. [Minor] Timeline cards (shared `timeline.json`, `einstein-emc2-1905`, `lawrence-cyclotron-1931`, `fission-1938`): "E = mc²", "c²", "80 keV", "4.8 MeV" and "200 MeV" are plain text. That breaks the course rule that all maths is LaTeX. Fix: `$E = mc^2$`, `$80\ \text{keV}$` and so on in `text`. The card title is not passed through `md`, so either the title avoids maths ("Einstein: mass and energy") or the component renders titles with `md` and typesets them.
3. [Minor] `unit.md` *What the timeline shows*: "about 120 years" from 1920 to 2039 is fine. "Since 2015 the events come from at least seven countries" is a count students cannot easily check in the strip. Fix: name them in brackets.

## Checked
- The timeline after the strip change, own Playwright run at 390, 1280 and 360, all eras and each of the four eras. At 390 the viewBox is 340 for a 340-px strip (scale 1.000), with year labels 1900/1950/2000, or every 5–10 years within an era. At 1280 the viewBox is 1000 drawn at 1134 px (scale 1.13), with labels every 10 years, or every 5 within an era. Year labels never overlap and are ≥ 14 px. The legend is 17 px. No horizontal scroll at any width. Clicking a mark scrolls to and focuses its card. Biographies show years only. Card ids are prefixed with the element id.
- Captures regenerated for this hash: contact-1, -5; tl-all and tl-era1–4 at 390 and 1280 (own); fx-2 (match) and fx-3 (say); hero at 390 and 1280 (no text). No `.katex-error`, no raw `$`, no console errors. Hash unchanged at the end.

## Scores
illustrations 4 · typography 3 · English 4 · accessibility 4

## Shared issues
- `assets/units/fy14/fx/timeline.js` + `site` CSS: `article svg{border;padding:.4rem;background}` also hits the strip's SVG. The result is a frame inside the `.fx-tl-strip` frame (a double border at both widths). The strip is then drawn about 4 % smaller than "1 unit = 1 px", with year labels about 14.4 px rather than 15. Fix in `units.css`: `.fx-tl-strip svg{border:0;padding:0;background:none;border-radius:0}`.
- `timeline.js` `draw()` rebuilds the whole card list on every resize over 20 px (a phone rotated from 390 to 844). Any open *Who was …?* biography closes, and the reader loses their place (tested: open biography → closed after rotation). Fix: on resize, redraw only the strip, and keep `list.replaceChildren` for filter changes.
- Table headers centred over left-aligned cells (seen in fy14-big-machines): shared table style. Left-align `th` in text columns.
