VERDICT: PASS
CONTENT-HASH: 901e18a6fefc4a77

## Blocking

## Polish
- lesson.md:455 (Esimerkki, Tulos) — "Ainemäärän rajoittaa tilavuus 5,0 l ja massan lisäksi moolimassa 4,0 g/mol" is garbled. Fix: "Ainemäärän tarkkuutta rajoittaa tilavuus $5{,}0\,\textsf{l}$, ja massan tarkkuutta rajoittavat lisäksi moolimassa $4{,}0\,\text{g/mol}$; kumpikin on annettu kahdella numerolla, joten tulokset annetaan kahdella merkitsevällä numerolla."
- lesson.md Esimerkki, Tulos stage — the stage also does a new calculation (m = nM = 0,83 g); the answer stage should only state and round. Fix: move the m calculation into Sijoitus (n and m together) and keep Tulos for the answer and the significant-figure reason.
- inquiry.json check-2 solution (Periaate) — "pV = NkT" brings in $k$, which the lesson never defines. Fix: "tilanyhtälön $pV = nRT$ mukaan $p \propto nT/V$, ja $n$ on verrannollinen hiukkasmäärään $N$".
- lesson.md and inquiry.json — numbers with units stay plain in places (101 kPa:n, 0,207 mol, 24 litraa, 5,0/24, 60 ml, 2,0 litrassa) beside LaTeX ones; the Etsi virhe feedback has `\text{l}` where the rest uses `\textsf{l}`. Make them consistent.
- inquiry.json taulukko — the last column pV/(NT) is already computed, so the student only reads a result. Fix: leave one cell empty (e.g. row 3) for the student to compute before the question.

## Checked
- Path: hook question (how to compare gas amounts) is answered by the weighing, m/M ≈ 0,207 mol for four gases, then R ≈ 8,3 and pV = nRT; the Miksi/helium question is answered in Ydinajatus and Esimerkki Järkevyys; slot goals (tilanyhtälö, ratkaiseminen, particle-level pressure sim) covered.
- Predictions: pred-n is committed before exp-1 and refutable (50/100/200 particles); pred-1 is an inference after the data and each wrong option repairs its misconception (heavier = more particles, helium "packs tighter").
- Experiments: T and V locked in exp-1, T = 600 K locked in exp-2; N has step 10, so the answer 50 is reachable and 49 to 51 is a fair tolerance; the prediction p/p_ref is not displayed by the sim.
- Computation check: all table rows (pV/(NT) 1,05/1,00/0,98/0,98/0,99), the three wrong values of laske-r (121,7, 8302, 0,008302), siirto (91 200 mol, 2640 kg) and check-2 (3,0; 2,25; 1,69) match their mistake feedbacks.
- Each choice item has one correct option; Etsi virhe (20 K instead of 293 K) is unambiguous; exit ticket (0,601 mol; equal n but heavier CO2; p doubles) tests the core idea.
- Solutions follow the seven parts with symbols first; the model-value versus example-data distinction is stated in the conclusion.
- Figures judged from aria-labels (no captures): scale claims (speed ratio 2,7:1, masses) agree with the numbers. Workload is heavy but optional items (kertaus, reflect, virhe, siirto, check-3) are marked.
- Round 2: re-check of round-1 Blocking items against the fix diff. There were none; the diff changes two sentences in Ydinajatus and Kaava to mark the weighing masses as example values ("esimerkkipunnituksessa (keksityt arvot, joissa on punnituksen hajontaa)", "Esimerkkipunnituksesta saadaan"). Grammatical, consistent with the inquiry's source note, no number or answer changed.
