VERDICT: FAIL
CONTENT-HASH: 6efd6dde9d89f690

## Blocking
- lesson.md:231 (Kaava, "Miksi pienin sopiva alue") — **B**: "Prosenttiosa $p \cdot x$ on sama kaikilla saman suureen alueilla" and "numeroiden osuus pienenee kymmenesosaan" hold only for ranges that have the same $p$ and $n$ and lie a decade apart. The table just above contradicts this for current (200 mA: 1,0 % + 2; 10 A: 2,0 % + 3; the ranges are 50× apart). Fix: state the condition, e.g. "Jännitealueilla $2\,\text{V}$ ja $20\,\text{V}$ prosenttiosa on sama …" or "kun alueiden $p$ ja $n$ ovat samat" (the Esimerkki's Järkevyys already says this).

## Polish
- inquiry.json (virhe, correct option and last distractor's feedback) — "$\Delta U = 0{,}050\,\text{V}$" has two figures; the rule now taught gives $0{,}05\,\text{V}$.
- lesson.md:313 and the error-bands figure — 0,0095 → 0,01 → 0,010 V applies "first digit 1" to the already rounded value. The value is defensible because it matches the decimals of 1,500 V, but add one clause as in exercise L1-05 so the step is visible.
- inquiry.json (koe-1 intro) — "mitä mittarille tapahtuu?" for the ammeter across the lamp: the model shows 136,4 mA and no fuse blows (carried over).

## Checked
- One script recomputed everything: example 0,0275 → 0,03 V and 0,0095 → 0,010 V, relative 2 % / 0,67 %, ratio ≈ 1/3; 4,50 ± 0,04 V; virhe 0,05 V; siirto 152 % → 150 %, mistakes 2 % and 17 %, check 2,1 %; tarkistus-2 6,23 → 6 mV, mistakes 4,23 / 24,23; exit 0,035 → 0,04 V. All match lesson-answers.py.
- The rounded answers 6 mV and 150 % are inside the relative tolerances.
- Sim recomputed: 97,83 mA, 0,09998 A, U_L 1,500 V, series voltmeter 4,49998 V / 0,45 µA, ammeter across the lamp 136,4 mA (lamp 1,24 mW, dark), across the resistor 272,7 mA (fuse). sim.js solve/fuse/OL implement this.
- The error-bands figure is to scale (6000 px/V).
- The rounding rule is stated in the Tulos and applied in tarkistus-2, siirto and the exit ticket.
- The manufacturer's error limit is kept apart from the total uncertainty.
- koe-1/2/3 isolate the varied parameter, and the simState keys give the quoted values.
- Every choice item has exactly one correct option, and each distractor's feedback is correct.
- The circuit figures agree with the model.
- Content hash unchanged start/end.
