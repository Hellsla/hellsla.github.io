VERDICT: PASS
CONTENT-HASH: c2716084d9c1d0b9

Round 2 (delta review of round 1 fixes; round 1 hash 82147d0c9120ddde)

## Verified
1. Blocking 1 fixed: the Miksi question (source and built page) asks why the coupled wagons "jatkavat hitaammin kuin
   ennen kytkeytymistä". It no longer states the half-speed or half-energy result.
2. Blocking 2 fixed in substance. `puskurit` now asks the student to read the peak forces (80 N and 20 N) and the
   durations (0,04 s and 0,16 s). The correct option, "nelinkertainen ... neljäsosan ajasta", is not printed on
   the figure. The distractors are the real misconceptions ("peak force sets the impulse" and "longer time means more
   impulse"). The figure still carries "yhtä suuret pinta-alat". To use it against the distractors, a student must know
   that the area is the impulse, which is the concept tested. A caption-free variant would need a shared edit (see Shared issues).
3. virhe-kimpoaminen options are now 72/82/73 characters. Fixed.
4. teacher.md: in class, slow students do only *Pienvesivoimala* and *Turvavyö kolarissa*, and the explain task is homework.
   Line 29 named only *Taklaus* as homework, so I corrected it (my own edit). It now says *Pyöräilijä alamäessä* and
   *Taklaus vastakkaisista suunnista* go home, which matches the 35–55 min line.
5. Kaava: the Sovellukset display block holds $P_\text{vesi}$ and $P_\text{tuuli}$ with their symbols and conditions. Fixed.
6. tarkistus-1 correct feedback now has a "luvussa *Mekaanisen energian säilyminen ja energiaperiaate*" link. Fixed.

Task counts, points (95) and rubrics are unchanged. `practice.py check`: OK.

## Polish
- `puskurit`: once a caption-free `fy4-9/pysaytys` variant exists, switch to it.

## Shared issues
- `lessons/FY4/fy4-9/figures.py` `pysaytys`: add a variant without the "yhtä suuret pinta-alat" caption, for review units.
