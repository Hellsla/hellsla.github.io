VERDICT: FAIL
CONTENT-HASH: d5bac6dee83b4a91

## Blocking
- lesson.md:166 — (A) "Pyörivässä käämissä vuo vaihtelee siis koko ajan tasaisesti arvojen $BA$ ja $-BA$ välillä": *tasaisesti* has moved from the rotation to the flux, so the sentence now says the flux changes at a steady rate (linearly). That is the very misconception the next section refutes (the flux changes fastest at Φ = 0 and hardly at all at Φ = ±BA). The Finnish original says "tasaisesti pyörivässä käämissä". — Fix: "Kun käämi pyörii tasaisesti, vuo vaihtelee koko ajan arvojen $BA$ ja $-BA$ välillä."
- inquiry.json:19 (hook) — (A) "Kaikki verkon voimalaitokset pyörivät samassa tahdissa" says that every power plant rotates at the same rate. The same hook says the wind rotor turns once every five seconds, and lesson.md says that a frequency converter decouples the turbine from the grid. In the original, the plants "tahdistuvat samaan taajuuteen 50 Hz", i.e. their voltage has the same frequency. — Fix: "Kaikki verkon voimalaitokset tuottavat jännitettä samalla taajuudella $50\,\text{Hz}$."

## Polish
- lesson.md:164 — "muuttaa pyörimisen sähköksi": the glossary has "sähköenergiaksi". "muuttaa pyörimisliikkeen energian sähköenergiaksi" is more exact.

## Checked
- Every number in lesson.md, inquiry.json, exit-ticket.json and figures.json is the same as in the Finnish version (multiset comparison). The correct flags, reveal, initial, locked and vary values and the measure keys are identical.
- Recomputed: worked example e₀ = 6,786 V and U = 4,798 V; sim e₀ = 1,26 / 2,51 / 5,03 V; transfer task 16,0 V with all four mistake values; kettle I₀ = 12,30 A; 325 V.
- Derivation e₀ = NBA·2πf (θ between v and B, maximum when the plane is parallel to the field) is correct.
- Effective value and P = UI; the power figure (mean ½P₀) is correct.
- Predictions: exactly one option is correct, and the feedback of each option is right.
- Experiments koe-1 and koe-2 isolate f and B respectively.
- Exit ticket and tarkistus-3 model answer agree with the theory.
