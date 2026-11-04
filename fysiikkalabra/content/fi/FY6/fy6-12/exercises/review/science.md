VERDICT: FAIL
CONTENT-HASH: 88e6763624511d13

## Blocking
- exercises.json:209 and :217, solutions.md:158 (fy6-12-L2-06) — (B) the condition "from rest" is missing, which leaves a force-equals-velocity picture. Feedback "positiivinen varaus liikkuu aina kentän suuntaan" / "liikkuu aina kohti pienempää potentiaalia" and the model answer "Suurempaan potentiaaliin positiivinen varaus pääsee vain, jos jokin ulkoinen voima tekee työtä" are false for a moving charge. See L3-03: a proton climbs on its kinetic energy. — Fix: write "kiihtyy aina kentän suuntaan" / "levosta lähtiessään liikkuu kohti pienempää potentiaalia" (the lesson's Tiivistelmä wording: "lähtee liikkeelle"). In the model answer, write "...pääsee vain, jos sillä on liike-energiaa tai ulkoinen voima tekee työtä".
- solutions.md:147-148 (L2-05) vs exercises.json:152 — the task says "Sovita ... origon kautta kulkeva suora ja laske sen kulmakertoimesta E", but the solution never fits a line. It takes the mean of the raw ratios V : x (guardrail: slope from the fitted line, not raw points). — Fix: either draw the origin line and read its slope from a point on it, e.g. (5,0 cm; 25,1 V): E ≈ 5,0 V/cm = 5,0e2 V/m, U ≈ 30 V (least squares 30,1 V). Or reword a) to "laske suhde V : x jokaiselle pisteelle ja niiden keskiarvo".

## Polish
- solutions.md:168 (L2-07) — "6,7e-27 kg ... kolme merkitsevää numeroa" shows two significant figures. Write 6,66e-27 kg.
- solutions.md L2-05, L3-05 — "Kuvaajan lukeminen" with a table only. Use "Taulukon tulkinta".
- docs/exercise-bank/FY6.md fy6-12 Taso 2 — the planned V(x) graph task for two situations was replaced by the ion-mass data task L2-07. Update the plan line.

## Checked
- Hash 88e6763624511d13 at start and end. All new numeric answers recomputed in one script: 900 eV; 30,2 V (fit 30,1 V); 6,66e-27 kg (v²–U fit 6,69e-27); 2,78 mm (= U_p L² : 4 d U_k); 4,14e6 m/s. All agree with answers.py and exercises.json.
- L1-06, L1-07: exactly one correct option, and the feedback is right.
- L2-07: per-row masses 6,77 / 6,47 / 6,68 / 6,63 / 6,75 e-27 kg, so the ion is He+.
- L3-04: v = 2,52e7 m/s (8 % of c, classical model fine). y = 2,78 mm < 7,5 mm. F : mg = 1,4e14.
- L3-05: retarding-grid logic right (an electron passes if E_k ≥ eU_v). Bins 2 / 27 / 49 / 19 / 3 % add up to 100 %. Mean 48,8 eV.
- Scope: uniform field only, E_p = qV, W = qU, eV. No point-charge potential. No duplicates.
