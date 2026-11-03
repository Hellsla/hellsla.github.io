VERDICT: PASS
CONTENT-HASH: 5154640e532cb66e

## Blocking

## Polish
- lesson.md (Hiukkaskiihdytin): the ring raises B at a fixed r, as a synchrotron does. Exercise L3-02's cyclotron keeps B fixed and lets r grow. Fix (optional): add the clause "(syklotronissa kenttä pysyy vakiona ja rata laajenee)".
- inquiry.json simulaatio.model: "Painovoima ... noin 10¹² kertaa magneettista voimaa pienempi" holds at the default settings (2·10¹²). At the slider extremes (B = 0,01 T, v = 0,5 · 10⁶ m/s) the ratio is about 5·10¹⁰. Fix (optional): "vähintään noin 10¹⁰ kertaa".

## Checked
- I recomputed every lesson and inquiry number in one script with my own formulas: 3,2·10⁻¹⁴ N and 5,2 cm, F : G ≈ 2·10¹², the r-graph (10,4 / 20,9 cm), kertaus and its distractors, koe-1 d 10,44 / 20,89 cm, koe-2 24 / 48 fN, virhe 4,57 → 6,46 cm, siirto 0,2252 T with its mistakes 0,159 and 0,00712, tarkistus-3 6,22 cm (12,4 for q = e), the exit ticket, m_p : m_e ≈ 1840, and LHC 1,09·10⁻⁶ J. All agree.
- Worked example, symbolic first: v = E : B₁ = 3,00·10⁵ m/s and m = 3,324·10⁻²⁶ kg = 20,01 u. Ne-22 lands at 27,4 cm. v is about 0,10 % of c. Three significant figures are justified.
- Directions are right: force-dir (B into the page, + up, − down), circle-path (B out of the page, + turns clockwise, F toward the centre), spectrometer (E up, B₁ out, F_s up and F_m down, + curves down in B₂, the heavier ion lands farther), track-sign (curves down, so negative).
- sim.js: Boris steps with q(v×B). An E×B balance gives exactly y = 0 (I checked this algebraically). The force arrows show q v × B. The model box matches the code.
- koe-1 isolates v, the hits fit on the 22 cm detector, and vLoppu stays constant. In koe-2 the slider steps reach 150 kV/m, 0,15 T and 1,0 Mm/s. The keys Fm15, Fs15 and poikkeama exist.
- The round 1 polish items are fixed: units are now Mm/s and fN, pohdi names the selector, the glossary adds "samalla varauksella", and the example says "noin 0,1 %".
- Every choice item has exactly one correct option, and every distractor's feedback gives the right reason.
- Conditions are stated where the laws are used (v ≪ c, perpendicular entry, homogeneous field, vacuum, no gravity). Scope fits FY7 and the täsmennys.
