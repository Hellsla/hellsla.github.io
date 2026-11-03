VERDICT: PASS
CONTENT-HASH: f775c61f5a128688

## Blocking

## Polish
- inquiry.json:171, 227: the unit `10⁶ m/s` follows the value with no multiplication sign, so the Alkutila box shows "vauhti v = 1 10⁶ m/s", which reads as 110⁶ m/s. The table column "vauhti v" also has no unit. Fix: make the unit `· 10⁶ m/s`, as the sim adapter does.
- inquiry.json:294 (pohdi): the prompt says "sama varaus ja sama vauhti", but the hook (line ~267) says the ions are accelerated and then steered into the field. After the same voltage, C-12 and C-14 have different speeds. Fix: write "sama varaus ja sama vauhti (nopeusvalitsimen jälkeen)", or drop "sama vauhti".
- lesson.md:454: 3,00 · 10⁵ m/s is 0,1001 % of c, not "alle 0,1 %". Fix: "noin 0,1 %".
- glossary.json, massaspektrometri: "säde on verrannollinen massaan" holds only for ions with the same charge. The lesson text gets this right ("samalla vauhdilla ja varauksella"). Fix: add "ja varauksella".

## Checked
- I recomputed every lesson and inquiry number in one script with my own formulas (5,2 cm, kertaus, virhe, siirto and its mistakes, tarkistus-3, exit ticket, LHC 1,09·10⁻⁶ J). All agree.
- Worked example, symbolic first: 3,324·10⁻²⁶ kg = 20,01 u. Ne-22 lands at 27,4 cm. Rounding is justified.
- Directions in force-dir, circle-path, spectrometer (E up, B out) and track-sign (negative) are all right. The right-hand rule as stated gives v×B.
- r-graph is to scale at 0,20 T.
- sim.js: Boris integration is correct, with sign q(v×B). Results come from integration. Limits are stated.
- koe-1 isolates v (d 10,44/20,89 cm, vLoppu constant). koe-2 gives y = 0 for all particles, F 2,40/4,81·10⁻¹⁴ N. The simState keys exist.
- Every choice item has exactly one correct option, and the distractor feedback is right.
- The relativistic limit is stated. Scope fits FY7 and the täsmennys.
