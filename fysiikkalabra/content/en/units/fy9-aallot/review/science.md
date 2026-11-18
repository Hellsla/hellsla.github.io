VERDICT: FAIL
CONTENT-HASH: 050bccd79e623421
SCOPE: delta: new tasks fy9-aallot-s7 and s8 with their figures and the changed intro; s1–s6 not re-judged; fidelity to fi checked.

## Blocking
- **A, significant-figure reasons stated wrongly (rounding to data precision)** (same in en):
  - s8 a Vastaus: "kaksi merkitsevää numeroa kuten silmukoiden lukumäärässä ja pituudessa". The length read off the ruler, 1,20 m, has three significant figures and the loop count is exact, so λ = 0,600 m by the data; give 0,600 m or a correct reason.
  - s7 b Vastaus: "kolme merkitsevää numeroa kuten nopeudessa": 343,4 m/s has four; the three come from f = 343 Hz.
  - s7 a Vastaus and the a `units_precision` criterion: "kuten ruutujen lukumäärissä": counts are exact; the two figures come from the square side 0,50 m.

## Polish
- s8 d model answer: off resonance the string settles to a steady forced vibration at 20 Hz with small amplitude; "epäsäännöllisellä" describes only the transient.
- s8 c criterion and solution: the speed depends on the tension and the mass per unit length (not "massasta"); harmless here since the string is unchanged.
- s7: 343,4 m/s is MAFY's value (20 °C); the text could name the temperature.
- (en) solutions.md s7 and s8 use decimal commas (`0{,}50`, `343{,}4`, `686{,}8`) while en tasks.json and en s1–s6 use decimal points. Make it uniform.

## Checked
- Geometry from speaker_grid() (36 px squares): S1 (0,0), S2 5 squares up, P 12 right → s1 = 6,0 m, s2 = √42,25 m = 6,5 m, Δs = 0,50 m.
- λ = 343,4/343 = 1,0012 m; Δs/λ = 0,499 (destructive, in-phase sources); next maximum Δs = λ → f = 686,8 Hz ≈ 690 Hz (2 sf from 0,50 m), answer 687 Hz ±2 %; reasoning 2·343 Hz consistent.
- String figure: sin(4πu) over 0…1,20 m, five nodes incl. ends → 4 loops; λ = 0,60 m, v = 30 m/s, f3 = 3v/(2L) = 37,5 Hz ≈ 38 Hz, f1 = 12,5 Hz, f2 = 25 Hz, 20/12,5 = 1,6 loops, λ(20 Hz) = 1,5 m; Hyväksytään myös correct.
- Standing-wave conditions (nodes at both ends, L = nλ/2, f_n = nv/(2L), v fixed by the string) correct.
- Rubric points: s7 4+2+3+3 = 12, s8 3+3+4+3 = 13, criteria sum to part points; practice.py check OK (8 tasks, 120 points). Intro: eight tasks, matches.
- Scope: FY5 interference and standing waves; nothing beyond. My script and answers.py agree on every s7/s8 value.
- Hash identical at start and end.
