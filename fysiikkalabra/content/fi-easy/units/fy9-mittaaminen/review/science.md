VERDICT: PASS
CONTENT-HASH: ce981cbb7ceb9e3a
SCOPE: delta: round 3, the fixes of round 2 in fy9-mittaaminen-s7 and -s8 (s8 a rubric criterion 5, s7 c formula rows); older tasks s1-s6 untouched (not re-judged).
Round 3: delta against the version round 2 reviewed (fix round 2).

## Blocking
None.

## Polish
- s8 a, criterion 5: the new sentences "Kaikki suorat, jotka kulkevat pisteiden $\pm 0{,}01\,\text{m}$:n välien kautta, leikkaavat $s$-akselin välillä $+0{,}003\ldots{+}0{,}012\,\text{m}$. Mikään origon kautta kulkeva suora ei sovi." are correct, but the model answer (solutions.md row 812) does not show them. The grader should not require them. Add them to the model answer or mark them as extra.
- s7 c, rubric detail 3: $\tfrac{1{,}2}{30{,}0} \approx 4{,}1\,\%$ is arithmetically $4{,}0\,\%$. The solution (row 727) uses $1{,}22$, so write $\tfrac{1{,}22}{30{,}0}$. The result $\pm 0{,}6\,\text{cm}$ does not change.
- Carried from round 2: the interval $10{,}19\ldots10{,}48$ versus $10{,}35 \pm 0{,}15$ in s8 c. Both are defensible.

## Checked
- Round-2 item 1 is fixed in the fi-easy tasks.json. s8 a criterion 5 no longer says "joten se ei ole merkitsevä". It is now split into short sentences: the constant term is about $0{,}01\,\text{m}$, about the size of the reading uncertainty, it is small, zero is excluded, and it does not affect the slope because the line is not forced through the origin. Recomputed (scratchpad s8r2.py): the admissible intercepts are $+0{,}0033\ldots+0{,}012\,\text{m}$, so the rounding is correct. The numbers are identical to fi, and the criterion agrees with the model answer.
- s7 c, rubric detail 2: the chain is now an `aligned` block with real newlines and aligned rows ($4{,}5/30{,}0 = 0{,}150\,\text{m} = 15{,}0\,\text{cm}$). It is the same chain as the solution. Recomputed: $\Delta k = 1{,}22\,\text{N/m}$, $\Delta x = 0{,}61\,\text{cm}$, $x$ between $14{,}4$ and $15{,}6\,\text{cm}$. Detail 1 ("jousivakio yksikössä $\text{N/m}$") is clear.
- s7 b detail ("Tässä aineistossa suoran saa pakottaa origon kautta …"): correct physics, simpler wording than fi, same meaning.
- The unit fields are language-neutral.
- `practice.py check`: OK for fi-easy (8 tasks, 116 points). The hash is $ce981cbb7ceb9e3a$ at the start and at the end.
