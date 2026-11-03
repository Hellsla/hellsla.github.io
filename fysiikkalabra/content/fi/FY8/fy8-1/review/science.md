VERDICT: PASS
CONTENT-HASH: a7773fffb83c1316

## Blocking

## Polish

## Checked
- Round-2 blocking item fixed: the siirto solution (Järkevyys) now says that red starts at about 620 nm and that the tube sees red light from its short-wavelength end up to 653 nm but not 700 nm. This agrees with exercises L1-03 ✓. The round-2 polish is fixed too: koe-3 now refers to "punaisella valolla kokeessa 1" ✓.
- One script recomputed every number. 500 nm: 3,973·10^-19 J = 2,480 eV. hc = 1240 eV nm. 3,20·10^-19 J = 2,00 eV. Worked example: 4,905 − 3,653 = 1,252·10^-19 J = 0,782 eV. λ0 for Na 543,9 nm, Mg 337,0 nm, Zn 287,7 nm. f0 for Na 5,51·10^14 Hz and Zn 10,42·10^14 Hz. koe-3 at 300/400/500/540/545 nm: Ek 1,85/0,82/0,20/0,016/0 eV. siirto 652,6 nm, with mistake values 4,59·10^14 Hz and 1,05·10^-16. tarkistus-1 4,88/1,91 eV, tarkistus-2 2,756 eV, exit 6,6·10^-19 J = 4,1 eV, 590 nm 2,10 eV, 470 nm 2,64 eV, kertaus 7,5/4,6·10^14 Hz, virhe 3,97·10^-28 J. All agree with the lesson and lesson-answers.py ✓.
- "energia" figure measured from its coordinates (60,1 px/eV): the arrows are 1,91, 2,28 and 3,05 eV, so it is to scale ✓. "kuvaaja" figure: the Na and Zn lines start at 5,51 and 10,42·10^14 Hz and reach 4,34 and 2,31 eV at 16·10^14 Hz. The slope triangle (4·10^14 Hz, 1,655 eV) lies on the Na line and its slope is h ✓. "ilmio" figure and hero: 254 nm is above Zn's work function and 650 nm below it, and both figures say they are not to scale ✓.
- sim.js: E = hc/λ; electrons are emitted if and only if E ≥ W; Ek = E − W; n = 0,4·I and does not depend on λ. The energy panel is to scale. The light is drawn in its approximate spectral colour, as intended, with UV shown as violet; howto says so ✓. The model box gives the model's limits: its quantum efficiency, that intensity means photon rate, that work functions depend on the surface, and that the readings are model values ✓.
- koe-1/2/3: the initial and locked values isolate the varied parameter, and simState holds E, Ek and n ✓. In koe-3 the 5 nm step places the threshold between 540 and 545 nm, and the answer tolerance of 2 % accepts a value read from the table ✓.
- Predictions, tarkistus-1 and virhe: each has exactly one correct option, and each distractor's feedback is right ✓.
- Conditions are stated: no gathering of energy from several photons "tavallisessa valossa"; E_k,max refers to the most weakly bound electrons; the intensity–photon-count link holds "samanvärisellä valolla" ✓.
- The model answers for johtopäätös and tarkistus-3 and the exit ticket say what the theory says and use model values ✓.
- Scope is within FY8 (energy quantisation, the photon, E = hf, eV conversion by substitution). There is no de Broglie wavelength ✓.
