VERDICT: PASS
CONTENT-HASH: 73c55536e9b48ef1
Round 1, science, mode full. Scope: the new YO-skill task fy6-13-L1-09 (true/false, type 8); the rest of the set was PASS and is unchanged. Checked from text only, no renders.

## Blocking

## Polish
- fy6-13/exercises/exercises.json:135 — "eristeen läpi kulkee yhä pieni virta" is marked false, but a real 100 µF electrolytic capacitor does have a small leakage current. A student who knows this may mark it true — say "virta kulkee eristeen läpi samalla tavalla kuin johtimessa", or add "ideaalisen kondensaattorin" to the stem (kind C, an ideal model; keep it, but word it so the false statement is false by the lesson's model alone).

## Checked
- Numbers recomputed: Q = CU = 1,2 mC, W = ½CU² = 7,2 mJ, QU = 14,4 mJ, at 24 V W = 28,8 mJ. The truth values are T, F, F, F, T, and answer, statements and solution agree.
- "Half to the resistor" holds for charging through a resistor from a constant-voltage source, which is the lesson's model, and the stem states "ladataan vastuksen kautta".
- The false statements carry the lesson's three warned misconceptions (total charge, current through the capacitor, C growing with U) and the QU-for-energy error.
- No statement stands out by form: true and false statements are of similar length and certainty.
- Notation C = Q/U and W = ½CU² is the lesson's, with \tfrac. Charging stays qualitative (no exponential), as LOPS says.
- The solution is complete (Kysytty · Periaate · Mallivastaus) and gives each statement its reason.
- All numeric answers of the set were recomputed from answers.py in one call: no mismatch.
- Inline width (text estimate): `W = ½CU² = ½ · 100 · 10⁻⁶ F · (12 V)²` in the solution is about 290 px, close to 300 px. It can break at "=", but the visual reviewer should measure it.
