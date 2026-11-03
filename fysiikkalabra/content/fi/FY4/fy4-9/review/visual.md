VERDICT: PASS
CONTENT-HASH: c474b60ee95b8098

## Blocking

## Polish
- [Minor] inquiry.json exp-1/2/3 `measure` labels (exp-1-390, lab-1280-1, exp-3-390-2) — the table headers set `(s)` and `(N)` in KaTeX but `(N·s)` and `(kg·m/s)` in plain sans, so one header row uses two typefaces for units — write the labels so the build sets the unit as maths, e.g. `"$I$ ($\\text{N}\\cdot\\text{s}$)"`, `"$\\Delta p$ ($\\text{kg}\\cdot\\text{m/s}$)"`.
- [Minor] inquiry.json exp-1/2/3 Alkutila line (exp-1-390-1, lab-1280-1) — reads "massa $m$: $1{,}0\,\text{kg}$, alkunopeus $v_0$ = $2\,\text{m/s}$": colon vs a sans "=", and $2$ where the intro and the readout say $2{,}0$ — give `v1` a `values` entry `"2": "$2{,}0\\,\\text{m/s}$"` like `m` has.
- [Minor] lesson.md Esimerkki (example-390-1/2) — the Sijoitus block writes the unit as $\tfrac{\text{m}}{\text{s}}$ in rows 2–3 and $\text{m/s}$ in row 4; the Järkevyys gives "$145\,\text{N}$" (three figures) beside an answer of two; and the inline $F_\text{ka}\,\Delta t = mv - mv_0$ wraps at the minus at 390 px — use `\text{m/s}` throughout, write "noin $1{,}5 \cdot 10^2\,\text{N}$", and keep the inline formula short (e.g. "Impulssiperiaatteesta saadaan" + the display formula).
- [Minor] exit ticket (open-exit-1280, open-tarkista-1280-3) — the card heading reads "Exit ticket" in English on a Finnish page; it comes from `lang/fi.json` `exit_ticket`, so it is site-wide, not this lesson's — for the teacher: if not a deliberate choice, "Lähtölippu" (the activity id already says `lahtolippu`).
- [Minor] lesson.md Yleinen virhekäsitys — straight quotes "imee liikemäärän" — Finnish ”imee liikemäärän”.

## Checked
- contact-1…6 for triage; top-390, top-1280/intro-1280 (hero at both widths)
- fig-2…6 at 390 (liikemaara, pysaytys, kimpoaminen, keskivoima, tarkistus-kolmio): colours FY4 (v blue, p violet, I/F red), labels LaTeX, arrows to scale, nothing clipped
- theory-1280-1, -2, -3 (figures beside/below their paragraphs, display formulas); stage-selita-390-4
- example-390-1, -2 (all seven stages)
- sim-390, sim-1280, lab-1280-1, -2 (the lab-side panel scrolls by design; the readout's rest is reached by scrolling inside it)
- exp-exp-1-390-1 (cropped and enlarged the Alkutila line), contact views of exp-2/exp-3
- open-ennusta-1280-1, open-tarkista-1280-1, -2, -3, open-exit-1280
- Text: lesson.md, inquiry.json, exit-ticket.json in full from the packet. No plain number+unit found in student prose.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
