VERDICT: PASS
CONTENT-HASH: 2f9de8817eb2638d
SCOPE: delta (round 2): new tasks fy9-kaasut-s8 (fy3-10/pt-suorat) and s9 (fy3-11/pv-isobaari) and the changed intro, judged afresh; s1-s7 not re-judged. Hash at start and end identical. Language: fi.

## Blocking
(none)

## Polish
- s9: heating air to about 1170 K (about 900 C) is still not plausible for a school cylinder; a smaller volume ratio or a one-line note ("the gas is idealised") would help. Not blocking, the task is explicitly an invented example.

## Checked
- Round-1 blockers verified in the current text, not trusted: (1) s9 now says the movable piston carries weights that hold the pressure constant, "light" is gone, consistent with the constant 250 kPa in the figure; (2) s9 b and c both use two significant figures, answer.value 1172.6 K with tolerance 3 %: 1.2e3 K is 2.3 % off, so inside tolerance, and n = 0.10 mol gives 1203 K (2.6 %), also inside; (3) the intro no longer calls the last task the source task, it says only that one of the tasks is source-based; (4) the s9 c common-mistake line now reads "temperature not converted from Celsius to kelvins or the answer says it quadruples in Celsius (80 C)", which is correct.
- Own recomputation (R = 8.31, 273.15): s8 a n = 100000*2.0e-3/(8.31*400) = 0.0602 mol (200 K / 50 kPa point gives the same); s8 b 60/100 = 0.60, so 40 % smaller, n_B 0.036 mol; s8 c 253.15/400*100 = 63.3 kPa; s9 a 250 kPa*3.0 l = 750 J; s9 b n = 0.1026 mol; s9 c T2 = 4*293.15 = 1172.6 K (880 K rise, 899.5 C). All match tasks.json answers and solutions.
- s8: rigid vessel, constant V and n, so p proportional to T; comparison at equal T and V is physically sound; reading from two far-apart points; precision (two figures) matches the data; the -20 C part lies within the graph's range logic (253 K between 200 K and 400 K).
- s9 d: heating at constant pressure, internal energy up, Q = dU + W, so Q > W; sign convention and energy wording correct. Magnitude check (0.04 mol of air per litre at 101 kPa, 2.5x pressure gives 0.10 mol) right.
- Points add up per part, criteria match the parts, scope FY3, figure values are readable from the figures (V and 20 C given in the text).
- Fidelity: numbers, criteria and physics identical across fi, en and fi-easy.
