VERDICT: PASS
CONTENT-HASH: c56ea1f6766e2d73

## Blocking
- none.

## Polish
- solutions.md fy2-1-L2-01 Järkevyys — "mikä sopii sähkömoottorille, joka on paljon polttomoottoria tehokkaampi" is an efficiency comparison the lesson does not teach, and was already flagged; the diff touched this very line (lämpöä to lämpöenergiaa) but left it. Replace with "ja loput on lämpöenergiaa, jota syntyy aina".
- exercises.json fy2-1-L3-03 and L3-02 — contexts still repeat the lesson's check-1 (reactor chain) and data task (bouncing ball); earlier Polish, untouched by this diff.
- solutions.md fy2-1-L2-02 Vastaus — "kaksi merkitsevää numeroa kuten liike-energiassa $2400\,\text{J}$ eli $2{,}4\,\text{kJ}$" still reads ambiguously; say "kuten $0{,}60\,\text{kJ}$ ja $2{,}4\,\text{kJ}$".

## Checked
- Diff only changes wording: "syntyy lämpöenergiaa" to "muuttuu lämpöenergiaksi" (L1-02, L1-03, L2-01, L2-03, L3-01, L3-02), "lämpönä siirtyvä" for energy that goes to the water (L2-04), and "lämmöksi" to "lämpöenergiaksi" in solutions; no number, unit, answer or tolerance changed.
- The new wording is correct physics (energy converts, it is not produced) and agrees with the lesson's vocabulary; each task still has one clear question as its last sentence.
- L2-04 "veteen lämpönä" correctly uses heat as energy transferred; $360 - 331 = 29\,\text{kJ} = 29\,000\,\text{J}$ unchanged.
- L3-03 model answer now separates "siirtyy lämpönä" from "muuttuu lämpöenergiaksi", consistent with the lesson's heat vs thermal-energy distinction.
- L3-01 Järkevyys reworded sensibly; 20 J, 150 J, 130 J and 880 − 750 = 130 J all hold.
- Hash unchanged at the end.
