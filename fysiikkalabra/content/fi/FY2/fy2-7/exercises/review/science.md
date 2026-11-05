VERDICT: PASS
CONTENT-HASH: c5d377ec0ca6ef49

Round 3 (round 2: PASS; round 1: FAIL, 1 Blocking). New YO-skill task L2-08; since round 2 only two lines of its solution changed (commit 4ab4e1a5d, layout for a phone).

## Blocking

## Polish
- exercises.json L2-08, correct reason "…sähköverkkoon lähtee paljon enemmän energiaa…" and the correct choice's feedback "pienempikin osuus on energiana suurempi" (carried from round 2). "Much more energy" decides only because the energy ratio (1000 : 300 = 3,3) is larger than the share ratio (9,0 : 4,0 = 2,3). This is C at FY2 level, since the solution shows 40 MWh against 27 MWh. Optional: "…niin paljon enemmän, että osuus kertaa energia on suurempi".

## Checked
- Round-3 change (solutions.md L2-08 Mallivastaus): each chain is now split into "$E_\text{häviö} = 0{,}040 \cdot 1000\,\text{MWh}$, eli $E_\text{häviö} = 40\,\text{MWh}$" and the same for $0{,}090 \cdot 300\,\text{MWh} = 27\,\text{MWh}$. The numbers, symbol and units are unchanged and correct, and the formula still stands before the substitution.
- `git diff` from the round-2 commit 9fd1b2088 to HEAD: in fy2-7's exercises and answers.py nothing changed apart from these two lines and the review files.
- Recomputed L2-08: 0,040 · 1000 MWh = 40 MWh and 0,090 · 300 MWh = 27 MWh, so the answer is Sähköverkossa.
- Ran answers.py against exercises.json in one script: all 18 numeric answers are within tolerance.
- Round-2 checks still hold: exactly one correct choice and one correct reason; every wrong option and its feedback are right; round-1 Blocking and Polish are resolved.
- Hash unchanged at the start and the end (c5d377ec0ca6ef49).
