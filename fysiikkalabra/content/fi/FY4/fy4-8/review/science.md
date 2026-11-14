VERDICT: PASS
CONTENT-HASH: 8701713dc6e7b8e3

## Blocking
None.

## Polish
1. lesson.md (fi, en, fi-easy), paragraph "Painon eli painovoiman ja kitkan eron…": "Kitkan ja ilmanvastuksen tekemä negatiivinen työ kasvaa jokaisella kuljetulla metrillä" has no condition of its own. In context it is about the coaster, and the paragraph on the energy principle already gives the conveyor-belt exception, so it is a C simplification. Adding "kun ne vastustavat liikettä" there too would match the corrected sentence word for word.
2. Still from the earlier report: notes 1–4 (Tiivistelmä W labels, the v_2 index clause, comments in the code and figures.json, the wording of the concept card) are unchanged and are still polish.

## Checked
- Work–kinetic energy paragraph (fi, en, fi-easy): "Kun kitka ja ilmanvastus vastustavat kappaleen liikettä, niiden tekemä työ on negatiivinen…" now states its condition (B removed). It agrees with the energy principle paragraph (stationary surface or air; a moving belt or wind can do positive work) and with the worked example ("negatiivinen, koska … vastustavat liikettä").
- No "aina negatiivinen / always negative" and no "aina korkein / always the highest" is left in lesson.md, inquiry.json, exit-ticket.json or meta.json in any of the three languages. "Kokonaisenergia säilyy aina" and "energia säilyy aina" (a distractor) are correct as they are.
- Miksi question (fi, en, fi-easy): "perinteisen ketjuhissillä toimivan … yleensä korkein, jos junalle ei anneta myöhemmin lisää energiaa" fits the model. Launched coasters and booster wheels are now outside the claim, and the condition "no energy added later" is stated.
- check-3 prompt (fi, en, fi-easy) agrees with its criteria and model answer: the chain lift supplies the mechanical energy, nothing adds to it afterwards, without losses the train reaches at most the starting height, and resistive work grows with distance so "mäet yleensä madaltuvat". The prompt's "yleensä" matches the model answer's "yleensä". The criteria ask only for what the prompt asks.
- The Pohdinta phenomenon (inquiry.json, chain lift to 40 m, then nothing pulls the train) and the Ydinajatus coaster paragraph (rolling resistance and air resistance oppose the motion the whole way) match the new assumptions.
- No numbers or symbols changed in the diff, so nothing needed recomputing. The content hash was the same at the start and the end.
