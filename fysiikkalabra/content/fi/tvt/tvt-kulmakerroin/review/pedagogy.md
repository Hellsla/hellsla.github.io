VERDICT: PASS
CONTENT-HASH: dd68b9034e7f878c

## Blocking

None.

## Polish

- Order: for a GA Pro guide the main route is step 3 (read the fit box); steps 1–2 (two points from the line) are framed as a check. Consider putting step 3 first and the two-point calculation after it as "tarkista käsin", so a student following in order does not do the hand calculation before learning the program already gives the answer.
- Step 3 and step 5 both state the slope-unit rule; keep it in step 5 only.
- Step 3: name the letter GA Pro uses for the slope in the fit box (see tvt-suoran-sovitus polish). Also **Show units in linear fit parameters** has no location in the verified facts; add "kysy opettajalta, jos et löydä asetusta" as the other guides do.
- Step 7, third bullet: "Joskus mallissa kuuluu olla vakiotermi" → "Joskus malliin kuuluu vakiotermi" reads more naturally.

## Checked

- Read guide.json, guide.md and the figure's labels in full; ran the hash. Menu names (Apply Curve Fit, Show units in linear fit parameters) are in the verified facts.
- Goals (slope and intercept with units; physical meaning via the model) match steps 1–7; checklist covers both.
- Clear "Δ tarkoittaa muutosta, ei epävarmuutta", which keeps the notation consistent with tvt-epavarmuus.
- Worked example labelled "keksityn esimerkkiaineiston"; $g = 4\pi^2 : 4{,}05\,\text{s}^2/\text{m} \approx 9{,}75\,\text{m/s}^2$ with a unit check; colon for division, units in LaTeX.
- Intercept causes (zero offset, inconsistent method, real physical term) are concrete and tied to real investigations. Mistakes are real ones, each with a fix.
- Figure shows the slope triangle and intercept b without numbers. Cross-links to suoran-sovitus sensible. No spreadsheet/Excel/Tracker leftovers.

## Delta 1 (2026-10-31, Finnish UI and screenshots)

- Screenshots render inside their list item (section>ol>li), not wrapped in <p>; alt texts describe what is shown; captions say "esimerkkiarvoja" only on pictures with values; no licence holder or school name visible (the start-screen crop stops above the "Lisenssin haltija" row). guides.py check: ok.
- The screenshot sits in the step that reads the tulosruutu; alt text lists every value; caption says esimerkkiarvoja. Good link between UI "m" and the guide's k.
- Polish (optional): the example copies all four digits (1,671) into the report; a half-sentence pointing to [[ohje:tvt-epavarmuus]] for rounding would stop students reporting the program's digits as significant.
- UI text quoted from the screen (y = mx + b, m: 1.671 g/cm3) as plain text is fine; the report-form value is in LaTeX.
