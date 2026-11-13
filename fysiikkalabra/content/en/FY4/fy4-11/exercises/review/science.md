VERDICT: PASS
CONTENT-HASH: 87f657abf999e6b7
SCOPE: delta added-exercise from 696dd89d4770c31a base 81db4a6fd727
## Blocking

## Polish

## Checked
- Round 2 diff, L1-09 Answer is now $\approx 31\,\text{m}$. Recomputed: $v_0 = 22.22\,\text{m/s}$, $a = 0.8 \cdot 9.81 = 7.85\,\text{m/s}^2$, $s = 31.46\,\text{m}$. This equals answers.py and exercises.json (31.46, tolerance 5 %).
- The friction range is now stated correctly: $\mu = 0.8$ is the upper end of MAFY's 0.5–0.8, so 31 m is the shorter end. At $\mu = 0.5$, $s = 493.8 / 9.81 = 50\,\text{m}$, which is longer. The remark that the range dominates over rounding is right.
- The task text's literal `\\n` was fixed to a real paragraph break; no wording changed.
- The model is right: on a level road $N = mg$, sliding friction is the only horizontal force, and the deceleration is constant.
- The Finnish diff makes the same change with the same numbers.
- answers.py run: every numeric answer equals exercises.json.
- Script comparison with content/fi for all 24 tasks: every number in the texts and solutions.md identical.
