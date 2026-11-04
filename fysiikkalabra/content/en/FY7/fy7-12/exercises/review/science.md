VERDICT: PASS
CONTENT-HASH: 3a06d4134f855a4c

## Blocking

## Polish
- content/en/FY7/fy7-12/exercises/review/packet-science.md:"Exercise brief" — the brief is empty in the en packet (review_packet.py looks for the Finnish section names Kaava/Esimerkki, and en headings are "Formula: Critical angle", "Worked example"); not a content finding, but the en exercise packets carry no lesson context — let review_packet.py match the translated section names.

## Checked
- One script recomputed all 12 answers from the task texts with my own formulas: 48.75°, 24.41°, 61.04°, 2.041·10⁵ km/s, 0.50 ms, 1.456, 1.414, 2.007·10⁵ km/s, 1.217 ms, 2.053 m, 67.58 ns, 77.61°. All match answers.py and exercises.json within tolerance.
- Numbers in exercises.json and solutions.md are identical to the Finnish originals; the translation changed no datum, answer or unit.
- L2-02 (Porro prism): light enters via the hypotenuse face and meets a leg face at 45°; n ≥ 1/sin 45° = 1.41 is right, with the ≥ boundary convention stated.
- L3-01: right triangle h, r at α_r with a vertical normal; r = h tan α_r correct.
- L3-02: zigzag path L/sin α_r, Δt = (n1 L/c)(n1/n2 − 1); 2 s.f. justified by Δn = 0.020; modal-dispersion conclusion correct.
- L3-03: checks glass–water α_r = 62.46° > 60° before refracting; air case 41.8° stated. Correct.
- Every solution states given/find/principle, solves symbolically first, converts units right and has a real reasonableness check; rounding follows the limiting datum.
- Scope: critical angle, refraction and v = c/n only, within FY7 "kokonaisheijastuminen" and the prerequisite fy7-10.
