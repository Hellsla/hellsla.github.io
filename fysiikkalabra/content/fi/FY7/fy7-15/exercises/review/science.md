VERDICT: PASS
CONTENT-HASH: 3d1522308c46aedd

## Blocking

## Polish
- content/fi/FY7/fy7-15/exercises/solutions.md:58 (L2-01 Vastaus) — "kolme merkitsevää numeroa kuten kulma 40,0°": 900 W/m² is ambiguous (round 1, still open). Optional: name the angle as the limiting datum "(900 tulkitaan tarkaksi)".
- Scope (round 1, still the teacher's call): the numeric Malus tasks go past "polarisaatio kvalitatiivisesti".

## Checked
- Round-1 fixes: L1-04 now uses acrylic (n = 1,49), so α_B = 56,13° → 56,1°. The taitekulma 33,87° and the Snell check 0,830 = 0,830 are correct. L1-05 now compares with acrylic's 56,1°. The answers.py comment for L1-05 now reads 67,5°.
- One script recomputed all twelve answers from the task text with my own formulas (L2-04 by Snell's law), and all agree with exercises.json and answers.py: 320; 150; 9,358; 56,13°; 67,55°; 264,07; 60,0°; 1,5697; 33,69°; 75,0; 36,94°; 117 lx.
- L3-01: the angle to the last sheet is 60°, and the 45° maximum of 100 W/m² is a real check.
- L3-02 (light from water): n₁ = 1,33 is right, α_B = 36,9° is below the critical angle of 48,8°, and the reversibility argument is correct.
- L3-03: the task states the background-plus-Malus model with its assumptions (the background does not depend on the film's angle, an ideal film, a reading proportional to intensity), and the solution uses the same model.
- Every solution has the seven steps and solves for the unknown symbolically first. The units, the realistic data (plastics 1,49–1,58, diamond 2,42) and the rounding are right.
