VERDICT: PASS
CONTENT-HASH: 613d454f2b784ce1

Round 1 (exercises): full review; new YO-skill task fy7-12-L2-08 (two-stage perustelumonivalinta), the rest of the set PASS before. Checked from the text only; no renders.

## Blocking

## Polish
- exercises.json:264 (L2-08, option "Kaikki valo taittuu ilmaan") — "Rajapinnassa osa valosta heijastuu aina" is not exact for a laser: polarised light at the Brewster angle (36,9° water → air) does not reflect at all — fix: "Rajapinnasta heijastuu tavallisesti osa valosta".
- exercises.json:242 (L2-08) — the wrong options' feedback already states "50,0° > rajakulma", so a student who picks a wrong option first sees the reason. Allowed by the rule (only the correct option's feedback is checked), but a shorter wrong-choice feedback would keep the reason stage open.
- Carried over: answers.py:17 `0.50e-3` → `0.500e-3`; solutions.md L3-04 significant-figure wording; L3-05 triangle figure.

## Checked
- Hash 613d454f2b784ce1 at start and end.
- L2-08 physics: α₁ = 90° − 40,0° = 50,0°; α_r = sin⁻¹(1,00 : 1,33) = 48,75°; 1,33 · sin 50,0° = 1,019 > 1, so total reflection. Margin robust: n = 1,325–1,335 gives α_r 48,5–49,0°.
- L2-08 options: correct choice same length and form as the others; its feedback ("säde kokonaisheijastuu") does not give the reason away. Correct reason is not the longest and not the only one with numbers.
- L2-08 distractors: angle from the surface (40° < 48,8°), swapped indices (sin = 1,33, "valo pääsee aina ilmaan", the direction confusion the lesson warns about), a true but non-deciding statement, grazing refraction only at exactly α_r. "Optisesti harvempi" is taught in fy7-10.
- L2-08 solution: Kysytty · Periaate · Mallivastaus, α_r solved symbolically, angle from the normal, reflection angle 50,0°, every distractor explained. Inline and display lines are short (text estimate under 300 px).
- All answers recomputed independently in one python call: 19 numeric answers equal exercises.json; answers.py output equals exercises.json.
- Scope: within fy7-12 and fy7-10 (critical angle, normal).
