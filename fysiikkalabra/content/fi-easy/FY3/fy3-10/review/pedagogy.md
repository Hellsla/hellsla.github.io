VERDICT: PASS
CONTENT-HASH: 8eeb15b65d9bab34

## Blocking

## Polish
- inquiry.json exp-2 `tolerance` 0.02 (answer 50) — the student is told to find N by measuring where the 2 s average is "noin 1,00", but the sim noise (about ±10 % at N≈20) makes 47 or 53 a legitimate measured result, which would be marked wrong with no mistake feedback — widen to about 0.1 or word the prompt as "laske tai mittaa; tarkka vastaus on kokonaisluku". Not verified in the sim (no captures).
- inquiry.json pred-1 — after `punnitus-vertailu` has already said "yhtä monta moolia", pred-1 is a recap, not a prediction, yet reflect treats it as one; fold it into the retrieval of the opening question or drop it to optional (workload).
- lesson.md "Kelvinlämpötila on suoraan verrannollinen hiukkasten keskimääräiseen liike-energiaan" — E_k is FY4 in this course; say "hiukkasten keskimääräiseen liikkeeseen (nopeuteen)" or keep it as a one-line model statement without naming the quantity.
- inquiry.json check-1 (volume halves, hits per wall rise) — the experiments vary only N and T, so the volume mechanism is met only in `taulukko` and free play; add one optional volume row to exp-2 or a pointer in `kokeile` ("kokeile V:tä ja katso välähdysten tiheyttä").
- inquiry.json virhe, option 3 feedback — "2,0 l" is typeset with \text{l} while the rest of the lesson uses \textsf{l}; make it \textsf{l}.

## Checked
- Path: hook question is answered in Ydinajatus only after weighing, sim and conclusion; slot goals (tilanyhtälö, ratkaiseminen suureelle, kaasulait yhdistettynä, hiukkastason paine) covered, nothing extra.
- Mole and m/M are used in `punnitus` before the theory, but the item defines mole and M in one sentence and its solution explains n = m/M; followable.
- pred-n is committed before exp-1, wrong options repair the misconception (no change, crowding, collisions), and exp-1 can refute them (hit rate and pressure both recorded).
- The weighing data are labelled invented, with scatter; arithmetic of m/M (0,2075 / 0,2064 / 0,2076 / 0,2068), R ≈ 8,3, the taulukko pV/(NT) column, the 3,0 prediction and the exit ticket (0,601 mol) all recompute correctly.
- Model vs measurement is kept apart (source tags, "mallin tulokset ja esimerkkiaineisto" criterion); the sim's constant-T volume change is disclosed in `model`.
- Worked example is staged one step per stage with unit conversions and a sanity check; it uses the same balloon as the opening, which is coherent though the result is already known from Ydinajatus.
- Mistake feedback in laske-r, siirto and check-2 names the actual slip (°C, litres, kPa); check-2 and virhe distractors are misconception-based.
- Finnish reads plainly; case endings after number+unit correct in the text I read.
- Not checked: figures, 360/1280 px layout and sim behaviour, because the packet lists no captures (screenshots not yet run) and I did not open the preview; exercises are outside this packet.
