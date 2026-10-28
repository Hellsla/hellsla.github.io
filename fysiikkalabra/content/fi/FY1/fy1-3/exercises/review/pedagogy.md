VERDICT: FAIL
CONTENT-HASH: de0a10e74e106226

## Blocking
- exercises.json L2-01 / solutions.md L2-01 Vastaus — the delta made the model solution's final answer "5 %" while `answer` is 4.83 with tolerance 0.04 (accepts 4,79–4,87): a student who follows the solution and enters 5 is marked wrong, and a student who rounds to the data's figures cannot know to give 4,8. Also the Sijoitus line still ends "4,83 %", which contradicts "Vastaus 5 %". Fix: make answer and solution agree. Either keep `answer` 4.83 with tolerance 0.2 (accepts 4,6–5,0 and so both 4,8 and 5) and word Vastaus "$4{,}8\,\%$ (kaksi merkitsevää numeroa, koska keskiarvo tunnetaan kolmella; virhe-arvio $0{,}09\,\text{s}$ rajaa luotettavan tarkkuuden noin viiteen prosenttiin)", or set answer 5 with tolerance 0.3 and end Sijoitus with "≈ 4,8 %" before the rounding. Remove the unexplained claim "virhe-arvion tarkkuus ei riitä toiseen numeroon".

## Polish
- exercises.json — still no task on karkea virhe, which the teacher asked to be covered. Swap L2-03 (pure conversion) or add to L2 a series such as 3,12 s, 3,25 s, 3,07 s, 4,31 s, 3,19 s, 3,15 s: find the outlier, drop it, average the rest (avoid repeating the lesson's `karkea` data and the worked example).
- solutions.md Kaava lines (L1-05, L2-01, L2-02 and others) — "Kaava on jo ratkaistu kysytyn suureen suhteen: …" / "Kysytty on …" repeats the same formula; delete the repetition.
- solutions.md L1-02 Periaate — one sentence "Virheen merkintä on $\Delta x$" would stop confusion with $\Delta x$ as the half-range estimate in L1-03 and L1-05 and $\Delta t_\text{sys}$ in L3-01.
- solutions.md L2-02 Vastaus — "kolmen lukeman keskiarvo kantaa yhden numeron lisää" is unclear; write "Lukemat ovat millimetrin tarkkuudella, joten tulos $10{,}7\,\text{mm}$ ilmoitetaan kolmella numerolla."

## Checked
- Delta: tolerance 0.04 for L2-02 (10,67 mm) accepts the solution's 10,7 mm.
- Counts 5/4/3; situation first, question last; school-lab contexts; no task repeats the worked example.
- Solutions otherwise use $\Delta x$, $\Delta t$, $\Delta L_\text{sys}$; units and conversions shown; Finnish correct.
- Exercise captures listed not opened; layout checks pass.
