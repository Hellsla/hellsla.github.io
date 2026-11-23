VERDICT: PASS
CONTENT-HASH: 3387a78416b285c4
SCOPE: full: unit.md (three new pysahdy boxes first), inquiry.json, teacher.md, the Sovella task set s1-s8 with solutions and answers.py

## Blocking
- (none)

## Polish
- inquiry.json `tehtavat` says "Kuusi ylioppilaskokeen tyylistä tehtävää" and lists six kinds, and teacher.md uses tasks 1-6. The task set has eight (s7 friction and s8 coil were added). It is a count mismatch, not physics, but the page should say eight.
- Third pysahdy box (slope vs one point): the answer gives only the random-error reason. The next paragraph and check-3 also name the other reason: a constant offset shifts the line and leaves the slope unchanged. A short second clause would match check-3's model answer. The box is right as it stands (C).
- s8 c Periaate still reads "Virheen, joka on vakio ja ei riipu virrasta, kutsutaan systemaattiseksi", which sounds like a definition of systematic error that is too narrow (repeated from round 2).

## Checked
- Pysahdy 1 (one variable at a time): the reason is the causal one, and it matches the paragraph above, Yleisiä virheitä and ennusta-muuttujat. Pysahdy 2 (resolution 0,01 s vs hand timing): it answers no, because reaction time makes the uncertainty tenths of a second. This matches the paragraph, ennusta-resoluutio and mittausmatka (0,2 s). Pysahdy 3 matches the text and check-3 criterion 1. None of the three boxes gives away a later answer in a misleading way, and none makes a wrong claim. The check-3 model change only splits a paragraph, with the same words.
- I recomputed everything in one script. Inquiry: spring table k = F/x 16,4/20,0/21,3/28,6/22,7, mean 21,8; with the 1,0 cm subtracted and 8,85 cm assumed, every k is 24,7-25,2. Also: 2,29 % (mistakes 4,58 / 0,13 / 0,0229), 24,67 N/m, -275,1 °C (mistakes -295,1 / -355,1), 14 m, Δρ 0,238 (0,08 / 0,48), the instrument percentages 2/100/5/10 % and the zero-offset thermometer (ΔT unchanged). Every correct option is the only correct one, and every distractor's feedback is right.
- Task set: s2 160 s and 0,125 K/s; s3 9,695, 10,67, 8,923, Δg 0,872, 13 %; s4 T² row, LSQ k 4,020, b 0,103 (line passes 0,907 and 4,123: the reads 0,91/4,12 are fair), g 9,84, d 4,98 cm, row g 8,87-9,60, 10,1/9,6; s5 2677, 2757/2601, 78, 0,05 %/2,9 %; s6 v² row, 0,12 → 4,17 m/s² (origin LSQ 4,15), μ₀ ≥ 0,425, 10,25 %, 3,78, 0,39; s7 and s8 as in round 2. answers.py and tasks.json agree, the tolerances accept the rounded answers, and `practice.py check` OK gives 110 points in every language.
- Physics models and conditions: small-angle pendulum, μ₀ = tan α₀, the lower bound on static friction while braking, losses making c too large, the long-coil centre condition, and extrapolation flagged. The scope is FY1-FY7, which is right for FY9.
- Hash is 3387a78416b285c4 at start and end.
