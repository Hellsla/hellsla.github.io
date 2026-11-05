VERDICT: PASS
CONTENT-HASH: b053cd2d9ea1dacc

Science review of the Selkeä suomi translation of fy9-magnetismi-valo against content/fi/units/fy9-magnetismi-valo/ (already reviewed). Checked: unit.json, unit.md, inquiry.json, exit-ticket.json, teacher.md, sovella/tasks.json, sovella/solutions.md, figures.json.

Method: `check_i18n.py` (fi-easy: 0 errors), `practice.py check` (fi-easy: 6 tasks, 95 points, same as fi). A script compared every `$…$` formula and every number in all text files with the source: nothing is missing or changed (inquiry.json has one added `$\sin\theta$` in an explanation of "verrannollinen", which is correct). Correct options, tolerances, points and criteria are the source's. All key results recomputed in one Python call with my own formulas: 174 A / 38 % / 2,0 W; 19 mW and 35 mW; 0,45 s; 0,39 V; 9 925 K; 3,4 m; 580 nm (1 740, 348); 0,24 A; 455 A, 830 kW; 565 V/400 V, 0,225 %, 844 kW; 81,8°, 0,71 µs, 0,897 mW; k = 2,42 µT·m, µ0 = 1,268·10⁻⁶, b = 10,9 µT, 15,7 µT; 24,0° and 14,5°; 533/532 nm, 562/692 nm, x3 = 2,7 m; 18,3 MHz, 3,91·10⁷ m/s, 0,34 m, 4,37 µs, 4,5·10¹⁵ m/s². All agree.

Every sentence I compared keeps the source's physics. The added explanations are correct: "keskeisvoima eli voima, joka osoittaa ympyrän keskipisteeseen", "vastapiste on katsojan pään varjon suunta", "alkeisvaraus eli pienin vapaa varaus", "pyörrevirrat eli virrat, jotka kiertävät putken seinässä", "ferromagneettinen eli magneetti ei vedä sitä", and the verrannollinen and kääntäen verrannollinen examples (the doubling/halving examples are right).

## Blocking
None.

## Polish
1. unit.json `key_concepts` "magneettivuo": "$\Phi = BA$" is given without its condition. unit.md says "kun kenttä on kohtisuorassa pintaa $A$ vastaan". Fix: "…pinnan läpi. Kun kenttä on kohtisuorassa pintaa vastaan, $\Phi = BA$." (still under 25 words), or leave the formula out of the explanation.
2. unit.json `key_concepts` "taitekerroin": "Kertoo, kuinka paljon valo hidastuu aineessa" is acceptable with $n = \frac{c}{v}$ next to it. Clearer: "Kertoo, kuinka monta kertaa hitaammin valo kulkee aineessa kuin tyhjiössä: $n = \frac{c}{v}$."
3. unit.md Ydinajatus: "Kohdistaa tarkoittaa, että voima vaikuttaa niihin" is physically fine but loose: the field exerts the force. See pedagogy finding 1 for a better wording.
