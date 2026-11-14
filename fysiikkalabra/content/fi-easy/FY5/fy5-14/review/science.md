VERDICT: FAIL
CONTENT-HASH: 8f05b673f2238a02

## Blocking
1. `assets/sims/fy5/fy5-14/sim.js` lines 116 and 118: the canvas velocity arrows are still labelled `\overline{v}_\text{s}` and `\overline{v}_\text{h}`, while the slider labels (`lang/*.json` sims.fy5-14), the lesson text and the figure now say v_L and v_H. A student sees both symbols in one view. Change to `\text{L}` and `\text{H}`.
2. `lessons/FY5/fy5-14/figures.py` line 176 (and the beats alt text in `content/{lang}/FY5/fy5-14/figures.json` / the svg aria-label in lesson.md): the alt text ends "huojunnan jaksonaika T h" / "period of the beats T h", while the figure label is now T_H. Change to "T H" and regenerate.

## Polish
1. Heading "Etumerkit ja oletukset" could become "Kaavan valinta ja oletukset".

## Checked
Checked: diff vs origin/main normalised for the symbol swap: every other change is a pure v_s→v_L, v_h→v_H, f_h/f_b→f_H, T_h→T_H substitution or the sign sentence rewrite. The four Doppler formulas equal MAFY's (kaavanimet.tsv) with correct signs, and each "first/second formula applies" sentence matches its formula. v_L and v_H are defined where they first appear, f_H and T_H at the beats formula. answers.py and lesson-answers.py output is byte-identical to origin/main. Example recomputed: 341.10 Hz, 285.78 Hz, Δf 55 Hz.
