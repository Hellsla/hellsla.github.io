VERDICT: PASS
CONTENT-HASH: 63d1877e57a7774f

## Blocking
None.

## Polish
- fy4-s2 a) Järkevyys ("osa energiasta muuttuu lämmöksi") and b) Järkevyys ("energiasta muuttuu lämmöksi yli puolet") break guardrail P1 (B: should read "muuttuu sisäenergiaksi, joka siirtyy lämpönä ympäristöön"). Both sentences are rows 9–10 of `docs/physics-phrases-known.tsv` and belong to work queue 18, not to 8m; not blocking here. When corrected, delete the rows.

## Checked
- The 8m change (diff against origin/main): "liikekitka" → "liukukitka" in tasks.json fy4-s1 b) fbd_forces detail and c) text, solutions.md fy4-s1 b) model answer, c) Kysytty, fy4-s3 a) Periaate, and the fy4-s1-fbd figure description (figures.py and the SVG aria-label). Every occurrence is a body sliding (skis on snow, locked tyres), so liukukitka / liukukitkakerroin is the right term. No "liikekitka" or "kinetic friction" left in any language of the set. No body at rest needs static friction in this set, so "täysin kehittynyt lepokitka eli lähtökitka" has no place to be named; nothing missing.
- Recomputed every number from the task data with my own script: s1 slopes 0,39 / 0,245 (fit 0,3895 / 0,2447), g sin α 0,684, g cos α 9,786, μ_A 0,030, μ_B 0,045, Δμ 0,002 for ±0,02 m/s², ±0,1° ≈ 0,002, a0 0,449 (fit a = a0 − kv²), μ_A0 0,024, correction 0,006, accepted ranges 0,022–0,026 and 0,028–0,032 / 0,043–0,046; s2 17,2 m/s ≈ 62 km/h, 9123 J, 3889 J, 29,1 N (4,8 % of weight), 57 %, 13 979 J, 8745 J, 13,6 m/s (13,58 with 29 N); s3 7,86 m/s ≈ 28 km/h, 7,36 m/s², 13,6 m/s ≈ 49 km/h, 158 / 91 kJ (42 % lost), 4455 N, 6,7 × weight, 66 m/s², friction impulse 2605 N·s (11 %), v_B ≤ 15,2 m/s, μ ≈ 0,50 needed for 40 km/h. All agree with answers.py, solutions and rubric details.
- Physics of the changed sentences unchanged: F_μ = μN with N = mg cos α (slope) and N = mg (level road); friction up the slope against the motion; force diagram (G, N, F_μ; components dashed, a apart) agrees with the motion.
- Rubric points sum per part as stated; tolerances admit the rounded answers.
