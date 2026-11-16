VERDICT: PASS
CONTENT-HASH: 0afbb0e960a7159d
SCOPE: delta added-exercise from 14b54a6e061b7b91 base 415cbc7c6bc3

## Blocking

## Polish
- content/fi-easy/FY8/fy8-12/exercises/solutions.md:229 — "annosnopeusmittarilla tai GM-putkella … Annos saadaan kertomalla annosnopeus käyttöajalla": a GM tube gives a count rate, not a dose rate (the glossary says so), and a meter calibrated for gamma underestimates the beta skin dose — say that the dose needs a calibrated dose-rate meter or a skin dosimeter, and that the GM tube shows only that radiation is present and how it changes.
- content/fi-easy/FY8/fy8-12/exercises/solutions.md:229 — "ohut alumiinilevy" stops beta particles only if it is a few millimetres thick — write "muutaman millimetrin alumiinilevy".
- content/fi-easy/FY8/fy8-12/exercises/exercises.json (text, href) — the URL has "anti%2D5g" where the source's address has "anti-5g"; this is probably harmless, but use the plain address the source gives.

## Checked
- Recomputed: E = hf = 6,626e-34 J s · 3,5e9 1/s = 2,319e-24 J = 1,4476e-5 eV = 14,48 µeV; answers.py gives 14,476 ✓. Box 14 µeV with relative tolerance 0,04 accepts 13,4–14,6, including the 14,5 the solution names ✓.
- Ratios 10 eV / 1,448e-5 eV = 6,9e5 and 1e5 eV / 1,448e-5 eV = 6,9e9 ✓; "noin miljoona kertaa" is a fair order of magnitude.
- Causality: whether radiation ionises depends on the energy of one photon, not on intensity, as the glossary's definition says; right and stated without condition gaps.
- Source facts against the verified list: ten products, the names "Quantum Pendant"/anti-5G and "negative ion", RIVM's finding, the low level and low risk, the year-long 24 h skin limit, the sales ban, the advice to owners — all ✓. The claims are inferred from the names and labelled as inference; the methods are not attributed to RIVM ✓.
- Part d): the evidence (mechanism, blinded controlled studies, replication), the claim classed as physically wrong, and the real effect being the added ionising exposure are right.
- Hash 0afbb0e960a7159d at the start and the end.
