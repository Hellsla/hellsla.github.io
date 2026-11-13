VERDICT: FAIL
CONTENT-HASH: 41a96108e4632f78

## Blocking
- exercises.json:136 (L1-11) — A: `"unit": "min"` is left over from the old version of the task, which asked for the period. The task now asks for the gravitational acceleration, and the answer is 1.45 m/s², so the page would show "1.45 min". — Set `"unit": "m/s²"`, as in the Finnish version.

## Polish
- exercises.json (L1-11, hint) — "The values are found" is plural, but only the Moon's mass is looked up now. — Write "The mass of the Moon is found …".
- solutions.md (L1-10, Reasonableness) — "about a thousandth" is a rough estimate: 5.93·10⁻³/9.81 ≈ 6·10⁻⁴. — Write "less than a thousandth".

## Checked
- The hash was the same at the start and the end. Round 5: I reviewed the changed exercise L1-11.
- L1-11: the Moon's mass, 7.346·10²² kg, is from the VERIFIED row of docs/mafy-arvot.tsv. g = γM/r² = 1.448 m/s² → 1.45. This matches answers.py and the Finnish version.
- The 4 % tolerance covers values from other tables (7.35·10²² kg gives 1.449 m/s²). The rounding is justified by the radius, 1840 km, which has three significant figures.
- The reasonableness check is correct: 1.62·(1737/1840)² = 1.44 m/s².
- The answer, unit and tolerance of every exercise are the same as in the Finnish set. The numbers in the English solutions of L1-10, L1-11 and L2-08 are the same as the Finnish ones.
