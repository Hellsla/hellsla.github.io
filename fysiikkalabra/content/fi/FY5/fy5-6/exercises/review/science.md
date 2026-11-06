VERDICT: PASS
CONTENT-HASH: 1ae57cce87a7a6fc

## Blocking

## Polish
- solutions.md:211 (L1-09) — the reasonableness check attributes the lower speed to Mars's mass alone. Phobos's radius (9380 km) is also larger than a low Earth orbit's. Say "pienempi massa ja hieman suurempi säde", or compare with Phobos's measured period of about 7,65 h, which is a real check.

## Checked
- Diff against HEAD~1: only L1-09 (type 5, Suuruusluokka) is new.
- answers.py run once; all numeric answers inside tolerance.
- Recomputed: $v = 2137\,\text{m/s}$, $T = 2{,}758\cdot 10^{4}\,\text{s} = 7{,}66\,\text{h}$. This agrees with the real Phobos (about 7,65 h), so the model and the data are sound.
- Every distractor reproduces its stated error exactly: no square root gives 0,0036 h; r in km under the root gives 0,24 h; dividing by 60 gives 460 h. Neighbouring options are a factor of 32–67 apart, which fits type 5.
- All options have the same form ("noin X h"), so the correct one is not identifiable by form. Exactly one is correct.
- The chapter's warned $h$ vs. $R + h$ mistake does not apply, because the task gives the orbital radius; the substituted errors are fair.
- Notation ($\gamma$, $M$, $r$, $T = \tfrac{2\pi r}{v}$) is the lesson's, and the task stays inside fy5-6.
- Formula chains checked from the text only: the solution uses aligned blocks with short lines, and the feedback has one inline chain under 300 px.
