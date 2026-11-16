VERDICT: PASS
CONTENT-HASH: 3e3a82389aa5eced

## Blocking

## Polish
- solutions.md:253 (fy6-13-L2-09, Kohta d) — check that the chapter *Lähdejännite ja sisäinen resistanssi* exists under this title in FY6. A wrong title only leaves a broken reference.
- solutions.md:253 (fy6-13-L2-09, Kohta d) — "eikä latauksessa tai purkautumisessa tapahdu kemiallista reaktiota" holds for the plate capacitor of the chapter. Pseudocapacitive supercapacitors do use surface reactions, so "tässä mallissa" or "levykondensaattorissa" would keep it exact (C, not blocking).

## Checked
- One independent script recomputed all 20 numeric answers (L2-05 and L3-04 as fits through the origin, L3-05 ratio 6,89) and compared them with exercises.json: all are inside tolerance.
- L2-09 b): W = ½QU with Q = CU gives W = ½CU² = 72 mJ. 1000 µF is treated as exact and 12 V as two significant figures, which is justified. The check through ½QU and the unit F·V² = J are real checks.
- L2-09 c): (2U)² gives 4W = 0,29 J. The causal explanation (charge doubles and moves across twice the mean voltage) is right.
- L2-09 a): Q ∝ U at fixed geometry; C ∝ 1/d from C = ε₀ε_rA/d (the brief's formula and its conditions). With the battery connected, Q falls when d grows; that is correct. The example 0,44 pF and 0,22 pF (A = 2,0 cm², d = 4,0 and 8,0 mm) and 0,66 pC at 1,5 V recompute correctly. It is marked as a calculation, not a simulation reading, and its values lie in the simulation's ranges.
- L2-09 d): energy in the field versus chemical energy; 3,85 V · 5,0 Ah = 19,25 Wh = 69 300 J, about 9,6·10⁵ times. The uses named (flash, smoothing, regenerative braking with supercapacitors; phone, e-bike) are sound.
- No exponential function and no capacitor connections appear, as the scope notes require. The notation W for energy and E for field matches the brief.
- Reflowed chains (L2-08 and others): same numbers, signs and units in the same order.
- Hash read at start and end: unchanged.
