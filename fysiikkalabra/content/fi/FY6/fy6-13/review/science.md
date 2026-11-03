VERDICT: FAIL
CONTENT-HASH: 011b4e99d4a6ac33

## Blocking
- lesson.md:265–271 and :332 — B: C = ε0εrA/d and "kapasitanssi kasvaa εr-kertaiseksi" are stated without their conditions: the gap is small compared with the plates (homogeneous field, edge effects ignored), and the dielectric fills the whole gap. The sim's model box says both, but the theory does not. — fix: add after the formula "kun levyjen etäisyys on pieni levyjen kokoon verrattuna ja eriste täyttää levyjen välin", and at :332 "eristelevy, joka täyttää levyjen välin".

## Polish
- inquiry.json:103 (ennuste-2 feedback) — "lasin suhteellisen permittiivisyyden 5,6 verran pienemmäksi" reads as minus 5,6. — fix: "5,6-kertaisesti pienemmäksi" or "1/5,6-osaan".
- lesson.md, Esimerkki Tulos — W = 6,8 J is justified by "kuten purkautumisajassa 1,0 ms", but W does not depend on t. — fix: justify W by C and U, and P by t.
- inquiry.json:533 (tarkistus-1) — the "paksumpien levyjen" distractor is right only when the gap d stays the same. The feedback implies this, but the option could say it.

## Checked
- Dielectric table: εr and E_max are air 1,0 / 3 MV/m, teflon 2,1 / 60, paper 3,7 / 16, glass 5,6 / 14. These are the standard textbook values (Serway/Halliday; glass = Pyrex), and "likimääräisiä" is stated. Polystyrene 2,6 / 24 MV/m in the exercises is also standard. Accepted.
- Every number recomputed: C = 88,5 pF; 11 → 44 µJ; Q 44 → 89 nC; glass disconnected 0,179 kV and 7,9 µJ; example 6,75 J and 6750 W with 3,4 s at 2 W; paper 160 V; virhe 0,034 J and its distractors; siirto 190 µJ and its mistakes; TV 12 J; kertaus 150 kV/m; exit 1,2 mC.
- The connected and disconnected table (U, Q, W) is correct, including the field pulling the slab in.
- Charging and discharging are qualitative only (no exponential), as the approved plan requires. The current direction reverses on discharge. Each checks item has exactly one correct option.
- The half-of-QU heat loss is stated for charging through a resistance.
- sim.js: Qheld is captured at disconnection (the koe-3 screenshot shows 88 nC with air). Breakdown for E > E_max is at 3,1 kV for 1 mm of air. The polarised molecules show their negative half toward the + plate. W = ½QU.
- Polarisation, energy-in-field and breakdown mechanisms are right at this level. W is the capacitor-energy symbol, E is the field and \overline{E} is green.
