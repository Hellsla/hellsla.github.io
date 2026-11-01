VERDICT: FAIL
CONTENT-HASH: 4d93fdd86e12b6e3

## Blocking
- [Critical] simulation in Koe 2 (`exp-exp-2-390-1`) — after *Aseta alkutila* at 390 px the canvas is drawn at the wrong scale: "Tilannekuva" and "$t = 0{,}00\,\text{s}$" are huge, the track labels "1,0 m"/"2,0" overprint each other, the free-body box and $\overline{N}$, $\overline{F}$ are cut at the right edge, and the $v_x$ graph has collapsed into one row of overlapping axis labels ("$v_x$ (m/s)", "$t$ (s)", tick numbers). Koe 1 and Koe 3 at the same width and the 1280 px lab render correctly — the student cannot read the velocity graph on which the mass experiment depends — make the sim re-measure its canvas and KaTeX overlay when it moves into the Koe 2 card / when the mass changes, then re-capture `exp-exp-2-390` to confirm.

## Polish
- [Minor] inquiry.json exp-1/2/3 Alkutila line — renders "voima $F$ = 1 N" with the quantity in plain text and with less precision than the intro's $1{,}0\,\text{N}$ — add `values.F` (`"1": "$1{,}0\\,\\text{N}$"`, `"2": "$2{,}0\\,\\text{N}$"`).
- [Minor] lesson.md Esimerkki, Sijoitus — `9{,}81\,\tfrac{\text{m}}{\text{s}^2}` is the only stacked unit on the page; write `9{,}81\,\text{m/s}^2` like every other line.
- [Minor] inquiry.json prior — `\dfrac{\Delta v}{\Delta t}` inline pushes the line apart (`intro-1280`); use `\tfrac`.
- [Minor] figure kuvaaja — the text calls the points "Mittaukset kärryllä", but they lie exactly on the lines (model values); say in the aria-label and the paragraph that they are the simulation's model values.
- [Minor] figure nosturi — "$a = 0$" sits beside the box in *levossa* but down at the $\overline{G}$ arrowhead in *nousee tasaisesti*; place the $v$/$a$ labels the same way in all four panels.

## Checked
- contact-1…6 (triage); `top-390`, `intro-1280`, `fig-1-390` (hero), `fig-2/3/4-390`, `fig-6…9-390` (valitse options)
- `theory-1280-1/2/3` (all theory figures at full size, Yleinen virhekäsitys, Tiivistelmä)
- `example-390-1/2` (zoomed the esimerkki figure; arrow lengths checked against source lines 545–571: $T$ 135 vs $G$ 122,5)
- `sim-390`, `lab-1280-1`, `exp-exp-1-390-1`, `exp-exp-2-390-1`, contact view of `exp-exp-3-390`
- `open-tarkista-1280-2` (check-2 generated force diagram and Sijoitus), contact view of `open-ennusta-1280`, `open-exit-1280`, stage captures #13–#29
- source scan of lesson/inquiry/exit-ticket prose for plain number+unit: none apart from the generated Alkutila value above

## Scores
illustrations 4 · typography 4 · Finnish 5 · accessibility 2
