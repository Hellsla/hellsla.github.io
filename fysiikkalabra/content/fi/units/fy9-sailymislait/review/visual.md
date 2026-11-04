VERDICT: PASS
CONTENT-HASH: c2716084d9c1d0b9

Round 2 (delta review of round 1 fixes; round 1 hash 82147d0c9120ddde)

## Verified (built preview, Playwright at 390 and 1280, all details open)
1. Blocking 1 fixed: the third box of `kartta` is headed "sovellukset", which matches the aria-label. It is rendered cleanly at 390 px.
2. `kartta` uses $\overline{p} = m\overline{v}$, $\Sigma\overline{F}\,\Delta t = \Delta\overline{p}$ and
   $\overline{p}_\text{ennen} = \overline{p}_\text{jälkeen}$, the same notation as Kaava. Fixed.
3. `tormays`: the lost-energy box is a neutral grey with a dashed edge, and the labels 51 200 kg·m/s, 41 kJ and 20 kJ fit
   without overlap at 390. The velocity arrows are blue. Fixed.
4. Kaava "missä" units are LaTeX. Fixed.
5. Both widths: no horizontal overflow (scrollWidth = clientWidth), 0 `.katex-error`, no raw $ in the text,
   no console or page errors. The Miksi line is rendered correctly. The puskurit task is legible at 390.

## Polish
- `fy4-9/pysaytys` ticks are about 13 px at 390 px. This is a shared figure (see Shared issues).

## Shared issues
- `lessons/FY4/fy4-9/figures.py` `pysaytys`: enlarge the tick labels.

## Scores
illustrations 4 · typography 4 · Finnish 5 · accessibility 4
