VERDICT: PASS
CONTENT-HASH: f258a83e4f50ee9b

## Blocking
(none)

## Polish
- inquiry.json pred-2 — the correct option is the longest and already states "ΔU = W" before the theory section; a student can pick it by form. Shorten it to "Tehty työ: kaasu lämpenee enemmän sillä kerralla, jolla työtä tehdään enemmän." and leave ΔU = W to the feedback.
- inquiry.json koe-1 intro — "Vertaa ... ΔU ja työtä W sekä lämpötilan nousua ΔT" names the comparison for the student; consider "Mitä huomaat lukemista?" to let them find ΔU = W.
- inquiry.json pred-1 Aino feedback — "1,33-kertaiseksi" but the sim reads 1,34 · p₀; write "noin 1,3-kertaiseksi".
- inquiry.json koe-2 — the student waits for T ≈ 293 K; the sim ends at 294 K (ΔU +0,2 J). Say "noin 293–294 K" so nobody thinks the run failed.

## Checked
- Hash at start and end identical (above).
- Koe 1 at 390 px, 3 rounds of hidas/nopea with "Aseta alkutila": identical every time, hidas W = ΔU = +40,8 J, ΔT +114 K; nopea +47,2 J, +132 K. Matches the pred-2 feedback and the table.
- Wrong pred-2 ("Männän nopeus itse") committed first: feedback stays gated ("Palaute näkyy, kun olet tehnyt mittaukset"), then after 2+ measurements it cites 132/114 K and 47,2/40,8 J, gives 2,8 K/J for both, and repairs the misconception. Round-1 blocking issue is gone.
- Correct pred-2 option now says temperature follows work, speed acts only through W; no contradiction with the readout.
- Readout no longer shows "(Q + W = …)"; it shows W, Q, ΔU, T, V, p. Nothing clipped at 390 px; controls and bars legible.
- Koe 2: insulated 40,8 J / 407 K, conducting W +35,1 J, Q −34,9 J, ΔU +0,2 J, T 294 K; the question and its feedback agree with these numbers.
- Variable control: Koe 1 varies only push (wall locked), Koe 2 only wall (push locked); both can refute their predictions.
- Pred-1 options are now of similar length and each has misconception-repairing feedback.
- Haaste is gone; exercises 5/4/3, transfer task hints and check-2/check-3 are consistent with sign convention.
- Finnish reads well; no new errors found.
