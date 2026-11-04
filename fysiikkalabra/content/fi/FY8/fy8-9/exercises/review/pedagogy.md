VERDICT: FAIL
CONTENT-HASH: 796546d7348c683e

## Blocking
- exercises.json fy8-9-L2-05 (text, part b) and solutions.md fy8-9-L2-05 — The hint "320 s:n kohdalla nettopulssimäärä on pudonnut suunnilleen neljäsosaan" leads a student to T = 320/2 = 160 s, but the accepted answer is 149 s ±6 % (140–158 s), so the student who follows the hint is marked wrong. The solution also says 283/64 = 4,42 is "lähes kaksi puoliintumisaikaa", but 4,42 > 4, so it is slightly MORE than two (2,14). Fix: write the hint as "hieman alle neljäsosaan (64 on noin 23 % luvusta 283)", and in the solution "hieman yli kaksi puoliintumisaikaa"; alternatively drop the hint or raise the tolerance to 0,08.

## Polish
- fy8-9-L1-07 is the same type as the existing L1-02 (percent remaining, integer half-lives); consider making the data different in kind (e.g. a graph reading) or accept it as practice.
- fy8-9-L2-05 is marked kind "graph", but no graph is asked for (the plan says to plot on a log scale). Add a short c) "piirrä logaritmiasteikolla" or drop "graph".
- fy8-9-L2-07 (background mean, net rate, √N) is closer to level 1 in demand; fine as the experiment task, but keep it as the first L2 data task.
- fy8-9-L3-04 c): "noin 240 000 vuodessa" assumes Pu-239 alone dominates the activity; say "jos plutonium-239 on määräävä nuklidi".
- fy8-9-L3-05: the lesson does not teach effective half-life; the task text explains λ_eff = λ_fys + λ_bio itself, which is good. Keep.

## Checked
- All new answers recomputed: L1-06 (1/4), L1-07 3,125 %, L1-08 17,5 a, L2-06 60 s, L2-07 33,2 1/s, L3-04 2,68 d (200 MBq, 80 %), L3-05 4,96 d, 50,1 %.
- L2-06 error analysis: student's 70 s explained correctly (background does not decay).
- L3-04 and L3-05 solutions are complete (principle, conversion, substitution, sanity check).
- MC distractors are real misconceptions with repairing feedback (L1-06).
- Lead-length rule: no new lead over ~45 words in one paragraph (L3-05 has 70 words, already in 2 paragraphs).
- Levels fit the plan in docs/exercise-bank/FY8.md; no duplicate of existing tasks beyond L1-07/L1-02 similarity.
- Finnish and cases after number+unit are fine.
- Screenshots: only 1280 px captures in the packet; I did not open them.
