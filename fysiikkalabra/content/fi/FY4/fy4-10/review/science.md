VERDICT: FAIL
CONTENT-HASH: ed4405cce2870c9d

## Blocking
- assets/sims/fy4/fy4-10/sim.js:1318 (`outside()`), also the header comment at :1245 — **A**. The run stops at an arrow tip only once `R.after !== null`. Before the collision, or while the gliders are still touching, nothing stops it except `endCheck` (a glider reaching the end of the track). So whenever glider 2 moves right (v2 > 0) and the collision comes late or never (for example v1 = 0, v2 = 0,1 … 1,0 m/s, or v1 = 0,2, v2 = 0,1 m/s), the arrows run off the canvas. At x2 = 1,9 m the tip of the $\overline{v}_2$ / $\overline{p}_2$ arrow is at X ≈ 552 + 105 = 657 px on a 600 px canvas, so the arrowhead is cut off. My sweep over every control setting found 2448 such settings (wide layout) and 2555 (narrow), 153 of them during contact. This breaks the brief ("arrows never vanish at the edges") and the file's own claim at :1245. — Fix: test `outside()` on every step whatever `after` is (`if (outside()) R.done = true;`), or check before the run starts that glider 2 will not reach the edge first.

## Polish
- packet "lesson-answers.py" header — it says "Velocity Verlet", but model.js integrates with RK4. The kimmoton values differ in the 4th decimal (0,1261 vs 0,1258), and the text uses neither. — Say RK4, or import the model's numbers.
- inquiry.json `simulaatio.calc` — "E_sis lasketaan puskurin vaimennuksen tekemästä työstä" leaves out two sources: the energy of the bumper left compressed when the velcro holds, and the spring relaxing off contact in kimmoton. `model` covers the first. — Add "ja puristuneeksi jääneen puskurin energiasta".
- sim.js pChart/eChart — the "after" group is labelled *nyt*. That is correct while the sim runs, but at the end the readout says *Jälkeen*. — Consider "nyt / jälkeen".

## Checked
- Recomputed each of the 12 experiment runs: model.js (RK4) against my own closed forms. Elastic: (0,20; 0,80), (0; 0,60), (−0,12; 0,48). Sticky: 0,40 / 0,30 / 0,24 m/s, E_k′ 0,048 / 0,036 / 0,029 J. Explosion: (−0,632; 1,265) with p = ∓0,253 and E_k′ = 0,24 J. Momentum drift is under 1e-15; E_k + E_p + E_sis drifts under 1e-6 J; E_sis is never negative.
- Sticky (tarra): critical damping gives v_rel = 0 at maximum compression with F > 0 throughout. The velcro holds, the gliders share V, and E_p goes into E_sis. Physically sound.
- Explosion: d = 4,0 cm, ½·300·0,04² = 0,24 J. "Ennen" shows E_p = 0,24 J and E_k = 0. The energy column starts as E_p.
- Bumper forces are F on glider 2 and −F on glider 1 from the contact point, with equal lengths. They are never negative (clamped), so the bumpers never pull.
- Bars: momentum is signed about a zero line with +/− marks, and both groups share one scale (B.P bounds every outcome). Energy is clamped at ≥ 0, stacked, on one scale, with the dashed E0 line. The bumpers never visually overlap (d_max 6,3 cm < 7 cm).
- The lesson's numbers check out: worked example 1,14 → 1,1 m/s, 38,3 → 32,5 kJ (15 %). Inline example 0,30 m/s and 0,072 → 0,036 J. Distractor v/√2 = 0,42. Virhe 0,025 vs 0,475. Siirto 1,0, with 0,706 correctly explained as velocity relative to the boat. check-2 0,15 (0,60 / 0,20).
- Figures: tarra (v halved, p equal) and tyypit (equal and opposite p) are drawn to the scale they claim.
- Billiards derivation (2v₁′v₂′ = 0, excluding pass-through) is correct. The spin caveat is stated.
- Conditions: "ulkoisten voimien impulssi merkityksettömän pieni" is stated in the theory, summary, glossary, tasks and exit ticket. The causal chain from N3 to equal impulses is sound.
- Every choice item has exactly one correct option, and each distractor's feedback is correct. The experiments isolate m2, and simState provides u1, u2, pJ and EkJ.
- `node tests/models/fy4-10.test.js`: 4791 checks pass. The hash is unchanged at the end.
