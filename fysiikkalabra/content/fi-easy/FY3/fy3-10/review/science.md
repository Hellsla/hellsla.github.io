VERDICT: PASS
CONTENT-HASH: 22d5a045d608c2a4

## Blocking
None.

## Polish
- content/fi-easy/FY3/fy3-10/lesson.md:40 — the weighing paragraph has the reader divide each mass by its molar mass, but the lesson text gives no molar mass for nitrogen (28,0 g/mol). Name "typpi 28,0 g/mol" there.
- content/fi-easy/FY3/fy3-10/inquiry.json:168 — "Tilavuuden muutos ei muuta hiukkasten nopeuksia. Siksi lämpötila pysyy samana." This is the sim's assumption, but a real piston pushed in quickly heats the gas. Add a few words, e.g. "(kuin hidas puristus, jossa lämpötila ehtii pysyä samana)", so check-1 (line 444) is not read as a general law.

## Checked
- I recomputed every number in one script and all agree. Weighing: the masses sit within ±0,02 g of n·M with n = 0,2072 mol. m/M = 0,2075 / 0,2064 / 0,2076 / 0,2068, mean 0,2071. R from the mean is 8,32 ≈ 8,3, and from helium 8,302 (mistakes 121,7, 8302 and 0,008302 are right).
- Worked example: n = pV/(RT) = 0,2073 → 0,21 mol and m = 0,83 g, symbolic first. 2 significant figures are justified by the 5,0 l volume and the 4,0 g/mol molar mass. 24 l/mol and the 6,0 g air balloon are right.
- Taulukko: each pV/(NT) column value (1,05; 1,00; 0,98; 0,98; 0,99) follows from its p/p_ref.
- Koe 2: N = 50 (the mistakes 200 → 4,00, 71 = 100/√2 and 25 → 0,50 are right). check-2: 3,0 (2,25 and 1,69 are right). check-c2: 313,15/293,15 = 1,068, about 7 %. Etsi virhe: 1,2 vs 0,083 mol. Exit ticket: 0,601 mol.
- Siirto: m = pVM/(RT) = 2645 kg → 2,64·10³ kg (mistakes 9870 and 2,64 are right).
- sim.js: a 2D box with wall-only elastic hits. The impulse per unit time per unit perimeter gives p = NkT/A exactly. A Python replica gives a mean of 1,005 at N = 20, 0,998 at N = 100, and a 2 s window sd of 5,5 % at N = 20, so the "noin ±10 %" in calc is fair.
- Experiments isolate N, with T and V locked. simState has hitRate and pMeasured.
- Model and conditions: point particles, the limits (high pressure, low temperature), absolute pressure, kelvins and the Pa·m³ = kPa·l = J units are stated. The causal account of pressure is right throughout.
- Exactly one option is correct in each choice, and every distractor's feedback is right.
