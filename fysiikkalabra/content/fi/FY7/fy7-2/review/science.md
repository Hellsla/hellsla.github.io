VERDICT: PASS
CONTENT-HASH: 8c950558e4f8652d

## Blocking

## Polish
- lesson.md:232–234: the cyclotron photo follows the sentence about a ring accelerator whose field is strengthened to keep $r$ fixed (a synchrotron). The caption's "taivuttaa hiukkaset ympyräradalle" and "joka kierroksella" fit a cyclotron only loosely: its field stays constant, the path spirals outwards, and it is accelerated twice per revolution. Fix: "kiertävät magneettikentässä ulospäin laajenevaa kierrettä, ja sähkökenttä kiihdyttää niitä kiihdytysvälissä" (C level, not an error that blocks).
- inquiry.json:140 (simulation `model`): "Vauhdit ovat alle 1 % valon nopeudesta". A proton fired at $0{,}5\cdot10^6$ m/s with $E = 300$ kV/m and $B = 0$ reaches the plate at about $1{,}2\,\%$ of c. Classical mechanics still holds, so the fix is only the wording: "noin 1 % tai alle".
- inquiry.json:140: "Painovoima … noin $10^{12}$ kertaa magneettista voimaa pienempi" holds at the default 0,20 T and $10^6$ m/s. With weak fields from the sliders the ratio drops to about $10^{10}$. Fix: "vähintään miljardeja kertoja pienempi", or leave it as it is.

## Checked
- I recomputed every number in one script (scratchpad fy72.py) with my own formulas and compared them with lesson-answers.py: Ydinajatus F, r and the weight ratio; the r-graph points (10,4 cm and 20,9 cm, and the pixel positions are to scale); the worked example (v = 3,00·10⁵ m/s, 3,32·10⁻²⁶ kg, 20,0 u, Ne-22 at 27,4 cm); kertaus and its distractors (1,76·10⁶ and 7,04·10⁶); virhe (4,57 and 6,46 cm); siirto (0,225 T, with the mistake values 0,159 and 0,00712 T); tarkistus-3 (6,22 cm, with the mistake value 12,4); the exit ticket; 1837 for the proton–electron mass ratio; and the LHC 1,09·10⁻⁶ J. All agree.
- The simulation's Boris integrator matches m dv/dt = q(E + v×B). I replicated it in Python for koe-1, which gives d = 5,22, 10,44, 15,66 and 20,89 cm with the end speed unchanged. For koe-2 the deflection is 0 for all four particles, and Fm15 = Fs15 = 24,03 and 48,06 fN. At v ≠ E/B, faster particles bend towards F_m and slower ones towards F_s, as the theory says.
- The koe-1 and koe-2 setups each change only one parameter, the simState keys `d`, `vLoppu`, `poikkeama`, `Fm15` and `Fs15` exist, and the 20,9 cm hit lies within the 22,4 cm half-height.
- The force directions in force-dir, circle-path (clockwise for B out of the page), the spectrometer (selector F_s up and F_m down, ions curving down in B₂, lighter ions closer) and track-sign (negative) are correct by v×B.
- In the hero, the rarer, heavier C-14 beam bends less.
- Every prediction has exactly one correct option, and the feedback on every distractor gives the right reason with model values.
- The formula conditions are stated: v ⊥ B for the circle, v ≪ c, and gravity neglected. The relativistic caveat for the LHC is given.
- The model answers of johtopäätös and tarkistus-4 agree with the theory and the sim values, and are called model values.
- Scope: F = qvB, the circular path, the velocity selector, the mass spectrometer and the accelerator are all inside the FY7 contents.
- Units and significant figures: E/B in m/s, 1 C·m/s·T = 1 N, and the example is limited by its three-figure data.
