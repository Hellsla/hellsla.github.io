VERDICT: FAIL
CONTENT-HASH: 6e4ee6b95a982499

## Blocking
- inquiry.json:262 — (A, assessment correctness 7 / consistency 6) The third self-assessment criterion of `johtopaatos` still asks for "Sanoin, että bensiinimoottorin häviöt ovat suuri osa otetusta tehosta. Sanoin myös, että ne ovat lämpöä." The conclusion now comes after koe-2 (the hehkulamppu at 40 W). Its prompt asks only how efficiency is computed and why the running time does not affect it, and its model answer does not mention the engine. koe-1 (bensiinimoottori) is now optional, so a student on the core path has no engine data. The criterion asks for something the task neither gives nor asks, and the model answer does not meet it. — Fix: rewrite the criterion for the lamp, e.g. "Sanoin, että loput $95\,\%$ ovat häviöitä, enimmäkseen lämpöenergiaa." It then matches the model answer's last sentences.

## Polish
- None.

## Checked
- Delta review, round 3: ennuste-1 and koe-1 now `optional`. ennuste-1 reveals after koe-1, so the optional prediction and the optional experiment stay paired. ennuste-2 and koe-2 remain on the core path. No other activity, lesson.md or exit-ticket text refers to koe-1.
- koe-1 hint 3 in kJ: at $60\,\text{kW}$, $t = 10\,\text{s}$ gives $E_\text{o} = 600\,\text{kJ}$, $E_\text{h} = 0{,}75 \cdot 600\,\text{kJ} = 450\,\text{kJ}$, ratio $0{,}75$. The ratio of kJ values is correct and dimensionless.
- johtopaatos model answer recomputed: lamp $P_\text{o} = 40\,\text{W}$, $\eta = 5\,\%$. $t = 10\,\text{s}$ gives $400\,\text{J}$ / $20\,\text{J}$, $t = 20\,\text{s}$ gives $800\,\text{J}$ / $40\,\text{J}$, $P_\text{a} = 2{,}0\,\text{W}$, losses $95\,\%$. All agree.
- The model answer's physics is right: at constant power the time cancels, the values are called model values, and the model's constant-η assumption is stated.
- `after: koe-2` points to a non-optional experiment that records Eo and Ea at two or more times with laite and Po locked.
- Hash identical at start and end.
