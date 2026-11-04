VERDICT: PASS
CONTENT-HASH: 70198ef3a97a2407
Round: 2

## Blocking
(none)

## Polish
- solutions.md:218 (L3-05) — the header "Kuvaajan lukeminen" still sits over a table (carried over). Use "Taulukon lukeminen".
- solutions.md:242 (L3-05 Perustelu c) — "kaksiatomisella kaasulla vakiopaineessa työn osuus on noin 2/7" is correct (R/C_p), but it rests on C_p, which the brief does not teach. Either mark it as extra information ("Lisätieto: ...") or delete it, so the solution needs nothing beyond the lesson.
- solutions.md:161 (L2-05) and :211 (L3-04) — "kolmas numero annetaan, jotta pyöristys ei vie vastausta ulos hyväksytystä välistä" is not a physics reason, and it is not even true: 31 % and 2,7 are both inside the 2 % tolerance. Give 31 % and 2,7 as the results, with the three-digit values as intermediate values for the comparison.
- solutions.md:244 (L3-05 Järkevyys) — the volume grows 2,2-fold at constant p, so the air ends near 370 °C (T ∝ V, from about 20 °C). The data are consistent (n ≈ 0,103 mol, nC_pΔT ≈ 1,05 kJ ≈ Q), but one sentence would make the extreme heating visible, e.g. "Tilavuus kasvaa 2,2-kertaiseksi, joten ilma kuumenee voimakkaasti; tämä on ajatuskoe."
- docs/exercise-bank/FY3.md:79ff — the plan still lists a cycle pV graph (L2) and the Carnot limit (L3). Neither is in the set (carried over). Update the plan.

## Checked
- Round-1 Blocking 1 resolved: L3-05 now P = 260 W, Q = 1040 J, W_k = 300 J, ΔU = 740 J = 0,74 kJ. W_k/Q = 28,8 % ≈ 2/7, so the data fit air heated at constant pressure. The answer, answers.py, c), Vastaus and Järkevyys agree.
- Round-1 Blocking 2 resolved: solutions.md:218 now says "Paine on annettu vakioksi; tasainen nousu sopii vakiotehoiseen lämmitykseen."
- Round-1 Polish resolved: L1-08 kind is data. L2-07 has no experiment tag. L3-04 now explains why ε falls in frost.
- One script recomputed every new answer from the task text: L1-08 3,25; L2-05 31,40 % (21,2/28,9/31,4/29,8); L2-07 20,9 kWh; L3-04 2,743 (mean 2,88, saving 8,7 MWh, 64 % from outside air); L3-05 0,740 kJ. All agree with exercises.json and answers.py within tolerance.
- L1-06, L1-07 and L2-06 were reshuffled. Each still has exactly one correct option, and the answer field equals that option's text. The distractors and their feedback are right.
- L2-07: daily ε falls monotonically with T_ulko (3,05; 2,70; 2,58; 2,38).
- Scope is unchanged: no Carnot limit and no cycles beyond the brief. ΔU = Q − W_k is used as the brief defines it.
- No duplicates. The levels fit.
- The hash was identical at the start and the end.
