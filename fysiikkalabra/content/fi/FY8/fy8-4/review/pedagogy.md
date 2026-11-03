VERDICT: FAIL
CONTENT-HASH: b4cca44759d1deba

## Blocking
- inquiry.json, ennuste-1 prompt — the prediction cannot be argued before the evidence: the student is not told that  = 1{,}0\,\text{mm}$ is a dark fringe ("hieman sivussa keskikohdasta" suggests a bright region), and the interference chapter gives no way to place it. The right option needs this hidden fact, and an aalto-minded student who guesses a bright fringe picks "Osuus kasvaa", so the experiment refutes the geometry guess, not the kuula reasoning. Fix: state in the prompt that $ is a place where the waves from the two slits arrive half a wavelength apart (a dark fringe of the wave model), then ask whether the kuula model and the wave model predict an increase or a decrease and which the data will support.

## Polish
- inquiry.json, siirto solution "Järkevyys" — "suunnilleen hyttysen paino" is wrong by about a factor of ten: 0,3 mN is the weight of about 30 mg (a mosquito weighs about 25 µN). Fix: "suunnilleen kolmenkymmenen milligramman painon, esim. useamman hyttysen".
- lesson.md, Comptonin ilmiö — "säteilisivät samaa taajuutta, jota ne saavat" is clumsy Finnish. Fix: "säteilisivät samalla taajuudella kuin tuleva säteily".
- inquiry.json, johtopaatos prompt — "Mitä aallon ja yksittäisen osuman välillä on?" is not idiomatic. Fix: "Mikä on aallon ja yksittäisen osuman yhteys?"
- inquiry.json, ennuste-2 feedback (option 1) — "vaatii vuorovaikutuksen elektronin kanssa" presents the loss of fringes as a disturbance only; the lesson's own claim is that the which-path information removes the interference. Fix: "kun reitti tiedetään, kahden raon aallot eivät enää interferoi".
- Workload: hook, retrieval, two predictions, sim, two experiments, explain, Compton data, a long theory part (four models, Compton, flux), example, error item, transfer, 12 exercises, three checks and exit ticket is well over an hour. Fix: make the siirto task optional and let the student choose 2 to 3 exercises per level.

## Checked
- Opening question is answered by the conclusion and the dualism paragraph; de Broglie is correctly left out.
- Prediction options have misconception-repairing feedback; ennuste-2 is arguable and refutable (koe-2 changes only the path measurement).
- Koe-1 and koe-2 lock the right variables, vary one, and are called model values in the text and the model answer.
- Compton table matches the Compton shift (0,00243 nm times 1 - cos of the angle); distractors are real misconceptions.
- Worked example: one step per stage, numbers re-computed and correct; sanity check ties to the lesson's example.
- Figures buildup, patterns and compton are legible at 390 px; colour is not the only carrier; x0 marker in the patterns figure comes after the experiments.
- Phone captures of the sim and the experiment show no clipping; readout is understandable.
- Solar-sail force 290,5 µN, hints and mistake values are correct.
- Exit ticket tests the core idea (models, p = h/lambda).
