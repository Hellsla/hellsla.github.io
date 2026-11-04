VERDICT: FAIL
CONTENT-HASH: fda9f57419ebbcfb
Round: 2. Round 1 had no Blocking items. Checked the diff since 00b2dcb54: round-1 Polish was applied (ideal meters in L2-05, "mittaustarkkuuden rajoissa", "kuorman resistanssi"), L1-06/L1-07 options were reordered, and L3-04/L3-05 were split into paragraphs. The edit added one defect.

## Blocking
- exercises/solutions.md:204 (fy6-5-L3-05 Sijoitus) — the c) line is duplicated: lines 202 and 204 are identical, and both render as two identical c) calculation blocks (open-exercises-L3-1280-8). — Fix: delete line 204 and the blank line before it.

## Polish
- docs/exercise-bank/FY6.md plan, level 3 — the plan's error analysis "silmukka väärään suuntaan → negatiivinen virta" is still not in the set (L3-05 replaces it). Update the plan, or add one c) item to L3-04: "jos I₃ olisi oletettu toiseen suuntaan, ratkaisu antaisi −0,10 A; mitä merkki tarkoittaa?"

## Checked
- Hash fda9f57419ebbcfb at start and end.
- answers.py was recomputed and compared with every numeric answer in exercises.json; all agree (L2-05 0,59 A; L2-06 40 Ω; L2-07 −3,0 V; L3-04 0,30 A; L3-05 250 Ω).
- L1-06 and L1-07 after reordering: exactly one correct option each. `answer` equals the correct option's text, and the reworded distractors and their feedback are still right.
- L2-05: adding "Lähde, johtimet ja virtamittarit oletetaan ideaalisiksi" makes the U/R check valid. The physics of the paragraph split is unchanged.
- L3-04: the display-block rewrite keeps the same equations and results (I₂ = 0,30 A, 3,3 W = 3,3 W).
- L3-05 a): the added series/voltage-law reasoning is right. "Pienempi kuorman resistanssi laskisi potentiaalin" is now right.
- The 360 px layout check in review/checks.txt is FAIL from an earlier run. Rerunning check_layout.py fy6-5 --width 360 now passes (2 wide tables scroll).
- Set: 8/7/5, with no duplicates.
