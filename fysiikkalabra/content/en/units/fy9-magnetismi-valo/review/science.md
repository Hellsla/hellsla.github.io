VERDICT: PASS
CONTENT-HASH: a73bb95a8b0fdfba
SCOPE: full: the three new "Pysähdy ja mieti" boxes first, then the unit (unit.md, inquiry.json, exit ticket, teacher.md) and the Sovella task set s1–s9.

## Blocking
None.

## Polish
- Carried from round 1: the solution headings "Yleisiä virheitä" and "Hyväksytään myös" in solutions.md are presumably parser keys. They are no finding if the page shows them translated.
- s9 b still rounds its intermediate values ($0.41\,\text{W}$, $0.29\,\text{J}$, $0.082\,\text{J}$). The result $0.37\,\text{J}$ is right (unrounded $0.369$). The Finnish text has the same chain.

## Checked
- `units.py hash --lang en` gave a73bb95a8b0fdfba at the start and at the end. `practice.py check`: OK (9 tasks, 137 points in fi, en and fi-easy).
- **Pysähdy boxes**, compared line by line with the Finnish unit.md (lines 13, 127, 208). The physics is the same in each:
  1. Flux must change for an induced voltage; constant flux gives none. This is right, and it matches the Key idea, lt-2 and the Common mistakes.
  2. The magnetic force is perpendicular to the velocity, so it changes only the direction. This is right and fits the circle derivation that follows.
  3. Going from higher $n$ to lower $n$, the ray bends away from the normal. This is right ($n_1 > n_2$ gives $\alpha_2 > \alpha_1$), and it agrees with the paragraph above and the rajakulma figure.
- **Diff since the PASS (9b32e666f)**:
  - Three inline SVGs are now WebP images: hero, ympyra, rajakulma. I viewed them.
  - ympyra: B is into the page and the charge is positive. At the bottom v points right and F points up, to the centre; the motion is anticlockwise. This is consistent with $Q\overline{v}\times\overline{B}$ at all four points.
  - rajakulma: at the critical angle the refracted ray runs along the boundary and a weak ray is reflected. Above the critical angle there is total reflection at an equal angle, with the normals dashed.
  - inquiry.json and solutions.md: only paragraph splits. I compared them with whitespace normalised: tasks.json is identical and solutions.md identical apart from line breaks.
- **Recomputation script** (my own formulas from the task text; everything agrees):
  - s1: $565.5\,\text{V}$ / $399.9\,\text{V}$; $0.225\,\%$; $844\,\text{kW}$; $67\,\text{MW}$.
  - s2: $81.81^\circ$; $68.6\,\mu\text{s}$; $\Delta t = 0.71\,\mu\text{s}$; $0.897\,\text{mW}$; $0.98$; $46.7$.
  - s3: $Br$ series; $\mu_0 = 1.268\cdot10^{-6}$; $b = 10.9$; $15.7\,\mu\text{T}$.
  - s4: $24^\circ$ / $14.5^\circ$.
  - s5: $533.0$ / $532.2\,\text{nm}$; $562$ / $692$; $\theta_3 = 73.3^\circ$; $x_3 = 2.7\,\text{m}$.
  - s6: $T = 5.468\cdot10^{-8}\,\text{s}$; $18.29\,\text{MHz}$; $3.914\cdot10^7\,\text{m/s}$; $0.3406\,\text{m}$; 80 revolutions; $4.37\,\mu\text{s}$; $4.50\cdot10^{15}\,\text{m/s}^2$; $7.5\,\text{pN}$.
  - s7: $299\,780\,455\,\text{m/s}$; $0.99996$; interval $2.9976$–$2.9980\cdot10^8$; $1.0894\,\mu\text{J}$; classical $3.6\cdot10^{10}\,\text{m/s}$ (120 c); $435.7\,\text{MJ}$; $0.5787\,\text{MJ}$; 753 cars; 58.
  - s8: $1.5$; $0.75\,\text{ns}$; $41.8^\circ$ ($42.2^\circ$ for $n = 1.49$).
  - s9: $2.4$ / $1.8\,\text{V}$; $0.369\,\text{J}$; $0.25\,\text{s}$.
  - Unit: hook $174\,\text{A}$, $15\,\text{kW}$, $38\,\%$, $2.0\,\text{W}$, $0.005\,\%$; Tutki $18.69$ / $35\,\text{mW}$, $0.45\,\text{s}$, $0.15\,\text{mJ}$; wings $0.391$ / $0.407$ / $0.110\,\text{V}$; Sirius $9925\,\text{K}$; diver $3.42\,\text{m}$; oil $1740$ / $580$ / $348\,\text{nm}$; line loss $830\,\text{kW}$ ($1.7\,\%$); lt-5 $41^\circ$, $1.16$; transformer $0.24\,\text{A}$; diamond $2.42$; teacher extra $12.5 \approx 13\,\text{A}$.
- **Assessment**: each choice item has exactly one correct option, and every distractor and its feedback is physically right. Lenz items lt-3 and tarkistus-3, the generator position item and the polarisation glare item are right.
- **Scope and wording**: within FY7, and FY5 for circular motion. s7 e explicitly declines relativistic $r$. No "heat" wording breaks the guardrails ("internal energy, transferred as heat").
