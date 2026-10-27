VERDICT: FAIL
CONTENT-HASH: 73f0ca12470c1103

## Blocking
- exit-ticket.json:q3 — The question says "Raskas ja kevyt kuula putoavat samasta korkeudesta ilmassa lähes yhtä nopeasti". Koe 3 shows the opposite for same-size balls: at 4 s the 1 kg ball is about 27 m/s and the 10 kg ball about 37,5 m/s, and the 0,1 kg ball about 10,5 m/s. The answer's "Putoamiskiihtyvyys ei riipu massasta" is a vacuum statement, here applied to air. A student who did Koe 3 meets a premise that contradicts their own table, on the check of the core idea. Fix: ask "Tyhjiössä höyhen ja vasara putoavat yhtä nopeasti, mutta ilmassa höyhen putoaa hitaammin. Miksi?" and begin the answer "Tyhjiössä putoamiskiihtyvyys on sama kaikille kappaleille."

## Polish
- inquiry.json:exp-1/2/3 "initial" — The "Alkutila" panel shows "ympäristö = 0" and "ympäristö = 1". A student cannot know that 0 is tyhjiö and 1 is ilma. Fix: show "ympäristö = tyhjiö / ilma".
- inquiry.json:data question mistakes — value 10 is inside the relative tolerance 0,03 of 9,8 (accepted range up to 10,09). The wrong-answer feedback can never be the one a student sees, and reading 5,0 is marked correct. Fix: drop that mistake entry or set the tolerance to 0,01.
- Workload — Three experiments with a numeric question, two predictions, a reflection, an error-spotting item, a transfer task, twelve exercises, three checks and an exit ticket. The slope calculation Δv/Δt appears five times (exp-1, data, L1-04, L2-04, siirto). Mark `reflect` and `virhe` optional, or drop L1-04 or L2-04.
- exercises.json:L2-02 — Almost the same shape as the worked example (compute v from t, convert to km/h). Use a different context, such as a time from v in km/h.
- Exp-1 (vacuum, t slider) only reproduces v = gt. The emergent evidence is in Koe 3, so the order is acceptable, but the conclusion should say that Koe 1 and 2 are model values.

## Checked
- Learning path: the prior-knowledge retrieval, the predictions and the Apollo hook (answered by Koe 2 and the reflection) follow from fy1-5, and the lesson stays within the slot's goals.
- Predictions can be refuted by the experiments; masses and the environment are locked and one quantity varies per experiment.
- The example has seven stages and a symbolic-first solution. Solutions are complete and logical. The data-task figure reads correctly (the line is just under the 5 m/s grid line at 0,5 s).
- The figures in the captures are legible and sit beside their paragraphs. The simulation at 390 and 1280 px has little text and its explanations are behind closed boxes.
- Exercise levels, counts and feedback are good; mistake values match the stated misconceptions.
- Finnish and glossary terms are correct (putoamiskiihtyvyys, vapaa pudotus, kiihtyvyys).
