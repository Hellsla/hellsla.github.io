VERDICT: PASS
CONTENT-HASH: f56ae41225b29686
SCOPE: delta: round 2, the fixes of round 1 in fy9-magnetismi-valo-s8 and -s9; s1-s7 and the intro untouched, not re-judged.
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
None.

## Polish
- s9 b: the chain now rounds its intermediate values ($0{,}405 \to 0{,}41\,\text{W}$, $0{,}288 \to 0{,}29\,\text{J}$, $0{,}081 \to 0{,}082\,\text{J}$). The result is the same: $0{,}29 + 0{,}082 = 0{,}372 \approx 0{,}37$, and the unrounded sum is $0{,}369 \approx 0{,}37$. Keeping a guard digit ($0{,}288 + 0{,}081$) would be cleaner, but this is no error.
- Carried from round 1: the alt text of figure fy7-5/flux-task-2 says "käämin läpi kulkeva magneettivuo", but the task text says "yhden kierroksen läpi kulkeva". This text belongs to the owner figure (lessons/FY7/fy7-5/figures.py, line 191) and is unchanged.

## Checked
- `units.py hash` gave f56ae41225b29686 at the start and at the end. Packet check: `practice.py check: OK`.
- Round-1 Blocking item, s9 Yleisiä virheitä line 2: it now reads "jännite on tuhatkertainen ($2400\,\text{V}$ oikean $2{,}4\,\text{V}$:n sijaan)". This matches $120 \cdot 8{,}0 / 0{,}40 = 2400$. Fixed in solutions.md line 658 and in the packet.
- Round-1 Polish, s8 line 1: it now reads $0{,}30 : 0{,}45 \approx 0{,}67$, which my recomputation confirms ($0{,}667$). Fixed.
- I diffed the sovella files against the round-1 commit (ad5dcedf). The changes are:
  - s9 b: the chain in solutions.md and in the tasks.json detail now has aligned rows, with the power row added.
  - s9 text: the sign convention is reworded, with the same meaning.
  - s9 c: the question is reworded and still does not reveal the answer.
- My recomputation script:
  - $e = 2{,}4$ and $1{,}8\,\text{V}$; $P = 0{,}72$ and $0{,}405\,\text{W}$; $W = 0{,}369 \approx 0{,}37\,\text{J}$.
  - $I = 0{,}30$ and $0{,}225\,\text{A}$; flux zero at $t = 0{,}25\,\text{s}$.
  - s8: $n = 1{,}5$, $v = 2{,}0 \cdot 10^8\,\text{m/s}$, $\alpha_\text{c} = 41{,}8^\circ \approx 42^\circ$.
- The Järkevyys line ("teho alle watin, aikaa alle sekunti, energia alle joulen") holds, because $\sum P\,\Delta t < 1\,\text{W} \cdot 0{,}60\,\text{s}$.
- Nothing newly broken:
  - the rounding of the answer is two significant figures, matching the data;
  - the unit fields are unchanged and language-neutral;
  - the task texts name no formula or method.
