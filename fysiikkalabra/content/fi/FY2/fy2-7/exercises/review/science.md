VERDICT: FAIL
CONTENT-HASH: dca6b1359dc2ef02

## Blocking
- content/fi/FY2/fy2-7/exercises/solutions.md:190 (L3-05 c, model answer) — A, causality: "suurempi virta lämmittää johtimia enemmän, joten lämmöksi muuttuu suurempi osa energiasta" does not follow. That argument explains a larger loss, not a larger *share*: if the loss grew in proportion to the current, the share would stay the same. The share grows only because the loss grows faster than the transmitted power. — Fix: "Suurempi teho vaatii suuremman virran, ja häviö kasvaa virtaa nopeammin (kaksinkertainen virta antaa noin nelinkertaisen häviön, vrt. tehtävä L2-06), joten häviö kasvaa nopeammin kuin syötetty teho ja sen osuus kasvaa." Add one line saying the same thing to the task text, or ask in c) only why the loss grows.
- content/fi/FY2/fy2-7/exercises/solutions.md:155 (L2-05 b, explanation) — A, the claim contradicts the task's own data: "luovuttaa lämpöä maahan lähes yhtä paljon kuin talvella". In the table the loss falls from 75 MWh (January) to 49 MWh (April), a drop of 35 %. — Fix: "häviö pienenee (75 → 49 MWh) paljon vähemmän kuin syötetty energia (820 → 430 MWh), koska putket ovat kuumia ja maa kylmää myös keväällä, joten häviö on suurempi osuus pienemmästä energiasta."

## Polish
- solutions.md:155 — "kaksi merkitsevää numeroa kuten kolmen numeron energioiden osamäärässä" is self-contradictory. 255/2650 gives three significant figures (9,62 %), so either give 9,62 % or say that 9,6 % is a choice for comparison.
- solutions.md:158 ff. (L2-06) — extrapolating one doubling to 320 kV: state the assumption (same line, same transmitted power 100 MW), as the guardrail on extrapolation requires.
- exercises.json L3-05 data — the shares (1,5; 3,5; 4,5; 7,0 %) do not follow the loss ∝ I² picture at fixed voltage, which predicts 1,5; 3,5; 4,2; 5,5 %. 4,2 and 5,5 % would make c) exact (answer about 4,0 %).
- docs/exercise-bank/FY2.md:44 — two plan items were not carried out: supply and return temperatures, and heat pump versus direct electric heating. This is defensible for scope (temperatures would need Q = cmΔT, which is FY3), but the plan should record why.

## Checked
- Recomputed all 6 new numeric answers in one script, independently of answers.py: L1-07 4,8 %, L1-08 72 kW, L2-05 9,62 %, L2-06 0,0625 MW, L3-04 6,59 MWh, L3-05 4,73 %. All agree within tolerance, and answers.py matches.
- Every Järkevyys check is numerically true: the monthly shares 9,1/8,9/9,8/11 %, 16² = 256, house total 8,0 kW, 0,593/6,593 = 9,0 %, plain mean 4,1 %, evening 48 % of the loss.
- Scope of L2-06: the lesson teaches the high-voltage effect only qualitatively ("virta pieni → häviö vähäinen"). The factor of 4 per doubling is inferred from the table, not presented as a law, so it fits FY2 as a data task (C). The L2-06 table is consistent with a fixed line resistance of R = 0,64 Ω.
- L1-06 and L2-07 multiple choice: exactly one correct option each, and every feedback is physically right (energy does not vanish; the cause is heating, not speed).
- L3-04: no U-value or conduction formula is used, only the given power reductions, so it stays within FY2 scope. A/B/C savings are 6000/3600/4500 kWh, and the plant-side division by η is correct.
- Notation matches the lesson; the hash was unchanged at the end.
