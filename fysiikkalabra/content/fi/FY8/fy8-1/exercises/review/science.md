VERDICT: FAIL
CONTENT-HASH: cb48bd7706c41840

## Blocking
- exercises/solutions.md:386 (also :221, :259) — **A**: the slope of the $E_\text{k,max}(f)$ line is called $\tfrac{h}{e}$. L2-08 writes $E_\text{k,max} = hf - W = \tfrac{h}{e}(f - f_0)$, which is false as written ($hf - W = h(f - f_0)$); L2-07 says "Planckin vakio $\tfrac{h}{e}$" and L2-06 "$\tfrac{h}{e} = 4{,}14 \cdot 10^{-15}\,\text{eV/Hz}$" ($h/e$ has the unit V s). This contradicts the brief's lesson and the Periaate of L2-06 (slope is $h$) and blurs the difference from L2-05, where the slope of $U_\text{s}(f)$ really is $h/e$ — fix: write $h = 4{,}136 \cdot 10^{-15}\,\text{eV}\,\text{s}$ (that is $0{,}4136\,\text{eV}$ per $10^{14}\,\text{Hz}$) and $E_\text{k,max} = h(f - f_0)$ in all three places; numbers unchanged.

## Polish
- exercises/solutions.md:251 — L2-07 "kolme merkitsevää numeroa kuten datan energioissa": $0{,}55\,\text{eV}$ has two; $W$ is a difference known to the hundredth — give that reason.
- lessons/FY8/fy8-1/answers.py:45 — comment says "387,6 nm -> 388 nm"; the value is 387,5 → 387 (as exercises.json and the solution).
- exercises.json L3-04, L3-05 — the solutions use $e = 1{,}602 \cdot 10^{-19}\,\text{C}$ and $eU_\text{s} = E_\text{k,max}$, which these task texts do not give (only L2-05 does); add them to the given values.
- exercises/solutions.md L3-04 a) — the table only shows $0{,}70\,\text{V} < U_\text{s} \le 0{,}80\,\text{V}$; say that $0{,}80\,\text{V}$ is the smallest tabulated value with zero current.

## Checked
- All 21 numeric answers recomputed from the task texts with my own script: every one agrees with exercises.json and answers.py inside half the tolerance (L2-02 2,2 % of 3 %).
- L2-05 least-squares fit: $k = 4{,}195 \cdot 10^{-15}\,\text{V/Hz}$, $h = 6{,}72 \cdot 10^{-34}\,\text{J}\,\text{s}$, $f_0 = 5{,}57 \cdot 10^{14}\,\text{Hz}$, $W = 2{,}34\,\text{eV}$; residuals within $\pm 0{,}02\,\text{V}$; line points (6,0; 0,179) and (8,0; 1,018) are on the fit.
- L1-10 calcium $3{,}20\,\text{eV}$ matches the verified MAFY row (docs/mafy-arvot.tsv).
- L1-06: exactly one correct option; each distractor wrong and its feedback right. L1-09: truth values 1 F, 2 T, 3 F, 4 T, 5 F correct.
- Figure kuvaaja-ab: $f_{0,\text{A}} = 5{,}56$, $f_{0,\text{B}} = 7{,}01 \cdot 10^{14}\,\text{Hz}$; readings 2,7 eV and 428 nm inside tolerance; description does not give the answer.
- L3-04: yield 0,0930 % at both powers, $W = 2{,}30\,\text{eV}$. L3-05: A 2,64 eV, B 2,00 eV, C 3,40 eV; 1,516 + 0,294 µA; $U_\text{s} = 1{,}10\,\text{V}$.
- L3-01 non-relativistic ($v/c = 0{,}2\,\%$); L3-02 wave-model assumptions stated in the task.
- Scope: inside FY8 contents; stopping voltage defined in L2-05; no de Broglie.
- Symbols ($W$, $E_\text{k,max}$, $f_0$, $\lambda_0$) as in the lesson brief; solutions symbolic before substitution.
