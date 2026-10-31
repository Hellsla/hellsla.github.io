VERDICT: PASS
CONTENT-HASH: 7646d6b7c3a92e84

## Blocking
(none)

## Polish
- solutions.md fy1-3-L2 (line 59) — "kuten virhearviossa" next to "suhteellinen epävarmuus" elsewhere; the lesson writes both "virhe-arvio" and "virhearvio". Pick one spelling for the whole set (the lesson text decides).
- solutions.md fy1-3-L3-02 Vastaus — "Siinä on yksi merkitsevä numero" is right for 2 µm, while exercises.json stores 2.0 (tolerance 0.02); a student answering 2 is inside the tolerance, so no fix is needed, but "2,0" in Sijoitus and "2" in Vastaus may puzzle a reader. Add "(0,0020 mm pyöristetään)" or write 2,0 in both.

## Checked
- Delta review: the diff (terminology "suhteellinen virhe" to "suhteellinen epävarmuus" in L2 Periaate and L3-02 Järkevyys, plus two figures.json descriptions) read in context. The terms now match the lesson, glossary and Kaava (ε, "suhteellinen epävarmuus").
- L3-02 Järkevyys recomputed: 2 µm / 100 µm = 2 %; 0,5 mm / 0,1 mm = 500 %; stack of 250 gives the 250-fold reduction. The rewritten sentences are shorter and clear: the "500 %" is now said to be of the sheet's thickness, which was missing before.
- The task text still asks for "virhe-arvio", the solution answers it, and the Järkevyys step uses epävarmuus for the relative size: consistent, no leftover "suhteellinen virhe" in solutions.md or exercises.json.
- Figure `fy1-3/pendulum-dots`: description gives the five values and the axis; neither gives the answer away.
- Phone captures of the exercises do not exist yet; not judged.
