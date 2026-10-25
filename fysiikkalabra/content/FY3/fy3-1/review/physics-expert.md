VERDICT: FAIL
CONTENT-HASH: fc5375c46d696bd5

Reviewer: physics-expert, round 2 (fresh review of the revised lesson). Hash checked at start and at end: fc5375c46d696bd5 both times (unchanged).

## Findings

1. sim.js:65 — The weight arrow does NOT scale with G. Its length is `20 + 50 * G / G_FULL`, i.e. a constant 20 px offset plus a small proportional part, so the drawn arrow is barely different for very different weights: at 10 kg the Moon arrow is 20.3 px and the Earth arrow 22.0 px (ratio 1.08, true weight ratio 6.06); on Earth 1 kg gives 20.2 px and 100 kg gives 39.8 px (ratio 1.97, true ratio 100). sim-spec.md says the arrow length is "suoraan verrannollinen painoon G = m g", and the lesson's whole message is the ratio of weights (Moon about 1/6 of Earth). The arrow in the picture contradicts this (the stretch at line 42 and the bars at lines 46/74 are correct; the arrow is the only quantity that is not proportional to G). The comment at sim.js:7-8 only mentions a "minimum arrow length", not an offset of 20 px. Fix: make the arrow proportional, e.g. `aLen = Math.max(8, 160 * G / G_FULL)` (or any pure k*G with a small floor only for the tiniest weights), and say in the comment and sim-spec that only a floor of a few pixels is applied; or drop the arrow offset and scale the arrow the same way as the bars. Re-check that the arrow still fits inside the 400 px canvas at 100 kg on Jupiter.
   (Non-blocking, same area: at 100 kg on Earth the spring stretches only 75 px of 190 and at 10 kg on Earth 7.5 px, 1 kg on the Moon 0.12 px. That is correct physics for one fixed scale and is acknowledged in the spec, so it is not a FAIL, but the stretch for small masses is almost invisible.)

2. lesson.md:52 — Minor wording, no change required: "Kylpyhuonevaaka ... mittaa voimaa" is correct (it measures the support force, equal to the weight when at rest), and the claim that its scale is made on Earth by dividing the force by 9,81 N/kg is correct. The "silti" sentence could also state the consequence ("Kuussa se näyttäisi noin kuudesosan"), which would tie it to L3-03. Optional.

3. lesson.md:14 — Minor, no change required: "Massa ... kertoo, kuinka paljon ainetta kappaleessa on" is the usual school-level description and is acceptable for FY3 (inertia belongs to FY4).

No other problems found.

## Checks, item by item

(1) lesson.md statements and scope. All correct and inside FY3 scope. Weight is presented as the strength of the Earth-body interaction (lesson.md:14), never as the cause of acceleration (MAOL guide, FY3: "paino ... Maan ja punnuksen välisen vuorovaikutuksen voimakkuuden mittana eikä putoavan kappaleen kiihtyvyyden aiheuttajana"). Force is used as a magnitude; the arrows are only illustrative (allowed by the guide). No Newton's laws, no vectors, no equation of motion.
- G = m g with g in N/kg (lesson.md:19-21): correct. 1 N/kg = 1 m/s² is true (N = kg·m/s²); the paragraph only states the numerical/unit identity with the FY1 free-fall acceleration and does not claim that weight causes the acceleration. Fine.
- g table: Moon 1,62, Mars 3,71, Earth 9,81, Jupiter 24,8 N/kg. All standard (Jupiter 24,79 at the 1 bar cloud-top level). The note that Jupiter's value refers to the cloud tops is correct and necessary.
- Spring proportionality, graph through the origin, example 5,0 N : 2,0 cm -> 10 N : 4,0 cm and 2,5 N : 1,0 cm (lesson.md:10): correct, with the caveat "kun jousta ei venytetä liikaa" present.
- Calibration (lesson.md:12) with known weights: correct.
- Doubling argument (lesson.md:17): two identical bodies stretch the spring twice as much, so weight is proportional to mass: correct (mass is additive, spring in the linear range).
- "noin 1 N on sadan gramman omenan paino": 0,1 kg · 9,81 = 0,98 N, correct. "Kuudesosa": 1,62/9,81 = 0,165, correct.
- Bathroom scale: see finding 2, correct.
- Worked example: 120 kg · 9,81 = 1177,2 N (1180 N, 1,18 kN, correct); 120 kg · 3,71 = 445,2 N (445 N, correct).
- Misconception paragraph: 70 kg · 9,81 = 686,7 N, "noin 690 N" correct.
- SVG: spring hung from a support, block m, downward arrow labelled G = m g: correct.

(2) Units and magnitudes: all consistent (N, kg, N/kg, cm). Magnitudes plausible (spring constant in L2-04 about 131 N/m, egg 0,59 N, astronaut 1422 N on Earth).

(3) Independent recomputation of exercises.json answers from the problem text alone (python3 -I, g = 9,81 unless stated, Moon 1,62 from the lesson table for L1-03):

```
id            computed   answer   rel err   within tolerance (0.02)
fy3-1-L1-01   39.24      39       0.0061    OK
fy3-1-L1-02   8.1        8.1      0.0000    OK
fy3-1-L1-03   48.6       49       0.0082    OK
fy3-1-L1-04   1.5        1.5      0.0000    OK
fy3-1-L1-05   62.0       62       0.0000    OK
fy3-1-L2-01   4.9949     5.0      0.0010    OK
fy3-1-L2-02   0.5886     0.59     0.0024    OK
fy3-1-L2-03   1187.55    1190     0.0021    OK
fy3-1-L2-04   5.886      5.9      0.0024    OK
fy3-1-L3-01   6.80734    6.8      0.0011    OK
fy3-1-L3-02   133.2222   133      0.0017    OK
fy3-1-L3-03   0.99083    0.99     0.0008    OK
```
All 12 answers are correct and within the relative tolerance, also for a student who rounds sensibly. The lifting assumption in L3-02 is stated in the task itself (force equal to the weight of 22,0 kg), so the problem is well posed. L3-03 is well posed (the scale is defined in the text) and tests the mass/weight distinction. Exit ticket: 3,0 kg -> 29,43 N (29 N) on Earth, 4,86 N (4,9 N) on the Moon, ratio about 1/6; 15 N / 5,0 N · 2,0 cm = 6,0 cm; 70 kg -> 686,7 N (about 690 N). All correct.

(4) solutions.md: read after the recomputation. All substitutions, units and answers agree with my values. Sanity checks are valid (L2-03: 1 - 1,62/9,81 = 83,5 % "noin 83 %"; L1-05: 24,8/9,81 = 2,53 "noin 2,5-kertainen"; L1-03: 294 N on Earth). The L3-01 reasoning (mass unchanged, G_Mars = m g_Mars, or ratio 3,71/9,81) and L3-03 (the scale reads force / 9,81 N/kg) are correct and consistent with FY3 scope. No wrong reasoning found.

(5) sim.js:
- BODIES g values 1,62 / 3,71 / 9,81 / 24,8 N/kg: correct. G = m * g (line 41): correct. simState = {m, body, g, G, stretch, bars}.
- stretch = 190 * G / G_FULL (line 42), G_FULL = 100 * 24,8 = 2480 N: pure proportional to G, so it changes with both mass and body (e.g. 100 kg: Moon 12,4 px, Mars 28,4, Earth 75,2, Jupiter 190 px; Earth 1/10/100 kg: 0,75/7,5/75,2 px). The drawn spring adds a fixed rest length (REST = 40) with a dashed marker for the unloaded end, which is a correct way to draw a stretch.
- bars (line 46 and drawn heights at line 74): proportional to m g / G_FULL, with a 2 px minimum only in the drawing (disclosed in the spec); the values printed above the bars are exact (m * gg). Correct for the bar chart.
- Readout text (line 44-45): m, g in N/kg, G in N with decimal comma; correct.
- Weight arrow (line 65): NOT proportional, see finding 1.

## Verdict reasoning
Lesson text, exercises, exit ticket and solutions have no physics, number, unit or scope errors. The single blocking issue is the simulation's weight arrow, which is not proportional to G (offset of 20 px) and so shows Moon and Earth weights as nearly equal, contradicting the sim spec and the lesson's message. The fix is a one-line change in sim.js.
