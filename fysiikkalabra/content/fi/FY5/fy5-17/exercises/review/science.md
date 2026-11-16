VERDICT: PASS
CONTENT-HASH: 16bb16e0f37b499a

## Blocking

## Polish
- content/fi/FY5/fy5-17/exercises/exercises.json:348 (L2-10) — the answer is still stored as 11.905 (five figures), but the solution gives 12 s with two figures. The 3 % tolerance accepts both. — Store 11.9, or say in the solution that 12 is accepted in the box.
- content/fi/FY5/fy5-17/exercises/exercises.json:347 (L2-10 text) — "sivun asteikolla Suomen maanjäristykset ovat välillä 0–4" reads as though the page has its own scale. The source says only that Finnish earthquakes are of magnitude 0–4. — Write "sivun mukaan Suomen maanjäristysten magnitudit ovat välillä 0–4".

## Checked
- The hash was the same at the start and at the end. Round 2. `git diff 09d57eb5ac..HEAD` changes only L2-10. Its text adds that the tables hold natural earthquakes only, what a magnitude is, and in c) the km per second of lag. In the solution, a) has a new preliminary-results sentence, the Vastaus has 8,4 km per second, and d) is split into paragraphs. No line of answers.py changed.
- Round-1 Blocking is fixed. The 2026 table's heading has an asterisk, and results not yet in FENCAT are preliminary analysis results. This now follows the verbatim quotation in the additions, and "arvot voivat vielä tarkentua" is a fair consequence of it.
- "Natural earthquakes only, no induced ones" agrees with "Taulukot eivät sisällä … indusoituja maanjäristyksiä", and the source notes put the blasts on the map service. So "mikä tahansa rivi kelpaa" is right.
- Round-1 Polish on the link's place is settled. The additions confirm that the link is at the end of the main page.
- New numbers recomputed: Δt = 100/3,5 − 100/6,0 = 11,905 s. One second of lag is v_P v_S/(v_P − v_S) = 21/2,5 = 8,4 km = 100 km/11,905 s. 2 km corresponds to 0,238 s, so 0,24 s is right.
- Magnitude as a number computed from seismograms that tells how strong the earthquake is: a correct definition for this level.
- The unchanged exercises rest on the round-1 recomputation of all 23 numeric answers (round-1 report, hash 7b8809a307253ebd).
