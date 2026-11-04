VERDICT: FAIL
CONTENT-HASH: ec2ed7b04e946880

## Blocking
- exercises.json:290 (L3-04 b) — A, scope: the task needs I = U : R and Ω/MΩ, which are not in the fy6-2 brief or in its prerequisite fy6-1. Ohm's law is a later chapter. The existing L3-01 avoids this with a burden in mV/mA, and L3-05 states R = U : I in its own text. The student cannot solve b) from what has been taught. Fix: add to the "Apuna" sentence "Vastuksen läpi kulkeva virta on $I = U : R$." Also replace the parallel-combination check at solutions.md:179 (resistors in parallel are not taught) with a back-substitution: $(12{,}0 - 5{,}714)\,\text{V} : 1{,}0\,\text{M}\Omega = 6{,}29\,\mu\text{A} = 5{,}714\,\mu\text{A} + 0{,}571\,\mu\text{A}$.
- exercises.json:223 and solutions.md:162 and the following lines (L2-07) — A, definition: a lead-acid car battery's nominal voltage (nimellisjännite) is 12 V. 12,6 V is the rest voltage of a fully charged battery. The conclusion "akku on todennäköisesti osittain purkautunut" is right only for that meaning. Fix: write "Täyteen ladatun akun lepojännite on $12{,}60\,\text{V}$" in the task, and "lepojännite" in d) and in the solution.

## Polish
- solutions.md:178 (L3-04): "oikea jännite 6,00 V jää sen ulkopuolelle" — the meter shows the loaded voltage 5,71 V correctly. Write "jännite ilman mittaria, $6{,}00\,\text{V}$, jää sen ulkopuolelle".
- exercises.json:193 (L2-06, correct option and solutions.md:156): add that the circuit is switched off or opened before the red lead is moved to the other jack, so that the safety statement is exact.
- L1-08 is the fourth plain Δx = p·x + n·r task at level 1 (with L1-01, L1-02 and L1-05), and it repeats the existing L2-01 scenario (small motor, 10 A range, ±(2,0 % + 3)). Its `kind: ["data"]` is also wrong, because it has no table. The plan's "suhteellinen virhe" part would make it different.
- L3-05 (plan: "ilman mittarin vaikutusta"): d) could add one sentence that the voltmeter's current (10 MΩ against 118 Ω) is negligible here, which ties it to L3-04.

## Checked
- All 16 numeric answers recomputed in one script with my own formulas; they agree with answers.py and exercises.json: L1-08 0,0304 A, L2-05 11,235 mV (20 V: 29,25 mV; 200 V: 209 mV), L2-07 0,08245 V, L3-04 4,76 %, L3-05 2,90 Ω.
- L2-07: mean 12,49 V and half range 0,03 V. The guardrail wording holds: half range is not the uncertainty of the mean, and repetition does not reduce the meter's error limit.
- L3-04: U = 12,0 V : 2,10 = 5,714 V and ΔU = 0,0486 V, so the change is 5,9 times the error limit. The 10 kΩ case gives 0,05 %.
- L3-05: R = 117,71 Ω, relative limits 0,94 % and 1,52 %, so 118 ± 3 Ω, which contains 120 Ω. The quotient rule is given in the task.
- The tolerances accept the rounded answers (0,03 A, 11 mV, 0,08 V, 4,8 %, 3 Ω), counting the one-digit step rule in lesson.js.
- MC L1-06, L1-07 and L2-06: exactly one correct option each, and the distractor feedback is right. OL as over-range matches the glossary.
