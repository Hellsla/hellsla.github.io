VERDICT: PASS
CONTENT-HASH: 9e418b3b567bd336

## Blocking

## Polish
- inquiry.json (johtopaatos `model`) — "joten $P_2$ ei kasvanut koko ajan" is true, but on the student's rows (4, 8, 16 Ω) $P_2$ actually fell: 9,0 → 8,0 → 5,76 W. It rises only below $R_2 = R_1$. Consider "joten $P_2$ jopa pieneni (9,0 W → 8,0 W → 5,76 W)".
- sim.js beaker(): with the glow scaled to PMAX = 72 W, the default series state (4 W and 8 W) glows at 6 % and 11 %, which is barely visible. The ratio is right and the bar and the numbers carry the comparison, so this is a visual matter, not physics.

## Checked
- Round-1 Blocking 1 (koe-1 model answer) is fixed. The answer now compares within a row ("samalla virralla …, $P_2 > P_1$ joka rivillä, jossa $R_2 > R_1$") and says that raising $R_2$ lowers the common current. Recomputed: series rows with $R_1 = 4\,\Omega$ give (I, P1, P2) = (1,5; 9,0; 9,0), (1,0; 4,0; 8,0), (0,60; 1,44; 5,76). The statement holds for every slider value 2–20 Ω, and the reverse holds for $R_2 < R_1$.
- Round-1 Blocking 2 (glossary **sähköenergia**) is fixed: "laitteen sisäenergiaksi, joka siirtyy lämpönä ympäristöön". No "lämmöksi" or "muuttuu lämpö…" anywhere in the lesson, inquiry.json, the exercises or the glossary terms.
- Round-1 Polish is applied: the toaster ratio 59 : 0,050 ≈ 1200 now follows the numbers (recomputed 1176); "kun resistanssi pysyy likimain samana"; tarkistus-3 says "yhtä nopeasti".
- The sim glow is now `P / PMAX`, the same scale as the bar (0–72 W). In parallel at 12 V, 2 Ω and 4 Ω now glow 1,0 : 0,5, in proportion to their power. The howto ("hehkuu sitä kirkkaammin, mitä suurempi sen teho on") matches. No change to the physics, simState or the stop at 80 °C.
- All lesson numbers recomputed again: 6,0 W; 4/8 W and 36/18/54 W; koe-2 rows 72/54/45 W; example 9,6 W, 4,8 W, 4320 J, 1,2 A; siirto 37,24 min with mistakes 2235, 77,6, 447; tarkistus-1 1322/529 Ω; tarkistus-2 12,8 W; exit 5,0 A and ×4; kertaus 0,20 A.
- Within-circuit comparisons in the theory, Yleinen virhekäsitys, the summary, virhe and the predictions stay correct and consistent with the corrected model answer.
- The energy wording follows the FY6 rule throughout (sisäenergiaksi, siirtyy lämpönä).
