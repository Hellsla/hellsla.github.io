VERDICT: PASS
CONTENT-HASH: 6e26a08a08a64312
SCOPE: delta (round 2): new tasks fy9-aallot-s7 and s8 (figures fy5-12/ruudukko-tehtava, fy5-13/kuvio-tehtava) and the changed intro; s1-s6 not re-judged. Language: en; fidelity to fi checked for en and fi-easy.

## Blocking
(none)

## Polish
- s7: the task text says the loudness difference from the unequal distances is ignored, yet the c model answer adds "not completely silent because the farther loudspeaker is heard more weakly". Physically right, but mildly at odds with the stated simplification; one clause could say "in practice".
- s8 d: the model answer could add that off resonance the string settles to a small-amplitude forced vibration at 20 Hz (it says "small amplitude", which is correct).

## Checked
- Round-1 blocking items verified fixed in tasks.json and solutions.md: s7 a (two sf from the 0,50 m square side; counts exact), s7 b (three sf from f = 343 Hz; 343,4 has four), s8 a (0,600 m three sf from L = 1,20 m; loop count exact). s8 c now says tension and mass per unit length. en decimal points are periods throughout.
- Recomputed: s1 = 12*0,50 = 6,0 m; d = 2,5 m; s2 = sqrt(42,25) = 6,5 m; Δs = 0,50 m (12:5:13 triangle). λ = 343,4/343 = 1,0012 m; Δs/λ = 0,499 (destructive for in-phase sources); next maximum Δs = λ gives f = 343,4/0,50 = 686,8 Hz ≈ 690 Hz (answer 687 Hz, 2 % tolerance), consistent with 2*343 Hz.
- s8: λ = 2*1,20/4 = 0,600 m; v = 50*0,600 = 30 m/s; f3 = 3*30/(2*1,20) = 37,5 Hz ≈ 38 Hz (2 sf limited by 30 m/s); f1 = 12,5 Hz, f2 = 25 Hz; 20/12,5 = 1,6 loops; λ(20 Hz) = 1,5 m. Speed fixed by tension and linear density, unchanged.
- MAFY constant: 343,4 m/s at 20 °C stated in the task text; speed of sound 343 m/s at nominal. Standing-wave conditions (nodes at both ends, L = nλ/2, f_n = nv/(2L)) correct. Scope is FY5 interference and standing waves; no content beyond.
- FY9 wording: command words and "Perustele" used correctly; rubric points s7 4+2+3+3 = 12, s8 3+3+4+3 = 13; criteria sum to part points; practice.py check OK for all three languages (8 tasks, 120 points). Intro says eight tasks, matching.
- Fidelity: en and fi-easy tasks and solutions carry the same numbers, reasons and conclusions as fi.
- Content hash 6e26a08a08a64312 at start and end, unchanged.
