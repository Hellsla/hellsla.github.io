VERDICT: FAIL
CONTENT-HASH: 424b0972f9e99c5a

## Blocking
- solutions.md fy1-8-L3-02 Sijoitus — "$r_1 = \dfrac{80{,}0\,\text{K} - 68{,}0\,\text{K}}{5{,}0\,\text{min}}$" and "$52{,}0\,\text{K} - 47{,}0\,\text{K}$" write the Celsius temperatures as kelvins (80,0 K is about −193 °C), contradicting the Annettu line and teaching that °C and K are the same scale. Fix: `\dfrac{80{,}0\,{}^\circ\text{C} - 68{,}0\,{}^\circ\text{C}}{5{,}0\,\text{min}} = \dfrac{12{,}0\,\text{K}}{5{,}0\,\text{min}} = 2{,}4\,\text{K/min}` (the difference is in kelvins, as the Muunnokset line says); likewise for $r_2$.

## Polish
- solutions.md fy1-8-L3-01 and L2-01 Vastaus — the stored answers are the unrounded 0,033 m/s and 2,5 %, but the text now says the reported values are 0,03 m/s and about 3 %. A student who rounds as told (0,03; 3) is marked wrong. Say in the task "Anna laskettu arvo" or widen the tolerance to cover the rounded forms (0.005 and 0.5).
- exercises.json fy1-8-L2-03 — "90 cm" and "342 cm" are plain text while the times beside them are LaTeX; write `$90\,\text{cm}$` and `$342\,\text{cm}$`.
- solutions.md fy1-8-L3-02 Kaava — $\Delta t$ and $\Delta r$ stand for a time interval and a rate difference where elsewhere $\Delta$ means an uncertainty (earlier Polish, still open); use "viiden minuutin aikana" and "laskunopeuksien erotus".
- solutions.md fy1-8-L1-01 Vastaus — "$5\,\%$ … (laskimen arvo $5{,}0\,\%$)" is the same number twice; either state "$5{,}0\,\%$" or drop the parenthesis.

## Checked
- Diff is LaTeX conversion of numbers with units in nine tasks and clearer wording in L2-01, L2-02 (situation then measurement), L3-01 Periaate and L1-04 Periaate; no answer, unit or tolerance changed.
- L2-02: $3{,}0\,\text{m} : 1{,}5\,\text{m/s} = 2{,}0\,\text{s}$, $0{,}20 : 2{,}0 = 10\,\%$; "$3{,}0\,\text{m}$:n matkan" has correct case.
- L1-03 Järkevyys "alle kolmasosa kävelyvauhdista": $0{,}42 : 1{,}4 = 0{,}30$, true.
- L1-04 Periaate now says the half range describes the spread of repeats and that repeats do not reveal a systematic error; consistent with fy1-3.
- L3-01: $0{,}033\,\text{m/s}$, $v = 0{,}43 \pm 0{,}03\,\text{m/s}$ and the "ennuste $0{,}50$ ei mahdu väliin" argument are correct.
- Counts, levels and contexts unchanged; no task repeats the worked example.
- Hash unchanged at the end.
