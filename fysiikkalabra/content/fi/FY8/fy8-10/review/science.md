VERDICT: FAIL
CONTENT-HASH: abb80c1fb9ef4479

## Blocking
- content/fi/FY8/fy8-10/lesson.md:178 — A: "Neljän numeron vakioilla tulos olisi 931,6 MeV" is wrong as stated. With four-figure constants 1,661·10⁻²⁷ kg, 2,998·10⁸ m/s, 1,602·10⁻¹⁹ J the result is 931,9 MeV. The 931,6 in lesson-answers.py:61 uses 1,6605·10⁻²⁷ kg, which has five figures. — fix: write 931,9 MeV, or name the constants actually used.
- content/fi/FY8/fy8-10/lesson.md:276 — B: "elektronien määrä on molemmin puolin sama … beeta miinus -hajoamisessa". This holds only if the emitted electron is not added on its own: the daughter atom (Z+1 electrons) already contains it. A student who adds m_e is off by 0,511 MeV. — fix: add "(beeta miinus -hajoamisessa syntyvän elektronin massaa ei lisätä erikseen)".
- content/fi/FY8/fy8-10/inquiry.json:376 (tarkistus-3 criterion) — A: "ydinreaktiossa noin 10⁻³ tai enemmän". A reaction's relative mass change is 1,9·10⁻⁵ in the lesson's own U-238 alpha decay and about 10⁻³ in fission. The 0,8 % in the model answer (:373) is helium-4's mass defect (binding), not a reaction's mass change. — fix: "ydinreaktiossa noin 10⁻⁵–10⁻³, miljoonia kertoja enemmän". In the model answer, call the 0,8 % the binding mass defect, or cite the D+D → He-4 reaction (0,64 %).

## Polish
- lessons/FY8/fy8-10/lesson-answers.py:1148 (NUCLIDES, same in sim.js) — From memory I cannot confirm W-184 183,950933 (I recall …931), Au-197 196,966570 (…569), U-235 235,043928 (…930) or U-238 238,050787 (…788). They may be off by up to 2 µu. The effect is ≤ 1·10⁻⁵ MeV per nucleon, so no displayed number changes. — check against the AME2020 file when online.
- content/fi/FY8/fy8-10/lesson.md:178 — "pieni pyöristys näkyy jo neljännessä numerossa" will follow whatever fix is made above. Make the sentence say that four-figure constants shift the fourth digit.

## Checked
- All 37 atomic masses in lesson-answers.py match sim.js exactly. 33 of them agree with my AME2020 recollection to ≤ 0,5 µu (H-1, n, H-2, He-3/4, Fe-56, Ni-62, Th-234, Po-210, Pb-206 among them).
- 1 u → MeV: 1,66054e-27 · (2,99792e8)² = 1,49241e-10 J; ÷ 1,602177e-19 = 931,49 MeV ≈ 931,5. Every step is right, and c² cancels correctly in the substitution.
- Every E_B/A in the feedback, the model answer and sim-spec (1,112; 7,074; 5,607; 7,680; 7,976; 8,790; 8,795; 8,554; 7,868; 7,570) recomputes exactly. U-238 E_B is 1801,7 MeV and Fe-56 is 492,3 MeV.
- U-238 alpha decay: 0,004583 u, 4,27 MeV (literature 4,270). Po-210 transfer task: 5,408 MeV, alpha share 5,30 MeV (measured 5,304). The mistake values 3734 and −5,408 are right.
- Etsi virhe: 92,16 MeV, and the wrong result 8,3·10¹⁸ is right. The unit argument is right.
- tarkistus-2: exactly one option releases energy. The curve values in the feedback are right.
- Carbon burning: 4,4·10⁻¹² kg, ratio 1,0·10⁻¹⁰.
- Exit ticket: Bi-209 7,85 MeV and Ca-40 8,55 MeV per nucleon. The table gives 1640,2 MeV and 342,06 MeV.
- Electron binding: under 1 MeV total even for U, so under 10⁻³ of E_B (type C). The surface and Coulomb causes on the curve are type C.
- sim.js computes Δm = Z m_H + N m_n − m, rounds to µu and uses ×931,5. simState carries dm, EB and EBA for both experiments. The limits are stated in the model box.
