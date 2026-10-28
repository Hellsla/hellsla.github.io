VERDICT: FAIL
CONTENT-HASH: f4e6eeab469a347c

## Blocking
- lang/fi.json:586–587 (sims.fy1-1 `rivi_kohde`, `rivi_nakyvissa`; shown by assets/sims/fy1/fy1-1/sim.js readout) — the readout prints the object names (`{{nimi}}`, `{{nimet}}`) and the count `{{n}}` as plain text ("Kooltaan lähin kohde: **ihminen**", "Näkyvissä 4 kohdetta: euron kolikko, …", see shots/fy1-1-sim-1280.png); the teacher's rule (CLAUDE.md Lesson form 1) makes every readout label and value LaTeX, as the canvas already is. — Wrap them as on the canvas: `$\text{{{nimi}}}$`, `$\text{…}$` for each name in `nimet` (build the list in sim.js as LaTeX) and `${{n}}$`.

## Polish
- lang/fi.json:602–603 + sim.js:41–44 (au, saturn, neptune, helio, oort) — the label value is the orbit's radius (e.g. Neptunuksen rata, $4{,}5\cdot10^{12}\,\text{m}$) but the picture is drawn at the diameter; against the scale bar the drawing is twice the label, said only in Mallin oletukset. — Name them "… radan säde" or label the drawn diameter.
- lang/fi.json:611, sim.js:19 — "gammasäteily $1{,}0\cdot10^{-12}\,\text{m}$" is a wavelength, not a size of anything; neither label nor model box says so. — "gammasäteilyn aallonpituus".
- inquiry.json:124 (exp-1 intro) — Lähennä ×10 lands on whole L: at $L=-9$ the nearest object is the water molecule and at $L=-10$ the helium atom, so the hydrogen-atom row ($L\approx-9{,}4$) is reachable only with the slider. — Say "liukusäätimellä" for that row.
- lesson.md:106 — $\Delta n = n_2-n_1$ of the exponents of $a\cdot10^n$ is called "suuruusluokkien ero"; the two differ when a coefficient is over about 3 (Everest). — "noin suuruusluokkien ero", or compute Δn from the orders.
- inquiry.json:116 (sim model) — stray ". ja ytimien …" fragment.

## Checked
- All 12 exercises and inquiry numbers recomputed in one script: match answers.py; rounded answers stay inside tolerance.
- sim.js `mainObj`/`kohdeExp` replicated: every experiment's L values give the objects and n the inquiry states.
- All 43 OBJ sizes realistic (Sgr A* horizon from 4,3 M☉, neutron star 24 km, observable universe 93 Gly).
- Figures 2 and 7: axis positions to scale (11,8 and 26 px per decade); figure 6 nesting values and figure 8 force direction right.
- Lesson facts (heliopause, Oort cloud, nuclear mass share, beta decay, strong range, EM/gravity 10³⁶) correct.
- Worked example and all solutions: symbolic first, conversions, rounding and reasonableness checks correct.
- Every correct option and feedback in inquiry.json; exit ticket.
- Content within FY1 scope and the 2026-10-28 brief (qualitative; no equations beyond ratios and s = ct).
