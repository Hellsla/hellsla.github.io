VERDICT: FAIL
CONTENT-HASH: 4e8678dce2802a4d

## Blocking
- inquiry.json:392 (virhe, last option's feedback) — **B**: "Hyvän mittarin virheraja on alueella 20 V alle prosentti lukemasta" is stated as general, but it holds only when the reading is a large part of the range; it contradicts the lesson's own point (lesson.md "Miksi pienin sopiva alue", siirto: 152 %). — Tie it to this reading: "Tällä lukemalla virheraja on alle prosentti lukemasta (0,050 V : 6,00 V ≈ 0,8 %)."

## Polish
- inquiry.json:260 (koe-3) — intro asks the student to move the meter across the resistor, but `kytkenta` is in `locked` (screenshot shows it "vakio"), so the OL observation the exit ticket builds on cannot be made — unlock `kytkenta` or drop the sentence.
- lesson.md:162 — "lamppu sammuu, ja … sulake palaa": add that once the fuse has blown the meter is out of the circuit and the lamp lights again (the sim does exactly this), so no student infers a lasting dark lamp.
- lesson.md:317 — "Pienempi alue ei voi olla epätarkempi" holds because both ranges have the same p; say "kun alueiden prosenttiosa on sama".
- inquiry.json:420 (siirto, Järkevyys) — 18,6 mA is a value assumed for illustration, not derivable from 0,02 A; write "esimerkiksi".
- lesson.md:313 — 1,50 V ± 0,028 V gives the limit one digit finer than the reading; acceptable, but ± 0,03 V would match the display.

## Checked
- All numbers recomputed in one script: worked example 0,0275/0,0095 V, 1,83 %/0,633 %, ratio 2,9; virhe 0,050 V; siirto 152 % and mistakes 2 %/17 %; tarkistus-2 6,23 mV and mistakes 4,23/24,23; exit ticket 0,035 V.
- Sim model: 97,8 mA (200 mA), 0,10 A (10 A), 1,500 V lamp, 3,00 V resistor (OL on 2 V), 4,50 V voltmeter in series (0,45 µA), ammeter across lamp 136 mA, lamp 1,2 mW < 4 mW (dark), across resistor 273 mA and across battery 4,5 A blow the fuse.
- Experiments koe-1/koe-2: initial values, locks and simState keys ImA/UV/lamppu give the quoted readings.
- ennuste-1/2, kertaus, tarkistus-1: exactly one correct option; distractor feedback correct.
- error-bands figure to scale (6000 px/V): ±165 px = 0,0275 V, ±57 px = 0,0095 V.
- Circuit figures: ammeter in series, voltmeter in parallel, conventional current + → −; wrong-connection figure consistent with the model.
- Manufacturer's error limit defined per guardrail terms; total uncertainty caveat present.
- tarkistus-3 model answer: ~2 % current drop matches the sim (2,2 %).
- Scope: within FY6 "jännite ja sähkövirta" and measurement; resistance only named forward to Ohm's law chapter.
- Content hash unchanged start/end.
