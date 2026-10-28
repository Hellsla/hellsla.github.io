VERDICT: FAIL
CONTENT-HASH: 4afa2160cff0bd47

## Blocking
1. exercises.json, every task text (L1-01 … L3-03) — quantities, units and percentages are plain text ("500 MWh", "4,0 %", "2,5 kW") while the solutions are LaTeX; the teacher's rule is everything LaTeX, and fy2-1 … fy2-6 write them as `$500\,\text{MWh}$`, `$4{,}0\,\%$` — rewrite all 12 texts with LaTeX values.

## Polish
1. Level 3 is not reasoning: L3-03 is L1-05 with a week instead of a day (a unit conversion, level 2), and L3-02 is a sum of two losses; replace L3-03 with a task that needs a decision (e.g. which of two networks delivers more energy to the user given different input and η) and let L3-02 ask for a comparison.
2. Overlap: L1-01 has the same computation as the worked example; L2-01 and L2-02 repeat tarkistus-2 (E_perille : η at 91 %); L2-03 is a one-step percentage of a given number (level 1) and the 3,3 TWh is nearly the lesson text's "noin 3 TWh". Give level 2 a real second step.
3. L1-05, L2-04 and L3-03 all multiply a loss power by a time; none asks for a result with a physical interpretation (e.g. compare the heat loss with a household's use).
4. solutions.md L1-02, L2-03 — the significant-figure reasons are weak ("erotus on täysinä megawattitunteina"; "kaksi merkitsevää numeroa kuten kulutuksessa" while 4 % has one); say that the least precise datum sets the figures.
5. No task is conceptual (insulation, voltage, why the percentage is of the input); if the schema only allows numeric answers, add one where the wrong base gives a distinct value.

## Checked
- Levels 5/4/3 as required; answers and tolerances consistent with the solutions (1055 vs 1050 kWh within tolerance).
- Every solution has the seven parts, symbols first, conversions stated; followable by a student who could not solve the task (1280 px capture).
- Input-versus-output base for percentages is addressed (L2-01, L2-02, L2-04).
- Finnish and terms (siirtohäviö, hyötysuhde) correct; chapter names used, no ids.
