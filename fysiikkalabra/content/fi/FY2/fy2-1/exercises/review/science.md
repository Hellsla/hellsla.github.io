VERDICT: PASS
CONTENT-HASH: 2b3698a734643bfa

Round 2: the round-1 blocking item (L1-07, a defensible third option) is fixed. The new distractor "kokonaisenergia pienenee, koska lämpö siirtyy ympäristöön" is clearly wrong, its feedback is right, and solutions.md:55 now says "katoaa tai pienenee". All three round-1 Polish items were taken up (L2-05 reason, L2-07 lamp data, L3-05 reflection).

## Blocking
(none)

## Polish
- solutions.md L3-04 c) Vastaus and exercises.json L3-04 c) — "Kokonaiskulutus voi pysyä samana, koska energiaa ei synny eikä katoa" gives the conservation law as the cause, but a constant total is the task's assumption, not a consequence of the law. In real primary-energy statistics, replacing fossil fuels with wind or hydro usually lowers the total because combustion losses go away. Fix: ask "selitä energian säilymislain avulla, miksi korvaavan energian on katettava sama käyttö" and answer "käytöt tarvitsevat saman energian, eikä sitä synny tyhjästä, joten vesi- ja tuulivoiman on tuotettava se, minkä fossiilinen tuotti (mallissa kokonaiskulutus oletetaan samaksi)".
- solutions.md:174 (L3-05 Vastaus a–c) — the model now says the rest is "lämpöenergiaa tai heijastuu", but a) to c) still call all 4,86 MJ lämpöenergia ("86 % kaikesta lämpöenergiasta"). Write "lämpöenergiaksi muuttuva tai heijastuva energia (hukka)" once in a), or say in Periaate that the reflected part is counted with the heat.
- exercises.json L1-07 third option feedback — "Ympäristö kuuluu systeemiin": the task names no system. Write "Kun ympäristö otetaan mukaan systeemiin, ...".

## Checked
- Recomputed in one script (scratchpad recompute_r2.py): L2-05 60,0 %; L2-06 20 J; L2-07 (216 − 11) − (216 − 54) = 43 kJ; L3-04 470/1200 = 39,2 %, 218 GJ per resident, c) more than 470 − 400 = 70 PJ, and 71 PJ gives 399/1200 = 33,25 %; L3-05 4,86 MJ, 86 %, 2,8 %. All match the answer key and solutions.md.
- L2-07 new data: 216 kJ/h is 60 W. The light shares 5,1 / 7,4 / 25 % are realistic, and 43 kJ to two significant figures is justified by 11 kJ.
- L3-04 c) boundary case (exactly 70 PJ gives exactly one third, so more is needed) is stated correctly.
- L1-07 has exactly one correct option, and every distractor's feedback is right.
- FY2 scope holds: no mgh, no c·m·ΔT, and no product of chain efficiencies. Invented data are now marked "esimerkkilukuina".
- The hash was the same at the start and the end.
