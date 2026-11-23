VERDICT: PASS
CONTENT-HASH: 28edb98601f1d43b
SCOPE: full; the change since f5355edae2761e52 is three new ```pysahdy boxes in unit.md, the hero and "pallo" figures now WebP (teacher-approved, the same files as fi), and one inquiry solution split into paragraphs

## Blocking
None.

## Polish
- s8 common mistakes, part a (still open, as in fi): "$\mu = 16 / 20\,\text{cm} = 0.80\,\text{1/cm}$" belongs to the old reading point. With the points now used, (0; 80) and (10; 20), the quotient error is $4 / 10\,\text{cm} = 0.40\,\text{1/cm}$. No physics is wrong.
- Pysähdy 1: the answer only repeats the Key idea sentence and gives no reason (as in fi). "One photon to one electron" holds for absorption and the photoelectric effect. That is a type C simplification at this level, so no finding.

## Checked
- Pysähdy boxes, judged first against fi line by line. The physics is the same:
  - Box 1 (one photon to one electron) matches the Key idea and s3 d.
  - Box 2 (no electrons when $hf < W$) matches the formula text "only when $hf \geq W$".
  - Box 3: after $2T_{1/2}$, $(\tfrac12)^2 = \tfrac14$ is left. This matches the decay law, the "puolitus" figure and the mistakes list.
  - Each box has one correct answer and fits FY8 scope. Decimal points and LaTeX are as in fi.
- Diff:
  - The inquiry lead solution has the same words and numbers, only split into paragraphs; $d_{1/2} = 5.79\,\text{mm}$ recomputed.
  - The pallo WebP shows a point source, two sphere surfaces and one cone whose area grows with distance. The labels $r_1$, $r_2$, $\dot H_1$, $\dot H_2$ are unchanged, and the figure matches the inverse-square text. Both images are in teacher-figures.tsv and are the same files as in fi.
- One script (scratchpad rc.py) recomputed the unit's and the task set's numbers from the task data with my own formulas and found each in the en text:
  - intro: 1.88 eV
  - s1: 1.87 pm, 1050 Bq/kg, 0.068 mSv, 0.33 ng
  - s2: 656.5 nm, 7080 km/s, 101 Mpc, 497.6 nm
  - s3: h ≈ 6.61e-34, f0 5.43e14 Hz, 552 nm
  - s5: 151 s two-point
  - s6: 37 %, 1.34e20 1/s, 1650 kg, 1.51 kg, 58 600 kg/s
  - s7: 1.54, 9.4 kg, 1.05 %
  - s8: 0.14 1/cm, 6.6 µSv/h, 2.2 mSv, 23.6 → 24 cm rounded to the safe side
  - s9: 72 km/s/Mpc, 117 Mpc, 1.4e10 a
  - inquiry: 5.79 mm
  All agree. Rounding and models are unchanged from the passed version and from fi.
- practice.py check: OK for en (9 tasks, 136 points). The hash was 28edb98601f1d43b at the start and at the end.
