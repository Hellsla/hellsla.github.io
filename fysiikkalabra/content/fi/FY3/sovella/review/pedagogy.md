VERDICT: PASS
CONTENT-HASH: 2bcc336fe1b09523

## Blocking
None.

## Polish
- fy3-s3 b) Kaava still opens with the combined `p_1 V_1 = p_2 V_2`. House rule: start from `pV = nRT` with n and T constant, as a) and now c) do. Add that row.
- fy3-s3 c) Annettu: the Kaava uses `p_1`, `p_2` (tank states) and `Δp_s`, but Annettu names only `V_s`, the gauge readings and `p = 248 kPa`. Name the two tank pressures there, and say in Periaate that Δn is the air used.
- fy3-s3 c) Annettu writes `q = 20\,\text{l/min}`, and the other litres are `\textsf{l}`. Write `20\,\textsf{l}/\text{min}` in Annettu, Sijoitus and the task text, so the litre is spelled one way.
- fy3-s1 c) Kaava: `P_a = P` sits between definitions as a loose row. Move it before the `η` row, or say in words that the useful power is b)'s power.

## Checked
- Round 2 change, s3 c Kaava: it now starts from the tank's two states, `p_1 V_s = n_1 RT` and `p_2 V_s = n_2 RT`. These give `Δp_s V_s = Δn RT`, which is equated with the breathed air `pV = Δn RT`. It solves to `V`, then `t = V/q`, all symbolic before the Sijoitus. The step follows from one amount of substance and one temperature, as the task's assumption says. This closes the earlier Polish about the unexplained n.
- The c) Periaate says why overpressures can be subtracted, and the rubric's concept criterion on this matches the Kaava. The numbers are 15 000 kPa · 12,0 l / 248 kPa = 725 l and 36 min, which agree with answers.py.
- Litre written `\textsf{l}` in the task texts, the answer unit and the solutions, apart from the `l/min` spot above.
- Tasks, rubrics and common mistakes are unchanged since the last pass. Each task still demands independent application: no heading names a model, parts rise in demand, and the three tasks differ (graph and data, table and interpolation, qualitative to quantitative). The workload fits a 2 op course.
- The common mistakes are real: gauge pressure used as absolute, Celsius in the gas law, body temperature forgotten, the surface pressure used for the tank.
- s1 graph figure: the description gives the readings without hiding the method, and the tangent and chord are labelled with text as well as colour.
