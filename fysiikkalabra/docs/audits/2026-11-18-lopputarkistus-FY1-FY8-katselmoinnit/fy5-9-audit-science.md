VERDICT: PASS
CONTENT-HASH: 6fd865c43f88554e

## Blocking

## Polish
- content/fi/FY5/fy5-9/inquiry.json:538 (virhe, correct option feedback) — "alle metrin heiluri heilahtaa noin kahdessa sekunnissa": "heilahtaa" can be read as a half swing, and the $0{,}80\,\text{m}$ pendulum's period is $1{,}79\,\text{s}$ (feedback gives it a line earlier). Not wrong, but loose — write "jaksonaika on vajaat kaksi sekuntia". Minor, C.
- content/fi/FY5/fy5-9/inquiry.json:550 (virhe, angle distractor) — "tehtävän heiluri heilahtaa tavallisesti": the prompt says nothing about the swing size. The distractor is still clearly wrong (an error of $22\,\text{s}$ against $1{,}8\,\text{s}$), so the feedback holds. Better: "jos heilahdukset ovat pieniä, kulma ei vaikuta merkittävästi". Minor, B (only a stylistic condition).
- content/fi/FY5/fy5-9/inquiry.json:650 (tarkistus-3 model) — "nopeus kaksinkertaistuu. Siksi kaksinkertainen matka kuljetaan samassa jaksonajassa": this is only true if the speed doubles at every corresponding point $x \to 2x$, not just at the top speed. $v = \sqrt{k/m}\sqrt{A^2-x^2}$ shows it in a few words. Minor, C (the theory's "Miksi amplitudi" paragraph already says "jokaisessa vastaavassa kohdassa").
- content/fi/FY5/fy5-9/lesson.md "Vaimeneminen" — the clock passage says "eikä kello edistä eikä jätätä" with no limit attached. "lähes" would fit the sentence before it. Minor, C.

## Checked
- One script recomputed every number: koe 1–5 (spring $0{,}993$/$1{,}987\,\text{s}$, $v_\text{max}$; exact pendulum period via the elliptic integral $2{,}007$–$2{,}153\,\text{s}$, the $T:T_0$ table $1{,}002$–$1{,}073$), the worked example $24{,}7\,\text{N/m}$ and its check $0{,}795\,\text{s}$, mittaus $2{,}004\,\text{s}$, $g = 9{,}83$ ($9{,}64$–$10{,}03$), siirto $73{,}8\,\text{kg}$, tarkistus-2 $62\,\text{N/m}$, and every mistake value. All agree with lesson-answers.py and the texts.
- A Python port of sim.js `measure()` gives the same $T$ and $v_\text{max}$ at every experiment's initial values. The slider steps reach every value the experiments ask for, and `simState` exposes T, vmax, E.
- Each experiment locks the right variables (koe 3 m varied with l and α₀ locked, and so on).
- The sim integrates the exact $\alpha'' = -(g/l)\sin\alpha$ as its model box says. The pendulum's acceleration arrow (tangential plus normal) is physically right.
- The pendulum force diagram: at the extreme $S = G_\text{n}$ (stated as holding at the extreme only), the components are dashed, and there is no double counting.
- The circular-motion derivation uses $T$ and $a_\text{n}$ with no ω (scope note kept). The vertical-spring remark is correct.
- Uncertainty: hand timing is $0{,}2\,\text{s}$ against a resolution of $0{,}01\,\text{s}$. Half the range is used as scatter and never called the uncertainty of the mean. The example data are labelled. The formula value lies inside the interval.
- Each prediction has exactly one correct option, and every distractor's feedback is right. Tarkistus-1's factor is $\sqrt{6}$. The exit ticket matches the theory.
- The figure "energia" (said to be to scale): $E = 0{,}10\,\text{J}$, $E_\text{p}(5\,\text{cm}) = 0{,}025\,\text{J}$. kuvaaja-k: peaks at $0$, $0{,}40$ and $0{,}80\,\text{s}$, $A = 3{,}0\,\text{cm}$.
- Damping becomes internal energy (no "lämmöksi"). The terms match the glossary.

## Scores
- 1 Physics and mathematical correctness: **5** — every number recomputes, the models' conditions (small angles, no friction, point mass) are stated where they are used, and only Minor C-level wording remains.
- 6 Experimental reasoning (physics): **5** — the uncertainty is propagated correctly ($\Delta g/g = 2\,\Delta T/T$), scatter and uncertainty are kept apart, model values are labelled as model values, and the controlled variables are isolated.
- Severity: all four findings are Minor. None is Critical or Major.
