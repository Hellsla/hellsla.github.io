VERDICT: FAIL
CONTENT-HASH: 4465c40cddfece9f
SCOPE: delta: new tasks s8 (Betoniseinä) and s9 (Galaksien etääntyminen) and the changed intro; older tasks s1-s7 untouched

## Blocking
- **A (causality), s8 d Oletukset:** "Lähteen aktiivisuuskaan ei pysy vakiona. Siksi oikea seinä kannattaa tehdä tulosta paksummaksi." A decaying source gives a *smaller* dose rate over time, so the reason points the other way. Keep the scattering reason; replace this one with a reason that really raises the dose (voimakkaampi tai vaihdettu lähde, pidempi oleskelu) or drop it. Same error as in fi.
- **Assessment (7), s8 d criterion 4 (transfer, 1 p):** d asks only the least thickness. The criterion scores naming an assumption, which d does not ask, and "annosnopeus on vakio" is given in the task text. Ask for it in d or move the point.
- **B (6, consistency), s9 c:** the Periaate "Oletetaan, että galaksi on liikkunut ... ja lähtenyt samasta paikasta kuin muut" (part text "jokainen galaksi on liikkunut koko ajan samalla nopeudella", criterion 1 "kulkenut matkan d") is the explosion-from-a-point picture that s9 d's model answer, its Yleisiä virheitä ("kuin räjähdyksen sirpaleet") and the chapter *Maailmankaikkeuden kehitys* reject. Say it with distances: "galaksien väliset etäisyydet ovat kasvaneet nollasta koko ajan samaa tahtia", t = d/v = 1/H0.

## Polish
- s9 a: the text gives the grid point (250 Mpc; 18 000 km/s), so the graph_read point is earned by copying it; the alt-text already carries it.
- s9 d criterion 2 requires "avaruus itse laajenee"; the no-centre argument is criterion 1. Consider accepting either.
- s8 a: (20 cm; 5,0 µSv/h) is near the axis of a linear graph; ±0,5 µSv/h reading gives µ = 0,134-0,144 1/cm, outside the 3 % tolerance. (10 cm; 20 µSv/h) is more robust, or widen the tolerance.

## Checked
- Read the fi-easy tasks.json entries and solutions of s8 and s9 and the intro in this language's packet. Every number, unit and rounding is the same as in fi (0,14 1/cm, 6,6 µSv/h, 330 h, 2,2 mSv, 3,03 µSv/h, 23,6 -> 24 cm rounded up; 72 km/s/Mpc, 120 Mpc, 2,333e-18 1/s, 4,286e17 s, 1,358e10 a); criteria, common mistakes and accepted methods mean the same as in fi. The split into short sentences keeps every physical reason (exponential law: same factor per equal thickness; why d rounds up; why 1/H0 is rough).
- One script (scratchpad rc_moderni.py) recomputed all numbers from the figures' own data (80 µSv/h, half-value 5,0 cm; H0 = 72, nine points) beside answers.py: all agree.
- Physics and scope as in fi (FY8); points 13 and 13, criteria sum to part points.
- Intro: nine tasks; the facts are those of fi.
- practice.py check OK; hash the same at start and end.
