VERDICT: FAIL
CONTENT-HASH: 14f290f6e62807dd

## Blocking
- content/fi/FY1/fy1-5/exercises/solutions.md:203–204, exercises.json:219 (fy1-5-L2-08) — **B, internal consistency.** The lesson says "Tässä luvussa kappale liikkuu yhteen suuntaan, joten nopeus on positiivinen" and never teaches negative velocity. The solution gives "−1,0 m/s, ja miinusmerkki kertoo…", and its Periaate and option A's feedback say "kulmakertoimen etumerkki kertoo suunnan". This contradicts the lesson. The task can be solved without the sign. — Fix: remove the −1,0 m/s sentence and the two "etumerkki" clauses, and keep "paikka pienenee → suora laskee". Otherwise state the condition explicitly, which would also mean changing the lesson sentence.

## Polish
- exercises.json:224 (option B) — pick-vt shows +1,0 m/s on the way back, which is the wrong sign under the solution's own convention. This is harmless once the sign is dropped.
- lessons/FY1/fy1-5/figures.py:124 (pick-distance) — The caption and axis say "paikka s", but feedback D (exercises.json:235) calls the graph a distance graph. Consider "kuvaaja esittää kuljettua matkaa, vaikka akselilla on s".

## Checked
- All 19 numeric answers were recomputed with my own formulas in one script and agree with answers.py. L2-05 least squares gives 18,04 m, L3-01 3419,8 vrk, L3-02 41,58 h.
- L2-08: arrival at 4,0 s + 6,0 m / 1,0 m/s = 10 s. Only C matches, and A, B and D are wrong for the reasons their feedback gives.
- L2-08 figure captions match the plotted points and do not give the answer away.
- L1-03 / line-read: (8 s; 20 m) gives 2,5 m/s, and 150 m gives 60 s.
- L3-04: slopes 3,0 and 1,0 m/s, average speed 40 m / 30 s.
- L3-05: the vertical-line reasoning and the scale (3,0 cm rise, 0,10 cm run) are correct.
- L2-07: 0,2 s / t ≤ 2 % gives t ≥ 10 s and s ≥ 8,0 m, and the hand-timing value follows the guardrail.
- The L2-05 fit wording and extrapolation caveat follow the guardrails.
- Voyager and constant values match the scope notes, and the notation matches the lesson.
