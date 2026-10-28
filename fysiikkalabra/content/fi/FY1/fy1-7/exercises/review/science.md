VERDICT: PASS
CONTENT-HASH: dc94aa09f627304b

Delta review over the audit's PASS (4336e3fb3c6c8370): L2-03 (steel ball, given readings) replaced by a reading task on fy1-7/cylinders-read; numbers with units turned into LaTeX.

## Blocking
(none)
## Polish
- solutions.md:79 — "10 ml luetaan noin 1 ml:n tarkkuudella" would make ρ uncertain by about 10 %, wider than the tolerance 3 %; the levels sit on 10 ml long lines, so say that the readings are on long lines and therefore exact enough for two figures.
## Checked
- Figure: scale 0–100 ml, ticks every 2 ml, long every 10 ml, numbers every 20 ml; water at 40 ml before and 50 ml after, both on long lines; piece fully submerged; description matches.
- Recomputed V = 10 ml = 1,0·10⁻⁵ m³, ρ = 0,0890 kg / 1,0·10⁻⁵ m³ = 8900 kg/m³; answers.py 8900; tolerance 0,03 (8633…9167) accepts 8900 and 9,0·10³; rejects 89 g/50 ml (1780) and 89 g/40 ml (2225).
- Copper 8960 kg/m³ hedged ("voi olla"), consistent with check-3. LaTeX conversions keep every value (11,3; 94,5; 400; 1800; 920; 1,9; 2,0; 788; 4,4; 71).
