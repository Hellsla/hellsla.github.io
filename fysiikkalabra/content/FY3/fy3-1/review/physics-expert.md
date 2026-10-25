VERDICT: FAIL
CONTENT-HASH: 307c0dfc144588a5

Reviewer: physics-expert, fy3-1 re-review after g changed from N/kg to m/s².

## Findings

1. FAIL (unit/concept slip, lesson.md line 57, Tiivistelmä): "$g = 9{,}81\,\text{m/s}^2$: yhden kilogramman massan paino Maassa." As written g in m/s² is equated with a weight. That is a leftover of the old N/kg wording. The weight of 1 kg is 9,81 N, and g is the strength of gravity / free-fall acceleration. Suggested fix: "$g = 9{,}81\,\text{m/s}^2$ Maan pinnalla, joten 1 kg:n paino Maassa on 9,81 N."
2. OK, lesson.md line 21 (rewritten g paragraph): g = 9,81 m/s² is the same quantity as the FY1 free-fall acceleration. G = mg is in N with m in kg and g in m/s², and 1 N = 1 kg·m/s² is deferred to FY4. "Paino ... ei ole syy minkään liikkeen tai putoamisen alkamiseen" explicitly avoids the "weight causes motion" implication. Table values (Kuu 1,62, Mars 3,71, Maa 9,81, Jupiter 24,8 m/s², Jupiter at cloud-top level) are correct. Scope is fine: weight is a measure of the interaction, with no Newton's laws.
3. OK, other lesson.md statements: 1 N is about the weight of a 100 g apple (0,98 N). Moon weight ratio 1,62/9,81 = 0,165, about a sixth. The spring proportionality example is correct. Worked example: 120 kg gives 1177,2 N (1,18 kN) on Earth and 445,2 N on Mars. 70 kg gives 686,7 N (about 690 N). The bathroom scale remark (force divided by 9,81 m/s², about a sixth of the mass on the Moon) is correct.
4. OK, exercises.json: all 12 answers recomputed and within tolerance 0,02 (output below). Every text gives g in m/s² or points to the table. Units work out to newtons (or kg or cm as stated).
5. OK, solutions.md: reasoning and substitutions are correct, with units that cancel to N, kg or cm. Sanity checks hold (L1-05 ratio 2,53 is about 2,5; L2-03 reduction 83,5 % is about 83 %; L3-03 reading 0,991 kg). No N/kg left.
6. OK, exit-ticket.json: 3,0 kg gives 29 N on Earth and 4,9 N on the Moon (29,43 and 4,86). 20 N / 8,0 N · 3,0 cm = 7,5 cm. 70 kg gives about 690 N. No slips.
7. OK, sim.js and sim-spec.md: G = m·g with g = 1,62 / 3,71 / 9,81 / 24,8 m/s². Readout "g = … m/s²" and "G = m · g = … N". Stretch, arrow and bars are all proportional to G on the fixed scale G_FULL = 100·24,8 = 2480 N, with the display-only floors documented. No N/kg anywhere (grep over the lesson folder excluding review/ finds nothing).

## Python output (python3 -I)
```
L1-01 39.24 39 True
L1-02 6.0 6 True
L1-03 48.6 49 True
L1-04 1.5 1.5 True
L1-05 62.0 62 True
L2-01 4.9949 5 True
L2-02 0.5886 0.59 True
L2-03 1187.55 1190 True
L2-04 5.886 5.9 True
L3-01 6.8073 6.8 True
L3-02 133.2222 133 True
L3-03 0.9908 0.99 True
120 kg: 1177.2 N Earth, 445.2 N Mars; 70 kg: 686.7 N
```
Hash re-run at the end: 307c0dfc144588a5 (unchanged).
