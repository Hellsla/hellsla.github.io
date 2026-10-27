VERDICT: PASS
CONTENT-HASH: 672f7ee203dab054

## Blocking

## Polish
- lesson.md:310 and solutions.md:28: trailing zeros are counted differently. 120 kg is called three significant figures, while 30 kg is called two. Both readings can be defended. Fix: say once, e.g. in the Tulos stage, that 120 kg is taken as exact to 1 kg, or write the data unambiguously (1,20·10² kg).
- lesson.md:324 (scene figure): the aria-label says the stretches are drawn to scale. The drawn spring lengths are 144 px and 44 px, which is a 1 : 6 ratio of stretches only if the unloaded spring is 24 px long. The reader cannot see that rest length. Fix: show the rest position with a dashed mark, or drop "mittakaavassa".
- inquiry.json:373 (check-2, Järkevyys): "taulukon taivaankappaleista se ei ole mikään" is an observation, not a check. The palautuslasku in the same paragraph is the real check. Fix: keep the palautuslasku and add the magnitude argument, e.g. "close to the Earth value, a plausible g for a rocky planet".

## Checked
- One script recomputed answers.py, every exercise and the siirto, check-2, mistake values (19,44; 117,72; 7,41; 0,114; 44,9), the exit ticket, prediction feedback (98,1 / 294 / 248 N; ratio 2,53), calibration (3,5 N; distractor 8,96 ≈ 9,0 N) and the misconception (70 kg → 687 ≈ 690 N). All agree, and every rounded answer is within its 2 % tolerance.
- The worked example and all 12 solutions plus the two numeric solutions in inquiry.json have all seven parts. Each states a principle that fits: same mass with g changing, or stretch proportional to force under no overstretching. Each solves for the unknown in symbols first.
- Conversions are correct: g → kg in L2-02 with a 1000× sanity check, and cm cancelling in the ratios. N/kg = m/s² and N/(m/s²) = kg are argued from 1 N = 1 kg·m/s². That identity is flagged as FY4.
- Rounding: each answer has the significant figures of its least precise datum, and the reason is stated (2 sf for 4,0 kg, 49 N, 18 N and 26 kg; 3 sf for 145 kg and 22,0 kg).
- Reasonableness checks are real: ≈10 N/kg estimates, g ratios (1/6; 0,38; 2,5) and back-substitution.
- L3-03 is reasoned correctly: the reading times 9,81 gives the force, and dividing by g_Mars gives 68,75 kg.
- Scope: force appears only as a measure of interaction and G = mg. There are no Newton's laws or vectors; the arrow shows only the direction.
- Figures: force-extension (0,40 cm/N through the origin) and weight-mass (all four slopes to scale, Jupiter clipped at 1101 N) match their values. The forcemeter figure has 50/100 px stretches, i.e. 2×.
- sim.js: G = m·g, stretch and arrow are purely proportional to G on a fixed 2480 N scale, and the ruler uses the same scale. Each bar chart's scale is printed. The model note says the values are computed.
- Experiments: exp-1 locks body and varies m; exp-2 locks m and varies body. simState exposes m, g and G. All correct options and feedback physics are right.
