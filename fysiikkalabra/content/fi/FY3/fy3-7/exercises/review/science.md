VERDICT: PASS
CONTENT-HASH: bf811b5954b48e62
Round: 3

Round 3 checks commit 3b0a55d57, a one-sentence change in the L2-08 Mallivastaus of solutions.md. The rest of the set is unchanged since the round-2 PASS.

## Blocking
- none

## Polish
- none

## Checked
- The mass order is now listed from smallest to largest: kiehuva vesi 0,10, jääpussi 0,50, kattila 0,60, teekannu 1,0 kg. This is correct.
- The sentence "Lämmön järjestys on lähes päinvastainen" is correct. The heat order is teekannu, jääpussi, kattila, kiehuva vesi (84 < 167 < 201 < 226 kJ, recomputed). The reverse of the mass order is teekannu, kattila, jääpussi, kiehuva vesi, so only jääpussi and kattila differ.
- No number, formula, option or answer changed. `order` and the answer string still match my recomputation.
- Renders vs text: I judged this round from the diff text only. The change is prose plus the inline masses that were already there, so there are no new formula chains.
- The hash was the same at the start and at the end.
