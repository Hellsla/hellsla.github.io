VERDICT: FAIL
CONTENT-HASH: c61d1449074a7c36

## Blocking
- exercises/solutions.md:35 (L1-04) — A: "pystysuoran ruudukkoviivan $x = 30\,\text{m}$" is wrong. In a (t,x) graph the line x = 30 m is horizontal. — Write "vaakasuoran ruudukkoviivan $x = 30\,\text{m}$".

## Polish
- L2-04 "Vastaus: 3,8 s eli 3,75 s": state which value is the answer (3,8 s) and that 3,75 s is the unrounded value.
- L3-01: the task could say "ensimmäisen kerran" is the smaller root. The solution says this already; the task is fine as it is.

## Checked
- One script recomputed every answer from the task text with its own meeting-root model. All 12 agree with answers.py and exercises.json (L3-01 4 − √6 = 1,5505 s; L3-03 roots 10 s and −18 s).
- Figure fy4-12/kaksi-karrya (A 0→60 m and B 40→20 m in 10 s) gives v_A = 6,0 m/s, v_B = −2,0 m/s, a meeting at 5,0 s and 30 m, and a 10 m gap at 3,75 s.
- Unit conversions are right: 90 and 72 km/h become 25 and 20 m/s, 18 km/h becomes 5,0 m/s, and 12 km / 144 km/h = 5,0 min.
- L3-01 says correctly that both positive roots are meetings. L3-03 rejects its negative root with a reason.
- Every solution is solved symbolically first. The rounding follows the data, and the reasonableness checks are real substitutions.
- Standing rules: \cdot is used and × never appears. All symbols are in LaTeX.
