VERDICT: FAIL
CONTENT-HASH: 6708d4d6bec4b88b

The lesson delivers its goals: p = F/A, ρgh derived from the column's weight, p = p₀ + ρgh as a line (slope ρg, constant p₀) in text, SVG and sim, and force as a magnitude because it is perpendicular to the surface. Buoyancy is left to FY4. Length and structure match fy3-1/fy3-3 (theory 842 vs 717/829 words, solutions 839 vs 739/745, 5/4/3 exercises, same six sections). The opening question is never answered.

## Blocking
- lesson.md:3 — the dam hook is never answered. Line 10 only says the force is horizontal, whereas fy3-1:38 closes its hook. — Add one sentence (end of line 8 or Tiivistelmä): pressure, and so the force per m² of wall, grows with depth, so the base carries the most. Give a number, e.g. about 290 kPa at 30 m.

## Polish
- exercises.json — no task reads the slope ρg or the constant p₀ from (h, p) data, although the skill goal, SVG and sim centre on them. — Make one task (e.g. L2-03) use two gauge readings at two depths: ρ from the slope, p₀ from the constant. Update answers.py and solutions.md.
- lesson.md:30–35 — the SVG p axis is not to scale. With 0 at y 250 and 101 at y 160, 199 kPa belongs at y ≈ 73, not 52. — Move the end point, circle and label.
- lesson.md:54 — "kaavan p = ρgh" reuses p, which is total pressure in line 23. — "termi ρgh on vain ylipaine".
- solutions.md:12,36,52,60,92 — p_h is never introduced in the lesson. — Name it in lesson.md:25 ("p_h = ρgh") or write ρgh.
- lesson.md:51 — "Sukeltaja ei tunne vastaavaa voimaa" sits oddly next to the eardrum in line 10. — Say the body is not crushed because the pressure acts from every side and inside; air spaces such as the ears need equalising.

## Checked
- The lint reports 0 errors and 0 warnings.
- The goals match curriculum.json. "noste" is swapped for "tiheys" deliberately, and "tiheys" is in glossary.json.
- No vectors, Newton's laws or buoyancy. The only prerequisite formula is G = mg.
- No exercise repeats the example with new numbers.
- The example's numbers check: 117,7 kPa, 219 kPa, 1,77 kN.
- The sim matches sim-spec.md, its readout is in the DOM, and simState is complete.
- p₀ = 101 kPa and g = 9,81 m/s² are the same everywhere.
