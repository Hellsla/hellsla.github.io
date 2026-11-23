VERDICT: PASS
CONTENT-HASH: e15d7cb149da0d0d
none

## Blocking
None.

## Polish
- fy5-s1 e) Kaava: the chain ends with `v = 2πr/T` after `tan θ = v²/(rg)`. Per the "simplify to the end" rule, substitute v and give `tan θ = 4π²r/(gT²)` before the numbers. The Sijoitus then computes v separately and does not use the last symbolic form.
- fy5-s1 b) Sijoitus: the moment terms are computed first and m is then found from a numeric sum. The rubric accepts this, but substituting once into `m = (M_max + m_v g r_v − m_p g r_p)/(g r_max)` would match the rule.
- fy5-s3 d): the task says "lisämassa c-kohdan kuvaajasta" (14 g from the intercept). The model solution uses `m_eff = m + m_j/3`, and a student cannot know the 1/3 from the task. The "Hyväksytään myös" line covers the 14 g route, but the transfer criterion should name the intercept route first.
- fy5-s4 d) Kaava starts from `I ∝ 1/r²`. It would be more basic as `I = P/(4πr²)` (the Periaate has it) and `L = 10 dB · lg(I/I0)`.
- fy5-s4 a) and s2 a) (Kuvaaja step): the basic equations are in the prose and the Kaava line is short. This is fine.

## Checked
- The rewritten Kaava steps in all four tasks. s1 a), b) and e), s2 b) and c), s3 b) and d) and s4 b) and c) start from the basic law (M=Fr and F=mg; F=γMm/r²=mv²/r; T=2π√(m/k); E_k=E_p; L=λ/2 and v=fλ). They simplify symbolically (g, m and the moon's mass cancel) before the Sijoitus.
- Sijoitus, answers and rubric points are consistent with answers.py (21 m, 2580 kg, 0,60°, 1,9e27 kg, 160 000 km, 19,9 N/m, 0,43 m/s, 250 Hz, 0,686 m, 5,2 Hz, 1,0 h).
- Independent application: each task has an unfamiliar authentic setting (crane, Jupiter data, spring measurements, organ pipe). Parts rise in demand, and no heading names the model.
- Rubrics are specific and fair. The criteria carry observable detail (both loading states in s1 c, the intercept explanation in s3 c). The common mistakes are real ones: pivot axis, loaded crane only, T² against m forced through the origin, peak spacing read as the period.
- Force diagram (s1 d): the task asks the student to draw it. The model figure is an FBD with the diagram before the equations, and the centrifugal force is named as the misconception.
- Variety: torque and equilibrium, gravitation graph, experiment analysis, wave and sound. Workload is about two hours in total and the course is 2 op. The links go to sensible chapters.
- docs/coverage/FY5.md is not in the packet, so I did not judge it.
