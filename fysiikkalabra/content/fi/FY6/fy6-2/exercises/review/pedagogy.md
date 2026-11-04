VERDICT: FAIL
CONTENT-HASH: ec2ed7b04e946880

## Blocking
- exercises.json L1-08 — near-duplicate of L2-01 (same small motor, same 10 A range, same ±(2,0 % + 3 numeroa), only the reading differs 0,02 / 0,35 A) and a fifth task of the form "ΔX = p·X + n·r" after L1-01, L1-02, L1-05 — replace it with a different level 1 skill, e.g. "Lukema on 1,53 V alueella 20 V (r = 0,01 V, ±(0,5 % + 2 numeroa)). Ilmoita mittaustulos muodossa U ± ΔU" (answer 0,03 V and the interval), or an MC on which range to start from when the size is unknown.
- solutions.md L3-04 Sijoitus b) — the algebra from the equation (U_0 − U) : R_1 = U : R_2 + U : R_m to U = U_0 : (1 + R_1 : R_2 + R_1 : R_m) is only stated ("josta"), then substituted — a student who cannot solve the task cannot follow it. Add the step: multiply by R_1, U_0 = U (1 + R_1 : R_2 + R_1 : R_m), divide.

## Polish
- exercises.json L2-05 — the table column "r (V)" is never named in the task — add "r on alueen resoluutio" to the text.
- exercises.json L2-07 — "Akun nimellisjännite on 12,60 V" is odd (a car battery is nominally 12 V; 12,6 V is a full charge) and a car battery is also used in L1-01 — "Täyteen ladatun akun jännite on noin 12,60 V" or switch to a power supply set to 12,60 V.
- exercises.json L3-04 — needs I = U : R for the meter and resistors and the sum-of-currents hint; fair, but add "Virta saadaan Ohmin laista I = U : R" ... or "R = U : I" wording as in the fy6-2 lesson, so the prerequisite is stated.
- exercises.json L2-06 — "johto siirretään sen liittimeen" assumes the student knows the mA jack differs from the 10 A jack; the lesson names only COM — add "(mittarissa on erillinen liitin suurille virroille)" to the correct choice's feedback.
- solutions.md L3-05 Järkevyys — "1,9 %" is 1,95 % (2,29 : 117,71); write "noin 2 %".

## Checked
- Counts 8/7/5 and kinds match docs/exercise-bank/FY6.md (MC meter connection, meter effect, range choice, wrong connection, repeated measurement, loading by the voltmeter, error report).
- Recomputed: L1-08 0,0304 A; L2-05 11,235 / 29,25 / 209 mV; L2-07 12,49 V, 0,03 V, 0,08245 V; L3-04 5,714 V, 4,76 %, 5,9×; L3-05 117,71 Ω, 0,94 %, 1,5 %, 2,90 Ω. All match the answer fields.
- L1-06, L1-07, L2-06: one correct option, each distractor a real misconception with repairing feedback.
- L2-07 d) logic (difference 0,11 V > limit 0,08 V; repetition does not reduce the meter's limit) is correct and well argued.
- L3-05 gives a convincing authentic report error (a difference from nominal is not a defect) with rounding by the error limit.
- Finnish and number+unit case correct (10 A:n, 12,0 V:n style) in the new tasks.
- L3-04 capture at 1280 px readable, no clipping; no 360 px exercise captures listed.
