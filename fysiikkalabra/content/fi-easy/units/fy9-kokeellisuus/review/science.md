VERDICT: FAIL
CONTENT-HASH: e8f3c72d018fd722
SCOPE: delta: new tasks s7 (Liukukitkan mittaus) and s8 (Käämin magneettikenttä ja virhelähteet) and the changed intro; older tasks s1-s6 untouched

## Blocking
- **s8 b, criterion 3 and Järkevyys (A, causality; 7, assessment).** The text is the same as in fi. The point is given for "Ei voi tietää, pysyykö riippuvuus suorana, esimerkiksi kun käämi lämpenee", and the reason given is "suuri virta lämmittää käämin johdinta ja kasvattaa sen resistanssia". The graph is $B$ against the current. For a coil with no iron, $B = \mu_0 n I$ stays linear, and resistance changes only the voltage needed for a given current. Fix it as in fi: the point goes for noting that $4{,}9\,\text{A}$ is outside the measured range, so the coil and supply must be able to give it, and the estimate is checked by measuring.
- **s8 Yleisiä virheitä, second item (A, assessment).** "$12 : 6{,}2 \cdot 2{,}5\,\text{A}$" gives $4{,}84\,\text{A}$. That is a correct proportion and is accepted in Hyväksytään myös, so it is not a mistake. Remove or replace it.

## Polish
- s8 d: "Virta lämmittää käämiä ja muuttaa sen resistanssia" needs its effect on the result (the current drifts with a voltage-set supply, or the sensor drifts).
- s8 a Vastaus: "kaksi- tai kolminumeroisia". The values read all have two figures.

## Checked
- The S2 text matches fi in every number, answer, tolerance, criterion and point. The sentences are split shorter and are clear. "Ilmasydäminen" becomes "Käämin sisällä ei ole rautaa", which is a faithful and helpful paraphrase. Kierrostiheys is explained as kierrokset metrin matkalla. Systemaattinen and satunnainen virhe are explained in s7 a Periaate ("sama joka kerta", "vaihtelee arvaamattomasti"), and the physics of these is right. s7 a says "nollakohta on kunnossa" (the fi text says "vähintään nollakohdan osalta"); both are correct.
- Numbers recomputed in the same script as fi (figure sources fy4-6 `MITTAUS`, fy7-3 data and fit): s7 0,2152 ± 0,005, c 0,24 / 0,21 / 14,3 %, d 4,5 % and 0,93 %; s8 2,467 mT/A, 1963 1/m, 4,86 A, 3,08 % and 0,645 %. All agree with answers.py.
- Intro: "Kahdeksan tehtävää" matches. Points 14 + 14.
- `practice.py check` OK; hash the same at start and end.
