VERDICT: FAIL
CONTENT-HASH: 424b0972f9e99c5a

## Blocking
- exercises.json:46 fy1-8-L2-01 and solutions.md:51 — (A) The answer key is 2,5 % with tolerance 0,02. The solution says that, because Δt = 0,2 s has one figure, the result should be reported as "noin 3 %". A student who follows that advice and enters 3 is 20 % off and is marked wrong (CLAUDE.md: a student rounding to the data's figures stays inside the tolerance). Fix: either drop the "noin 3 %" advice and justify two figures, or widen the tolerance so that 3 % is accepted.
- exercises.json:80 fy1-8-L3-01 and solutions.md:91 — (A) The same problem. The key is 0,033 m/s at 2 % tolerance, but the solution says the stated uncertainty is rounded to one figure, "± 0,03 m/s". Entering 0,03 is rejected. Fix: ask for "puolet erotuksesta (laskettu arvo)" explicitly, or accept 0,03.

## Polish
- exercises.json:28 L1-04 — a table that is 24 cm long is implausible. Use a book or a sheet of paper, or 124 cm.
- exercises.json:90 L3-02 — "Kuumaa vettä jäähtyy kupissa" should be "Kuuma vesi jäähtyy kupissa". The solution's reasonableness check uses a reading error of 0,1 K that the task never gives; either say "lämpömittarin lukematarkkuus 0,1 °C" in the task or drop the number.
- solutions.md:61 L2-02 — "reaktioajan 0,20 s virhe" mixes error and uncertainty (guardrail terms). Write "ajanoton epävarmuus 0,20 s". The phrase "kaksi kertaa suurempi kuin 5 %, mihin pitkä mittaus ylettäisi" is unclear; "kaksinkertainen 5 %:n rajaan verrattuna" says it directly.
- solutions.md L3-03 — "4,0 toistoa, kaksi merkitsevää numeroa": a count is an exact integer, so "tasan 4 toistoa" is enough.

## Checked
- One-script recomputation: L1 5,0 % / 12,4 s / 0,4167 m/s / 0,2 cm / 3,17 %; L2 2,5 % / 10 % / 0,42 m/s / 16 %; L3 0,033 m/s / 1,4 K/min / 4,0. All match answers.py and exercises.json.
- Every solution has all seven parts and solves symbolically first (ε = Δt v / s, n = (t_kok − t_val)/(N t_toisto)).
- The L2-03 intercept check (0,06 m) and the L3-01 comparison of 0,50 m/s with the 0,397–0,463 m/s interval are real reasonableness checks, worded "todennäköisesti" per the guardrail.
- L3-02: the Δ°C = ΔK conversion is right; the cooling data are plausible (roughly Newtonian with a room at about 25 °C), and the slowing is explained causally.
- Half the range is used and named as a simple estimate of the scatter; systematic error is noted as not revealed by repeats (L1-04).
- Symbols (ε, Δt, t̄, s = vt) are the same as in the brief's lesson.
- Hash identical at start and end.
