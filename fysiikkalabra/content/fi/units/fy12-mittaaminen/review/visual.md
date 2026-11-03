VERDICT: PASS
CONTENT-HASH: 9a4783083d3a7ff6

## Blocking
None. Both round 1 Blocking findings are fixed.
- **Label size.** I measured the KaTeX label size × SVG scale at 390 px with Playwright. Base labels are kartta
  15,5 px, anatomia and linearisointi 16,1 px, and s3-pisteet, s3-sovitus, s5 and s6 14,9 px. Every unit figure is
  at least 14 px. At 1280 px the labels are 18,7–28,4 px.
- **Collisions.** anatomia now has a jyrkin/loivin legend in the free corner, and the b ring sits between ticks 15
  and 30. s6: the k label is upper left, −V₀ is below the axis, and the x ticks are 4/8/12. linearisointi: k = a/2 is
  below the line. s3 "akseli alkaa 100 g" is legible. A bbox test finds no label–label overlap and no label–point
  overlap. The only hits are kartta's step numbers inside their own circles, which is by design.

## Shared issues
- `fy3-3/extrapolation-points` (FY3 catalog figure, used by Tutki): the tick labels render at 13,0 px and the
  °C superscript of the axis label at 9,1 px at 390 px. This figure belongs to FY3, not to this unit. The fix is in
  `lessons/FY3/fy3-3/figures.py` (raise the Fig size).

## Polish
- [Minor] s3-sovitus, s5-kuvaaja, s6-kuvaaja, linearisointi: units written as `\tfrac` (g/ml, m/s, 1/MPa, a/2) and
  the s6 axis label $\tfrac{1}{p}\ (\tfrac{1}{\text{MPa}})$ render at 10,4 px at 390 px. Use inline forms such as
  `\text{g/ml}`, `\text{m/s}` and `1/p\ (1/\text{MPa})` in `sovella/figures.py` and `figures.py`.
- [Minor] s3-sovitus: the m₀ ring at (0; 118,6 g) touches the y-tick label "120". Move the ring label or nudge the
  tick labels left by about 6 units.
- [Minor] s3-pisteet and s3-sovitus: the description promises "vaakasuora epävarmuusjana ±1 ml", but the bars are
  hidden under the points at every width. Say, as s5 does, that they are smaller than the points.
- [Minor] unit.md "Kertaa tarvittaessa" and `inquiry.json` › `tarkista-3` › practice: "astian massa vakiotermina"
  should be "vakioterminä".
- [Minor] `jousi-suora` solution, Annettu: at 390 px the inline pair "(L₁; F₁) = …" wraps inside the parentheses.
  Write "$L_1 = 15{,}0\,\text{cm}$, $F_1 = 1{,}2\,\text{N}$; …" so the line breaks between the values.

## Checked
- Full page at 390 and 1280 px with every `<details>` open: 0 `.katex-error`, no raw `$`, no console errors, no
  horizontal overflow.
- Opened at 390 px (also at 2× for kartta, s3-pisteet, s3-sovitus, s5 and s6): hero, fy3-3 extrapolation-points,
  kartta, anatomia, linearisointi, s3-pisteet, s3-sovitus, s5-kuvaaja and s6-kuvaaja.
- Opened at 1280 px: anatomia, linearisointi, s3-sovitus and s6-kuvaaja.
- Changed items at 390 px: lahto-4, aika-kuvaaja, and jousi-suora with all hints and the solution open. The kolikot
  and tarkista-2 feedback renders correctly.
- The hero's longer uncertainty bars are visible at 390 px. The s5 description now matches the figure.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
