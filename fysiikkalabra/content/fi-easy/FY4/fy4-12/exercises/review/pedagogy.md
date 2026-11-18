VERDICT: PASS
CONTENT-HASH: 4e1a211f752c40d9
Mode: full

## Blocking
None.

## Polish
1. solutions.md, fy4-12-L3-02 Kaava: "Sijoitetaan tämä välimatkaan ja sievennetään: $s_\text{min} = -x_{0\text{R}} - \dfrac{v^2}{2a}$" skips the algebra a weaker student needs ($\tfrac12 a (v/a)^2 - v\cdot v/a = -\tfrac{v^2}{2a}$). Show that line. Add also "(tässä $x_{0\text{R}} = -20\,\text{m}$, joten $-x_{0\text{R}}$ on positiivinen)" before Sijoitus.
2. solutions.md, fy4-12-L3-04 Kaava: "$s_\text{rel} = 10\,\text{m} + L_\text{k} + L_\text{h}$" has a number inside the symbolic step. Name it ($d_0$, alkuväli) and substitute it in Sijoitus. Also Vastaus says 267 m has "kolme merkitsevää numeroa" although the speeds have two; say that the sum is exact to the data or round to 270 m.
3. exercises.json, fy4-12-L3-05 text: "$1{,}5\,\text{s}$ pyöräilijän ohituksen jälkeen" is ambiguous, since ohitus also means the car overtaking the cyclist. Corrected: "$1{,}5\,\text{s}$ sen jälkeen, kun pyöräilijä ohitti pysäytysviivan". Same in the solution's Vastaus ("pyöräilijän ohituksesta" -> "siitä, kun pyöräilijä ohitti pysäytysviivan").
4. Provenance sentences in task prose: L2-05 "Aineisto on esimerkkiaineisto.", L2-07 "Aineisto on esimerkkiaineisto, josta mittausvirhe on jätetty pois", L3-05 "esimerkkiaineisto", L3-04 "Esimerkkitilanne:". The 2026-11-13 read-through says no provenance badge on example data; cut the sentences (keep the table).
5. solutions.md, fy4-12-L3-05 Vastaus: "kaksi merkitsevää numeroa" but $14{,}5\,\text{m/s}$ and $52{,}4\,\text{m}$ show three; give 15 m/s and 52 m or drop the claim.

## Checked
- Opened exercises.json and solutions.md whole (8 + 8 + 5 tasks; minimums 5/4/3 met); figure descriptions of the five graph ids from the packet.
- Recomputed every answer: 4,0 s; 20 s; 24 m; 5,0 s; 35 m; 7,0 s; 30 s; 5,0 min; 9,0 s; 3,75 s; 7,0 s; 6,0 s; 36 m; 2,0 s; 4,0 m; 10 s; 267 m; 52 m (v = 5,975 m/s stays inside the 5 % tolerance). All match.
- Every Kaava starts from $x = x_0 + vt$ or the constant-acceleration form, writes both positions, sets them equal, solves symbolically, then Sijoitus; no combined formula opens a solution.
- Level mix: L1 single step or reading, L2 conversion, data, error analysis, L3 quadratic, no-meeting, overtaking model; none repeats the worked example (cyclist 16 m ahead, car at 2,0 m/s²).
- L2-08 choices: each wrong graph maps to one named misconception (curve, v-crossing as meeting, equal start speeds) and its feedback explains it; values in the figure descriptions agree with the solution.
- L1-06 and L1-08 feedback is specific to each distractor; L2-06 error analysis names the mistake and gives the 16 m lead at the wrong time.
- Situations first, question last as its own sentence; case after number+unit correct ("$12\,\text{N}$:n" style) wherever present; data-table decimals are rendered with comma by the build.
- Captures not opened: only text and formula order are judged; no scroll or layout changes since the earlier layout checks.
- Hash the same at start and end.

## Scores
Level fit 4/5. Task clarity 4/5. Solution completeness 4/5. Finnish 4/5. Feedback quality 5/5.
