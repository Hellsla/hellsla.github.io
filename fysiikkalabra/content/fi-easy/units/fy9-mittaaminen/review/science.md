VERDICT: FAIL
CONTENT-HASH: e356f29b730cbfea
SCOPE: delta: new tasks s7 (Jousen kalibrointi) and s8 (Pudotettu teräskuula videolla), the s8-kuvaaja model graph and the changed intro; older tasks s1-s6 untouched (not re-judged).

## Blocking
1. **A, s8 c, the frame-interval cause is backwards.** This is in the solution ("Aikaskaalan virhe ... $0{,}974 \cdot 0{,}05\,\text{s} = 0{,}0487\,\text{s}$") and in the rubric `error_sources` detail ("kuvaväli on noin $2{,}6\,\%$ lyhyempi kuin oletettu"). We have $g = 2s/t^2$. If the real interval were shorter than assumed, the computed $g$ would be too small. The measured $10{,}35$ instead of $9{,}81\,\text{m/s}^2$ needs a *longer* real interval: $0{,}05\,\text{s} \cdot \sqrt{10{,}35/9{,}81} \approx 0{,}0514\,\text{s}$, about $2{,}7\,\%$ (the real frame rate lower than nominal). The same error is in fi and en.
2. **A, s8 a, "Se on yhtä suuri kuin lukemisen epävarmuus, joten se ei ole merkitsevä"** (5th criterion, model answer). Every line through all the $\pm 0{,}01\,\text{m}$ bars crosses the $s$ axis between $+0{,}003$ and $+0{,}012\,\text{m}$, and none passes through the origin. By the method of part b (and of s7 b), the constant term is therefore not shown to be insignificant. Reword as in fi: the constant term is small, about the reading uncertainty, and the slope is not affected because the line is not forced through the origin.

## Polish
- s8 b: "$g = 2 \cdot 5{,}18 \approx 10{,}35$". $2 \cdot 5{,}18 = 10{,}36$. Show $5{,}177$.
- s8 c rubric: "pituuskaavan virhe" should be "mittakaavan virhe". An S2 reader cannot work out "pituuskaava".
- Language level (not blocking, for the pedagogy reviewer): the s8 a-c solutions are the fi text word for word, with long sentences of several clauses (for example the a "Mallivastaus" and the c "Mahdolliset syyt"). The tasks and rubrics of s7 and s8, and the s7 solutions, are split into short sentences as NOTES §12 asks. The s8 solutions are not.

## Checked
- Fidelity to fi for s7 a-c and s8 a-c: the task texts, criteria, solutions, Yleisiä virheitä and Hyväksytään myös. The numbers, units, points, answers and tolerances are identical, and the splitting into short sentences has changed no physics. The s7 b principle sentence "Vakiotermi on merkitsevä vain, jos se on suurempi kuin epävarmuus" is a correct simplification.
- The same recomputation script as for fi (the fy5-8 and fy4-2 figure data; answers.py side by side): s7 $29{,}98\,\text{N/m}$, $\Delta k = 1{,}22$, $15{,}0 \pm 0{,}61\,\text{cm}$, intercepts $-0{,}20\ldots+0{,}27\,\text{cm}$. s8 $5{,}175$, $0{,}010\,\text{m}$, $5{,}094$/$5{,}242$, $10{,}35 \pm 0{,}15$, $0{,}54$ ($5{,}5\,\%$). All agree except items 1 and 2.
- The alt text of the s8-kuvaaja figure (fi-easy solutions) matches the solution's numbers.
- Intro: eight tasks, two with a ready graph, one with the gas law: true; the text is in short sentences.
- `practice.py check` OK. The hash is the same at the start and the end.
