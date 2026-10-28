VERDICT: PASS
CONTENT-HASH: 5e3c67f583461927

## Blocking

## Polish
- lesson.md:265 — "tarkoilla luvuilla kuten muunnoskertoimella $1000$" still names a conversion factor. Write "tarkoilla luvuilla, kuten $1\,\text{km} = 1000\,\text{m}$".
- lesson.md:349 (Esimerkki, Sijoitus) — "$(1{,}502\cdot10^{4} : 3600)\,\text{h}$" is correct but leaves the substitution implicit. Use the same form as the exercises: "Tunteja on $1{,}502\cdot10^{4}\,\text{s} : 3600\,\text{s} = 4{,}17$".
- sim (slider label vs view), open since round 1 — at the Sun the slider label reads $d = 10^{6{,}00}\,\text{km}$ while the readout reads $d = 0\,\text{km}$. Mark the label as the slider's lower limit.

## Checked
- Round-2 blockers are fixed. Siirto's solution, hints 2–3 and its first mistake now count the AU with ":" (no km/AU). Tarkistus-2's solution counts minutes, $193{,}1\,\text{s} : 60\,\text{s}$, and its mistake 193 does the same (no s/min).
- Round-2 polish: virhe feedback now substitutes $1\,\text{km}^2 = (1000\,\text{m})^2$ instead of naming a "muunnoskerroin". The worked example now uses ":".
- Regression scan of lesson.md, inquiry.json, exit-ticket.json and the sim texts: no ×, \times or ÷; products use \cdot; no conversion-factor units (km/AU, s/min, s/h, km/px).
- One script recomputed every number again and found no change: Neptune $4{,}503\cdot10^{9}\,\text{km}$ and $4{,}17\,\text{h}$, siirto $3{,}236\,\text{AU/a}$, Mercury $193{,}1\,\text{s}$ and $3{,}22\,\text{min}$ (mistakes 193 and 0,0536), 1 AU in 499 s, and the koe-1 and Voyager values.
- The changed solutions keep all seven parts, are symbolic first, and their rounding is justified.
- The formulas ($s = vt$, $t = s : c$, unit substitution, significant figures) are inside FY1 central contents.
- Content hash is identical at the start and the end.
