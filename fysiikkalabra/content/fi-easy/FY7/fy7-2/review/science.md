VERDICT: PASS
CONTENT-HASH: 0cd8a55bb646cb06

Delta re-review. The diff holds three changes, none of them a number or a symbol:
- inquiry.json `siirto`: "teslaina" is now "tesloina" in the prompt and in the solution's Kysytty line.
- figures.json: the description of the exercise figure `fy7-2/r-points` is reworded, and the `pick-ulos` entry got a trailing comma.
- lesson.md: only teacher-approved figures and formula names changed.

## Blocking

## Polish
- lesson.md:275: "Säde on kääntäen verrannollinen varaukseen ja kenttään" should say "varauksen suuruuteen $|q|$ ja kenttään", to match $r = mv/(|q|B)$. Carried over from the last report.

## Checked
- inquiry.json `siirto`: I recomputed the answer: $m = 1{,}829 \cdot 10^{-26}\,\text{kg}$, $v = \sqrt{2qU/m} = 5{,}919 \cdot 10^{5}\,\text{m/s}$, $B = mv/(qr) = 0{,}2252\,\text{T}$. This matches `answer` 0.225 and the solution. The physics, the unit (T) and the significant figures are unchanged.
- figures.json `r-points`: the new description carries the same facts as the old one and as figures.py: the field is 0,20 T, there are four points at 0,5 to 2,0 · 10⁶ m/s, and the line goes through the origin. It still does not reveal the mass. The figure is used only by exercise fy7-2-L2-09.
- figures.json `pick-*`: the text of these entries is unchanged; only the JSON comma changed.
- lesson.md: the teacher-approved figures and formula names fall outside science (categories `teacher-figure` and `formula-names`).
- The rest of the lesson is as I passed it at 36f1e76b61ba6c02, and my earlier recomputations carry over.
- Hash at start and end: 0cd8a55bb646cb06.
