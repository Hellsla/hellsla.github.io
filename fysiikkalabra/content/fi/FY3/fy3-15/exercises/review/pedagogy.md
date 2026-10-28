VERDICT: PASS
CONTENT-HASH: b41a8c9ef224a497
## Blocking
## Polish
- exercises.json fy3-15-L3-02 — "($1\,\text{GWh}$ = 3,60 · 10¹² J)" and "(1 kt = 10⁶ kg)" stay plain while the rest of the sentence is LaTeX; write "$1\,\text{GWh} = 3{,}60 \cdot 10^{12}\,\text{J}$" and "$1\,\text{kt} = 10^6\,\text{kg}$". Likewise "20,0 m²" in L1-03 and the efficiencies in L2-01…L3-03.
- solutions.md fy3-15-L3-02 Järkevyys — "ostettu polttoaine, joka kuluu: sen energiasta noin $38\,\%$ muuttuu …" has a stray colon; "hiilivoimalassa nimittäjä on ostettu polttoaine, jota kuluu: sen energiasta noin $38\,\%$ muuttuu sähköksi ja loput hukkalämmöksi, ja palamisessa syntyy päästöjä. Tuulen energia ei ole ostettava varasto."
- solutions.md fy3-15-L2-02 Järkevyys — "hieman suurempi kuin koko laitoksen tavallinen hyötysuhde … ja se on ketjun heikoin lenkki" holds two ideas in one sentence; split the "heikoin lenkki" clause into its own sentence.
## Checked
- Delta (numbers with units to LaTeX; Järkevyys reworded for the tuulivoimala losses, the 43,1 % steam cycle, the heat pump explanation): no number, answer or tolerance changed.
- The new heat pump explanation (sisälle tulee sähkön lisäksi ulkoilmasta siirretty lämpö, sähköä kolmasosa) is correct and consistent with the fy3-11 lämpökerroin text.
- The tuulivoimala reasoning ("osa roottorin ottamasta energiasta … lämpönä ympäristöön") fixes the earlier "loput häviää" and is physically sound.
- Recomputed L1-01 90,2 %, L2-01 109 MW, L3-02 13,6 kt, L3-03 87,7 kWh (263 and 111 kWh for the comparisons).
- Case endings after math units read correctly (`$40\,\%$:n`, `$4\,\text{kW}$`).
- Levels and counts unchanged; none repeats the worked example.
