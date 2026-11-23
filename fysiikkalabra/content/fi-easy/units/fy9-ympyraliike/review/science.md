VERDICT: PASS
CONTENT-HASH: f6825d133f2e7219
SCOPE: full on the changes since 88634686642ae585 (three new pysahdy boxes, three SVG figures now WebP backgrounds with the same overlays, one inquiry model answer split into two paragraphs); sovella tasks, solutions and answers.py unchanged since the passed hash.

## Blocking
- (none)

## Polish
- (none) The kartta label in fi-easy says "gravitaatio kääntää rataa" where the Finnish one says "gravitaatio kaartaa". Same physics. This label was already in the version that passed.

## Checked
- Pysahdy 1 (Ydinajatus): in uniform circular motion the net force points to the centre because it points the same way as the acceleration (Newton 2). Correct, and the same physics as the Finnish box (unit.md line 13). The box keeps the stated condition "tasaisessa ympyräliikkeessä". Matches the bullets above it and the theory.
- Pysahdy 2 (Tasainen ympyräliike): velocity is tangent to the path and the normal acceleration points to the centre. Correct, the same as the Finnish box (line 134), and it agrees with the paragraph after it.
- Pysahdy 3 (gravitaatiolaki): when r doubles, F_g falls to 1/2² = 1/4 of its value, because F_g ∝ 1/r². Correct and the same as the Finnish box (line 196). The text keeps the stated condition (point-like or spherically symmetric bodies).
- My script: F(2r)/F(r) = 0,25. v(4r)/v(r) = 0,5 (inquiry model "nelinkertaisella säteellä ratanopeus on puolet"). Geostationary r/R = 6,62, which matches the label "r ≈ 6,6 R".
- Inquiry model change: only a paragraph break. The words, numbers and conditions (m ≪ M, circular orbit) are unchanged.
- Figures: the geo, hero and tilanteet SVGs in fi-easy are identical to the Finnish ones apart from the aria-label, and they use the same WebP files.
  - geo, measured on the raster: Earth radius about 34,5 units and orbit radius about 227–232 units, a ratio of about 6,6, so the claim that it is to scale holds. The Earth and the satellite both turn anticlockwise. v is tangential and F points to Earth's centre. The ghost antenna and satellite are a quarter turn on, which agrees with the new "6 h myöhemmin" label (6 h ≈ T/4).
  - tilanteet: on the plank, N₂ is about 2·N₁ and the support lever arms are about 90 and 182 (moment balance holds). N₁ + N₂ ≈ G.
  - Hump: G is longer than N, and a points down to the centre.
  - Satellite: gravity only, and a points to the centre. No velocity is drawn as a force.
- No later-course physics was introduced, and no term breaks the guardrails. Hash f6825d133f2e7219 was the same at the start and the end.
