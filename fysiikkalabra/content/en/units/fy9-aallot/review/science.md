VERDICT: FAIL
CONTENT-HASH: 6cc9e05376028525

Delta review (work queue 11c): the new `hints` of all 31 written parts in `sovella/tasks.json`, checked against each part's rubric, answer and `sovella/solutions.md`, and against the fi hints.

## Blocking
1. (A, internal consistency) s4 c, hint 2, en: the hint names the permitted time $t_\text{perm}$, but the en rubric (equation and calculation criteria) and the solution use $t_\text{allowed}$; the brief requires the same symbols. Replace `t_\text{perm} = \dfrac{t_0}{2^{\,n}}` with `t_\text{allowed} = \dfrac{t_0}{2^{\,n}}`.

## Polish
2. s7 c, hint 3, en: "Consider how the waves are in phase relative to each other" presupposes they are in phase, while the answer is that they arrive in antiphase. Replace with "Consider what the phase relation of the two waves is at $\text{P}$ and what that means for the loudness of the sound." (fi: "millä tavalla aallot ovat vaiheessa toisiinsa nähden" is neutral.)

## Checked
- Every other hint says the same physics as fi and matches the en rubric and solution symbols: $f_\text{string}$, $f_\text{h}$, $f_\text{s}$, $v_\text{L}$, $v_\text{H}$, $t_\text{max}$, $t_\text{min}$, $T^2 = kl + b$, upward-positive Newton II, $f = \dfrac{nv}{\Delta s}$.
- Recomputed values: $\bar t = 0.48\,\text{s}$, $\Delta t = 0.07\,\text{s}$, $15\,{}^\circ\text{C}\cdot 0.6\,\text{m/s} \approx 2.6\,\%$, $b/k \approx 1.4\,\text{cm}$, $3.4\,\text{m}$ and $17\,\text{cm}$ against $2\,\text{m}$, $80\,\text{dB}$, $686.8\,\text{Hz}$, $12.5$ and $25\,\text{Hz}$, $1\,\text{N/m} = 1\,\text{kg/s}^2$; all agree with answers and solutions.
- No hint states a final answer; units in LaTeX with decimal point.
