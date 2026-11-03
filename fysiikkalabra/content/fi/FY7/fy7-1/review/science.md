VERDICT: PASS
CONTENT-HASH: bd1fbbb2ff520dfa

## Blocking

## Polish
- lessons/FY7/fy7-1/lesson-answers.py:41 — the θ comment still says 22,9° and 6,2° at 16 and 24 cm, but the model gives 22,8° and 6,6°. No student-facing number is affected. — Fix: "22,8°; 11,6°; 6,6°", or "printed by the script" as on line 40.

## Checked
- Round-2 polish applied. Both experiment tables are labelled "B_m (µT)", which matches the Bm key and the B_m ratio question. The table and the text now say "noin 45 T", matching the NHMFL hybrid magnet. lesson-answers.py computes the exit ticket's 5000 µT and 96.
- My own two-pole model (poles ±4 cm, 30,0 µT at 10 cm) agrees with lesson-answers.py on every key. exp-1: B_m is 30,0/15,5/9,15/5,88/2,87/1,62 µT and θ is 65,0/47,9/33,2/22,8/11,6/6,6°. The ratio is 10,45; the readout gives 10,34, inside the 4 % tolerance of 10,4.
- exp-2 (Earth off, r = 14 cm): θ is 90° on both axis sides and −90° beside the middle, with 13,3° and 166,7° at 45° and 135°. The flipped magnet gives −65,0°. pred-2: west is correct.
- Kaava: B_h 14,3 µT and B_v 50,0 µT. The figure gives 24,4 µT at 55,0°. Worked example: 17,9 µT, with a total of 22,7 µT by both routes, and the reasonableness check is a real one.
- virhe: 22,8 µT at 52,1°. siirto: 37,6°. Its mistakes (55,0°, 59,0° and 52,4°) match their feedback. kertaus: 50 N.
- Exit ticket: 5 mT = 5000 µT, and 5000 : 52 ≈ 96, about a hundred times. The model answers and the field-line answer agree with the theory.
- Every choice item has exactly one correct option, and each distractor's feedback is physically right. check-2 rightly says the kind of like poles cannot be told without arrows.
- Definitions and models: field direction comes from the compass N end, field lines are closed loops, and there is no monopole. Domains and the 770 °C Curie point are correct. Earth's magnetic S pole lies near the geographic north; the declination and inclination ranges match WMM2025.
- Scope: no para- or diamagnetism (other materials are only "very weak"), and the tesla is deferred to the charged-particle chapter.
- sim.js is unchanged since the round-2 full review, and the hash is the same at the start and the end.
