VERDICT: FAIL
CONTENT-HASH: 776976f81cfa9ae4

## Blocking
- exercises/solutions.md:155 (L2-07 c) — A: "lampun jälkeinen virta on joskus suurempi (mittaus 4) kuin ennen lamppua, mikä ei olisi mahdollista, jos virta kuluisi" is false. The pair in measurement 4 differs by 0,01 A, one display step, and the Periaate (line 153) itself says such differences in either direction come from the reading's uncertainty. A single higher reading is therefore entirely possible even if the current did drop slightly. The model solution teaches a wrong inference from data. Fix: replace the sentence with "Lisäksi erot ovat mittauksittain kumpaankin suuntaan eivätkä ylitä yhtä näyttöaskelta $0{,}01\,\text{A}$, joten ne selittyvät lukeman epävarmuudella."

## Polish
- exercises.json:210 and :215 (L2-07): "Ampeerimittarin pienin lukema on 0,01 A" literally names the smallest value the meter shows, not its resolution (guardrails: keep the terms apart). Write "Ampeerimittarin resoluutio eli pienin näyttöaskel on $0{,}01\,\text{A}$" and use the same term in the answer and in solutions.md:155.
- exercises.json:332 (L3-05): "kaikki johdon elektronit liikkuvat samalla nopeudella" should be "kaikki johdon vapaat elektronit", because the given count and the model are about free electrons only.
- solutions.md:149 (L2-06 Periaate): "Virta kulkee mieluummin johtoa pitkin" gives the current a will. Write "Paksu johto päästää virran kulkemaan paljon helpommin kuin lampun hehkulanka, joten lähes koko virta kulkee johdon kautta."
- L1-08 vs L2-02: the same N = It/e computation, and the level-1 task (two conversions) is harder than the level-2 one (none). Consider giving L1-08 the values in A and s, or swapping their levels.
- Plan drift (docs/exercise-bank/FY6.md): L1-07 asks about an open switch instead of "mikä kaavio vastaa kuvattua piiriä", and L2-06 describes the two faulty circuits in words instead of the planned two diagrams. This is acceptable, but update the plan or the tasks so that they agree.

## Checked
- All 15 numeric answers recomputed in one script with my own formulas; they agree with answers.py and exercises.json: L1-08 9,36·10¹⁷, L2-05 22,8 C (mean 0,38 A), L3-04 12,5 Wh, L3-05 0,0192 mm/s.
- L2-07 means 0,310 A and 0,306 A. L3-04: 3,35 Ah, U_ka 3,73 V, 45 kJ, estimate 13,4 Wh, 7,2 % too high. L3-05: 14,5 h for 1,0 m.
- The data are realistic: 1,3·10²³ free electrons per metre is a copper wire of about 1,5 mm². The phone-battery data (4,0 → 3,4 V, about 12 Wh) and the dimming-lamp table are both plausible.
- The tolerances accept each solution's rounded answer (23 C, 9,4·10¹⁷, 13 Wh at 4 %, 0,019 mm/s), counting the one-digit step rule in lesson.js.
- MC L1-06 and L1-07: exactly one correct option each, and every distractor's feedback is right and matches the brief's misconceptions.
- Notation (I, Q, t, U, E, N, e) matches the brief, and every new task has a complete solution that is symbolic first.
