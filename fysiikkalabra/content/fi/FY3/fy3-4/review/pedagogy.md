VERDICT: FAIL
CONTENT-HASH: 85b6e93f673b2a8b

## Blocking
- lesson.md "## Kaava: Paine ja hydrostaattinen paine", kaavat-rivi `hydrostaattinen paine :: p = p_0 + \rho g h` — the box names the total pressure "hydrostaattinen paine", but the next paragraph, the glossary and the example say that only the term $\rho g h$ is hydrostaattinen paine (= ylipaine). A student memorises the label and then loses the p0 distinction the lesson is built on — rename the line to a pressure-in-liquid name (e.g. "paine nesteessä"), and keep "Kaava:" heading consistent with it.

## Polish
- inquiry.json pred-3 / check-c2: the check repeats pred-3 almost word for word (tube vs. pool, same options), so it retrieves what was just told. Change the check's situation (e.g. slanted or bulging vessel, same depth) so it tests transfer.
- pred-3 has no experiment, so the hydrostatic paradox is settled only by derivation; the sim cannot refute it. Acceptable, but say in reflect that this one is argued, not measured.
- inquiry.json check-3 criterion 1 asks for "noin 29 kPa", but the prompt asks only for concepts (paine, ylipaine, voima); drop the number from the criterion or ask for it.
- lesson.md example stage "Sijoitus": three calculations (ρgh, p, F) in one stage, against "one step per stage". Split F into its own stage.
- The simulation only computes the formula the student predicts (admitted in the model answer); fine for FY3 since the conclusion says so.

## Checked
- Learning path: hook, retrieval, prediction, data, theory, example, answers the dam question after the student has acted; stays inside the slot (p = F/A, p0 + ρgh, ylipaine, force perpendicular).
- Predictions: pred-1 and pred-2 refutable by the sim (150 → 199 kPa; 98 → 122 kPa); feedback repairs the missing-p0 and the "volume matters" misconceptions without restating answers early.
- exp-1 holds ρ locked, varies h, numeric question has the typical mistakes (Pa/kPa, total/h); conclusion `after` exp-1; workload is one lesson with the optional items.
- Speakers Aino/Bea/Cem: the right one is a different person from the first prediction; no letter references.
- Figures at 390 px (brick, graph, simulation): legible, labelled, colour not alone; sim has little text, notes behind named boxes.
- Etsi virhe, the barometer transfer (three hints, mistake feedback) and check-2 solutions are complete and followable.
- Exit ticket tests the core idea (p = F/A; ρgh + p0).
- Finnish: no case slips found ("$290\,\text{kN}$:n voima" correct).
- Only the sim, one figure (fig-2/4) and the sim captures opened; the rest rests on the packet text.
