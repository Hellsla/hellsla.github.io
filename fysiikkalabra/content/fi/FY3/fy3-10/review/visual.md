VERDICT: PASS
CONTENT-HASH: e0f90cf823e55c4a

## Blocking
(none)

## Polish
- [Minor] Carried over unchanged from earlier rounds: readout break "keskiarvo 0,3 s / :n ajalta" in sim-390 and exp-1-390; canvas labels about 8 px on a phone; fig-4 doubled speed barely visible. Not touched by this diff.
- [Minor] laske-r "Näytä ratkaisu" is closed in every capture, so the reworded Periaate sentence ("ja todelliset kaasut noudattavat niitä hyvin, kun kaasu on harvaa") was judged from source. It is plain prose with no maths, so it carries no layout risk.

## Checked
- The diff changes two solutions in inquiry.json: laske-r (Tutki) and check-2 (Tarkista task 3). It adds no symbols or units that were not already there, except $pV = nRT$, $N$ and $n$ in check-2.
- Opened open-tarkista-1280-2 and -3: check-2 with hints and solution open. The new Periaate paragraph renders cleanly: inline $pV = nRT$, "$p \propto \dfrac{NT}{V}$," with a comma after the fraction, $N$ and $n$ in italics, no red KaTeX source, no clipping. Kaava, Sijoitus (aligned rows), Vastaus (boxed) and Järkevyys are intact. The next card and the exit ticket follow normally.
- Finnish in check-2: "Tilanyhtälöstä pV = nRT seuraa keskimääräiselle paineelle p ∝ NT/V, koska hiukkasmäärä N on verrannollinen ainemäärään n" is fluent and uses the glossary terms (tilanyhtälö, ainemäärä, hiukkasmäärä). The hint-2 wording "Paine on verrannollinen…" agrees with it.
- Opened stage-tutki-390-5 and -6: the laske-r card (task, answer field, closed hint and solution rows) and the johtopäätös card are intact at 390 px.
- Finnish in laske-r: the new clause "ja todelliset kaasut noudattavat niitä hyvin, kun kaasu on harvaa" is grammatical, and it fixes the earlier "harvat todelliset kaasut" ambiguity.
- Other figures and captures were not re-opened: the diff does not touch them, and the hash differs from the earlier PASS only through these two solutions.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
