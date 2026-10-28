VERDICT: PASS
CONTENT-HASH: 0de2fc46804dab65

## Blocking

## Polish
- lesson.md:265 — "tarkoilla luvuilla kuten muunnoskertoimella $1000$" still names a conversion factor, against the lesson's own substitution method. Write "tarkoilla luvuilla, kuten $1\,\text{km} = 1000\,\text{m}$". Still open from the last round.
- lesson.md:349 (Esimerkki, Sijoitus) — "$(1{,}502\cdot10^{4} : 3600)\,\text{h}$" is correct, but the substitution is left implicit. Use the form that tarkistus-2 uses: "$1{,}502\cdot10^{4}\,\text{s} : 3600\,\text{s} = 4{,}17$".
- sim (slider label vs view) — at the Sun the slider label reads $d = 10^{6{,}00}\,\text{km}$ while the readout reads $d = 0\,\text{km}$. Mark the label as the slider's lower limit.

## Checked
- Changes since the last pass: the prefix sentence now names senti and desi as exceptions to the 10³ steps, which is correct. tarkistus-1's distractor feedback now places the last zero of 0,0250 m at 10⁻⁴ m = 0,1 mm, which is correct. Two numbers with units are now in LaTeX, with their values unchanged.
- One script recomputed every number: Neptune $4{,}503\cdot10^{9}\,\text{km}$ and 4,17 h; 1 AU in 499 s = 8,32 min; light covers 7,2 AU in an hour and 1212 AU in a week; 10⁷ and 10⁹ km take 33,4 s and 3340 s; siirto 3,236 AU/a (mistake 3236); Mercury 193,1 s = 3,22 min (mistakes 193 and 0,0536); exit ticket 79 min; Sun 401 px, Earth 3,7 px, Neptune 1,29·10⁶ px.
- Voyager model d = d₀ + v(t − t₀), with leap days: 1.1.2026 gives 142,9 AU and 19,8 h; mid-February 2026 gives 143,3 AU (JPL 143,05); the 5 November values in the table (119,7/132,6/145,6/158,5 AU; 16,6/18,4/20,2/22,0 h; km values) all match. sim.js uses exactly these constants, and the sim calls the signal time from the Sun with the ±8 min caveat for Earth.
- Significant figures: 0,0250 m has 3; the 30,1 AU product has 3 (4,50·10⁹ km); 1,85 m · 0,92 m = 1,7 m².
- Every choice item has exactly one correct option, and every distractor's feedback is correct. koe-1 varies only n with the date locked; koe-2 varies only the date.
- SI table (seven base quantities and units), the prefixes, km² = 10⁶ m², and light-year as a length: correct.
- Scope: s = ct and unit substitution are inside FY1. The deterministic "answer positions" FAIL is a layout/option-order check, not physics.
- Hash identical at start and end.
