VERDICT: FAIL
CONTENT-HASH: 2c1c2a557074f30d

## Blocking
- inquiry.json:530 — (A) the siirto mistake value 1,65 does not match its own feedback: 5,2 V · 0,30 A = 1,56 W, so a student who multiplies the differences gets 1,56 and never sees this feedback — set `"value": 1.56`.
- inquiry.json:534 — (A) siirto "Vastaus": the rounding reason is wrong. Every datum used (18,0 V; 5,50 A; 12,8 V; 5,80 A) has three significant figures and the difference 99,0 W − 74,2 W is good to 0,1 W, so the result is 24,8 W. The nominal "12 V" does not enter the calculation — answer "$24{,}8\,\text{W}$, kymmenesosawatin tarkkuudella kuten tehot 99,0 W ja 74,2 W" (tolerance 0.02 already accepts it), or keep ≈ 25 W but give a correct reason.

## Polish
- lesson.md:269, 624 (and glossary *estosuunta*) — (B, mild) "koko lähteen jännite on diodin yli, virtaa ei kulje" holds only below the diode's reverse breakdown voltage. The sim's model box states this (an LED is often rated for only about 5 V in reverse), but the theory does not — add "kunhan jännite ei ylitä diodin suurinta estojännitettä".
- lesson.md:380 and inquiry.json:602 — the lamp is said to follow Ohm's law approximately and, in the same breath, to have a resistance that grows as it heats. The main reason it survives is that its filament has a sizeable resistance, so I = U : R (for a lamp rated for that battery); the rise with temperature only adds to this. Make the two places say the same.
- lesson.md:565 — the efficiency is computed with the maximum power. Say "maksimitehopisteessä" (with any other load, η is smaller).
- inquiry.json:121 — the example voltages in koe-1 (2, 3, 5, 7, 9 V) leave out 6,0 V, which ennuste-1 and its feedback compare (1,91 V and 12,4 mA). Add 6,0 V.
- assets/sims/fy6/fy6-14/sim.js (ledPicture) — the canvas literals `$\text{virta yli } 20\,\text{mA}$` and `$\text{estosuunta: ei virtaa}$` break the FY6 thread rule (word labels via `__('key')`). Not physics. Also, koe-2 reads U_D = −5,00 V while the model answer says "5,0 V": one clause on the sign would help.

## Checked
- I recomputed everything in one script with my own solver: koe-1 U_D 1,77/1,85/1,90/1,92/1,94 V, I 0,70→21,4 mA; ennuste-1 3,5→12,4 mA (×3,5), U_R ×3,5; koe-4 0,710/1,897/2,874 V.
- Panel: the true MPP is 4,96 V, 185 mA, 0,918 W, R 26,8 Ω (the text's 5,0 V / 184 mA / 27 Ω / 0,92 W is right). P(300 Ω) = 0,12 W; U_t(500) = 5,72 V; η = 15,3 %; FF 0,77 is realistic.
- Worked example (200 Ω, 0,080 W, power balance 0,12 W, 18 mA with 220 Ω), kertaus 200 Ω, Etsi virhe 350 Ω / 15,6 mA, tarkistus-3 2,5 A (the model gives 2,3 A), exit ticket 105 W: all correct.
- Every prediction and check has exactly one correct option. Each distractor's feedback is physically correct.
- sim.js implements the stated diode and panel models (the same constants as lesson-answers.py). simState gives UD, UR, I, Upv, Ipv, Ppv, Ik and Ut; each experiment locks every parameter except the one it varies.
- Figures: ominaiskayra, kenno, teho and etuvastus match the models and their captions.
- Current arrows are violet #7048e8. No electrons are drawn.
- Energy wording: "sisäenergiaksi" is used throughout; there is no "lämmöksi".
- Sim numbers are called model values (mallin arvot) everywhere, including the conclusion's model answer.
- No error limits appear. Scope: the materials physics stays qualitative, as the LOPS täsmennys requires.
