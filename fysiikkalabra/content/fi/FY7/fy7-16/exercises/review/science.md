VERDICT: PASS
CONTENT-HASH: 17151a3c70a4f503

Round 1 (exercises): full review; new YO-skill task fy7-16-L2-08 (suuruusluokka), the rest of the set PASS before. Checked from the text only; no renders.

## Blocking

## Polish
- exercises.json:227 (L2-08) — the distractors carry unit errors only, none of this chapter's warned mistakes (dB read as percent, range of the charger, hot glass). Physics is fine; flag for pedagogy whether a chapter-specific distractor is wanted.
- exercises.json:252 (L2-08, "noin 12 s") — 1000 times the answer, outside docs/exercise-types.md's "factor 10–100". Acceptable; "noin 120 ms" (factor 10, e.g. n forgotten twice) would fit the rule.
- Carried over: L1-06 aluminium distractor; L3-05 a) overlap.

## Checked
- Hash 17151a3c70a4f503 at start and end.
- L2-08 physics: v = c : n = 2,04 · 10⁸ m/s, s = 2 · 1,2 · 10⁶ m, t = 11,76 ms → "noin 12 ms"; check 4,9 µs per km · 2400 km = 11,8 ms right. Assumptions (axial ray, no device delays) stated in the task.
- Distractors recomputed: L as 1200 m → 11,8 µs; 1,2 · 10⁵ m → 1,18 ms; v as 300 000 with L in m → 11,8 s. Each feedback names its error correctly.
- Form: four options same form "noin 12 …"; correct not identifiable by form. Correct feedback right (11,8 ms).
- Scope: t = s : v with v = c : n from prerequisite fy7-12; fits an applied chapter.
- Solution complete, symbolic before substitution, conversion km → m shown; display lines short (text estimate).
- answers.py output equals exercises.json for all 19 numeric answers.
