VERDICT: PASS
CONTENT-HASH: d0e4b45564aa64a8
Round: 2

Round 2 checks commit 6bbde30c5 against my round-1 report (L2-08). The rest of the set is unchanged.

## Blocking
- none

## Polish
- none

## Checked
- Round-1 Blocking 1 is resolved. The mass order is now listed correctly (teekannu 1,0, kattila 0,60, jääpussi 0,50, kiehuva vesi 0,10 kg), and the text now says "lähes päinvastainen (jääpussi ja kattila vaihtavat paikkaa)". My script confirms it.
- Round-1 Blocking 2 is resolved. The Kattila line now reads "$Q = 201\,120\,\text{J} \approx 201\,\text{kJ}$", which is the exact product.
- Round-1 Polish is resolved. The Periaate now names $c$, $s$ and $r$ instead of "kerroin". Each long chain is split at ", eli", so every line is at most about 240 px wide.
- The items in the task text were reordered (kattila, kiehuva vesi, teekannu, jääpussi). The order is no longer readable from the text, the data are unchanged, and `order` and the answer still match my recomputation (83,8 < 167 < 201,1 < 226 kJ).
- Renders vs text: I viewed review/shots/fy3-7-open-exercises-L2-1280-11.png and -12.png (taken 23:13, after the commit). The reordered text, the split Mallivastaus lines and the corrected mass sentence render cleanly. I judged the phone width from the 1280 px image's scale, not from a 390 px shot.
- The hash was the same at the start and at the end.
