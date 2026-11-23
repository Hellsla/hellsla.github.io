VERDICT: PASS
CONTENT-HASH: 02d275f66d6dc23f
SCOPE: delta md-paragraphs,numbers,reflow,typography,wording from a5c6089260b9a4af base 64d4935
Mode: delta (work queue 8g: Formula steps rewritten as basic laws then derived formula; paragraph splits)

## Blocking
(none)

## Polish
- exercises/exercises.json (fy8-13-L2-10, carried over) — the graph's $d_{1/2} = 5.0\,\text{cm}$ differs from the lesson's Cs-137 value for concrete (about 4 cm). Fix: add a clause saying the source is not Cs-137.

## Checked
- Hash 02d275f66d6dc23f (`--exercises --lang en`) at the start and the end.
- I compared the old and new text word by word. Only the Formula lines of L2-01, L2-02, L3-01, L3-03 and L3-05 changed. Everything else is blank lines and paragraph splits with identical words and numbers (the radon heating-season and flight-dose passages included).
- L2-01: the aligned block $D_\text{T} = E/m$ → $H_\text{T} = w_\text{R} D_\text{T}$ → $H_\text{E} = w_\text{T} H_\text{T} = w_\text{T} w_\text{R} E/m$ is correct.
- L2-02: the inverse-square law, then $H = \dot H_2 t$, then $t = H/\dot H_2 = (H/\dot H_1)(r_2/r_1)^2$. The inversion is correct.
- L3-01: the two dose rates (distance and shield) are each multiplied by $t$, and the difference is factored correctly into $\dot H_1 t[(r_1/r_\text{A})^2 - (\tfrac12)^{d/d_{1/2}}]$.
- L3-03: the alpha dose goes through $H_\text{T}$ and $w_\text{T}$, the uniform gamma dose through $w_{\text{R},\gamma}D_\gamma$ (the tissue weights sum to 1), and the two are added. Physically right.
- L3-05: the attenuated rate $\dot H_d$ is scaled by $(r_1/r_2)^2$, and $t = (H/\dot H_1)(r_2/r_1)^2\,2^{d/d_{1/2}}$ is correct. The order of the two factors does not matter.
- answers.py run against exercises.json: all 22 numeric answers are within tolerance. exercises.json and answers.py did not change.
- Every chain starts from the quantity and is solved symbolically before substitution. The notation ($\dot H$, $w_\text{R}$, $w_\text{T}$, $d_{1/2}$) is the same as in the rest of the set.
