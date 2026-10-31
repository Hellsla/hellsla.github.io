VERDICT: DONE

Round 1 fix, visual reviewer's two Major findings. Only `lesson.md` changed (typesetting only; no physics, numbers or wording beyond what maths needed).

- Ydinajatus: opening values `5,00 litran`, `101 kPa:n`, `0,207 mol` now inline maths (`$5{,}00\,\textsf{l}$`, `$101\,\text{kPa}$`, `$0{,}207\,\text{mol}$`); the "paineessa ... ja lämpötilassa ..." wording adjusted so the units need no inflection.
- Avogadro constant: `{6{,}022 \cdot 10^{23}}` and `{N_\text{A} = 6{,}022 \cdot 10^{23}\,\text{1/mol}}` wrapped in one brace group, so it cannot break across lines.
- Kaava: `0,2071 mol`, `273,15` in maths; the plain chain `1 Pa · m³ = ... = 1 J` is one inline maths chain.
- Esimerkki: `101 kPa`, `0,21 mol`, and the garbled precision sentence rewritten as the reviewer proposed (Polish item, same paragraph).
- Järkevyys: `24 l`, `5,0 l : 24 l/mol ≈ 0,21 mol`, `0,2073 mol · 29 g/mol ≈ 6,0 g` all in maths, colon for the division.
- Not done (Polish, not listed): opening-sentence split, balloon-scene summary line, stage-tutki `±`, sim label size.

check_lesson.py: all lines ok.
