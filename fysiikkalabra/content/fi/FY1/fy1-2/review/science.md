VERDICT: FAIL
CONTENT-HASH: 62584511c014f39e

## Blocking
- inquiry.json:117 (sim `calc`) — "kulunut aika $t = s/c$" writes a division as an operation with a slash, against the teacher's rule of 2026-10-28 — write $t = s : c$ (as in the rest of the file) or $t = \frac{s}{c}$.
- inquiry.json:417 and :422 (tarkistus-3 model answer and criterion) — they teach conversion as "muunnoskerroin, joka on kahden yksikön suhde, $1{,}496\cdot10^{8}\,\text{km/AU}$", a general conversion-factor rule, against the teacher's rule (conversion by understanding: replace the unit by its value) and against the lesson's own Kaava section — say that the unit is replaced by its value, e.g. "AU:n paikalle kirjoitetaan $1{,}496\cdot10^{8}\,\text{km}$", and change the criterion to match.
- inquiry.json:235 and :240 (johtopaatos model answer and criterion) — "muunnoskerroin vie yksiköstä toiseen" / "mainitsin muunnoskertoimen": same rule — "yksikön paikalle kirjoitetaan sen arvo toisessa yksikössä".
- inquiry.json:258 (pohdi) — "muunnoskaavaan" refers to a conversion formula that the lesson no longer has — "yksikkömuunnoksiin".

## Polish
- inquiry.json:351 (siirto solution) — "$s_\text{AU} = \dfrac{vt}{1\,\text{AU}}$" and dividing by "km/AU" is formula-like. Say how many AU fit in the distance: $4{,}842\cdot10^{8}\,\text{km} : 1{,}496\cdot10^{8}\,\text{km} = 3{,}236$, so the answer is 3,236 AU.
- sim.js (slider vs view) — at the Sun (d = 0) the slider label reads $d = 10^{6{,}00}\,\text{km}$ while the readout says $d = 0\,\text{km}$. Mark the label as the slider's lower limit, or hide it below 10⁶ km.

## Checked
- All numbers recomputed in one script (worked example, ennuste/koe values, Voyager table and 1.1.2026, siirto, Merkurius, mistakes, sim scale): every value agrees within rounding.
- Voyager model matches the brief (119,7 AU, 15,341 km/s, 2018-11-05); the values are labelled as model values, Sun vs Earth light-time caveat stated.
- No ×, \times or ÷ anywhere; multiplication is \cdot; other divisions use ":" or \frac.
- The lesson's Kaava section teaches conversion by replacing the unit by its value (4,2 km = 4,2 · 1000 m); km² handled as (1000 m)².
- Significant figures and scale examples correct.
- SI table fully visible at 360 px (Playwright: 314 px wide in a 328 px column, KaTeX symbols render); Voyager table fits too.
- SVG figure labels are LaTeX and their numbers are correct; sim canvas labels render as LaTeX.
- The lesson has no measurement-error content, so the Δx rule and the gross-error (karkea virhe) point do not apply here.
