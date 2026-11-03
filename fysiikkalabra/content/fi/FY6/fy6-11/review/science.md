VERDICT: FAIL
CONTENT-HASH: f9ea5baa5155e9c8

## Blocking
- lesson.md:459, :597; inquiry.json:537 — (B, missing condition) "kiihtyvyys $a = qE : m$ on vakio" holds only when the electric force is the only significant force (in vacuum); the lesson then applies the picture to dust in air, and the tarkistus-3 model answer says the force "kiihdyttää sitä koko matkan" in the air purifier, where drag gives a nearly steady drift — add "tyhjiössä, kun muut voimat ovat pieniä" at :459 and in the summary; in inquiry.json:537 write "työntää sitä koko matkan kohti toista levyä" instead of "kiihdyttää".
- inquiry.json:107, :297 (also short forms at :116, :387, :466, :475, :537) — (A, course rule) the field is written "kenttä $E = U : d$" and "kentän voimakkuus $E = F : q$", although E is lähdejännite elsewhere in FY6 and lesson.md:127 promises "puhutaan aina sähkökentän voimakkuudesta $E$" — write "sähkökentän voimakkuus $E$" (and "sähkökentän voimakkuus" in the short forms).

## Polish
- lesson.md:319 (Ilmanpuhdistin) — "työntää jokaista varattua hiukkasta … samalla voimalla" can read as the same force on every particle — "työntää varattua hiukkasta kohti levyä yhtä suurella voimalla koko matkan".
- lesson.md:127 and glossary *testivaraus* vs fy6-10 *koevaraus* — one term across chapters (raised as blocking in fy6-10).
- Electron figure (fig 14): the dashed path keeps bending after the plates' end, where the field is nearly zero — draw it straight past the plates.

## Checked
- Independent 2D boundary-element model (400 strips per plate, constant-potential plates): E·d = U at h = 0,5…3,5 cm for d = 2, 4, 6 cm; midline profile 50,0 (0–6 cm), 49,8 (7), 38,7 (edge), 9,2 kV/m (14 cm) — matches the profile figure, sim and lesson-answers.py (koe-1 100 µN at all heights, koe-3 200/133/100/80/66,7 µN).
- koe-2 (5,0·10⁴ N/C), koe-3 (Ed = 2000 V), siirto (1333 m/s², weight 0,7 % of F), Etsi virhe (4,0·10⁴ V/m), Esimerkki (q = 4,807·10⁻¹⁹ C, n = 3,0), electron F/G, exit ticket (3,0·10⁵ V/m) recomputed.
- Derivation E = U/d from W = qEd = qU and the unit identity V/m = N/C correct.
- Each experiment locks all but the varied parameter; simState F gives the measured key; h is clamped inside the gap.
- Predictions, tarkistus-1/-2: exactly one correct option, distractor feedback right; abc figure: A, B between plates far from ends, C outside.
- Colours: field lines and E green, F red, v blue, a orange.

