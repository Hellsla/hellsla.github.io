VERDICT: PASS
CONTENT-HASH: fba7000b59694eb4
SCOPE: delta added-exercise from fb4c9e7694ba0259 base 89bcb63b7431

## Blocking
(none)

## Polish
- solutions.md (L1-09) — Periaate could add that the bag's air pressure equals the outside pressure because the bag is not stretched taut (as the worked example says "pääsee laajenemaan vapaasti"); optional, the task's "ilmapussi" implies it.
- Carried over from the previous round: L2-08 intermediate point named $V_2$; L2-05 mirror reason for B; L1-07 third plain Boyle compression.

## Checked
- Added task L1-09 only (delta added-exercise); other tasks unchanged per packet.
- Table value: docs/mafy-arvot.tsv row fy3-9, MAFY "Ilmanpaine, tiheys ja lämpötila eri korkeuksilla", 3000 m → 70 100 Pa (VERIFIED); agrees with the standard atmosphere (70,1 kPa).
- Recomputed: $V_2 = 101 \cdot 2{,}0 / 70{,}1 = 2{,}882$ l → 2,9 l; answers.py gives 2,881598; with 70,108 kPa 2,8813 — same rounded answer.
- Law and conditions: closed bag (fixed amount), temperature stated constant in the task; the solution notes that the real temperature falls with height (table 15 °C → −4,5 °C), so the assumption is explicit (guardrail "state the model's assumptions in the task").
- Unit l, two significant figures from $2{,}0$ l; tolerance 0,04 (±4 %) covers a student using 101,325 kPa or rounding the table value.
- Solution complete: given/asked, principle with reason, symbolic $V_2 = p_1V_1/p_2$ before numbers, conversion Pa → kPa, substitution, rounding reason, real check (pressure ratio 1,44 and $pV$ equal 202 kPa·l).
- Notation matches the brief ($p_1V_1 = p_2V_2$, \textsf{l}); inside FY3 central content (kaasujen tilanmuutokset); level 1 fits (one formula, one lookup).
- Hash identical at start and end.
