VERDICT: PASS
CONTENT-HASH: 9edd63389d0a681d

## Blocking

## Polish
- exercises.json:82 (fy3-1-L3-01) — Now that L3-03 is a Mars task, all three level-3 tasks come down to the same step, m · g₁ / g₂ (L3-01 18 · 3,71/9,81, L3-02 22,0 · 9,81/1,62, L3-03 26 · 9,81/3,71). L3-01 is the closest to L3-03, since both go from an Earth-based reading to Mars. None of the three uses the spring idea from lesson.md:8. — Change L3-01 so that it combines the proportional stretch with G = mg on another body: "Voimamittarin jousi venyy Maassa 4,0 cm, kun siihen ripustetaan 0,50 kg:n kappale. Marsissa (g = 3,71 m/s²) samaan jouseen ripustetaan toinen kappale, ja jousi venyy 6,0 cm. Mikä on kappaleen massa?" answers.py: 0,50 · 9,81 · 6,0/4,0 / 3,71 = 1,983, so the answer is 2,0 kg with tolerance 0,02.

## Checked
- The hash was 9edd63389d0a681d at the start and at the end. The lint reports 0 errors and 0 warnings.
- exercises.json:98 L3-03 now uses my wording. The lesson gives no Mars/Earth ratio, so the student has to combine the Earth calibration with Mars's g. That is real level-3 work. 26 · 9,81/3,71 = 68,75 → 69 kg, and 69 is 0,4 % off, which is inside the tolerance.
- lesson.md:22: the reworded Moon sentence (smaller body, weaker interaction) uses only ideas the lesson has already taught. It sets up the table without stating a ratio early.
- lesson.md:38: "≈ 0,17 ≈ 1/6" shows the step from the table value to the line 3 hook, so the student sees where "kuudesosa" comes from.
- lesson.md:50: the bathroom-scale paragraph prepares the student for L3-03 without giving its answer away.
- I re-ran answers.py and it matches all 12 answers. The exit-ticket values check out: 29 N → 4,9 N, 7,5 cm and 15 N.
- Levels are 5/4/3 and follow the rubric. L2-04 has two steps (weight, then proportion). No exercise repeats the 120 kg robot example.
- exit-ticket.json: q1 tests mass vs weight with the interaction reason, q2 tests proportional stretch, and q3 tests kg vs N. All three test core ideas, not details.
- Every meta.json glossary term, including voimamittari and putoamiskiihtyvyys, exists in glossary.json.
- Scope is FY3: there is no N/kg, no vectors and no force as a cause of motion. 1 N = 1 kg·m/s² is deferred to FY4 (lesson.md:29).
