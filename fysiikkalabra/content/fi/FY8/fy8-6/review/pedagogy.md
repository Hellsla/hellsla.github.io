VERDICT: FAIL
CONTENT-HASH: e6b0231aeaa552c8

## Blocking
- inquiry.json:392 (tarkistus-2 solution) — "Pystyruudun väli on 0,2·10^14 Hz ja vaakaruudun 0,1 V" has the axes swapped: frequency is on the horizontal axis, voltage on the vertical (capture #15). A student reading the grid by this sentence reads the wrong lines — fix: "Vaakaruudun väli on $0{,}2 \cdot 10^{14}\,\text{Hz}$ ja pystyruudun $0{,}1\,\text{V}$."

## Polish
- inquiry.json:16 (hook) — the hook already says "jännitteen nostaminen kirkastaa niiden valoa, mutta värit eivät muutu", which is exactly the answer to tarkistus-1 and the lesson's main misconception, before any prediction. Cut the sentence to "LEDit eivät syty yhtä aikaa" and leave brightness vs colour for the sim and tarkistus-1.
- inquiry.json:149 and :226 — koe-2 (fit by hand through 9 readings) and "aineisto" (Graphical Analysis Pro fit) both ask the student to fit a line, and the example, tarkistus-2 and exercise L3-01 do it again. Hour workload is heavy: consider making the "aineisto" GA Pro fit optional or dropping the paper graph in koe-2 to the table.
- lesson.md "Esimerkki" vs tarkistus-2 — both are "two points of a fitted line, h = e·k"; tarkistus-2 does not test a new skill. Give it a different slot (e.g. choose the correct slope unit/axis exponent, or read U_k intercept).
- inquiry.json:346 (tarkistus-1) — distractor "Mikään ei muutu" is weak; replace with "Virta pienenee, koska LED kuumenee".
- inquiry.json (ennuste-1) — distractor "kaikkien läpi yhtä suuri virta" is weak (the hook already shows LEDs lighting at different times); a stronger one is "kaikki syttyvät, mutta sininen himmeämmin".

## Checked
- Path Pohdinta → Ennusta → Tutki → teoria → Sovella → Tarkista follows house order; opening question answered (reflect, ydinajatus, tarkistus-3).
- Predictions 1 and 2 can be refuted by koe-1 and koe-2 (U locked in koe-1, λ locked in koe-2); wrong-option feedback repairs the misconception.
- Sim at 390 px (#2) and 1280 px (#44): readout, graph and boxes readable; experiment tables sit beside the sim.
- Figures: iu, sovitus and ryhma captures legible; tarkistus-2 figure description gives data without the answer.
- Worked example staged one step per stage; reaches h = 6,52e-34 Js consistent with fit data.
- Slot goals (threshold voltage and wavelength, h from slope, LED/laser/lamp spectra) covered, no more.
- Exit ticket tests U_k from λ and the wavelength-precision idea: fits core.
- Finnish and case endings (V:n, nm:n) correct; glossary terms used consistently.
- Hash unchanged at the end of the review: e6b0231aeaa552c8.
