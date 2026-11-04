VERDICT: PASS
CONTENT-HASH: 196fd38f148cdfeb
Round: 2

Round 2: I reviewed the round-1 fixes (`git diff HEAD~1`) in the 20-task set.

## Blocking
- none

## Polish
- solutions.md:169 and exercises.json:207 (L2-07): the Vastaus now argues correctly that the honest result is about 50 J, but the boxed answer and `answer` are still 50,4 J. The 2 % tolerance accepts 50, so nothing breaks. Fix: box "$\Delta U \approx 50\,\text{J}$" and set answer 50 (answers.py can stay at 50,4 before rounding).
- solutions.md L3-04: the heading "Kuvaajan lukeminen" sits above a table reading ("Taulukossa jakovälejä…"). "Taulukon lukeminen" would be accurate.
- Carried over from round 1: the plan's level-2 error item (forgetting the calorimeter) became a sign error (L2-06). This is fine physically, and pedagogy should judge it.

## Checked
- Round-1 Blocking (L3-05, a missing condition) is resolved. exercises.json:315 now says "vastuksen ja keittimen rungon oma lämpeneminen on merkityksetön". The Periaate uses the same assumption, so $Q_\text{ulos} = E_\text{v} - \Delta U$ is now fully the heat lost to the surroundings, and c) ("keittimen seinän kautta ilmaan ja pöytään") agrees with it. The phrase "kuten hyvin eristetyllä keittimellä" was dropped, and the text now says 15 % is "selvästi mitattava osa".
- Round-1 Polish was resolved. L1-07 states that the vessel's own warming is neglected, so "täsmälleen" in the correct option's feedback holds.
- Round-1 Polish was resolved. L2-05 removed the ideal-gas clause from the task and the solution; ΔU = 0 now rests on the internal energy being a state function. That is correct for any gas.
- L1-06 and L1-07 reorders and rewordings: each has exactly one correct option, the answer string matches the correct choice, and the feedback fits each option.
- I recomputed all eight new answers in one script, and they agree with answers.py and are within tolerance: L1-08 36 kJ; L2-05 −90 J; L2-06 20 J; L2-07 50,4 J (spread ±0,2 N ≈ 4,8 %); L3-04 18,72 J; L3-05 P = 1999 W, 34,8 kJ = 14,5 %, cumulative loss 8,1/16,3/26,1/34,8 kJ, mean 0,29 kW.
- Signs follow ΔU = Q + W throughout. The scope, the 8/7/5 levels and the absence of duplicates are unchanged.
- The L3 screenshot at 1280 px (part 8, taken after the fix commit) renders the changed L3-05 solution cleanly.
- The hash was the same at the start and at the end.
