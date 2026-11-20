VERDICT: PASS
CONTENT-HASH: f304f5ac9f6ebee7

## Blocking

## Polish
- lesson.md:177 (figure water-column, teacher-approved) — the label "bottom pressure $p = G/A = \rho g h$" leaves out the $p_0$ that the open container has. The text calls this the hydrostatic pressure, and the Common misconception section warns against leaving $p_0$ out. Fix: label it "pressure caused by the water" or $\Delta p$. This needs the teacher's approval of the figure again, so it is not blocking.
- inquiry.json exp-1 solution — the answer is rounded to two figures "because the depth difference $5.0\,\text{m}$ is known to two figures". But the slider positions are exact model settings, so the readout precision limits the answer, not the depth. The result ($9.8$ against the model's $9.81\,\text{kPa/m}$) is fine either way.
- lesson.md:193 — "about $290\,\text{kPa}$" at $30\,\text{m}$ (the model gives $294\,\text{kPa}$). Correct as an "about" value, but $295\,\text{kPa}$ / $295\,\text{kN}$ would agree better with three figures elsewhere.

## Checked
- One script recomputed every number: Pysähdy $300\,\text{kPa}$, the dam at $30\,\text{m}$, the worked example ($117\,720\,\text{Pa}$, $\approx 219\,\text{kPa}$, $1765.8\,\text{N} \approx 1.77\,\text{kN}$, $\approx 180\,\text{kg}$), the retrieval item ($29\,430\,\text{N}$, $306$), pred-1 and pred-2 ($150$/$199$, $49$/$98$, $122$/$223\,\text{kPa}$, $12\,\%$), the error-spotting item ($29\,\text{kPa}$), the transfer task ($0.757\,\text{m}$; mistakes $10.3$ and $0.000757$), check-2 ($891.9 \to 890$; mistakes $2180$ and $0.892$), check-3 ($29\,\text{kPa}$, $1.8\,\text{N}$), and the exit ticket. Everything matches.
- Simulation change (commit ccdfae583f): only the readout lines for slope and ratio were removed. The physics ($p_0 + \rho g h$, slope $\rho g$) is unchanged, and simState still holds h, rho, pOver and pTotal. In JS, toFixed gives 150.1 and 199.1 kPa at $5\,\text{m}$ and $10\,\text{m}$, which matches exp-1's solution and its mistake value of 19.9.
- exp-1 locks rho, varies h and starts at h = 5; exp-2 locks h = 10 and varies rho. Slider steps reach 720, 1000 and 1240. Each setup isolates its varied parameter.
- Predictions, error-spotting, check-1 and check-c2 each have exactly one correct option. Every distractor is wrong, and its feedback gives the right reason.
- The pressure-depth figure is to scale (0.9 px/kPa, 34.6 px/m, errors under 1 px). The pressure-area figure has $A_2 = 3A_1$ (40 px against 120 px).
- Model conditions are stated: liquid at rest, constant density, fixed $p_0$, values from a model. The causal chain is right: weight of the column, area cancels, isotropic pressure, gauge pressure on the dam and the window.
- Scope stays inside FY3 (pressure, hydrostatic pressure, linear graph). No buoyancy is used beyond the distractor.
- The formula name "hydrostatic pressure" is a teacher exception and is not judged.
