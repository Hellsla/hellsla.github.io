VERDICT: PASS
CONTENT-HASH: dd6fa15d7b090997

## Blocking
(none)

## Polish
- lesson.md:23 — the text says the balance equation can be solved for the final temperature, but the rearranged form is never shown, although lesson.md:71 (35 °C) and exit-ticket.json:12 (65 °C) expect students to find it — add a display line `T = \frac{c_1 m_1 T_1 + c_2 m_2 T_2}{c_1 m_1 + c_2 m_2}` (or one worked line for the 35 °C case).
- lesson.md:17 vs lesson.md:21 — the sign convention (Q > 0 warming, Q < 0 cooling) needs ΔT = T_loppu − T_alku, which is never stated, and the balance equation then switches to positive magnitudes — state ΔT = T_loppu − T_alku at line 17 and add "molemmat puolet ovat positiivisia" (equivalently Q₁ + Q₂ = 0) at line 23.
- solutions.md:2, 10, 18, 26, 34, 42, 50, 58, 66 — T₁ and T₂ mean start and end temperature of one body, while lesson.md:23 uses them as the initial temperatures of two bodies (T₂ = cold body) — use T_alku / T_loppu in the single-body solutions.
- lesson.md:66 — ΔT_vesi = 24,5 − 20,0 = 4,5 K has only two significant figures, so 375 J/(kg·K) claims one figure too many — write ≈ 3,7·10² J/(kg·K) or add one sentence that the 4,5 K difference limits the accuracy (which also supports the 375 vs 385 discussion).
- solutions.md:79 — "Kiviä tarvitaan vettä vähemmän, koska ne jäähtyvät paljon enemmän" omits that the stones' smaller c works the other way; the mass ratio is (4190 · 30)/(800 · 260) ≈ 0,60 — mention both factors (ΔT ratio ≈ 8,7, c ratio ≈ 5,2).

## Checked
- Balance equation lesson.md:21 correct; both sides positive for T₂ < T < T₁.
- Example: 5656,5 J / (0,200 · 75,5) = 374,6 ≈ 375; C = 1257 and 74,9 J/K; heat loss direction consistent with 375 < 385.
- SVG: 210 px per 4190; bar heights 105, 45, 40, 23, 19 and y = 250 − h match the table to the pixel.
- Misconception 35 °C, ratio 9,3, sand/water 0,19; exit ticket 420 kJ, ≈ 9, 65 °C.
- All 12 solutions recomputed: substitutions, rearrangements (t, T₂, c, m_k, V), signs and final rounding agree with answers.py.
