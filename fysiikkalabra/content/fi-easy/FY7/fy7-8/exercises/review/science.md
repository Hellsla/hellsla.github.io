VERDICT: PASS
CONTENT-HASH: 8612c63198757666

## Blocking

## Polish


## Checked
- Delta round 2: compared with the files at the round-1 review commit 1ec494e0df with the row markup stripped: exercises.json is byte-identical and solutions.md differs in one line (L3-04 c) only by row breaks; no number, sign, unit or word changed. answers.py unchanged.
- solutions.md:191 (L3-04 c, saving): rows are now "$= (43\,440\,\text{MWh} - 13\,140\,\text{MWh})$", "$\cdot 50\,\tfrac{\text{€}}{\text{MWh}}$", "$= 30\,300\,\text{MWh} \cdot 50\,\tfrac{\text{€}}{\text{MWh}}$", "$= 1{,}515 \cdot 10^{6}\,\text{€}$": the bracket is whole on one row and each relation starts a row; the chain reads correctly.
- Recomputed: $(43\,440 - 13\,140)\,\text{MWh} = 30\,300\,\text{MWh}$, times $50\,\text{€/MWh}$ gives $1\,515\,000\,\text{€}$; $4{,}959\,\text{MW} \cdot 8760\,\text{h} = 43\,440\,\text{MWh}$, $1{,}500\,\text{MW} \cdot 8760\,\text{h} = 13\,140\,\text{MWh}$.
- The packet for this language starts from an older passed version (hash aa0d1a01b2d22233), so its diff also holds the new task fy7-8-L2-10 (FY7-A1), judged here: every formula and number of the task text and of the solution (82 formula spans) is identical to the Finnish version passed in round 1; only the sentences are simplified.
- L2-10 recomputed from the task text: $I = P/(\sqrt{3}\,U)$ = 1049,7 A and 288,7 A; $P_\text{h} = 3RI^2$ = 13,22 MW and 1,000 MW (6,6 % and 0,50 % of 200 MW); ratio $(400:110)^2 = 13{,}2$; $1/0{,}90^2 = 1{,}23$; $RI = 4{,}2\,\text{kV}$; answers.py gives 13,22314 = box answer 13,2231 MW, shown 13 MW inside the 2 % tolerance.
- L2-10 model and wording: three-phase stated in the task, $U$ line voltage and $I$ phase-conductor current, $U^2 : R$ excluded with the right reason, "muuttuu sisäenergiaksi … siirtyy lämpönä"; the added plain-language gloss of "kääntäen verrannollinen" (loss falls as voltage rises) is true and the exact $1 : U^2$ relation stands beside it. Source numbers (5400, 1000, 7600 km; 320 km HVDC; 0,4–110 kV) as verified against the Fingrid page in round 1.
- Hash identical at start and end.
