VERDICT: PASS
CONTENT-HASH: 8c528e6b3d93aece
SCOPE: delta added-exercise from 2af3ee47b4394d1d base 81db4a6fd727

## Blocking

## Polish
- content/fi/FY4/fy4-4/exercises/solutions.md (L1-09) — the Periaate names the force diagram but shows none. A ```voimakuvio block with F up and G down, like the set's other force tasks, would follow the chapter's "Ensin voimat, sitten yhtälö".

## Checked
- L1-09: g_Kuu = 1,622 m/s² is the VERIFIED fy4-4 row of docs/mafy-arvot.tsv. The hint names only the table ("Aurinkokunta"). The model is stated: only weight and thrust act, and a = 0,50 m/s² upward while descending. Upward is positive, F − mg = ma, so F = m(g + a) = 31,83 kN. Two significant figures (32 kN) are justified by 0,50, and the hover check (24 kN) is a real one.
- L1-10 (fy4-4/kuvaaja-ab): A's points (1; 2), (2; 4) and (3; 6) sit on grid intersections, so m = 3,0 N : 6,0 m/s² = 0,50 kg, and 2 % fits.
- L2-09: B's point (3; 3) gives m_B = 1,0 kg, and a = 2,4 N : 1,0 kg = 2,4 m/s². The task makes the student go through the mass, since 2,4 N is between grid lines. Not the same as L1-10 (other cart, other quantity), nor L1-03 (data given in numbers).
- Neither figure task gives its answer away: the description lists the points but no masses.
- Notation as in the chapter: ΣF on the axis, m, a, and $\overline{F}$/$\overline{G}$ for vectors.
- Recomputed in one script (my formulas beside python -I answers.py): 31,83 kN, 0,50 kg and 2,4 m/s². All three agree with exercises.json.
- Scope: Newton's second law and G = mg, both from this chapter and the one before.
- Hash 8c528e6b3d93aece at the start and at the end.
