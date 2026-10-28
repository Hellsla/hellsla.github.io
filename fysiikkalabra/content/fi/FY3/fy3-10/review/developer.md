VERDICT: DONE

Complete model solutions (teacher 2026-10-27).
- solutions.md: all 12 blocks now have Annettu, Kysytty, Periaate (why the law fits: closed vessel, equal amounts at equal p and T, constant nR, gauge pressure cancels), Kaava ending in the unknown, Muunnokset, Sijoitus, Vastaus with significant-figure reason, and Järkevyys with real checks (litre of air about 0,041 mol, recomputed masses, ratio of kelvin temperatures, back-substitution).
- lesson.md: Esimerkki reorganised into the seven stages (added Periaate and Yksikkömuunnokset, moved conversions out of stage 1, added the significant-figure reason to Tulos). Nothing else touched.
- inquiry.json: added a solution to punnitus' question, exp-2's question, laske-r, check-2; rewrote siirto in the labelled form.
No numeric error found in the old solutions; all values recomputed and agree with answers.py and exercises.json. The old L2-01 Järkevyys was muddled (a self-contradicting remark on "estimate") and was rewritten.

## Rounding pass
- exercises.json (text only): L3-03 "200 l" -> "200,0 l".
- solutions.md: every Vastaus now lists all data instead of "kuten tiedoissa"; L1-05 limiting datum is M = 44 g/mol; L3-01 V = 0,55 l; L3-02 dm = 6,0 g and M_Ar - M_air = 11 g/mol; L3-03 dp = 10,0 - 7,0 = 3,0 bar (difference has one decimal). L2-03 Järkevyys recomputed (45,5/16,7 = 2,73, 303 K * 2,73 = 828 K; the old "2,7 -> 830 K" did not add up).
- inquiry.json: m/M step explains that 0,2075 is an intermediate value kept for the next step (the Vastaus is 0,21; stored 0.2075 is inside the 2 % tolerance of 0,21, so it was not changed); koe-2 N = 50 and p/p_ref = 3,0 reasons now say exact counts and 75 % / 300-450 K limit; R activity names p and V; kuumailmapallo: the old reason named V and the temperature, the real limiting datum was M = 29 g/mol, so prompt/solution/hints now give M = 29,0 g/mol and V = 2,80 * 10^3 m³ (answer 2640 kg, Vastaus 2,64 * 10^3 kg); Järkevyys uses 3360 kg and 2640 kg.
- lesson.md Esimerkki Tulos: n limited by V = 5,0 l, m also by M = 4,0 g/mol.
