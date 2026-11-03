VERDICT: PASS
CONTENT-HASH: 5cbf5e3e3414f7c9

## Blocking

## Polish
- inquiry.json (koe-1 intro) — asks "mitä mittarille tapahtuu?" for the ammeter across the lamp, but with the 30 Ω resistor in the loop the model gives 136 mA on 200 mA, so the fuse does not blow; a student may look for a fuse event that never comes — add to the johtopäätös model answer that the meter then showed about 136 mA (model value) while the lamp was dark.
- lesson.md "Esimerkki", Tulos — 1,50 V ± 0,028 V gives the limit one digit finer than the reading; acceptable, ± 0,03 V would match the display (unchanged from round 1, not blocking).

## Checked
- Round 1 Blocking fixed: virhe last option's feedback now tied to this reading (0,050 V : 6,00 V ≈ 0,8 %). Round 1 polish done: koe-3 kytkentä unlocked, fuse relight sentence in lesson, "kun alueiden prosenttiosa on sama", siirto "esimerkiksi 18,6 mA".
- One script recomputed everything from the data: example 0,0275/0,0095 V, 1,83 %/0,633 %, ratio 2,89; virhe 0,050 V; siirto 152 %, mistakes 2 %/17 %, 200 mA check 2,1 %; tarkistus-2 6,23 mV, mistakes 4,23/24,23; exit 0,035 V; all equal lesson-answers.py.
- Sim model: 97,83 mA (200 mA), 0,09998 A (10 A), UL 1,500 V, UR 3,000 V (OL on 2 V), voltmeter in series 4,49998 V / 0,45 µA, ammeter across lamp 136 mA with lamp 1,2 mW < 4 mW (dark), across resistor 273 mA and across battery 4,5 A blow the fuse; after the fuse the meter is open and the lamp lit.
- koe-1/koe-2/koe-3: initial values, locks and simState keys ImA/UV/lamppu give the quoted readings; each isolates its varied parameter.
- ennuste-1/2, kertaus, virhe, tarkistus-1: exactly one correct option, distractor feedback correct.
- error-bands figure to scale (6000 px/V): ±165 px = 0,0275 V, ±57 px = 0,0095 V.
- Circuit figures: ammeter in series, voltmeter in parallel, conventional current + → −; wrong-connection figure consistent with the model.
- Manufacturer's error limit per guardrail terms, total-uncertainty caveat present; ideal battery and constant lamp resistance stated in the sim model box.
- tarkistus-3 model answer ~2 % drop matches the model (2,2 %).
- Content hash unchanged start/end.
