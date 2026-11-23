VERDICT: PASS
CONTENT-HASH: f12fc65d9608b516
SCOPE: full: the three new "Pysähdy ja mieti" boxes (```pysahdy) in unit.md, judged first against the Finnish unit; then the unit texts and the Sovella task set since the version passed (3cc6d946afc32a21, commit ca27abed7)

## Blocking
- (none)

## Polish
- (none new.) The round 2 note on s8 c still holds and is not blocking: "An error that is constant ... is called systematic" reads like a definition, but a systematic error need not be constant.

## Checked
- Box 1 (after the six questions of a plan): "one variable at a time, otherwise either one could have caused it". It is the same as fi unit.md l. 157–161, says the right thing about causal inference, and agrees with the paragraph just above it.
- Box 2 (after the systematic-error paragraph): hundredths on the watch do not make the uncertainty a hundredth, because reaction time makes it tenths of a second. It is the same as fi l. 224–228 and agrees with the resolution paragraph and with s3 (hand-timed drops, $\varepsilon \approx 13\,\%$). Point 1 holds (resolution vs uncertainty, guardrails). Class C: the box does not say that a reaction-time error can also be partly systematic, which is fine at this level.
- Box 3 (after $y = kx + b$): a result from the slope is more reliable because every point affects the slope and the random error of one point counts for less. It is the same as fi l. 255–259. It correctly claims this only for random error, and the next paragraph adds that a constant systematic error shifts $b$ and leaves the slope as it was, so the two agree.
- inquiry.json: the only change is that the `model` answer is split into two paragraphs. The words, the numbers and the physics ($1\,\text{cm}$ offset, $k$ from the slope is right) are unchanged.
- sovella/solutions.md (git diff against ca27abed7): three paragraph splits (s1 a, s2 c, s5 d). The text is word for word the same. lessons/units/fy9-kokeellisuus (answers.py, figures.py) and tasks.json are unchanged.
- Recomputed with my own formulas, all in agreement with answers.py:
  - s3 $g = 2h/t^2 = 9.69\,\text{m/s}^2$
  - s4 $g = 4\pi^2/k$ with $k = 3.21/0.80$: $9.84\,\text{m/s}^2$
  - s8 $n = k/\mu_0 = 1963\,\text{1/m}$ and $I = 12\,\text{mT}/k = 4.86\,\text{A}$
  - the rest of the s1–s8 values are as in round 2.
- The scope is unchanged (FY1–FY8 experimental methods only). Units and the decimal point are correct.
- `practice.py check: OK` (packet). The hash was f12fc65d9608b516 at start and end.
