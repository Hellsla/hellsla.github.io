VERDICT: PASS
CONTENT-HASH: ee661fbb3a2d0ed1

## Blocking

## Polish
- inquiry.json:157, 228: the tables label the column "magneetin kenttä B (µT)", but B is the total field in the lesson and the readout (33,1 µT at 10 cm). The column holds B_m. A student who copies B gets a ratio of 2,3, not 10. Fix: label it "B_m (µT)".
- lesson.md:325/327: "yli 45 T", but the NHMFL hybrid magnet given as the example makes 45 T. Fix: "noin 45 T".
- lessons/FY7/fy7-1/lesson-answers.py:67: the comment still says "0,050 mT", but the exit ticket now asks 5000 µT : 52 µT ≈ 96, and no line computes it. Fix: add `5e-3 / 52e-6`.
- lessons/FY7/fy7-1/lesson-answers.py:40, 51: stale comments. The model gives 5,88 and 1,62 µT at 16 and 24 cm (comments: 5,93 and 1,53) and 13,3° at φ = 45° (comment: "145°(?)"). No student-facing number is affected.

## Checked
- My own pole model (±4 cm, 30,0 µT at 10 cm). exp-1: B_m 30,0/15,5/9,15/2,87 µT, θ 65,0/47,9/33,2/11,6°, ratio 10,45 (readout 10,3, inside the tolerance). exp-2: θ 90°/−90°/90°. pred-2: −90°.
- Worked example 17,9 µT; virhe 22,8 µT and 52,1°; siirto 37,6° (mistakes 55,0°/59,0°/52,4° match their feedback); B_h 14,3 and B_v 50,0 µT; exit ticket 96.
- To-scale figures: vector-sum 14 : 20 with the needle at 54,7° (55,0°) and the S pole facing the compass; inclination drawn at 74,05°.
- bar-field, domains, earth-field and hero: the compasses follow the field, and the iron end facing the N pole becomes S.
- Every prediction and check has exactly one correct option, with correct distractor feedback. In two-magnets, the like poles' kind cannot be told without arrows, as the feedback says.
- sim.js implements the stated model and its box gives the limits. The locked parameters isolate r and φ, and simState gives theta and Bm.
- Scope: domains, a Curie point of 770 °C, no monopole, no para- or diamagnetism.
- Earth: the magnetic S pole is near the geographic north, and the declination and inclination ranges match WMM2025. The round-1 polish items are applied.
