VERDICT: FAIL
CONTENT-HASH: 53b65d35068d0826

## Blocking
- content/fi/FY7/fy7-14/exercises/exercises.json:186–232 (L2-07 data) and solutions.md:141, 145–146 — A, the data are impossible for the stated coating. A single MgF₂ layer (n = 1,38) on glass of n = 1,52, built as a quarter wave for 540 nm, has a minimum of R = ((1,52 − 1,38²)/(1,52 + 1,38²))² = 1,26 %. (the lesson says 1,3 %). At 420 nm the model gives 1,8 % and at 700 nm 1,6 %, but the table has 1,1 % at the minimum and 2,9 % and 3,2 % at the edges. The solution's "kolmanneksen tai alle" and "2,6–2,9-kertainen" rest on those numbers. The task also never gives the lens glass index, which the two-shift reasoning needs (B) — fix: state "lasin taitekerroin on 1,52". Replace R with model values for 420, 460, 500, 540, 580, 620, 660, 700 nm: 1,84; 1,48; 1,31; 1,26; 1,30; 1,39; 1,50; 1,64 (two decimals keep the minimum at 540 nm). Reword the solution: about 1,3–1,5 times more violet and red than green.
- exercises.json:266 (L3-04 b) and solutions.md:184–185 — B: "on ensimmäistä kertaa kokonaan kumoutunut". Air–oil reflects with r = 0,19 and oil–water with r = 0,05, so the destructive minimum still reflects about 2,0 % (bare water reflects 2,0 %). The task's own solution c) says complete cancellation does not happen — fix: "heijastuu ensimmäistä kertaa heikoimmin (heikentävä interferenssi, 2nd = kλ)". The answer of 360 nm is unchanged.

## Polish
- L3-04 c "lähes mustalta" — a very thin oil film reflects about as much as bare water (2,0 % against 5,8 % at a maximum), so "värittömältä kuten pelkkä vesi" is better.
- L2-05 — the model goes through the origin (n = 1,333 that way, 1,315 with a free fit); both fall within the tolerance.
- L3-05 — 3 significant figures is weak with L = 80 mm; the air wedge is not in the plan (pedagogy).

## Checked
- All 19 answers recomputed in one script: exercises.json, answers.py and mine agree (L1-07 96,94 nm, L1-08 1,5, L2-05 1,315, L2-06 443,3 nm, L2-07 97,83 nm, L3-04 360,0 nm, L3-05 12,42 µm).
- L2-06: 665 nm is destructive with one shift; 443 nm is the only visible maximum.
- L3-04: one shift; maximum 529,2 nm, minima 661,5 and 441 nm; Δd = 90 nm.
- L3-05: one shift, so the contact line is dark; slope 1,896 mm; D = 12,4 µm.
