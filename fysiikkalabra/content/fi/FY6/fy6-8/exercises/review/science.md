VERDICT: FAIL
CONTENT-HASH: a20bcfba2d6f783c

## Blocking
- exercises/solutions.md:150 with exercises.json:154–156 (L2-05), and solutions.md:161 with exercises.json:200–202 (L2-06) — (A, assessment) The model answers accept ranges the checker rejects. L2-05 says "0,53–0,59 Ω", but tolerance 0.05 around 0,56 accepts only 0,532–0,588. L2-06 says "0,35–0,45 A", but tolerance 0.1 around 0,40 accepts only 0,36–0,44. The lines cross at a shallow angle (slope difference 0,28 Ω), so 0,01 V of fitting error moves the crossing by about 0,04 A, and the stated range is the realistic one. — Fix: tolerance 0.06 (L2-05) and 0.13 (L2-06), or narrow the stated ranges to the checker's.

## Polish
- exercises.json:247 (L2-07) — 1,58 V is not the *merkitty* 1,5 V. Drop "merkitty".
- exercises/solutions.md:162 (L2-06) — "B kestää suuremman virran" names the wrong cause. Write "B pystyy antamaan suuremman virran".
- exercises/solutions.md:178 (L3-04 c) — "pariston lämmöksi" breaks the heat guardrail. Write "muuttuu pariston sisäenergiaksi".
- L3-05 realism: a 6 V *akku* with R_s 0,80 Ω is unrealistic (lead-acid batteries have tens of mΩ). "Neljän AA-pariston ryhmä" fits the numbers. The comment at lessons/FY6/fy6-8/answers.py:57 says "5,5 A", but the task says 5,6 A.
- L2-07 repeats L1-06's idea at level 2. The plan's "mittarin virheraja, epävarmuus" (L2-05) is still missing. This is for pedagogy to judge.

## Checked
- All 20 answers recomputed in one script with my own least-squares fits: L2-05 0,559 Ω (E 1,539 V); L2-06 0,402 A; L3-04 1,09 Ω, 35,3 % (new cell 11,1 %); L3-05 1,103 Ω, E 6,109 V, giving 7,60 A (the pupil's 5,55 A); L1-08 0,38 Ω. All agree with answers.py and exercises.json.
- L3-04 c: 0,47 / 0,53 / 0,47 / 0,34 W, with the maximum at R = R_s and half the power heating the cell. The power balance 0,264 + 0,481 = 0,745 W is right.
- L3-05 model: U = E − (R_s + R_j)I is right, and so are the intercept E and the "with leads" check.
- L1-06, L1-07 and L2-07 each have exactly one correct option, and every distractor's feedback is right.
- Notation E, R_s, I_k follows the brief. The data are labelled esimerkkiaineisto. Everything stays in scope.
- The L3-04 solution at 1280 px renders cleanly.
