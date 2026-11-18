VERDICT: FAIL
CONTENT-HASH: ce624321f2f924f1
SCOPE: delta: round 2, the fixes of round 1 in fy9-mittaaminen-s7 and -s8 (s8 solutions, rubric, answers.py, the s8-kuvaaja model graph); older tasks s1-s6 untouched (not re-judged).
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
1. **A, s8 a, round-1 item 2 is fixed only in the solution.** The fi-easy model answer is now correct: "Vakiotermi on pieni. Suoraa ei ole pakotettu origon kautta, joten vakiotermi ei vaikuta kulmakertoimeen." The 5th rubric criterion of a (tasks.json, tag `graph`) still gives a point for "Se on yhtä suuri kuin lukemisen epävarmuus, joten se ei ole merkitsevä." Every line through all the $\pm 0{,}01\,\text{m}$ bars crosses the $s$ axis between $+0{,}0033$ and $+0{,}012\,\text{m}$ (recomputed), so zero is not included. The criterion rewards a wrong conclusion and contradicts the model answer. Reword it in short sentences, for example: "Suoran vakiotermi on noin $0{,}01\,\text{m}$. Se on pieni, suunnilleen lukemisen epävarmuuden suuruinen. Se ei vaikuta kulmakertoimeen, koska suoraa ei ole pakotettu origon kautta." The same item is open in fi and en.

## Polish
- s8 c: the interval $10{,}19\ldots10{,}48\,\text{m/s}^2$ (the limiting lines) differs slightly from $10{,}35 \pm 0{,}15$ ($10{,}20\ldots10{,}50$). Both are defensible.
- Language level (for the pedagogy reviewer): the fixed parts of s8 are now split into short sentences. The a-part sentence about the $(t,s)$ graph and the broken line is still long.

## Checked
- Round-1 item 1 is fixed in the fi-easy solution c ("Jos todellinen kuvaväli on pidempi kuin oletettu $0{,}05\,\text{s}$, ajat on arvioitu liian pieniksi. Silloin laskettu $g$ on liian suuri."; $0{,}0514\,\text{s}$, $2{,}7\,\%$, a lower frame rate), in the rubric `error_sources` detail and in answers.py `c-tscale`. "Lyhyempi" and $0{,}0487$ are gone from s8.
- The polish is fixed: $2 \cdot 5{,}177 = 10{,}35$; "pituuskaava" no longer appears. The rubric says "mittakaavan virhe".
- The same recomputation as for fi (scratchpad s8r2.py): slope $5{,}175$/$5{,}177$, intercept $0{,}0100\,\text{m}$, largest residual $0{,}008\,\text{m}$, bounds $5{,}094$/$5{,}242$, $\Delta g = 0{,}147$, $0{,}54$ ($5{,}5\,\%$, $3{,}7\Delta g$), $0{,}0514\,\text{s}$. All are identical to fi and agree with the data. The sentence splitting changed no physics. The added "systemaattinen virhe eli virhe, joka vaikuttaa joka kerta samaan suuntaan" is a correct explanation.
- Precision: $(10{,}35 \pm 0{,}15)\,\text{m/s}^2$ and $0{,}83\,\text{m}$ fit the data. No structure is revealed in the task text. Calculation chains are in aligned rows. The unit fields are language-neutral.
- The alt text of s8-kuvaaja matches the solution.
- `practice.py check` OK for fi-easy (8 tasks, 116 points). The hash is the same at the start and the end.
