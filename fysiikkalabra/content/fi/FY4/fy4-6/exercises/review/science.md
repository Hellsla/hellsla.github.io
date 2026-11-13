VERDICT: FAIL
CONTENT-HASH: 5560efdfc881bbd0

## Blocking
- content/fi/FY4/fy4-6/exercises/exercises.json (L2-09) — the added figure task repeats L2-03 on the same figure fy4-6/mittaus. Its whole reading, "Määritä liikekitkakerroin kuvaajasta" (fit a line through the origin, μ ≈ 0,21), is exactly L2-03's task. What it adds is one multiplication, a = μg. A student who has done L2-03 reads nothing new from the figure. The brief requires that a new figure task not repeat an existing task on the same figure. — Fix: give L2-09 its own reading of the figure, for example the friction read off the fitted line at an N that has no measured point, then the deceleration of a block at that N. Or make a = μg part b) of L2-03 and drop L2-09.

## Polish
- content/fi/FY4/fy4-6/exercises/exercises.json (L1-09) — the task says "liukukitkakerroin" (MAFY's word, and the name of the chapter's formula), while the chapter's text and the solution say "liikekitka(kerroin)". One clause "(liikekitkakerroin μ)" would join the two.
- content/fi/FY4/fy4-6/exercises/exercises.json (L2-09) — the question is not the last sentence: "Määritä liikekitkakerroin kuvaajasta" comes after it.

## Checked
- L1-09: μ = 0,014 (steel–ice, liukukitkakerroin) is the VERIFIED fy4-6 row of docs/mafy-arvot.tsv. The hint names only the table (*Kitkakertoimia*). Constant velocity and level ice give F = μmg = 6,18 N. Two significant figures are justified by 0,014. The force diagram (G = N, F = F_μ, drawn enlarged as stated) agrees with the motion.
- L2-09 physics is right: only friction acts horizontally, so a = μg. The origin fit gives μ = 0,2145 and a = 2,10 m/s², inside 5 %. A hand fit with μ between 0,20 and 0,22 stays mostly inside. Signs are stated (a_x = −μg). The condition N = mg is stated.
- Recomputed in one script (my formulas, least squares through the origin, beside python -I answers.py): 6,18 N and 2,10 m/s². Both agree with exercises.json.
- Notation μ, N, F_μ, G as in the chapter.
- Hash 5560efdfc881bbd0 at the start and at the end.
