VERDICT: FAIL
CONTENT-HASH: 2b3698a734643bfa
Round: 2

## Blocking
- exercises.json fy2-1-L3-05 text and solutions.md L3-05 (Periaate, Vastaus) — the fix added "loppu energia muuttuu vaiheessa lämpöenergiaksi tai heijastuu" and Periaate keeps $E_\text{tulo} = E_\text{ulos} + E_\text{lämpö}$, but a) asks for the energy that becomes heat and the model solution counts the whole difference (4,20 MJ in the panel, 4,86 MJ in total) as heat and c) says it "on muuttunut ... lämpöenergiaksi". If part of it is reflected, the difference is not heat and the conservation check 0,14 + 4,86 = 5,00 is not what the task text defines. Fix: either delete the reflection remark again (model: "loppu energia muuttuu vaiheessa lämpöenergiaksi", the reflected light of the panel is counted as heat for simplicity), or ask for "ympäristöön lämpönä tai heijastuksena menevä energia" in a), b), c), Periaate and Vastaus.

## Polish
- solutions.md L3-04 c) Vastaus — "korvaava vesi- ja tuulivoima lisää energiaa saman verran kuin fossiilinen vähenee" reads as if total energy grows; say "tuottaa saman verran energiaa kuin fossiilinen tuotti". The task asks "vähintään", the answer is "yli 70 PJ" (strict inequality); one clause saying that with the given 2-digit data 70 PJ is the limit would remove the tension.
- exercises.json L3-05 — invented data is still not marked "esimerkkiluvut" (L2-05, L2-07, L3-04 now are).
- L3-04 and L3-05 are well over the solution length guide (369 and 311 words, lint warning); move the c) reasoning of L3-04 into Periaate/Järkevyys if it is to be trimmed.

## Checked
- Round-1 Polish: L2-06 Vastaus and Järkevyys fixed ("kaksi merkitsevää numeroa", "väite vaatii 20 J energiaa tyhjästä"); L2-05 Periaate fixed and data marked as example; L2-07 now says the lamps take equal energy (216 kJ = 60 W for one hour, 11/54 kJ = 5 %/25 %), recomputed 205 − 162 = 43 kJ, answer key 43; L3-04 c) is now a real modelling part (fossil share under one third, 470 − 400 = 70 PJ, 71 PJ gives 33,25 %) and the repeated "energy becomes heat" explanation is gone from it.
- New L1-07 distractor "kokonaisenergia pienenee, koska lämpö siirtyy ympäristöön" targets a real misconception; feedback repairs it (environment belongs to the system).
- No duplicate of existing tasks, levels fit, plan (8/7/5 per level, data tasks at level 2, one qualitative level-3) kept.
- Recomputed: 39,2 % (470/1200), 218 GJ per capita, 4,86 MJ, 86 %, 2,8 %.
