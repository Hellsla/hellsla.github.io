VERDICT: PASS
CONTENT-HASH: 29b45f18108766eb

Round 2 (delta review of round 1 fixes; round 1 hash 63bd93568ec525b8). Science review of fy9-sahkokentta, 2026-11-04.

## Blocking from round 1

1. **s4, 20 kV line voltage vs. conductor-to-earth voltage: fixed.** The task text now says that the nominal 20 kV is between the phase conductors and that each conductor is about 12 kV from earth. Rubric a3, b2 and b4 use 12 kV. The solution's parts a and b use 12 kV and explain 20 kV/√3 ≈ 12 kV. Yleisiä virheitä has 4 mm and a new item for using 20 kV across the gap. answers.py has `s4-U-earth-kV` 11,55, `s4-gap-mm` 4,0 and `s4-I-body` 1,2.
   - I recomputed in Python: 20 kV/√3 = 11,55 kV; 12 kV : 3 MV/m = 4,0 mm; 12 kV : 10 kΩ = 1,2 A; 1,5 mV between the feet.
   - **A new problem from the fix, which I corrected myself:** the s4 b model answer said that 1,2 A is "satoja kertoja kammiovärinän rajaa suuremman". The chapter *Sähköturvallisuus kotona ja työssä* (fy6-15) gives about 50 mA, and 1,2 A / 50 mA = 24. The sentence now reads "kymmeniä kertoja suuremman kuin kammiovärinään riittävä noin 50 mA" (`sovella/solutions.md`, s4 b).

## Polish from round 1, verified

2. s3 c: the rubric and the Vastaus give (8,8 ± 0,3)·10⁻¹² F/m and accept 8,84 as an intermediate value.
3. s2 d criterion: now "säilyttää varauksensa, joten levyjen välillä on yhä satojen volttien jännite".
4. defibrillaattori: the Vastaus is 1,7 kV with two significant figures. I recomputed √(2·200/140·10⁻⁶) = 1690 V; the answer and tolerance are unchanged.
5. lt-5: the battery is now 3,0 V, and the only correct option is "Koko 3,0 V". The 1,9 V and 0 V distractors are still right.
6. s6 c: 5,64 kg with three significant figures in both the rubric and the solution.
- Other changed numbers that I recomputed: tarkistus-2 0,1126 J → 0,11 J (the 225,3 and 0,352 mistakes still hold); aineisto 7264 km/s.
- s1 force diagram: $\overline{G}$ points down, $\overline{T}$ runs along the thread towards the hook and $\overline{F}_\text{s}$ is horizontal, away from the other ball. All three are red, and the caption says that the angle is exaggerated.

## Checks
- `practice.py check`: OK, 6 tasks, 95 points.
- `physics_phrases`: 0 sentences.
- I built only `build.py fy9-sahkokentta`.

## Shared issues
None.
