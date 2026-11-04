VERDICT: FAIL
CONTENT-HASH: d63da7091321ba6b

Exercise-bank round: 8 new tasks reviewed in full; old tasks unchanged.

## Blocking
- solutions.md:133 and exercises.json:80 (fy3-13-L1-07) — A: the rounding rule taught is wrong. A sum is limited by its least precise term: −195,8 °C is given to 0,1 °C, so T = 77,4 K, not "77,35 K, kaksi desimaalia, sillä 273,15 ei pyöristetä ja −195,8 on annettu kymmenesosan tarkkuudella" (the reason contradicts the result). — Fix: answer 77.4; Vastaus "$77{,}4\,\text{K}$, kymmenesosan tarkkuudella kuten $-195{,}8\,{}^\circ\text{C}$; tarkka $273{,}15$ ei rajoita"; Sijoitus "= 77,35 K ≈ 77,4 K"; answers.py round(…, 1).

## Polish
- solutions.md:160 (L2-06) — sig-fig reason contradicts itself ("kolme numeroa, koska … kulmakerroin kahteen numeroon"). With k = 0,33 (2 numbers) the honest result is ≈ −3,0·10² °C; say "−302 °C, mutta vain noin kahden numeron tarkkuudella (k:ssa kaksi numeroa)".
- solutions.md:196 (L3-05) — "kolme numeroa kuten kalibrointipaineissa": the limiting datum is the difference 94,0 − 100,4 = −6,4 kPa (two numbers); with Δθ ≈ 2,7 °C, write −17 ± 3 °C or justify the extra digit from the uncertainty.
- solutions.md:130 (L1-07) — $T = \theta + 273{,}15\,\text{K}$ mixes a °C value and K; use the brief's $T = \theta + 273{,}15$.
- exercises.json:74 (L1-07) has kind "concept" though it is a numeric substitution; exercises.json:154 (L2-05) has kind "graph" but neither figure nor graph-reading step.
- solutions.md:139/161/186 — "toistaminen pienentää satunnaisvaihtelua" (say "keskiarvon satunnaista virhettä"), "välillä 75 °C" (→ "75 °C:n levyiseltä väliltä"), "Ääriviivat osuvat kumpikin samaan keskimääräiseen nollapisteeseen" (→ "Sarjojen välien keskikohdat ovat lähellä toisiaan").

## Checked
- One script recomputed every new answer: L1-07 77,35 K; L2-05 sums 250 / 588,9, centroid (50; 117,78), θ0 = −274,46 °C, and the least-squares slope of the data is exactly 0,363; L2-06 B −302,2 °C, A's LS fit −269,6 °C (stated −270, residual at 95 °C 0,13 kPa); L2-07 −370 °C, steps 6,6/5,4/4,0 kPa, first-two-point line −295 °C, ideal 125,3 vs 120,0 kPa; L3-04 A −242,5/−302,0 → 29,75, B −258,44/−279,90 → 10,73 °C, midpoints −272/−269; L3-05 k = 0,366, −17,49 °C, Δθ 2,73 °C.
- L1-06, L1-08: exactly one correct option, feedback right; motion does not stop at 0 K (guardrail).
- L2-07 leak mechanism (gas escapes on heating, slope falls) right; data consistent with ≈4 % loss.
- L3-04 extreme lines as in the brief's lesson; data close to ideal-gas values (129,7 / 180,4 kPa).
- Levels and plan coverage fit (fitting-range comparison, leaking vessel, extreme-line uncertainty); renders of new L3 tasks without overflow.
